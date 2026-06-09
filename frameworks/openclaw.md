# OpenClaw

OpenClaw is an agent runtime for providers, skills, tools, crons, channels, and
long-running operations. It is especially relevant to skill-based workflows
because skills can be part of scheduled or channel-driven automation.

## Role In The Skills Ecosystem

- Agent runtime and operations layer.
- Strong fit for crons, Telegram/other channels, provider routing, skills,
  tools, and durable workspace operations.
- Skills should include operational guardrails, output contracts, and recovery
  checks.

## Source-Backed Resources

| Label | Resource | Why it matters |
|---|---|---|
| Official | [OpenClaw docs](https://docs.openclaw.ai/) | Documentation hub for OpenClaw setup and tools. |
| Official | [openclaw/openclaw](https://github.com/openclaw/openclaw) | Public OpenClaw repository. |
| ASE | [OpenClaw skills catalog](https://agentskillexchange.com/browse-skills/?framework=OpenClaw) | Live ASE view of OpenClaw skills. |

## Skill Guidance

OpenClaw skills should state:

- provider/runtime assumptions
- whether the task is interactive or scheduled
- command and file boundaries
- health checks
- when to notify a channel

## Skill Patterns That Fit OpenClaw

- scheduled checks and crons
- provider and runtime setup
- workspace backup and restore
- channel-based operational workflows
- post-run health reporting

## Representative ASE Examples

- `run-day-2-openclaw-operations-with-production-runbooks-and-reusable-prompt-patterns-from-openclaw-runbook`
- `back-up-and-restore-an-openclaw-workspace-to-synology-nas-with-verification-and-rollback-safety-using-synology-backup`
- `deploy-an-agent-readable-openclaw-defense-matrix-and-hardening-audit-with-openclaw-security-practice-guide`
- `mirror-and-back-up-openclaw-workspaces-to-your-own-storage-with-openclaw-workspace-sync`

## Common Mistakes

- Building a cron skill without a clear success contract.
- Treating notification as success instead of verifying the underlying work.
- Hiding provider or auth assumptions.
