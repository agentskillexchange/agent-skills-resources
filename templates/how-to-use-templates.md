# How To Use Templates

Use these templates as a small evidence trail for skill evaluation. Pick the
smallest template that matches the decision in front of the team.

## Suggested Flow

1. Start with the [Skill Evaluation Worksheet](skill-evaluation-worksheet.md)
   for each candidate skill.
2. Use the [Pilot Plan](pilot-plan.md) when one workflow is ready for a bounded
   trial.
3. Fill out [Risk Review](risk-review.md) and
   [Security Review](security-review.md) before touching real repos, data, or
   production systems.
4. Use [Rollout Readiness](rollout-readiness.md) before moving from sandbox to
   limited team or production.
5. Finish with [Post-Pilot Review](post-pilot-review.md) so the next team can
   learn from the pilot.

## Choose The Next Template

Use the evidence you already have to pick the next artifact:

| Current evidence | Open next | Why |
|---|---|---|
| Promising skill, but no reviewer notes yet | [Skill Evaluation Worksheet](skill-evaluation-worksheet.md) | Records source, setup, permissions, verification, risks, and the first decision. |
| Worksheet shows one narrow workflow with an owner | [Pilot Plan](pilot-plan.md) | Turns the review into a bounded trial with success criteria and rollback. |
| Pilot needs real repos, data, commands, networks, or approvals | [Risk Review](risk-review.md) or [Security Review](security-review.md) | Captures the controls a team should review before the trial leaves a sandbox. |
| Pilot evidence supports adding more users | [Rollout Readiness](rollout-readiness.md) | Checks ownership, monitoring, rollback, training, and expansion limits. |
| Pilot finished or was rejected | [Post-Pilot Review](post-pilot-review.md) | Preserves the decision and evidence so the next team does not restart from memory. |

## How This Connects To The Repo

- Use [Playbooks](../playbooks/) to choose a team-specific adoption path.
- Use [Case Studies](../case-studies/) to see how multiple skills can fit
  together.
- Use [Adoption Matrix](../adoption-matrix.md) to compare risk and rollout
  levels.
- Use [Quality Checklist](../examples/quality-checklist.md) when a skill seems
  promising but needs closer review.

## Evidence Standard

Good evidence is short and replayable:

- command run, result, and date
- source URL or skill slug
- reviewer or owner
- approval or rejection reason
- open risk and next action

Avoid vague notes like "works well" or "seems safe" without the check that
supports the decision.
