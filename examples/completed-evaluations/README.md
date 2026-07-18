# Completed Evaluation Examples

These examples show what lightweight evaluation evidence can look like. They
are illustrative only and are not certification claims about the underlying
skills.

Each example references an existing public ASE skill slug from
`data/ase-skill-mapping.json` without duplicating the full skill body.

| Example | Workflow |
|---|---|
| [Staff Engineer Mode](staff-engineer-mode-evaluation.md) | Coding-agent review posture |
| [HumanLayer Approval Workflow](humanlayer-approval-workflow-evaluation.md) | Human approval gates for risky actions |
| [OpenClaw Runtime Ops](openclaw-runtime-ops-evaluation.md) | Day-2 runtime operations |

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
