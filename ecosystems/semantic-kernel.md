# Semantic Kernel

Semantic Kernel is a Microsoft SDK for building agent and AI orchestration
features into applications.

## Where It Fits

Semantic Kernel belongs in the application framework layer. It is relevant when
teams want agent workflows integrated with enterprise software, plugins,
functions, planners, and existing Microsoft-oriented engineering stacks.

## Skill-Like Concepts

- agents
- plugins and functions
- planners and processes
- memory connectors
- prompt templates
- application-level policy and telemetry

## Best Fit

- enterprise app integration
- .NET, Python, or Java teams
- workflows that combine business functions and model calls
- teams that need application-owned policy and deployment controls

## When Not To Use It

- simple local coding-agent workflows
- catalog browsing or skill installation
- workflows without an application host

## Safety And Rollout

- Treat plugins/functions as privileged tools.
- Review credentials and connector scopes.
- Keep telemetry and audit trails close to the app.
- Use human approval for production writes.

## Source Links

- [Semantic Kernel overview](https://learn.microsoft.com/en-us/semantic-kernel/overview/)
- [Semantic Kernel GitHub](https://github.com/microsoft/semantic-kernel)

## Relation To Skills

A skill can document a Semantic Kernel workflow by naming the plugin/function
surface, setup requirements, permission boundaries, and validation evidence.
