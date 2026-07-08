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
4. Before expanding beyond the first pilot, complete
   [Rollout Readiness](rollout-readiness.md) and finish with
   [Post-Pilot Review](post-pilot-review.md).

Keep the evidence short, specific, and reproducible.
