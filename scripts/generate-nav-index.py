#!/usr/bin/env python3
"""Generate a compact navigation index for key Markdown directories."""

from __future__ import annotations

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "generated" / "nav-index.md"
DIRECTORIES = [
    "frameworks",
    "workflows",
    "examples",
    "examples/completed-evaluations",
    "case-studies",
    "playbooks",
    "templates",
    "maintenance",
]


def title_for(path: Path) -> str:
    for line in path.read_text().splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return path.stem.replace("-", " ").title()


def link_to(path: Path) -> str:
    return os.path.relpath(path, OUT.parent).replace(os.sep, "/")


def main() -> int:
    lines: list[str] = [
        "# Navigation Index",
        "",
        "Generated from key Markdown directories. Edit the source pages, then",
        "rerun `python3 scripts/generate-nav-index.py`.",
        "",
        "## top-level",
        "",
    ]

    for page_name in ["overview.md", "getting-started.md", "best-practices.md", "adoption-matrix.md"]:
        page = ROOT / page_name
        if page.exists():
            lines.append(f"- [{title_for(page)}]({link_to(page)})")
    lines.append("")

    for directory in DIRECTORIES:
        root = ROOT / directory
        lines.append(f"## {directory}")
        lines.append("")
        if not root.exists():
            lines.append("- Missing directory")
            lines.append("")
            continue
        pages = sorted(
            path
            for path in root.glob("*.md")
            if path.is_file() and not path.name.startswith(".")
        )
        if not pages:
            lines.append("- No Markdown pages")
            lines.append("")
            continue
        for page in pages:
            lines.append(f"- [{title_for(page)}]({link_to(page)})")
        lines.append("")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(lines).rstrip() + "\n")
    print(f"Generated {OUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
