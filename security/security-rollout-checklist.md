# Security Rollout Checklist

Use this before expanding a skill-backed workflow beyond a sandbox.

## Workflow

- Workflow:
- Owner:
- Systems touched:
- Data classification:
- Review date:

## Checklist

- [ ] Source and upstream ownership are clear.
- [ ] Tool permissions are scoped.
- [ ] Secrets are isolated from prompts, traces, and artifacts.
- [ ] Prompt injection or untrusted-input risk was reviewed.
- [ ] Side effects require human approval.
- [ ] Logs/traces/evals are retained appropriately.
- [ ] Rollback path is documented.
- [ ] Security owner approved the pilot or rollout.

## Mitigation Priority

Use this before selecting `Revisit with mitigations`, `Limited rollout`, or
`Production rollout`:

| If the issue affects | Treat as | Evidence to capture |
|---|---|---|
| Secrets, write/delete actions, production data, or broad repo access | Launch blocker | Owner, fix, retest result, and approval before access expands |
| Missing logs, unclear rollback, or weak monitoring owner | Limited-rollout blocker | Monitoring or rollback note before expanding beyond a small group |
| Documentation gaps, narrower allowlists, or follow-up hardening | Follow-up item | Owner and review date in the rollout evidence record |

## Evidence

```text

```

## Decision

- [ ] Reject
- [ ] Revisit with mitigations
- [ ] Sandbox pilot
- [ ] Limited rollout
- [ ] Production rollout
