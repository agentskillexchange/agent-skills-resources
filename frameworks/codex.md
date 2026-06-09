# Codex

Codex is OpenAI's coding-agent surface for working with codebases, terminal
tasks, tests, and repository changes. In a skills context, Codex benefits from
clear repo instructions, reproducible commands, validation steps, and concise
workflow guidance.

## Role In The Skills Ecosystem

- Coding-agent runtime and workflow surface.
- Strong fit for repo inspection, code edits, tests, PR preparation, and
  terminal-driven workflows.
- Skills should be precise about commands, project context, and verification.

## Source-Backed Resources

| Label | Resource | Why it matters |
|---|---|---|
| Official | [openai/codex](https://github.com/openai/codex) | OpenAI's public Codex CLI repository. |
| Lab | [OpenAI Codex docs](https://developers.openai.com/codex) | Lab-owned Codex workflow and setup guidance. |
| ASE | [Codex skills catalog](https://agentskillexchange.com/browse-skills/?framework=Codex) | Live ASE view of Codex-related skills. |

## Skill Guidance

Codex-oriented skills should include:

- expected repository state
- setup commands
- test commands
- file paths to inspect
- safe stopping points
- PR or patch expectations

## Skill Patterns That Fit Codex

- code review and PR response workflows
- test-and-fix loops
- repo migration plans
- spec-to-implementation planning
- verification-first debugging

## Representative ASE Examples

- `staff-engineer-mode`
- `address-github-pr-review-comments-from-the-current-branch-with-gh-address-comments`
- `turn-notion-specs-into-implementation-plans-and-tasks-with-notion-spec-to-implementation`

## Common Mistakes

- Skipping tests because the change looks small.
- Asking Codex to "improve the repo" without a concrete acceptance check.
- Mixing unrelated refactors into a task-specific skill.
