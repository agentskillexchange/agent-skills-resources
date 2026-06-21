# Data And Secrets Handling

Skills often fail safely or unsafely based on data handling. A good skill names
what data it can see and what must never enter model context, logs, traces, or
external tools.

## Sensitive Inputs

- API keys, tokens, cookies, SSH keys
- private repository code
- customer data
- regulated records
- incident logs
- billing or financial data
- personal identifiers

## Review Rules

- Do not paste secrets into prompts.
- Keep credentials in environment or platform secret stores.
- Mask sensitive values in logs and traces.
- Minimize data sent to model providers.
- Separate read-only workflows from write workflows.
- Define retention for traces, eval data, and artifacts.

## Evidence To Save

| Evidence | Purpose |
|---|---|
| data access note | shows what the workflow can read |
| secret handling note | shows how credentials are isolated |
| trace/log policy | shows what gets retained |
| approval record | shows who allowed sensitive action |

## Related Resources

- [Security And Permissions](../cookbook/security-and-permissions.md)
- [Security Review Template](../templates/security-review.md)
