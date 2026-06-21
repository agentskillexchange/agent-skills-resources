# Agent Safety Review Guide

Agent safety review asks whether a skill-backed workflow can be run, observed,
and stopped safely.

## Review Areas

| Area | Questions |
|---|---|
| Source | Is the upstream source clear and maintained? |
| Permissions | Which files, repos, data, APIs, or systems can be touched? |
| Tools | Which tool calls can create side effects? |
| Data | Could private, regulated, or customer data be exposed? |
| Secrets | Are tokens, keys, cookies, or credentials handled safely? |
| Output | Could generated output mislead users or trigger unsafe action? |
| Approval | Which actions require human review? |
| Evidence | Are logs, traces, evals, or review artifacts saved? |

## Minimum Decision

- Reject when source, permissions, or side effects are unclear.
- Revisit when setup is plausible but evidence is missing.
- Pilot only when scope, approval gates, and rollback are defined.

## Related Resources

- [OWASP LLM Top 10](../ecosystems/owasp-llm.md)
- [NIST AI RMF](../ecosystems/nist-ai-rmf.md)
- [Security And Permissions Review Checklist](../checklists/security-and-permissions-review.md)
