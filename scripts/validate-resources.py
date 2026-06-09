#!/usr/bin/env python3
"""Validate structured resource data for agent-skills-resources."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
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


def main() -> int:
    resources_path = ROOT / "data" / "resources.json"
    mapping_path = ROOT / "data" / "ase-skill-mapping.json"
    resources = json.loads(resources_path.read_text())
    mapping = json.loads(mapping_path.read_text())

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

    print("PASS: resources valid")
    print(f"resources: {len(resources)}")
    print("type_counts:", json.dumps(type_counts, sort_keys=True))
    print(f"mappings: {len(mapping)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

