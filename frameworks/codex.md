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
