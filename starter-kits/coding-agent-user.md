# Coding Agent User Starter Kit

## Who This Is For

Developers using Codex, Claude Code, GitHub Copilot, Cursor, Gemini CLI, or
similar coding-agent surfaces who want reusable workflows instead of one-off
prompts.

## First 15 Minutes

1. Read [framework-comparison.md](../framework-comparison.md).
2. Open the guide for your primary surface:
   [Codex](../frameworks/codex.md),
   [Claude Code](../frameworks/claude-code.md),
   [GitHub Copilot](../frameworks/github-copilot.md),
   [Cursor](../frameworks/cursor.md), or
   [Gemini CLI](../frameworks/gemini.md).
3. Pick one repeatable repo workflow: PR review, test-and-fix, release notes, or
   spec-to-implementation.
4. Check the [quality checklist](../examples/quality-checklist.md) before using
   a new skill.

## First Useful Workflow

Start with a low-risk repository task:

1. Choose a skill that targets one workflow.
2. Run it on a branch or fixture repo.
3. Record commands, changed files, test results, and reviewer notes.
4. Promote it only after the verification step catches at least one realistic
   failure mode.

## Representative ASE Examples

- [`staff-engineer-mode`](https://agentskillexchange.com/skills/staff-engineer-mode/)
- [`address-github-pr-review-comments-from-the-current-branch-with-gh-address-comments`](https://agentskillexchange.com/skills/address-github-pr-review-comments-from-the-current-branch-with-gh-address-comments/)
- [`run-terminal-native-coding-agent-workflows-with-github-copilot-cli`](https://agentskillexchange.com/skills/run-terminal-native-coding-agent-workflows-with-github-copilot-cli/)
- [`sync-agent-rules-and-skill-files-across-coding-assistants-with-ai-rules-sync`](https://agentskillexchange.com/skills/sync-agent-rules-and-skill-files-across-coding-assistants-with-ai-rules-sync/)

## Safety Reminders

- Keep generated changes on a branch.
- Run tests or static checks before trusting a patch.
- Require human review for dependency, auth, CI, deployment, or security changes.
- Avoid skills that only describe a category without concrete setup and
  verification.
