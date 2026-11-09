# Evaluation Templates

Use these templates when a team is moving from reading about agent skills to
evaluating a real pilot. They are intentionally lightweight and should be copied
into an issue, document, or internal review packet.

| Template | Use it for |
|---|---|
| [How To Use Templates](how-to-use-templates.md) | Choosing the right template for a pilot stage |
| [Skill Evaluation Worksheet](skill-evaluation-worksheet.md) | Reviewing one skill before pilot selection |
| [Pilot Plan](pilot-plan.md) | Defining pilot owner, scope, success criteria, and rollback |
| [Risk Review](risk-review.md) | Recording data, repo, production, dependency, and model risks |
| [Security Review](security-review.md) | Checking secrets, commands, network, generated code, and evidence |
| [Rollout Readiness](rollout-readiness.md) | Deciding whether to expand beyond a pilot |
| [Post-Pilot Review](post-pilot-review.md) | Capturing what worked, what failed, and next decision |

## First Run Evidence Packet

For a first team trial, keep the packet small enough to finish in one review:

1. Copy the [Skill Evaluation Worksheet](skill-evaluation-worksheet.md) for the
   skill, workflow fit, setup, permissions, verification steps, risks, and
   decision.
2. Add a [Pilot Plan](pilot-plan.md) only after the worksheet points to a
   narrow workflow with a named owner and rollback path.
3. Use [Risk Review](risk-review.md) or [Security Review](security-review.md)
   when the pilot touches real repos, data, commands, networks, or approvals.
4. When the pilot ends, complete [Post-Pilot Review](post-pilot-review.md)
   before considering any wider stage.

Keep the evidence short, specific, and reproducible.

## After A Pilot: Keep The Evidence Moving

Use this order after a bounded pilot, so a promising result does not quietly
turn into wider access without a decision, owner, monitoring, and rollback
record.

| Stage | Open next | Carry forward |
|---|---|---|
| Pilot ends | [Post-Pilot Review](post-pilot-review.md) | Measured success, failure, safety, and any open evidence gap. |
| Decision is `Expand rollout` | [Rollout Readiness](rollout-readiness.md) | Decision reason, open issues, owner, monitoring path, and rollback trigger. |
| Readiness decision is `Go` | [Rollout Evidence](../ops/rollout-evidence.md) | Monitoring owner, review cadence, rollback trigger, and artifact/log location. |

For `Stop using`, `Revisit with changes`, or `Continue limited pilot`, do not
open rollout readiness: follow the next action recorded in the post-pilot
review and keep the scope bounded.
