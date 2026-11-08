# Rollout Readiness

Use this template before expanding a skill workflow beyond the current pilot
stage.

## Rollout Context

- Workflow:
- Pilot owner:
- Current stage:
- Proposed next stage:
- Decision date:

## Post-Pilot Decision

Complete this when the rollout follows an `Expand rollout` decision in
[`post-pilot-review.md`](post-pilot-review.md).

- Decision reason:
- Open issues to preserve:
- Owner:
- Monitoring path:
- Rollback trigger:

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

## Evidence Packet To Bring

Before filling out the readiness decision, gather the smallest reviewable packet
from the pilot instead of rewriting the whole history:

| Evidence from the pilot | Copy into this template |
|---|---|
| Measured success, failure, and safety criteria from [`pilot-plan.md`](pilot-plan.md) | Results and Go/No-Go decision reason |
| Stop/revise/continue/expand decision from [`post-pilot-review.md`](post-pilot-review.md) | Current stage and proposed next stage |
| Risk, security, or approval notes from [`risk-review.md`](risk-review.md) and [`security-review.md`](security-review.md) | Open issues, ownership, and rollback trigger |
| Artifact links, logs, or reviewer notes from the pilot run | Monitoring artifact/log location |

## Copyable Expand-Rollout Handoff

Use this only after [`post-pilot-review.md`](post-pilot-review.md) records an
`Expand rollout` decision. It makes the handoff reviewable: expansion stays
blocked until the named owner can monitor the next stage and execute the
rollback.

```text
Post-pilot decision: Expand rollout
Decision reason: The read-only release-note pilot met its completeness and
approval criteria across two squads; results and reviewer notes are attached.

Proposed next stage: Three squads, read-only access, with human approval before
every publication.
Open issue to preserve: The approval-log export is still manual; do not remove
the human approval boundary until its owner has tested the export.
Owner: Product Operations — owns the approval log and weekly review.
Monitoring path: Weekly completeness sample and approval-log review in
<linked review artifact>.
Rollback trigger: Any unapproved publication, out-of-bound repository access,
or two incomplete summaries in one weekly sample.
Rollback action: Pause new workflow runs, retain the log, and return to the
previous manual release-note process while the owner records the corrective
action.
```

Replace the example with the pilot's own measured evidence. A wider scope is
not ready if the monitoring path, rollback owner, or unresolved boundary is
missing.

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
