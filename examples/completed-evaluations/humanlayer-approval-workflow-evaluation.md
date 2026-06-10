# HumanLayer Approval Workflow Evaluation

This is an illustrative completed worksheet, not a certification claim.

## Skill

- Skill slug: `route-risky-coding-agent-work-through-human-approval-checkpoints-with-humanlayer`
- Workflow: human approval gates for risky coding-agent actions
- Source of example: representative mapping in `data/ase-skill-mapping.json`
- Decision: pilot with security review

## Workflow Fit

The skill fits workflows where agents can continue routine work but must pause
before risky actions such as production changes, broad repo edits, dependency
updates, or privileged commands.

## Permissions Reviewed

- Repo access: limited to a non-production pilot repo.
- Production access: blocked during first pilot.
- Network access: limited to approval channel and repo tooling.
- Human approval: required for any risky action defined in the pilot plan.

## Verification Evidence Example

```text
Pilot scenario: dependency update request with approval gate
Expected evidence: approval request, approver identity, decision timestamp,
blocked action if approval is denied
```

## Risk Review Summary

- Main risk: treating approval records as a replacement for code review.
- Mitigation: require both approval evidence and normal PR review.
- Open question: which actions belong in the mandatory approval list.

## Why A Team Might Pilot It

- It directly addresses agent safety and accountability.
- The first pilot can be run without production access.
- Approval evidence is concrete and reviewable.

## Why A Team Might Reject It

- The team lacks a clear approver or escalation path.
- The approval channel cannot retain records.
- The workflow would put secrets or sensitive payloads into approval messages.
