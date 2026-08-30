# Showcase Workflow Stacks

These showcase stacks combine framework guidance, representative ASE skills,
pilot notes, and verification evidence. They are examples for planning and
evaluation, not a replacement for the canonical
[agentskillexchange/skills](https://github.com/agentskillexchange/skills)
catalog.

## Choose A Workflow Stack By Outcome

Start with the outcome you need to prove, then open the closest stack for the
frameworks, representative skills, pilot notes, and verification evidence to
compare.

| Outcome to prove | Start with | Why this stack fits |
|---|---|---|
| A coding agent can review PRs without losing engineering context | [Coding Agent PR Review](coding-agent-pr-review-stack.md) | Connects coding-agent runtimes, review skills, and review evidence. |
| An agent can inspect databases through bounded MCP access | [MCP Database Inspection](mcp-database-inspection-stack.md) | Combines MCP tooling, database access boundaries, and evaluation notes. |
| Risky agent actions can pause for human approval | [Security Approval](security-approval-stack.md) | Focuses on approval gates, sandboxing, and high-risk workflow controls. |
| On-call teams can triage incidents with observable evidence | [SRE Incident Triage](sre-incident-triage-stack.md) | Joins runbooks, cluster signals, logs, and incident-triage skills. |
| Research workflows can keep citations and source checks visible | [Content Research](content-research-stack.md) | Pairs research agents with citation-heavy review expectations. |
| Runtime operators can keep OpenClaw workflows recoverable | [Runtime Ops: OpenClaw](runtime-ops-openclaw-stack.md) | Covers backups, hardening, scheduled ops, and rollback evidence. |

## High-Risk Proof Ladder

For high-risk stacks, do not treat a pilot as shareable just because the
workflow ran once. Use this ladder to decide which evidence the stack page
must help you collect before turning a private run into a team example.

| If the stack controls | Share only after you can show | Start with |
|---|---|---|
| Risky code, commands, dependencies, or approvals | Risk class, approval decision, sandbox or guardrail evidence, and final allow/revise/block outcome | [Security Approval](security-approval-stack.md#evidence-readiness-check) |
| Incident triage over logs, metrics, Kubernetes, or cloud signals | Alert context, read-only commands, supporting evidence, accepted or rejected hypotheses, and the final human decision | [SRE Incident Triage](sre-incident-triage-stack.md#evidence-readiness-check) |
| Runtime operations, backups, cron jobs, config, or rollback | Health check, restore proof, config diff, cron log, rollback command, owner approval, and keep/change/rollback decision | [Runtime Ops: OpenClaw](runtime-ops-openclaw-stack.md#evidence-readiness-check) |

## Medium-Risk Evidence Chooser

Medium-risk stacks can become useful team examples sooner, but only if the
artifact proves what happened, what was checked, and who accepted the result.

| If the stack demonstrates | Bring this minimum packet | Start with |
|---|---|---|
| Coding-agent PR review | Original review comment, exact file change, verification output, unresolved risk, and reviewer decision | [Coding Agent PR Review](coding-agent-pr-review-stack.md#evidence-readiness-check) |
| Read-only database inspection through MCP | MCP config, credential scope, queries and row limits, SQL validation, and data owner approval | [MCP Database Inspection](mcp-database-inspection-stack.md#verification-evidence-to-collect) |
| Cited content or research drafting | Source list, citation coverage, unsupported-claim notes, editorial comments, and publish or reject decision | [Content Research](content-research-stack.md#verification-evidence-to-collect) |

| Stack | Team / persona | Risk level | Primary surfaces | Representative skills | Page |
|---|---|---|---|---|---|
| Coding Agent PR Review | Engineering teams, tech leads | Medium | Codex, Claude Code, GitHub Copilot, Cursor | `staff-engineer-mode`, `address-github-pr-review-comments-from-the-current-branch-with-gh-address-comments` | [Stack](coding-agent-pr-review-stack.md) |
| MCP Database Inspection | Data engineers, platform teams | Medium | MCP, Postgres, LangChain/LangGraph | `postgresql-mcp-server`, `query-and-inspect-postgres-databases-through-mcp-with-pgedge-postgres-mcp` | [Stack](mcp-database-inspection-stack.md) |
| Security Approval | Security teams, engineering managers | High | Human approval, sandboxing, guardrails | `route-risky-coding-agent-work-through-human-approval-checkpoints-with-humanlayer`, `run-agent-generated-code-in-local-microvm-sandboxes-with-microsandbox` | [Stack](security-approval-stack.md) |
| SRE Incident Triage | SRE, platform, on-call engineers | High | Kubernetes, observability, runbooks | `investigate-production-incidents-across-kubernetes-and-cloud-signals-with-holmesgpt`, `tail-multi-pod-kubernetes-logs-by-label-during-incidents-with-stern` | [Stack](sre-incident-triage-stack.md) |
| Content Research | Research, content, docs teams | Medium | Research agents, citation workflows | `draft-cited-research-reports-with-storm`, `run-autonomous-deep-research-workflows-with-gpt-researcher` | [Stack](content-research-stack.md) |
| Runtime Ops: OpenClaw | Agent runtime operators | High | OpenClaw, backups, hardening, scheduled ops | `run-day-2-openclaw-operations-with-production-runbooks-and-reusable-prompt-patterns-from-openclaw-runbook`, `back-up-and-restore-an-openclaw-workspace-to-synology-nas-with-verification-and-rollback-safety-using-synology-backup` | [Stack](runtime-ops-openclaw-stack.md) |

## How To Use These

1. Pick the closest workflow stack.
2. Open the referenced framework and starter-kit pages.
3. Inspect each representative ASE skill in the canonical catalog.
4. Run a bounded pilot and capture evidence before expanding scope.

Use the [Team Evaluation Starter Kit](../starter-kits/team-evaluation.md) and
[Evaluation Templates](../templates/) to record the pilot.
