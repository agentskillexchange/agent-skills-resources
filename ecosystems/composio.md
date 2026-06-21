# Composio

Composio provides tools and connectors for agent workflows.

## Where It Fits In Agent Operations

Composio fits the connector and tool access layer. It helps agents interact with
external SaaS systems, APIs, and workflow tools.

## Skill-Adjacent Concepts

- tools and connectors
- authentication
- action execution
- agent tool integration
- workflow automation
- external side effects

## Best Fit

- agents that need many SaaS integrations
- workflows where tool setup is the hardest part
- connector-heavy pilots with clear approval gates

## When Not To Use It

- workflows that only need local files or commands
- high-risk actions without scoped credentials
- teams that cannot audit external side effects

## Safety And Rollout

- Scope credentials tightly.
- Separate read actions from write actions.
- Add approval before external messages, writes, or data changes.
- Record tool calls and outputs.

## Source Links

- [Composio docs](https://docs.composio.dev/)
- [Composio GitHub](https://github.com/ComposioHQ/composio)

## Relation To Skills

A skill can document exactly which Composio tools are required, how they are
scoped, and which actions require approval.
