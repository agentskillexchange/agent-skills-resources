# Team Lead Track

## Who It Is For

Engineering leads, platform leads, security partners, and operations owners who
want to pilot agent skills with a bounded team workflow.

## Expected Time

90 minutes for planning, plus the pilot window your team chooses.

## Prerequisites

- A workflow with a clear owner.
- A sandbox or low-risk test environment.
- A human approval path for risky actions.
- A way to collect logs, outputs, or review evidence.

## Recommended Order

1. [Team Adoption Basics](team-adoption-basics.md)
2. [Team Evaluation Starter Kit](../starter-kits/team-evaluation.md)
3. [Adoption Matrix](../adoption-matrix.md)
4. [Playbooks](../playbooks/)
5. [Showcase Workflow Stacks](../showcase/)
6. [Team Pilot Readiness Checklist](../checklists/team-pilot-readiness.md)
7. [Pilot Plan Template](../templates/pilot-plan.md)
8. [Rollout Readiness Template](../templates/rollout-readiness.md)
9. [Rollout Evidence Log](../ops/rollout-evidence.md) and
   [Security Rollout Checklist](../security/security-rollout-checklist.md)

## Practice Exercise

Choose one pilot workflow and define:

- pilot owner
- users included
- systems touched
- success criteria
- human approval gate
- rollback path
- review date

Before writing the pilot plan, compare the workflow with the
[completed evaluation examples](../examples/completed-evaluations/README.md).
Copy the closest evidence pattern into the team worksheet so the pilot starts
with reviewer notes, approval records, command output, rollback notes, or
editorial checks already in view.

## What Good Looks Like

- The first pilot is small and observable.
- Risky actions require human approval.
- Success criteria include quality and safety, not only speed.
- The team knows when to stop, revise, or expand.

## After The Pilot: Communicate One Defensible Decision

When the pilot window ends, complete the
[Post-Pilot Review](../templates/post-pilot-review.md) before telling the team
what happens next. Share the decision as a short, evidence-backed update—not
as a summary of every pilot discussion:

1. State one decision: `Stop using`, `Revisit with changes`, `Continue limited
   pilot`, or `Expand rollout`.
2. Name the measured result and the most important remaining risk or failed
   criterion.
3. Name the owner and next review date, or the cleanup owner when stopping.
4. Link the next artifact so someone else can verify the handoff.

| Decision | Tell stakeholders | Link next |
|---|---|---|
| Stop using | The boundary that failed, cleanup owner, and what proof would be needed before reconsidering. | [Post-Pilot Review](../templates/post-pilot-review.md) |
| Revisit with changes | The smallest fix, the proof required, and when the same boundary will be reviewed again. | [Pilot Plan](../templates/pilot-plan.md) |
| Continue limited pilot | The unchanged or narrowed scope, monitoring signal, and next success criterion. | [Pilot Plan](../templates/pilot-plan.md) |
| Expand rollout | The measured reason, open issues, accountable owner, and rollback trigger; expansion is still subject to readiness review. | [Rollout Readiness](../templates/rollout-readiness.md) |

Keep the detailed evidence in the linked artifact. The update is a route to
that record, not a substitute for it.

## Common Mistakes

- Starting with a production workflow.
- Adding too many skills at once.
- Skipping ownership, monitoring, or rollback.

## Next Step

Fill out [Pilot Plan](../templates/pilot-plan.md), then use
[Rollout Readiness](../templates/rollout-readiness.md) after the pilot. If the
decision is `Go`, carry the monitoring owner, review cadence, rollback trigger,
and artifact/log location into [Rollout Evidence](../ops/rollout-evidence.md);
use the [Security Rollout Checklist](../security/security-rollout-checklist.md)
before widening access for production-sensitive workflows.
