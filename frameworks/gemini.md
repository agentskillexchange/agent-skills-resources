# Gemini

Gemini CLI is Google's open-source terminal agent for Gemini-powered workflows.
Gemini-related skills are useful when they define terminal workflows, repository
tasks, and model-specific setup clearly.

## Role In The Skills Ecosystem

- Terminal agent and model-provider workflow.
- Strong fit for command-line research, coding, and automation tasks.
- Skills should include authentication, command, and verification details.

## Source-Backed Resources

| Label | Resource | Why it matters |
|---|---|---|
| Official | [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) | Official Gemini CLI repository. |
| Official | [Google AI Gemini API docs](https://ai.google.dev/gemini-api/docs) | Gemini API documentation. |
| ASE | [Gemini skills catalog](https://agentskillexchange.com/browse-skills/?framework=Gemini) | Live ASE view of Gemini-related skills. |

## Skill Guidance

Gemini skills should include:

- authentication setup
- model/provider assumptions
- terminal commands
- rate-limit or quota notes where source-backed
- expected output checks

## Skill Patterns That Fit Gemini

- terminal-native repo analysis
- model-provider setup
- bounded command loops
- multi-agent context history
- CLI-based research and coding flows

## Representative ASE Examples

- `run-terminal-native-repo-analysis-edits-and-command-loops-with-gemini-in-a-bounded-cli-workflow-with-gemini-cli`
- `capture-search-and-optionally-sync-local-coding-agent-session-history-across-claude-code-codex-cursor-cli-and-gemini-with-specstory`

## Common Mistakes

- Leaving auth or quota assumptions implicit.
- Treating Gemini CLI as a generic web search tool.
- Omitting terminal output checks.
