# Common Anti-Patterns

These patterns make skills harder to trust.

| Anti-pattern | Why it is weak | Better pattern |
|---|---|---|
| Generic tool wrapper | The skill only says "use this tool" | Add workflow, boundaries, and verification |
| Install boilerplate | It explains copying a skill file, not installing the tool | Provide real prerequisites and first safe test |
| Hidden permissions | The agent may need broad access without warning | Name scopes and approval gates |
| Catalog-only entry | The page lists metadata but no usable workflow | Explain when and how to use it |
| Unsupported popularity claim | Stars/downloads are stale or inherited | Remove the claim or source it clearly |
| Vendor claim drift | A feature is described without official backing | Link to official docs or mark as community observation |
| No stop condition | The agent keeps trying after a risky failure | Add explicit stop and escalation rules |

## Quick Rewrite Pattern

Turn this:

> Use Tool X to automate workflow Y.

Into this:

> Use Tool X for workflow Y when the input is bounded, credentials are scoped,
> and a dry-run or read-only check passes. Stop before production writes unless
> a human approves.

Good skills are specific about limits. That is what makes automation safer.
