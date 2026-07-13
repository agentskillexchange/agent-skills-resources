# Rollout Readiness

Use this template before expanding a skill workflow beyond the current pilot
stage.

## Rollout Context

- Workflow:
- Pilot owner:
- Current stage:
- Proposed next stage:
- Decision date:

## Results

- Sandbox result:
- Limited-team result:
- Verification evidence:
- Open issues:

Checklist:

- [ ] Sandbox result is recorded.
- [ ] Limited-team result is recorded or not applicable.
- [ ] Verification evidence is reproducible.
- [ ] Owner is assigned.
- [ ] Monitoring path is defined.
- [ ] Rollback path is tested or documented.

## Ownership

- Workflow owner:
- Security owner:
- Operations owner:
- Escalation channel:

## Monitoring

- Success signal:
- Failure signal:
- Review cadence:
- Artifact/log location:

## Rollback

- Rollback trigger:
- Rollback owner:
- Rollback steps:

## Go/No-Go Decision

- [ ] Go
- [ ] No-go
- [ ] Revisit

Decision reason:

```text

```

## Production Review Handoff

If the decision is `Go`, copy the monitoring owner, review cadence, rollback
trigger, and artifact/log location into
[`../ops/rollout-evidence.md`](../ops/rollout-evidence.md) so the expanded
workflow has a durable review record. For workflows with production data,
privileged tools, external actions, or security approvals, also complete
[`../security/security-rollout-checklist.md`](../security/security-rollout-checklist.md)
before widening access.
