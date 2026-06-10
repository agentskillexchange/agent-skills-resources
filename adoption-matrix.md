# Adoption Matrix

Use this matrix to choose a small first workflow. It is intentionally narrower
than the canonical [agentskillexchange/skills](https://github.com/agentskillexchange/skills)
catalog.

| Team type | Example use case | Suggested starting skills | Risk level | Recommended rollout path | Validation evidence expected |
|---|---|---|---|---|---|
| Engineering | PR review and comment follow-through | `staff-engineer-mode`, `address-github-pr-review-comments-from-the-current-branch-with-gh-address-comments` | Medium | Archived PR to one repo to production PRs with reviewer approval | Test commands, changed files, review-comment mapping |
| Security | Approval-gated agent actions | `route-risky-coding-agent-work-through-human-approval-checkpoints-with-humanlayer`, `run-agent-generated-code-in-local-microvm-sandboxes-with-microsandbox` | High | Fixture to internal repo to gated production workflow | Approval records, sandbox logs, denied risky actions |
| SRE / Platform | Incident triage and remediation drafts | `investigate-production-incidents-across-kubernetes-and-cloud-signals-with-holmesgpt`, `tail-multi-pod-kubernetes-logs-by-label-during-incidents-with-stern` | High | Historical incident to staging to read-only production triage | Commands run, timestamps, affected service, human-approved next steps |
| Data | SQL validation and database inspection | `query-and-inspect-postgres-databases-through-mcp-with-pgedge-postgres-mcp`, `translate-and-validate-sql-across-dialects-with-sqlglot` | Medium | Sample schema to staging read-only to production read-only | Query text, dialect, row limits, validation results |
| Content / Research | Cited research draft | `draft-cited-research-reports-with-storm`, `run-autonomous-deep-research-workflows-with-gpt-researcher` | Medium | Public-source draft to internal brief to editorial-reviewed publication | Citation list, unsupported-claim review, source labels |
| Runtime Ops | OpenClaw day-2 operations | `run-day-2-openclaw-operations-with-production-runbooks-and-reusable-prompt-patterns-from-openclaw-runbook`, `back-up-and-restore-an-openclaw-workspace-to-synology-nas-with-verification-and-rollback-safety-using-synology-backup` | High | Dry-run runbook to backup verification to scheduled operations | Runbook diff, backup restore evidence, rollback notes |

## Reading The Risk Level

- Low: read-only, fixture-based, or documentation-only work.
- Medium: real repo or data work with bounded permissions and human review.
- High: production, security, runtime, incident, or privileged access workflows.

When in doubt, start one level lower and require more evidence before expanding.
