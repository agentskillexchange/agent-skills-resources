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

## Choose The Closest Example Pattern

Before copying the scaffold, choose one annotated example that matches the job
shape of your skill:

| If your skill mainly helps an agent... | Start from this example pattern |
|---|---|
| Make engineering or review decisions | Coding and review |
| Connect to a tool, API, database, or MCP server | MCP tool connection or data platform |
| Investigate live operational state | SRE and incident ops or OpenClaw runtime ops |
| Pause for approval before risky actions | Security and guardrails |
| Research, cite, or synthesize claims | Content and research |
| Persist memory, schedules, or long-running context | Hermes / emerging runtime |

Use the matching [annotated example](../examples/annotated-skill-examples.md)
for workflow shape, setup evidence, and verification posture. Do not copy its
slug, metadata, or tool choice unless your source-backed skill genuinely shares
that context.

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

## Build The First Evidence Packet

Before asking for review, turn the scaffold into a short evidence packet:

| Scaffold field | Evidence to bring into review |
|---|---|
| Upstream source | Link to the official repo, docs, package, API reference, or workflow owner. |
| Required tool/account | Show the install command, account prerequisite, or provider setup path a reviewer can try. |
| Secret or permission | Name the minimum token, role, data access, or approval needed before the workflow writes anywhere. |
| Read-only inspection step | Show the first command, file, log, issue, trace, or record the agent should inspect before changing state. |
| Verification | Save the pass signal, failure signal, and blocked handoff in language a reviewer can copy into the [First Skill Review Checklist](../checklists/first-skill-review.md). |

If one row is empty, repair the draft before review. If every row has concrete
evidence, carry the packet into the review checklist instead of rewriting the
same rationale from memory.

## Representative ASE Examples

- [`staff-engineer-mode`](https://agentskillexchange.com/skills/staff-engineer-mode/)
- [`draft-cited-research-reports-with-storm`](https://agentskillexchange.com/skills/draft-cited-research-reports-with-storm/)
- [`query-and-inspect-postgres-databases-through-mcp-with-pgedge-postgres-mcp`](https://agentskillexchange.com/skills/query-and-inspect-postgres-databases-through-mcp-with-pgedge-postgres-mcp/)
- [`run-day-2-openclaw-operations-with-production-runbooks-and-reusable-prompt-patterns-from-openclaw-runbook`](https://agentskillexchange.com/skills/run-day-2-openclaw-operations-with-production-runbooks-and-reusable-prompt-patterns-from-openclaw-runbook/)

## Review Your Draft

Before publishing or submitting a new skill, run a quick pass with the
[First Skill Review Checklist](../checklists/first-skill-review.md). A first
draft is ready for deeper evaluation when the reviewer can identify the source,
setup path, permissions, verification evidence, and safety-sensitive actions
without inferring them from the skill title.

## Safety Reminders

- Do not call a third-party project official unless ownership proves it.
- Do not include stale stars or downloads unless refreshed and sourced.
- Do not use generic copy-folder installation as the main install guidance.
- Downgrade or reject skills that cannot explain setup, permissions, and
  verification.
