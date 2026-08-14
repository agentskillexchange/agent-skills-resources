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

## Next Decision

- [ ] Stop using
- [ ] Revisit with changes
- [ ] Continue limited pilot
- [ ] Expand rollout

Reason and next action:

```text

```

## Decision Packet

Before moving out of review, copy the evidence into the next artifact instead
of relying on memory from the pilot:

| If the decision is | Carry forward |
|---|---|
| Stop using | The blocker, failed criterion, and owner of any cleanup action |
| Revisit with changes | The smallest fix, the evidence that will prove it worked, and a review date |
| Continue limited pilot | The narrowed scope, remaining risk, monitoring signal, and next success criterion |
| Expand rollout | The decision reason, open issues, owner, monitoring path, and rollback trigger for [`rollout-readiness.md`](rollout-readiness.md) |
