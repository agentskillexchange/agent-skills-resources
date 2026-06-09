# Contributing

This repo is the companion resource hub for agent skills. The canonical skill
catalog remains [agentskillexchange/skills](https://github.com/agentskillexchange/skills).

## Contribution Types

- Add or update official framework resources.
- Improve a framework guide.
- Add source-backed ASE skill mappings.
- Improve ecosystem diagrams.
- Fix broken links.
- Improve validation scripts.

## Source Rules

- Use `Official` only for vendor/project-owned docs or repositories.
- Use `Lab` for frontier-lab or research-lab material.
- Use `Community` for third-party repos, posts, tools, or guides.
- Use `ASE` for Agent Skill Exchange resources.

Do not invent official status, popularity claims, or compatibility claims.

## Before Opening A PR

```bash
python3 scripts/validate-resources.py
python3 scripts/validate-links.py
```

