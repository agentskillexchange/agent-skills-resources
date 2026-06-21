# Red Teaming And Evals

Red teaming and evals help teams find failures before users or production
systems do.

## What To Test

- prompt injection
- unsafe tool calls
- data leakage
- insecure code generation
- hallucinated claims
- broken refusal paths
- missing approval gates
- regression after model or prompt changes

## Evidence To Keep

| Evidence | Why |
|---|---|
| test prompts | lets reviewers reproduce the issue |
| expected behavior | defines the safe result |
| actual behavior | shows current risk |
| trace/log link | explains how the agent reached the outcome |
| fix decision | records reject, revisit, or pilot |

## Related Ecosystems

- [promptfoo](../ecosystems/promptfoo.md)
- [garak](../ecosystems/garak.md)
- [PyRIT](../ecosystems/pyrit.md)
- [OWASP LLM Top 10](../ecosystems/owasp-llm.md)
