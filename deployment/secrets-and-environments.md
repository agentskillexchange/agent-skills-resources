# Secrets And Environments

Deployment quality depends on how credentials, environment variables, and
production boundaries are handled.

## Minimum Environment Plan

| Environment | Purpose | Expected controls |
|---|---|---|
| Local sandbox | first evaluation | test credentials only |
| Shared sandbox | team pilot | scoped secrets, logs, owner |
| Limited production | narrow real use | approval gates, monitoring, rollback |
| Broad production | repeated team use | audits, rotation, incident path |

## Secret Handling Rules

- Store secrets in the hosting platform or secret manager, not in docs or code.
- Use least-privilege tokens for the pilot.
- Separate read-only credentials from write-capable credentials.
- Rotate credentials after risky tests or broad access changes.
- Avoid logging raw prompts, tool payloads, or tokens.

## Environment Review Questions

- Which secrets does the workflow need?
- Who owns each secret?
- What can each credential read or change?
- Which logs might contain sensitive data?
- What happens if a credential expires or is revoked?

## Failure Modes

- development keys accidentally used in production
- broad GitHub or cloud tokens used for narrow workflows
- logs containing customer data or secrets
- hidden retries creating duplicate side effects
- missing ownership for rotation and revocation
