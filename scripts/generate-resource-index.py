#!/usr/bin/env python3
"""Generate a Markdown index from data/resources.json."""

from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "generated" / "resource-index.md"


def load_resources() -> list[dict[str, object]]:
    data = json.loads((ROOT / "data" / "resources.json").read_text())
    if not isinstance(data, list):
        raise SystemExit("resources.json must be a list")
    return [row for row in data if isinstance(row, dict)]


def link(name: object, url: object) -> str:
    return f"[{name}]({url})"


def rows_by(rows: list[dict[str, object]], key: str) -> dict[str, list[dict[str, object]]]:
    grouped: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        grouped[str(row.get(key) or "Unspecified")].append(row)
    return dict(grouped)


def write_grouped_table(lines: list[str], rows: list[dict[str, object]]) -> None:
    lines.append("| Resource | Framework | Why it matters |")
    lines.append("|---|---|---|")
    for row in sorted(rows, key=lambda item: str(item.get("name", "")).lower()):
        lines.append(
            "| "
            + link(row.get("name", ""), row.get("url", ""))
            + f" | {row.get('framework', '')} | {row.get('why_it_matters', '')} |"
        )


def main() -> int:
    resources = load_resources()
    lines: list[str] = [
        "# Resource Index",
        "",
        "Generated from `data/resources.json`. Edit the JSON source, then rerun",
        "`python3 scripts/generate-resource-index.py`.",
        "",
        "## By Source Type",
        "",
    ]

    for source_type, rows in sorted(rows_by(resources, "type").items()):
        lines.append(f"### {source_type}")
        lines.append("")
        write_grouped_table(lines, rows)
        lines.append("")

    lines.append("## By Framework")
    lines.append("")
    for framework, rows in sorted(rows_by(resources, "framework").items()):
        lines.append(f"### {framework}")
        lines.append("")
        write_grouped_table(lines, rows)
        lines.append("")

    tag_rows: dict[str, list[dict[str, object]]] = defaultdict(list)
    for row in resources:
        for tag in row.get("tags", []):
            tag_rows[str(tag)].append(row)

    lines.append("## By Tag")
    lines.append("")
    for tag, rows in sorted(tag_rows.items()):
        names = ", ".join(
            link(row.get("name", ""), row.get("url", ""))
            for row in sorted(rows, key=lambda r: str(r.get("name", "")).lower())
        )
        lines.append(f"- **{tag}**: {names}")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(lines).rstrip() + "\n")
    print(f"Generated {OUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
