# LlamaFirewall

LlamaFirewall is part of Meta's PurpleLlama work and focuses on runtime
protection patterns for LLM applications.

## Where It Fits

LlamaFirewall fits the runtime control layer. It is relevant when teams want
policy checks around prompts, responses, or tool-adjacent model behavior.

## Skill-Adjacent Concepts

- runtime filtering
- prompt and response checks
- unsafe behavior detection
- application-level guardrails
- policy enforcement

## Best Fit

- workflows needing runtime checks
- teams evaluating open-source guardrail patterns
- applications exposed to untrusted input

## When Not To Use It

- as the only review artifact
- without clear allow/block policy
- where human approval is required but absent

## Source Links

- [LlamaFirewall in PurpleLlama](https://github.com/meta-llama/PurpleLlama/tree/main/LlamaFirewall)
- [PurpleLlama GitHub](https://github.com/meta-llama/PurpleLlama)
