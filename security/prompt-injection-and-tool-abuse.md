# Prompt Injection And Tool Abuse

Prompt injection happens when untrusted content tries to override the agent's
intended instructions. Tool abuse happens when that influence reaches tools,
credentials, data, or external systems.

## Common Patterns

- untrusted web pages or documents instruct the agent to ignore rules
- retrieved content asks the agent to leak secrets
- tool output includes instructions that should be treated as data
- external text tries to trigger a write, send, or deploy action
- a prompt asks for hidden context, keys, or private logs

## Review Questions

- Which inputs are untrusted?
- Can untrusted input reach tool selection?
- Can tools write, send, delete, deploy, or change access?
- Is there an approval gate before side effects?
- Are secrets isolated from model-visible context?

## Good Controls

- separate instructions from retrieved content
- treat tool output as data
- constrain tool permissions
- require approval before side effects
- test with adversarial examples

## Related Resources

- [OWASP LLM Top 10](../ecosystems/owasp-llm.md)
- [promptfoo](../ecosystems/promptfoo.md)
- [garak](../ecosystems/garak.md)
- [PyRIT](../ecosystems/pyrit.md)
