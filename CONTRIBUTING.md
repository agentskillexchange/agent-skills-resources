# Contributing

This repo is the companion resource hub for agent skills. The canonical skill
catalog remains [agentskillexchange/skills](https://github.com/agentskillexchange/skills).

## Contribution Types

- Source-backed resource addition.
- Source label correction.
- Framework or resource page improvement.
- Completed evaluation example.
- Typo or link correction.
- Validation or generated-index script improvement.

Use the GitHub issue templates when possible:

- Resource addition
- Source label correction
- Framework page request
- Completed evaluation example

## What Not To Contribute

- Fake skills.
- Unsupported official, compatibility, or safety claims.
- Full catalog dumps from `agentskillexchange/skills`.
- Stale popularity claims such as stars or downloads unless they are fetched
  live and clearly sourced.
- Third-party resources labeled as `Official` without ownership evidence.

## Source Rules

- Use `Official` only for vendor/project-owned docs or repositories.
- Use `Lab` for frontier-lab or research-lab material.
- Use `Community` for third-party repos, posts, tools, or guides.
- Use `ASE` for Agent Skill Exchange resources.

Do not invent official status, popularity claims, or compatibility claims.

## Before Opening A PR

```bash
python3 scripts/generate-resource-index.py
python3 scripts/generate-skill-mapping-index.py
python3 scripts/generate-template-index.py
python3 scripts/generate-nav-index.py
python3 scripts/generate-repo-stats.py
python3 scripts/validate-resources.py
python3 scripts/validate-links.py --timeout 15
python3 scripts/audit-freshness.py --timeout 15
```

## Pull Request Checklist

Before opening a PR, confirm:

- You did not modify `agentskillexchange/skills`.
- You did not duplicate the full skills catalog.
- Source labels are evidence-backed.
- Third-party resources are marked `Community` unless ownership proves
  otherwise.
- Generated indexes were updated when source data or navigation changed.

See [.github/pull_request_template.md](.github/pull_request_template.md) and
[Contribution Review](maintenance/contribution-review.md).
