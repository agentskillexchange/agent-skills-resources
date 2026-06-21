# Microsoft AutoGen

AutoGen is a Microsoft agent framework for multi-agent applications and
research-oriented agent patterns.

## Where It Fits

AutoGen fits the multi-agent orchestration layer. It is useful when agents need
to collaborate, use tools, run code, or be assembled through reusable runtime
components.

## Skill-Like Concepts

- AgentChat and Core APIs
- tools and extensions
- AutoGen Studio workflows
- MCP workbench patterns
- Docker-backed code execution
- distributed runtime concepts

## Best Fit

- multi-agent prototypes
- research and evaluation workflows
- tool-using agent applications
- workflows that need explicit agent-to-agent coordination

## When Not To Use It

- small one-step automations
- workflows where a product-native coding agent is simpler
- production workflows without a defined runtime, logs, and review path

## Safety And Rollout

- Keep code execution sandboxed.
- Review tool permissions before connecting real systems.
- Save transcripts, generated code, and evaluation artifacts.
- Require human approval before writes or external side effects.

## Source Links

- [AutoGen docs](https://microsoft.github.io/autogen/stable/)
- [AutoGen GitHub](https://github.com/microsoft/autogen)

## Relation To Skills

A skill can describe an AutoGen workflow as a repeatable recipe: which agents
participate, which tools are allowed, what input is expected, and what evidence
confirms the workflow is safe to reuse.
