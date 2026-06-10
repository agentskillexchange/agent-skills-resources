#!/usr/bin/env python3
"""Generate a Markdown index for evaluation templates."""

from __future__ import annotations

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEMPLATES = ROOT / "templates"
OUT = ROOT / "generated" / "template-index.md"


def page_title(path: Path) -> str:
    for line in path.read_text().splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return path.stem.replace("-", " ").title()


def first_paragraph_after_h1(path: Path) -> str:
    lines = path.read_text().splitlines()
    seen_h1 = False
    paragraph: list[str] = []
    for line in lines:
        stripped = line.strip()
        if not seen_h1:
            if stripped.startswith("# "):
                seen_h1 = True
            continue
        if not stripped:
            if paragraph:
                break
            continue
        if stripped.startswith("#"):
            if paragraph:
                break
            continue
        paragraph.append(stripped)
    return " ".join(paragraph) or "Template page."


def link_to(path: Path) -> str:
    return os.path.relpath(path, OUT.parent).replace(os.sep, "/")


def main() -> int:
    pages = sorted(
        path
        for path in TEMPLATES.glob("*.md")
        if path.is_file() and not path.name.startswith(".")
    )
    lines = [
        "# Template Index",
        "",
        "Generated from `templates/*.md`. Edit the source templates, then rerun",
        "`python3 scripts/generate-template-index.py`.",
        "",
        "| Template | Purpose |",
        "|---|---|",
    ]
    for path in pages:
        lines.append(f"| [{page_title(path)}]({link_to(path)}) | {first_paragraph_after_h1(path)} |")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(lines).rstrip() + "\n")
    print(f"Generated {OUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
