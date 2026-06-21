# OpenTelemetry GenAI

OpenTelemetry GenAI semantic conventions define telemetry concepts for
generative AI systems.

## Where It Fits In Agent Operations

OpenTelemetry GenAI fits the vendor-neutral telemetry layer. It helps teams
standardize traces and metrics across models, tools, and agent systems.

## Skill-Adjacent Concepts

- semantic conventions
- traces and spans
- model request metadata
- tool call telemetry
- observability portability
- production monitoring

## Best Fit

- teams standardizing telemetry across providers
- production agent platforms
- workflows that need observability without vendor lock-in

## When Not To Use It

- early learning exercises
- one-off manual workflows
- teams without instrumentation ownership

## Safety And Rollout

- Avoid logging secrets or sensitive payloads.
- Define span naming and attribute conventions.
- Pair telemetry with retention and access policy.
- Use traces to support incident review and rollout evidence.

## Source Links

- [OpenTelemetry GenAI semantic conventions](https://opentelemetry.io/docs/specs/semconv/gen-ai/)
- [OpenTelemetry specification GitHub](https://github.com/open-telemetry/opentelemetry-specification)

## Relation To Skills

A skill can define expected telemetry fields so its workflow is observable in a
standard way.
