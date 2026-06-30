# Skill Author Starter Kit

## Who This Is For

People writing, reviewing, or improving source-backed agent skills for a public
or internal catalog.

## First 15 Minutes

1. Read [best-practices.md](../best-practices.md).
2. Review [examples/quality-checklist.md](../examples/quality-checklist.md).
3. Inspect [annotated examples](../examples/annotated-skill-examples.md).
4. Pick one real upstream tool, repo, API, or workflow.

## First Useful Workflow

Draft a skill around one concrete job:

1. Define the repeated task.
2. Link to the upstream source.
3. Write install/setup steps that install the real tool.
4. Add one usage flow and one verification step.
5. Name permissions, secrets, and stop conditions.
6. Avoid broad compatibility claims unless you tested them.

## Copyable First Skill Scaffold

Use this outline before writing a full skill. Keep every line grounded in a
source, command, workflow, or observable result.

```markdown
# Skill Name

## Use When

- The user needs to [specific repeated job].
- The upstream project, API, or workflow is [source link].

## Before You Start

- Required tool/account:
- Required secret or permission:
- Read-only inspection step:
- Stop or approval checkpoint:

## Workflow

1. Inspect [inputs, files, logs, docs, or records].
2. Run [lowest-risk command or tool action].
3. Make [bounded change or recommendation].
4. Capture evidence in [test output, logs, citations, screenshots, or records].

## Verification

- Pass condition:
- Failure condition:
- Handoff if verification is blocked:
```

## Representative ASE Examples

- [`staff-engineer-mode`](https://agentskillexchange.com/skills/staff-engineer-mode/)
- [`draft-cited-research-reports-with-storm`](https://agentskillexchange.com/skills/draft-cited-research-reports-with-storm/)
- [`query-and-inspect-postgres-databases-through-mcp-with-pgedge-postgres-mcp`](https://agentskillexchange.com/skills/query-and-inspect-postgres-databases-through-mcp-with-pgedge-postgres-mcp/)
- [`run-day-2-openclaw-operations-with-production-runbooks-and-reusable-prompt-patterns-from-openclaw-runbook`](https://agentskillexchange.com/skills/run-day-2-openclaw-operations-with-production-runbooks-and-reusable-prompt-patterns-from-openclaw-runbook/)

## Safety Reminders

- Do not call a third-party project official unless ownership proves it.
- Do not include stale stars or downloads unless refreshed and sourced.
- Do not use generic copy-folder installation as the main install guidance.
- Downgrade or reject skills that cannot explain setup, permissions, and
  verification.
