#!/usr/bin/env python3
"""Generate a Markdown index from data/ase-skill-mapping.json."""

from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "generated" / "ase-skill-mapping-index.md"


def load_mappings() -> list[dict[str, object]]:
    data = json.loads((ROOT / "data" / "ase-skill-mapping.json").read_text())
    if not isinstance(data, list):
        raise SystemExit("ase-skill-mapping.json must be a list")
    return [row for row in data if isinstance(row, dict)]


def skill_url(slug: str) -> str:
    return f"https://agentskillexchange.com/skills/{slug}/"


def render_skill_rows(lines: list[str], rows: list[dict[str, object]]) -> None:
    lines.append("| Skill | Framework | Workflow area | Why it matters |")
    lines.append("|---|---|---|---|")
    for row in rows:
        framework = str(row.get("framework", ""))
        workflow = str(row.get("workflow_area", ""))
        for skill in row.get("example_skills", []):
            if not isinstance(skill, dict):
                continue
            slug = str(skill.get("slug", ""))
            why = str(skill.get("why_it_matters", ""))
            lines.append(f"| [{slug}]({skill_url(slug)}) | {framework} | {workflow} | {why} |")


def main() -> int:
    mappings = load_mappings()
    by_framework: dict[str, list[dict[str, object]]] = defaultdict(list)
    by_workflow: dict[str, list[dict[str, object]]] = defaultdict(list)
    skill_count = 0
    for row in mappings:
        by_framework[str(row.get("framework", "Unspecified"))].append(row)
        by_workflow[str(row.get("workflow_area", "Unspecified"))].append(row)
        skill_count += len(row.get("example_skills", []))

    lines: list[str] = [
        "# ASE Skill Mapping Index",
        "",
        "Generated from `data/ase-skill-mapping.json`. This is a representative",
        "companion index, not the canonical catalog. Use",
        "[agentskillexchange/skills](https://github.com/agentskillexchange/skills)",
        "for the full skill source of truth.",
        "",
        f"- Mapping groups: {len(mappings)}",
        f"- Representative skills: {skill_count}",
        "",
        "## By Workflow Area",
        "",
    ]

    for workflow, rows in sorted(by_workflow.items()):
        lines.append(f"### {workflow}")
        lines.append("")
        render_skill_rows(lines, rows)
        lines.append("")

    lines.append("## By Framework")
    lines.append("")
    for framework, rows in sorted(by_framework.items()):
        lines.append(f"### {framework}")
        lines.append("")
        render_skill_rows(lines, rows)
        lines.append("")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(lines).rstrip() + "\n")
    print(f"Generated {OUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
