# Regression Testing

Regression tests protect a skill-backed workflow from silent quality drift after
prompt, model, tool, dependency, or provider changes.

## What To Freeze

| Item | Why |
|---|---|
| Input examples | makes before/after behavior comparable |
| Expected outputs or rubrics | prevents moving the goalposts |
| Tool allowlist | catches unexpected external actions |
| Safety cases | keeps refusals and approval gates intact |
| Run metadata | explains changes caused by model or runtime updates |

## Small Regression Set

Start with 10-20 examples:

- 5 common cases
- 3 edge cases
- 3 risky or approval-gated cases
- 2 known past failures
- 2 negative cases where the skill should refuse or ask for clarification

## Review Output

For each run, save:

- date and runtime
- model/provider if relevant
- skill version or commit
- input ID
- result
- trace or log link
- reviewer decision

## When To Rerun

- model/provider changes
- framework/runtime upgrade
- tool permission changes
- skill body or setup changes
- deployment target changes
- incident or user-reported failure
