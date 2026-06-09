#!/usr/bin/env python3
"""Audit resource freshness, source labels, links, and ASE slug mappings."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
import urllib.request
from collections import Counter
from pathlib import Path

from link_utils import check_url

ROOT = Path(__file__).resolve().parents[1]
PUBLIC_SKILLS_JSON = "https://raw.githubusercontent.com/agentskillexchange/skills/main/skills.json"
ALLOWED_TYPES = {"Official", "Lab", "Community", "ASE"}
REQUIRED_RESOURCE_FIELDS = {
    "id",
    "name",
    "type",
    "framework",
    "url",
    "repo",
    "description",
    "why_it_matters",
    "tags",
}
URL_RE = re.compile(r"^https://[^\s]+$")


def load_json(path: Path) -> object:
    return json.loads(path.read_text())


def load_skill_slugs(path: str | None) -> tuple[set[str], str]:
    if path:
        data = load_json(Path(path))
        skills = data.get("skills", data if isinstance(data, list) else [])
        return {str(row.get("slug")) for row in skills if row.get("slug")}, path

    local = ROOT / "skills.json"
    if local.exists():
        data = load_json(local)
        skills = data.get("skills", data if isinstance(data, list) else [])
        return {str(row.get("slug")) for row in skills if row.get("slug")}, str(local)

    req = urllib.request.Request(PUBLIC_SKILLS_JSON, headers={"User-Agent": "agent-skills-resources-audit/1.0"})
    with urllib.request.urlopen(req, timeout=20) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    skills = data.get("skills", data if isinstance(data, list) else [])
    return {str(row.get("slug")) for row in skills if row.get("slug")}, PUBLIC_SKILLS_JSON


def parse_date(value: str) -> dt.date | None:
    try:
        return dt.date.fromisoformat(value[:10])
    except Exception:
        return None


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--timeout", type=int, default=12)
    parser.add_argument("--skills-json", help="Optional local ASE skills.json for slug validation.")
    parser.add_argument("--skip-http", action="store_true")
    parser.add_argument("--json-out", help="Optional path for summary JSON.")
    args = parser.parse_args()

    resources = load_json(ROOT / "data" / "resources.json")
    mappings = load_json(ROOT / "data" / "ase-skill-mapping.json")
    issues: list[str] = []
    warnings: list[str] = []

    if not isinstance(resources, list):
        issues.append("resources.json must be a list")
        resources = []
    if not isinstance(mappings, list):
        issues.append("ase-skill-mapping.json must be a list")
        mappings = []

    ids: set[str] = set()
    url_counts: Counter[str] = Counter()
    primary_url_counts: Counter[str] = Counter()
    type_counts: Counter[str] = Counter()
    stale_entries: list[str] = []
    today = dt.date.today()

    for index, row in enumerate(resources):
        if not isinstance(row, dict):
            issues.append(f"resource {index} must be an object")
            continue
        missing = REQUIRED_RESOURCE_FIELDS - set(row)
        if missing:
            issues.append(f"resource {row.get('id', index)} missing fields: {sorted(missing)}")
        resource_id = str(row.get("id", index))
        if resource_id in ids:
            issues.append(f"duplicate resource id: {resource_id}")
        ids.add(resource_id)
        if row.get("type") not in ALLOWED_TYPES:
            issues.append(f"{resource_id} invalid source label: {row.get('type')}")
        else:
            type_counts[str(row["type"])] += 1
        for field in ["url", "repo"]:
            url = str(row.get(field) or "")
            if not url:
                continue
            if not URL_RE.match(url):
                issues.append(f"{resource_id} invalid {field}: {url}")
            url_counts[url] += 1
            if field == "url":
                primary_url_counts[url] += 1
        checked_at = row.get("last_checked_at")
        if checked_at:
            parsed = parse_date(str(checked_at))
            if not parsed:
                issues.append(f"{resource_id} invalid last_checked_at: {checked_at}")
            elif (today - parsed).days > 90:
                stale_entries.append(resource_id)

    duplicate_urls = sorted(url for url, count in primary_url_counts.items() if count > 1)
    if duplicate_urls:
        warnings.append(f"duplicate_urls: {len(duplicate_urls)}")

    try:
        skill_slugs, skill_source = load_skill_slugs(args.skills_json)
    except Exception as exc:  # noqa: BLE001 - report and continue
        skill_slugs, skill_source = set(), "skipped"
        warnings.append(f"skill_slug_validation_skipped: {type(exc).__name__}")

    unknown_slugs: list[str] = []
    mapped_count = 0
    for index, row in enumerate(mappings):
        if not isinstance(row, dict):
            issues.append(f"mapping {index} must be an object")
            continue
        for skill in row.get("example_skills", []):
            slug = str(skill.get("slug") or "")
            if not slug:
                issues.append(f"mapping {index} has empty slug")
                continue
            mapped_count += 1
            if skill_slugs and slug not in skill_slugs:
                unknown_slugs.append(slug)
    if unknown_slugs:
        issues.append(f"unknown ASE slugs: {', '.join(sorted(set(unknown_slugs)))}")

    link_results: list[dict[str, object]] = []
    hard_link_failures: list[dict[str, object]] = []
    temporary_link_warnings: list[dict[str, object]] = []
    if not args.skip_http:
        for url in sorted(url_counts):
            result = check_url(url, args.timeout)
            link_results.append(result)
            if not result["ok"]:
                if result["temporary"]:
                    temporary_link_warnings.append(result)
                else:
                    hard_link_failures.append(result)
        if temporary_link_warnings:
            warnings.append(f"temporary_link_warnings: {len(temporary_link_warnings)}")
        if hard_link_failures:
            issues.append(f"hard_link_failures: {len(hard_link_failures)}")

    if stale_entries:
        warnings.append(f"stale_last_checked_at_entries: {len(stale_entries)}")

    summary = {
        "ok": not issues,
        "resources": len(resources),
        "resource_type_counts": dict(sorted(type_counts.items())),
        "mapped_skill_groups": len(mappings),
        "mapped_skill_count": mapped_count,
        "skill_slug_validation": skill_source,
        "duplicate_url_count": len(duplicate_urls),
        "stale_last_checked_at_count": len(stale_entries),
        "link_count": len(link_results) if not args.skip_http else len(url_counts),
        "hard_link_failure_count": len(hard_link_failures),
        "temporary_link_warning_count": len(temporary_link_warnings),
        "issues": issues,
        "warnings": warnings,
    }

    print("Freshness audit")
    print(f"- ok: {summary['ok']}")
    print(f"- resources: {summary['resources']}")
    print(f"- resource_type_counts: {json.dumps(summary['resource_type_counts'], sort_keys=True)}")
    print(f"- mapped_skill_count: {mapped_count}")
    print(f"- duplicate_url_count: {len(duplicate_urls)}")
    print(f"- stale_last_checked_at_count: {len(stale_entries)}")
    print(f"- hard_link_failure_count: {len(hard_link_failures)}")
    print(f"- temporary_link_warning_count: {len(temporary_link_warnings)}")
    if issues:
        print("Issues:")
        for issue in issues:
            print(f"- {issue}")
    if warnings:
        print("Warnings:")
        for warning in warnings:
            print(f"- {warning}")
    print("Summary JSON:")
    print(json.dumps(summary, indent=2, sort_keys=True))

    if args.json_out:
        Path(args.json_out).write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n")

    return 0 if summary["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
