# Runtime Guardrails

Runtime guardrails are controls that run while the agent workflow is executing.
They complement skill instructions; they do not replace review.

## Guardrail Types

| Guardrail | Use it for |
|---|---|
| input validation | block malformed, unsafe, or unsupported input |
| output validation | check structure, policy, or safety before release |
| tool allowlist | limit which tools can be called |
| approval gate | require human review before side effects |
| policy check | enforce model, data, or action rules |
| runtime monitor | detect unsafe patterns during execution |

## Review Questions

- What does the guardrail inspect?
- What does it block?
- What happens on failure?
- Can the agent bypass it?
- Is the failure visible to a human?

## Related Ecosystems

- [Guardrails AI](../ecosystems/guardrails-ai.md)
- [Lakera](../ecosystems/lakera.md)
- [LlamaFirewall](../ecosystems/llama-firewall.md)
