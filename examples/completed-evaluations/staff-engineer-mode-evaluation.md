# Staff Engineer Mode Evaluation

This is an illustrative completed worksheet, not a certification claim.

## Skill

- Skill slug: `staff-engineer-mode`
- Workflow: coding-agent review and implementation judgment
- Source of example: representative mapping in `data/ase-skill-mapping.json`
- Decision: pilot

## Workflow Fit

The skill fits teams that want a consistent senior-engineering review posture
for design tradeoffs, implementation risk, and maintainability review before or
during coding-agent work.

## Permissions Reviewed

- Repo access: read/write only for the pilot branch.
- Production access: not needed.
- Data access: not needed.
- Human approval: required before broad refactors, dependency changes, or
  destructive git actions.

## Verification Evidence Example

```text
Pilot branch: example/review-loop
Checks requested: unit tests, lint, PR diff review
Expected evidence: commands run, changed files, unresolved risks, reviewer notes
```

## Risk Review Summary

- Main risk: agent over-expands review scope into unrelated refactors.
- Mitigation: constrain pilot to one PR and require explicit approval for
  scope changes.
- Open question: whether the team wants the skill used during planning,
  implementation, or final review.

## Why A Team Might Pilot It

- The workflow is narrow enough for a low-risk pilot.
- It does not need production credentials.
- Review evidence can be inspected by human reviewers.

## Why A Team Might Reject It

- The repo has no tests or reviewer ownership.
- The team needs task execution more than review judgment.
- The pilot cannot define what good review output looks like.
