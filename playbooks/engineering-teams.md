# Engineering Teams

## Who This Is For

Engineering leads, staff engineers, and developers evaluating coding-agent
skills for repo review, implementation planning, and PR follow-through.

## When Agent Skills Are Useful

- Repeated PR review and comment-resolution workflows.
- Turning product specs into scoped implementation plans.
- Standardizing senior-engineer review posture across agents.

## When Not To Use Them Yet

- The repo has no tests or review owner.
- The agent needs broad production credentials to complete routine work.
- The team cannot separate planning, editing, and review steps.

## First 30-Minute Evaluation

1. Pick a low-risk PR or old review thread.
2. Inspect `staff-engineer-mode` and
   `address-github-pr-review-comments-from-the-current-branch-with-gh-address-comments`.
3. Confirm the skill explains inputs, expected output, and verification.
4. Run the workflow in read-only or dry-run mode when possible.

## First Pilot Workflow

Use `turn-notion-specs-into-implementation-plans-and-tasks-with-notion-spec-to-implementation`
to produce a scoped plan, apply `staff-engineer-mode` for design review, then
use the GitHub PR comment skill to address a small set of review comments.

## Trust And Safety Checklist

- GitHub permissions are scoped to the branch and repo.
- The agent does not force-push without explicit approval.
- Tests or static checks are run before merge recommendations.
- Human reviewers can see which comments were addressed and why.

## Rollout Path

- Sandbox: use archived PRs or sample repos.
- Limited team: allow one team to use the loop on non-critical changes.
- Production: require test evidence, reviewer sign-off, and rollback notes.

## Metrics To Track

- Review comments resolved correctly.
- Rework caused by misunderstood requirements.
- Test pass rate after agent changes.
- Time from review comment to verified fix.

## Common Failure Modes

- Treating broad refactors as routine comment fixes.
- Losing the original spec while optimizing for code changes.
- Claiming tests passed without recording the command and result.

## Related Links

- [Coding Agent Review Loop](../case-studies/coding-agent-review-loop.md)
- [Codex](../frameworks/codex.md)
- [Claude Code](../frameworks/claude-code.md)
- [Generated skill mapping index](../generated/ase-skill-mapping-index.md)
