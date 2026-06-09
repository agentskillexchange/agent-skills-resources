# Coding Agent Review Loop

## Practical Scenario

A small engineering team wants a repeatable coding-agent loop for turning specs
into implementation plans, reviewing changes with senior-engineer judgment, and
closing GitHub PR feedback without losing context.

## Relevant ASE Skill Examples

| Skill | Role in the workflow |
|---|---|
| `turn-notion-specs-into-implementation-plans-and-tasks-with-notion-spec-to-implementation` | Converts product/spec context into implementation tasks before coding starts |
| `staff-engineer-mode` | Applies senior review posture to architecture, risk, and maintainability decisions |
| `address-github-pr-review-comments-from-the-current-branch-with-gh-address-comments` | Helps process actionable PR review comments after changes are proposed |

## How They Fit Together

1. Start with the spec-to-plan skill to turn ambiguous product context into a
   reviewable implementation plan.
2. Use `staff-engineer-mode` during design review and before finalizing the
   change set.
3. Use the PR feedback skill only after a branch and review comments exist.

## Setup Considerations

- GitHub access should be scoped to the repo and branch being reviewed.
- Any Notion or spec-source access should be read-only unless updates are part
  of the intended workflow.
- Keep the implementation plan separate from final code changes so humans can
  review scope before the agent edits files.

## Security And Trust Considerations

- Confirm the agent is not using stale PR comments or old branch state.
- Treat broad refactors as higher-risk than targeted fixes.
- Require explicit approval before force-pushes, destructive git actions, or
  dependency changes.

## What To Evaluate Before Adopting

- Does the skill preserve the original acceptance criteria?
- Are review comments mapped to specific files or commits?
- Does the workflow produce test or verification evidence?
- Can a human interrupt the loop before risky changes are applied?

## Related Pages

- [Codex](../frameworks/codex.md)
- [Claude Code](../frameworks/claude-code.md)
- [Best Practices](../best-practices.md)
- [Quality Checklist](../examples/quality-checklist.md)
