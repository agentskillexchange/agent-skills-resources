# Post-Pilot Review

Use this template after a pilot finishes so the next decision is based on
evidence rather than momentum.

## Pilot Summary

- Workflow:
- Skill slugs:
- Pilot owner:
- Team:
- Dates:

## What Worked

```text

```

## What Failed

```text

```

## Time Saved Or Lost

- Estimated time saved:
- New review/cleanup time:
- Net effect:

Evidence:

```text

```

## Quality Issues

- Incorrect output:
- Missing context:
- Test/verification gaps:
- Rework needed:

## Safety Issues

- Permissions issue:
- Secrets/logging issue:
- Unsafe command or network action:
- Human approval issue:

## Criteria Check

Compare the pilot evidence against the criteria from
[`pilot-plan.md`](pilot-plan.md) before choosing the next decision.

- Success criterion met:
- Failure condition triggered:
- Safety criterion met:
- Evidence still missing:
- Rollback path tested or not needed:

## Next Decision

- [ ] Stop using
- [ ] Revisit with changes
- [ ] Continue limited pilot
- [ ] Expand rollout

Reason and next action:

```text

```

### Choose From The Measured Evidence

Use the criteria check above to make one explicit post-pilot choice before
opening rollout readiness. Do not let an encouraging demo outweigh a failed
safety condition, missing evidence, or an untested rollback path.

| What the pilot evidence shows | Choose | Next artifact or action |
|---|---|---|
| A failure or safety criterion was triggered, or the workflow cannot be made safe within the agreed pilot boundary. | `Stop using` | Record the blocker and cleanup owner below; do not open rollout readiness. |
| The workflow is still promising, but one bounded fix, missing proof, or narrower scope must be tested. | `Revisit with changes` | Open a fresh [Pilot Plan](pilot-plan.md) with the fix and proof required for the next review. |
| Value is repeatable in the current scope, but an open risk, monitoring gap, or success criterion prevents wider access. | `Continue limited pilot` | Open a fresh [Pilot Plan](pilot-plan.md) with the narrowed scope, monitoring signal, and next criterion. |
| Success, failure, and safety criteria are met; evidence is reproducible; and ownership, monitoring, and rollback are ready for a wider stage. | `Expand rollout` | Open [Rollout Readiness](rollout-readiness.md) and carry the evidence packet forward. |

If the evidence fits more than one row, choose the more conservative decision
until the missing proof is available. `Expand rollout` is a decision to review
readiness, not permission to widen access immediately.

## Decision Packet

Before moving out of review, copy the evidence into the next artifact instead
of relying on memory from the pilot:

| If the decision is | Carry forward |
|---|---|
| Stop using | The blocker, failed criterion, and owner of any cleanup action |
| Revisit with changes | The smallest fix, the evidence that will prove it worked, and a review date |
| Continue limited pilot | The narrowed scope, remaining risk, monitoring signal, and next success criterion |
| Expand rollout | The decision reason, open issues, owner, monitoring path, and rollback trigger for [`rollout-readiness.md`](rollout-readiness.md) |

## Next Iteration Handoff

If the decision is `Revisit with changes` or `Continue limited pilot`, open a
fresh [`pilot-plan.md`](pilot-plan.md) and complete `Previous Pilot Decision`
before running the next iteration. Carry over the prior decision, the fix or
narrowed scope, the evidence that will prove the iteration worked, the
remaining risk, and the next review date.
