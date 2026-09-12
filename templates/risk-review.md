# Risk Review

Use this review before a pilot touches real repos, data, users, or production
systems.

## Context

- Skill/workflow:
- Reviewer:
- Date:
- Pilot owner:

## Access Review

| Area | Needed? | Scope | Risk | Mitigation |
|---|---|---|---|---|
| Data access | [ ] yes / [ ] no |  |  |  |
| Repo access | [ ] yes / [ ] no |  |  |  |
| Production access | [ ] yes / [ ] no |  |  |  |
| User/customer impact | [ ] yes / [ ] no |  |  |  |
| Dependency risk | [ ] yes / [ ] no |  |  |  |
| Model/provider risk | [ ] yes / [ ] no |  |  |  |

## Human Approval

- Approval required before:
- Approver:
- Approval record location:

Checklist:

- [ ] Read-only access is used where possible.
- [ ] Production writes require explicit approval.
- [ ] Customer/user impact is documented.
- [ ] Dependency and provider risks have owners.

## Open Risks

```text

```

## Decision Note From Evidence

Before choosing a decision, summarize the review in a note that someone else
can scan without reopening every artifact.

- Workflow reviewed:
- Evidence compared:
- Permission or access boundary:
- Approval or mitigation still needed:
- Decision owner and review date:

## Decision

- [ ] Accept for sandbox
- [ ] Accept for limited team
- [ ] Block until mitigated

Reason:

```text

```

## Exit Handoff

Use the decision above to open the next artifact instead of leaving the review
as a standalone note.

| Decision | Next artifact | Carry forward |
|---|---|---|
| Accept for sandbox | [Pilot Plan](pilot-plan.md) | Scope limit, owner, approval gate, and rollback condition. |
| Accept for limited team | [Rollout Readiness](rollout-readiness.md) | Remaining risks, monitoring owner, training need, and expansion limit. |
| Block until mitigated | [Security Review](security-review.md) or this review again | Blocking risk, required mitigation, evidence owner, and review date. |
