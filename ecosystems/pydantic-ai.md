# Pydantic AI

Pydantic AI is a Python agent framework built around typed agents, tools,
structured outputs, evals, graphs, and related runtime patterns.

## Where It Fits

Pydantic AI fits the Python application and evaluation layer. It is useful when
agent behavior should be typed, tested, instrumented, and reviewed as code.

## Skill-Like Concepts

- agents
- tools and toolsets
- structured outputs
- MCP support
- evals
- graph workflows and durable execution
- human-in-the-loop approval

## Best Fit

- Python teams that value typed interfaces
- workflows with structured outputs
- eval-heavy agent applications
- agent systems that need code-level review

## When Not To Use It

- non-Python teams that do not want a Python service layer
- simple prompt-only workflows
- workflows where the runtime already provides enough structure

## Safety And Rollout

- Keep schemas explicit.
- Test tool calls and structured outputs.
- Use evals before expanding scope.
- Add approval gates around risky tool actions.

## Source Links

- [Pydantic AI docs](https://pydantic.dev/docs/ai/overview/)
- [Pydantic AI GitHub](https://github.com/pydantic/pydantic-ai)

## Relation To Skills

A skill can document a Pydantic AI agent by naming the schema, tools, evals,
approval points, and expected evidence for safe reuse.
