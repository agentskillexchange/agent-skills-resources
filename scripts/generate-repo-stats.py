#!/usr/bin/env python3
"""Generate a compact stats snapshot for this companion repo."""

from __future__ import annotations

import datetime as dt
import json
import os
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "generated" / "repo-stats.md"


def md_count(directory: str) -> int:
    root = ROOT / directory
    if not root.exists():
        return 0
    return len([path for path in root.glob("*.md") if path.is_file() and not path.name.startswith(".")])


def link_to(path: Path) -> str:
    return os.path.relpath(path, OUT.parent).replace(os.sep, "/")


def main() -> int:
    resources = json.loads((ROOT / "data" / "resources.json").read_text())
    mappings = json.loads((ROOT / "data" / "ase-skill-mapping.json").read_text())
    type_counts = Counter(row["type"] for row in resources)
    mapped_skill_count = sum(len(row.get("example_skills", [])) for row in mappings)
    generated_indexes = sorted({
        *(path for path in (ROOT / "generated").glob("*.md") if path.is_file() and not path.name.startswith(".")),
        OUT,
    })
    generated_at = dt.datetime.now(dt.UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")

    lines = [
        "# Repo Stats",
        "",
        "Generated from current repository files.",
        "",
        f"- Last generated: {generated_at}",
        f"- Resources: {len(resources)}",
        f"- Representative mapped ASE skills: {mapped_skill_count}",
        f"- Framework pages: {md_count('frameworks')}",
        f"- Workflow pages: {md_count('workflows')}",
        f"- Case study pages: {md_count('case-studies')}",
        f"- Playbook pages: {md_count('playbooks')}",
        f"- Template pages: {md_count('templates')}",
        f"- Generated indexes: {len(generated_indexes)}",
        "",
        "## Resource Types",
        "",
        "| Type | Count |",
        "|---|---:|",
    ]
    for source_type, count in sorted(type_counts.items()):
        lines.append(f"| {source_type} | {count} |")

    lines.extend(["", "## Generated Indexes", ""])
    for path in generated_indexes:
        lines.append(f"- [{path.stem.replace('-', ' ').title()}]({link_to(path)})")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(lines).rstrip() + "\n")
    print(f"Generated {OUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
