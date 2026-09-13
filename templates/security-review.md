# Security Review

Use this checklist before a skill pilot can run commands, access networks,
handle secrets, or process generated code.

## Review Basics

- Skill/workflow:
- Security reviewer:
- Date:
- Pilot owner:

## Checks

| Check | Status | Evidence |
|---|---|---|
| Secrets handling | [ ] pass / [ ] fail / [ ] n/a |  |
| Command execution | [ ] pass / [ ] fail / [ ] n/a |  |
| Network access | [ ] pass / [ ] fail / [ ] n/a |  |
| Supply-chain risk | [ ] pass / [ ] fail / [ ] n/a |  |
| Generated code handling | [ ] pass / [ ] fail / [ ] n/a |  |
| Logs/artifacts | [ ] pass / [ ] fail / [ ] n/a |  |
| Approval evidence | [ ] pass / [ ] fail / [ ] n/a |  |

## Required Evidence

- Commands reviewed:
- Network destinations:
- Secrets excluded from logs:
- Dependency scan/result:
- Sandbox or isolation method:
- Approval record:

## Blockers

```text

```

## Security Decision

- [ ] Approved for sandbox
- [ ] Approved for limited team
- [ ] Blocked

Reason:

```text

```

## Exit Handoff

Use the security decision above to keep the review moving into a concrete
artifact instead of ending as a checklist.

| Decision | Next artifact | Carry forward |
|---|---|---|
| Approved for sandbox | [Pilot Plan](pilot-plan.md) | Allowed commands, network destinations, sandbox limit, and approval record. |
| Approved for limited team | [Rollout Readiness](rollout-readiness.md) | Remaining controls, monitoring owner, log location, and expansion limit. |
| Blocked | [Risk Review](risk-review.md) or this review again | Blocking control, required mitigation, evidence owner, and review date. |
