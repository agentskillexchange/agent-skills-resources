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

## Choose Risk Or Security Review

Use the smaller review unless the pilot crosses both boundaries:

| Pilot touches | Open | Evidence to capture |
|---|---|---|
| Real repos, business data, production scope, user/customer impact, dependencies, or model/provider choices | [Risk Review](risk-review.md) | Access scope, owner, mitigation, approval gate, and open risks. |
| Commands, network access, secrets, generated code, logs, sandboxing, or supply-chain controls | [Security Review](security-review.md) | Reviewed commands, destinations, secret handling, isolation, scan result, and approval record. |
| Both pilot scope and technical execution controls | [Risk Review](risk-review.md), then [Security Review](security-review.md) | Decide whether the pilot should proceed at all before checking how it can run safely. |

## Team Lead Artifact Sequence

Use this sequence when a visitor is moving from one reviewed skill to a team
pilot:

1. Start with the
   [Team Pilot Readiness Checklist](../checklists/team-pilot-readiness.md) to
   confirm the workflow, owner, approval gate, rollback path, and review date.
2. Open the [Pilot Plan](pilot-plan.md) only after the readiness checklist has a
   narrow sandbox or limited-team decision.
3. Use [Post-Pilot Review](post-pilot-review.md) when the pilot window ends, so
   stop, revisit, continue, or expand decisions are tied to evidence.
4. Use [Rollout Readiness](rollout-readiness.md) only for a continue or expand
   decision that needs more users, stronger ownership, monitoring, or rollback
   evidence.
5. Carry approved expansion evidence into
   [Rollout Evidence](../ops/rollout-evidence.md) before widening production or
   team access.

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
