# Skill Evaluation Worksheet

Use this worksheet to decide whether one skill should be rejected, revisited, or
piloted.

## Compare A Nearby Example First

Before filling the blank worksheet, open the completed evaluation that most
resembles your workflow and copy only the evidence shape, not the decision:

| Your workflow looks like | Compare against |
|---|---|
| Cited content or research review | [Content Research](../examples/completed-evaluations/content-research-evaluation.md) |
| Coding-agent review or PR feedback | [Staff Engineer Mode](../examples/completed-evaluations/staff-engineer-mode-evaluation.md) |
| Human approval for risky actions | [HumanLayer Approval Workflow](../examples/completed-evaluations/humanlayer-approval-workflow-evaluation.md) |
| Read-only MCP or database inspection | [MCP Database Inspection](../examples/completed-evaluations/mcp-database-inspection-evaluation.md) |
| Day-2 operations or runtime checks | [OpenClaw Runtime Ops](../examples/completed-evaluations/openclaw-runtime-ops-evaluation.md) |

## Skill

- Skill slug:
- Skill page:
- Source URL:
- Framework/runtime:
- Evaluator:
- Date:

## Workflow Fit

- Target workflow:
- Team/user:
- Trigger for using the skill:
- Expected output:

Checklist:

- [ ] The skill maps to a real repeated workflow.
- [ ] The workflow is narrow enough for a first pilot.
- [ ] The skill is not only a category label or generic prompt.

Evidence:

```text

```

## Install And Setup Clarity

- Required tools:
- Required accounts/API keys:
- Setup steps are:
  - [ ] clear
  - [ ] incomplete
  - [ ] not applicable

Evidence:

```text

```

## Permissions Needed

- Repo access:
- Data access:
- Network access:
- Production access:
- Human approval needed:

## Verification Steps

- Tests/checks to run:
- Expected pass signal:
- Logs or artifacts to save:

## Risks

- Main risk:
- Data/security concern:
- Operational concern:
- Mitigation:

## Decision

- [ ] Reject
- [ ] Revisit later
- [ ] Pilot

Decision reason:

```text

```

## Pilot Planning Handoff

Complete this only when the decision is `Pilot`, then open
[`pilot-plan.md`](pilot-plan.md) and carry forward the evidence below.

- Workflow and team from `Workflow Fit`:
- Required tools, accounts, and approvals from `Install And Setup Clarity` and
  `Permissions Needed`:
- Verification signal to reuse as pilot success evidence:
- Risk that must become a pilot guardrail:

Pilot-plan next step:

- [ ] Convert this worksheet into a bounded sandbox, limited-team, or production-candidate pilot plan.
