# GitHub Copilot

GitHub Copilot is GitHub's coding assistant and agent surface for IDE work,
GitHub.com workflows, code review, Copilot CLI, Copilot cloud agent, and the
Copilot SDK. In a skills context, Copilot matters because GitHub documents
agent skills as reusable folders of instructions, scripts, and resources that
Copilot can load when they are relevant to a task.

## Role In The Skills Ecosystem

- GitHub-native coding-agent and repository workflow surface.
- Strong fit for issue-to-PR work, code review, repository maintenance,
  release notes, and GitHub-centered automation.
- Skills can complement repository instructions, MCP servers, custom agents,
  hooks, and Copilot SDK sessions.
- Best used when the work should stay close to GitHub repositories, issues,
  pull requests, code review, Actions, or organization governance.

## Copilot Surfaces

| Surface | Where skills fit |
|---|---|
| Copilot Chat and IDEs | Repository instructions, project skills, MCP context, and task-specific guidance. |
| GitHub.com and cloud agent | Delegated issue/PR work, repository MCP configuration, code review, and bounded agent sessions. |
| Copilot CLI | Terminal-native workflows, local repo tasks, skill installation, and repeatable command loops. |
| GitHub Copilot app | Agent sessions and GitHub-native collaboration surfaces. |
| Copilot SDK | Programmatic agent loops, explicit skill directories, MCP servers, hooks, and streaming events. |

## Source-Backed Resources

| Label | Resource | Why it matters |
|---|---|---|
| Official | [GitHub Copilot docs](https://docs.github.com/en/copilot) | Main documentation hub for Copilot features, agents, CLI, SDK, MCP, and governance. |
| Official | [About agent skills](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills) | Explains Copilot's agent skill model and supported skill locations. |
| Official | [Adding agent skills for GitHub Copilot](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills) | Shows how to create, add, manage, and review skills for Copilot cloud agent and related surfaces. |
| Official | [Adding agent skills for GitHub Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills) | Covers skill usage in terminal-native Copilot CLI workflows. |
| Official | [Copilot SDK custom skills](https://docs.github.com/en/copilot/how-tos/copilot-sdk/features/skills) | Shows how SDK sessions load skill directories and combine skills with MCP servers. |
| Official | [Copilot MCP docs](https://docs.github.com/en/copilot/concepts/context/mcp) | Explains MCP support across Copilot surfaces and the GitHub MCP server. |
| Official | [Repository custom instructions](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions) | Helps distinguish persistent repo guidance from portable skills. |

## Skill Guidance

Copilot-oriented skills should include:

- the Copilot surface they target, such as CLI, cloud agent, code review, or SDK
- repository paths, issue/PR context, and branch expectations
- setup requirements for `gh`, GitHub auth, MCP servers, or local tools
- expected human review points before merge, release, or production changes
- clear verification evidence, such as tests, generated diffs, CI checks, or
  review summaries
- notes on permissions, secrets, repository access, and organization policy

## Skill Patterns That Fit GitHub Copilot

- issue-to-implementation workflows that stay inside GitHub
- pull request review, release notes, and repository maintenance
- terminal-native coding loops through Copilot CLI
- repository instructions paired with project skills
- MCP-backed GitHub workflows, such as issue, PR, code scanning, or Actions
  context
- SDK sessions that explicitly load skill directories

## Representative ASE Examples

- `run-terminal-native-coding-agent-workflows-with-github-copilot-cli`
- `github-copilot-ai-code-assistant`
- `generate-structured-release-notes-from-merged-pull-requests-between-two-refs-with-copilot-release-notes`

## When To Pick Copilot

Pick Copilot when the workflow is GitHub-native: issues, pull requests, code
review, repository policy, Actions, release notes, or organization-managed
developer environments. It is especially useful when the agent should work near
GitHub permissions and review flows.

Pick Codex when you want a terminal-first coding agent with explicit local
commands and patch control. Pick Claude Code or Cursor when the IDE or local
project workflow is the primary surface. Pick OpenClaw when scheduled runtime
operations, providers, channels, and crons are central. Pick Hermes when the
experiment is about self-improving agent memory and skill evolution. Pick
LangGraph when stateful orchestration is the core problem.

## Safety And Rollout Notes

- Inspect third-party skills before installing them, especially when they
  include scripts, hidden instructions, or tool calls.
- Pin or record skill provenance when installing shared skills.
- Treat repository instructions and skills as different layers: instructions
  set persistent local norms, while skills should encode repeatable workflows.
- Review organization policies for Copilot agents, MCP, code review, model
  access, and repository permissions before production rollout.
- Require human approval before merges, releases, destructive commands, or
  high-permission GitHub operations.
