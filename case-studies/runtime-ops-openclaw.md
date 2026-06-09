# Runtime Ops: OpenClaw

## Practical Scenario

A team runs an agent runtime with scheduled work, provider configuration,
workspace state, and operational runbooks. They want skills that make day-2
operations repeatable without hiding risk.

## Relevant ASE Skill Examples

| Skill | Role in the workflow |
|---|---|
| `run-day-2-openclaw-operations-with-production-runbooks-and-reusable-prompt-patterns-from-openclaw-runbook` | Captures recurring OpenClaw operations as runbook-backed skill workflows |
| `back-up-and-restore-an-openclaw-workspace-to-synology-nas-with-verification-and-rollback-safety-using-synology-backup` | Adds backup, restore, verification, and rollback safety |
| `deploy-an-agent-readable-openclaw-defense-matrix-and-hardening-audit-with-openclaw-security-practice-guide` | Connects runtime security posture to audit-friendly guidance |
| `mirror-and-back-up-openclaw-workspaces-to-your-own-storage-with-openclaw-workspace-sync` | Keeps workspace continuity visible and recoverable |

## How They Fit Together

1. Use runbook skills for routine provider, runtime, and cron operations.
2. Back up workspace state before risky changes.
3. Review the hardening matrix before exposing new tools or channels.
4. Mirror critical workspace state so recovery is not tied to one host.

## Setup Considerations

- Runtime credentials should be documented without exposing secret values.
- Backup jobs should include restore verification, not only copy success.
- Cron/runbook changes should include expected outcome and rollback notes.
- Provider and model changes should be tested before production schedules use
  them.

## Security And Trust Considerations

- Avoid logging API keys, OAuth tokens, or private chat payloads.
- Treat runtime write access as privileged production access.
- Separate monitoring recommendations from actual config mutations.
- Keep a human-owned rollback path for gateway, provider, and cron changes.

## What To Evaluate Before Adopting

- Can the skill explain what changed and how to reverse it?
- Does backup verification run against real restored state?
- Are runtime permissions scoped to the task?
- Are scheduled jobs observable when they fail?

## Related Pages

- [OpenClaw](../frameworks/openclaw.md)
- [Best Practices](../best-practices.md)
- [Freshness Audit](../maintenance/freshness-audit.md)
- [ASE Verification](https://github.com/agentskillexchange/skills/tree/main/verification)
