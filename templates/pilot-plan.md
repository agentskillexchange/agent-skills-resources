# Pilot Plan

Use this template to define a bounded skill pilot before the team runs it on
real work.

## Pilot Basics

- Pilot owner:
- Team:
- Workflow:
- Review date:
- Pilot stage:
  - [ ] sandbox
  - [ ] limited team
  - [ ] production candidate

## Starting Skill Examples

- Skill slug 1:
- Skill slug 2:
- Skill slug 3:

Why these skills:

```text

```

## Completed Evaluation Starting Point

Complete this when a [completed evaluation](../examples/completed-evaluations/README.md)
helped the team choose a pilot. Use the example as an evidence shape, not as an
endorsement; complete the worksheet before turning it into this plan.

| Completed-evaluation evidence | Preserve in this pilot plan |
|---|---|
| `Skill` and `Workflow Fit` | `Starting Skill Examples`, `Pilot Basics`, and the bounded workflow. |
| `Permissions Reviewed` | `Review Constraints To Carry Forward` and `Sandbox Scope`. |
| `Verification Evidence Example` | `Success Criteria` and the evidence expected from the pilot. |
| Decision, mitigation, or open question | The pilot guardrail, rollback trigger, or blocking condition. |

- Completed evaluation used:
- What differs in this team's workflow or risk boundary:
- Evidence the team must collect before expanding beyond the pilot:

## Evaluation Worksheet Handoff

Complete this when the pilot starts from `skill-evaluation-worksheet.md`.

- Worksheet decision reason:
- Workflow and team to pilot:
- Setup or approval evidence to preserve:
- Verification signal to reuse:
- Risk that must become a guardrail:

## Previous Pilot Decision

Complete this when the plan is a follow-up to a post-pilot `Revisit with
changes` or `Continue limited pilot` decision.

- Prior decision:
- Change or narrowed scope to test:
- Evidence that will prove this iteration worked:
- Remaining risk or blocker:
- Next review date:

## Review Constraints To Carry Forward

Complete this when the pilot follows a risk review, security review, or both.

- Approved scope:
- Allowed commands/data/systems:
- Required approval gate:
- Rollback trigger:
- Next review date:
- Blocking condition that stops the pilot:

## Sandbox Scope

- Test repo/data/system:
- Allowed actions:
- Disallowed actions:
- Required approvals:

## Success Criteria

- Quality criterion:
- Time/effort criterion:
- Safety criterion:
- Evidence expected:

Checklist:

- [ ] Success criteria are measurable.
- [ ] Failure conditions are explicit.
- [ ] Owner can stop the pilot.

## Rollback Path

- What can be reverted:
- Who can revert:
- Command or process:
- Backup/snapshot location:

## Pilot Notes

```text

```

## Pilot Exit Handoff

Before closing the pilot, copy the measured criteria, rollback result, and open
issues into the next artifact:

- Use [`post-pilot-review.md`](post-pilot-review.md) when the pilot is finished
  and the team needs to decide whether to stop, revise, continue, or expand.
- Use [`rollout-readiness.md`](rollout-readiness.md) when the pilot is a
  production candidate and the team is considering a wider rollout.
