#!/usr/bin/env python3
"""Validate structured resource data for agent-skills-resources."""

from __future__ import annotations

import json
import re
import sys
import argparse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PUBLIC_SKILLS_JSON = "https://raw.githubusercontent.com/agentskillexchange/skills/main/skills.json"
ALLOWED_TYPES = {"Official", "Lab", "Community", "ASE"}
REQUIRED = {
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


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def load_skill_slugs(path: str | None) -> tuple[set[str], str]:
    if path:
        data = json.loads(Path(path).read_text())
        skills = data.get("skills", data if isinstance(data, list) else [])
        return {str(row.get("slug")) for row in skills if row.get("slug")}, path

    local = ROOT / "skills.json"
    if local.exists():
        data = json.loads(local.read_text())
        skills = data.get("skills", data if isinstance(data, list) else [])
        return {str(row.get("slug")) for row in skills if row.get("slug")}, str(local)

    try:
        req = urllib.request.Request(PUBLIC_SKILLS_JSON, headers={"User-Agent": "agent-skills-resources-validator/1.0"})
        with urllib.request.urlopen(req, timeout=20) as resp:
            data = json.loads(resp.read().decode("utf-8"))
        skills = data.get("skills", data if isinstance(data, list) else [])
        return {str(row.get("slug")) for row in skills if row.get("slug")}, PUBLIC_SKILLS_JSON
    except Exception as exc:  # noqa: BLE001 - validation can still run without network
        print(f"WARN: could not load ASE skills catalog for slug validation: {type(exc).__name__}")
        return set(), "skipped"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--skills-json", help="Optional local ASE skills.json for slug validation.")
    parser.add_argument("--skip-skill-slugs", action="store_true", help="Skip ASE skill slug validation.")
    args = parser.parse_args()

    resources_path = ROOT / "data" / "resources.json"
    mapping_path = ROOT / "data" / "ase-skill-mapping.json"
    resources = json.loads(resources_path.read_text())
    mapping = json.loads(mapping_path.read_text())
    skill_slugs: set[str] = set()
    skill_source = "skipped"
    if not args.skip_skill_slugs:
        skill_slugs, skill_source = load_skill_slugs(args.skills_json)

    if not isinstance(resources, list):
        fail("resources.json must be a list")
    if not isinstance(mapping, list):
        fail("ase-skill-mapping.json must be a list")

    seen: set[str] = set()
    type_counts: dict[str, int] = {}
    for index, row in enumerate(resources):
        if not isinstance(row, dict):
            fail(f"resource {index} must be an object")
        missing = REQUIRED - set(row)
        if missing:
            fail(f"resource {row.get('id', index)} missing fields: {sorted(missing)}")
        resource_id = str(row["id"])
        if resource_id in seen:
            fail(f"duplicate resource id: {resource_id}")
        seen.add(resource_id)
        if row["type"] not in ALLOWED_TYPES:
            fail(f"{resource_id} has invalid type: {row['type']}")
        if not URL_RE.match(str(row["url"])):
            fail(f"{resource_id} has invalid url: {row['url']}")
        if row["repo"] and not URL_RE.match(str(row["repo"])):
            fail(f"{resource_id} has invalid repo url: {row['repo']}")
        if not isinstance(row["tags"], list) or not row["tags"]:
            fail(f"{resource_id} must have non-empty tags")
        type_counts[row["type"]] = type_counts.get(row["type"], 0) + 1

    for index, row in enumerate(mapping):
        if not isinstance(row, dict):
            fail(f"mapping {index} must be an object")
        for key in ["framework", "workflow_area", "example_skills"]:
            if key not in row:
                fail(f"mapping {index} missing {key}")
        if not isinstance(row["example_skills"], list):
            fail(f"mapping {index} example_skills must be a list")
        for skill in row["example_skills"]:
            if "slug" not in skill or "why_it_matters" not in skill:
                fail(f"mapping {index} has incomplete skill entry")
            if skill_slugs and skill["slug"] not in skill_slugs:
                fail(f"mapping {index} references unknown ASE slug: {skill['slug']}")

    print("PASS: resources valid")
    print(f"resources: {len(resources)}")
    print("type_counts:", json.dumps(type_counts, sort_keys=True))
    print(f"mappings: {len(mapping)}")
    print(f"skill_slug_validation: {skill_source if skill_slugs else 'skipped'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
