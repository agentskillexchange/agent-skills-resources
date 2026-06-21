# Model Gateways And Policy

Model gateways sit between applications and model providers. They are not
skills, but they matter when skill-backed workflows need routing, audit, cost,
or policy controls.

## What Gateways Can Help With

- model routing
- provider failover
- cost controls
- request logging
- policy checks
- rate limits
- provider abstraction
- audit trails

## How Gateways Differ From Skills

| Layer | Role |
|---|---|
| Skill | Describes how to perform a repeatable workflow |
| Agent framework | Runs reasoning, tools, state, and orchestration |
| Gateway | Routes model calls and enforces provider-level controls |
| Policy layer | Decides which actions, models, or data paths are allowed |

## Review Questions

- Which providers can the workflow call?
- Are model choices controlled by environment, policy, or code?
- Are prompts and outputs logged?
- Can sensitive data be filtered or blocked?
- What happens during provider failure?
- How are costs monitored?

## Related Ecosystems

- [Vercel AI Gateway](../ecosystems/vercel-ai-gateway.md)
- [Vercel AI SDK](../ecosystems/vercel-ai-sdk.md)
- [OpenTelemetry GenAI](../ecosystems/opentelemetry-genai.md)
