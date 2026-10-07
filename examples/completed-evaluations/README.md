# Completed Evaluation Examples

These examples show what lightweight evaluation evidence can look like. They
are illustrative only and are not certification claims about the underlying
skills.

Each example references an existing public ASE skill slug from
`data/ase-skill-mapping.json` without duplicating the full skill body.

| Example | Workflow |
|---|---|
| [Content Research](content-research-evaluation.md) | Cited research draft with editorial review |
| [Staff Engineer Mode](staff-engineer-mode-evaluation.md) | Coding-agent review posture |
| [HumanLayer Approval Workflow](humanlayer-approval-workflow-evaluation.md) | Human approval gates for risky actions |
| [MCP Database Inspection](mcp-database-inspection-evaluation.md) | Read-only database inspection through MCP |
| [OpenClaw Runtime Ops](openclaw-runtime-ops-evaluation.md) | Day-2 runtime operations |

## Compare The Examples

Start with the row that looks closest to your own workflow, then open the
example to copy its evidence shape into a worksheet or pilot plan.

| Example | Decision pattern | Evidence to compare |
|---|---|---|
| [Content Research](content-research-evaluation.md) | Revisit until editorial evidence is complete. | Source list, citation coverage, weak-claim notes, editorial comments, publish or reject decision. |
| [Staff Engineer Mode](staff-engineer-mode-evaluation.md) | Pilot a narrow review workflow. | Checks requested, changed files, unresolved risks, reviewer notes. |
| [HumanLayer Approval Workflow](humanlayer-approval-workflow-evaluation.md) | Pilot with security review. | Approval request, approver identity, decision timestamp, denied-action behavior. |
| [MCP Database Inspection](mcp-database-inspection-evaluation.md) | Pilot in staging with data-owner review. | MCP config, credential scope, query log, SQL validation, sample result checks. |
| [OpenClaw Runtime Ops](openclaw-runtime-ops-evaluation.md) | Revisit after runbook scope is defined. | Commands inspected, config paths reviewed, no write actions, operator notes. |

## Turn Evidence Into A Decision

Use these examples as patterns for a short decision note, not as catalog
endorsements. A useful note should connect the workflow, permissions, and
verification evidence to one next action:

| Evidence pattern | Decision to record | Next artifact |
|---|---|---|
| Workflow is narrow, permissions are bounded, and verification evidence is reviewable. | Pilot | [Pilot Plan](../../templates/pilot-plan.md) |
| Workflow is useful but setup, ownership, or approval evidence is incomplete. | Revisit | [Skill Evaluation Worksheet](../../templates/skill-evaluation-worksheet.md) |
| Workflow needs production access, secrets, or broad writes before evidence exists. | Stop | [Risk Review](../../templates/risk-review.md) |
| Pilot evidence shows repeatable value and a clear rollback path. | Expand carefully | [Rollout Readiness](../../templates/rollout-readiness.md) |

## Carry Non-Pilot Decisions Forward

When an example points to `Revisit` or `Stop`, do not leave the decision as a
dead end. Copy the blocker into the
[Skill Evaluation Worksheet](../../templates/skill-evaluation-worksheet.md)
and complete its `Non-Pilot Decision Handoff` fields:

| Example outcome | Copy into the worksheet |
|---|---|
| `Revisit` because setup, ownership, approval, or verification evidence is incomplete. | Missing evidence, follow-up owner, proof needed before another review, and the revisit trigger. |
| `Stop` because safe evaluation would require production access, secrets, or broad writes first. | Blocking reason, risk owner, safer evidence needed, and the condition that would make a future review worthwhile. |

## Repair A Revisit Outcome

When a `Revisit` example matches your skill, use the blocker as a draft-repair
cue before opening another review:

| If the example blocker is about... | Repair path |
|---|---|
| Missing source, setup, permission, workflow, or verification evidence. | Use the [Skill Quality Checklist](../quality-checklist.md#repair-before-first-review) to add the missing row, then rerun the first review. |
| Unclear skill shape or thin first draft. | Return to the [Skill Author Starter Kit](../../starter-kits/skill-author.md#copyable-first-skill-scaffold) and rebuild the scaffold around one source-backed workflow. |

Do not promote a `Revisit` example into a pilot plan until the repaired draft
has a source, setup path, permission note, workflow step, and observable check a
reviewer can verify.
