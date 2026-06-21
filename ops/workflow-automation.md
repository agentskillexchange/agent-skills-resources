# Workflow Automation

Workflow automation tools connect systems, move data, and trigger repeatable
steps. They can be enough for many AI workflow automation needs without a full
agent framework.

## Where Automation Fits

| Use case | Good fit |
|---|---|
| deterministic trigger-action flow | workflow automation |
| many SaaS connectors | connector platform |
| tool access for agents | connector or MCP layer |
| open-ended reasoning | agent framework |
| production side effects | automation plus approval gate |

## When Automation Is Enough

Use workflow automation when:

- the trigger is clear
- the steps are mostly deterministic
- the integrations already exist
- human review is easy to insert
- no long-horizon reasoning is needed

## When To Move Toward Agent Orchestration

Use agent orchestration when:

- the workflow needs planning
- tool choice depends on context
- retrieval or reasoning changes the path
- multiple agents or roles are useful
- evals and traces need to compare model behavior

## Risks

- credentials with broad access
- external side effects
- hidden retries
- duplicate messages or writes
- data movement across systems
- weak audit trail

## Related Ecosystems

- [n8n](../ecosystems/n8n.md)
- [Zapier](../ecosystems/zapier.md)
- [Composio](../ecosystems/composio.md)
