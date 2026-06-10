#!/usr/bin/env python3
"""Generate a compact navigation index for key Markdown directories."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "generated" / "nav-index.md"
DIRECTORIES = [
    "frameworks",
    "workflows",
    "examples",
    "case-studies",
    "playbooks",
    "maintenance",
]


def title_for(path: Path) -> str:
    for line in path.read_text().splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return path.stem.replace("-", " ").title()


def main() -> int:
    lines: list[str] = [
        "# Navigation Index",
        "",
        "Generated from key Markdown directories. Edit the source pages, then",
        "rerun `python3 scripts/generate-nav-index.py`.",
        "",
    ]

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
            rel = page.relative_to(ROOT)
            lines.append(f"- [{title_for(page)}]({rel.as_posix()})")
        lines.append("")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(lines).rstrip() + "\n")
    print(f"Generated {OUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
