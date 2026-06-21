# Deployment Readiness

Use this page before moving a skill-backed workflow from evaluation to repeated
team use.

## Readiness Table

| Area | Ready when | Evidence |
|---|---|---|
| Workflow fit | the task is repeatable and bounded | pilot notes |
| Runtime | hosting surface matches the workflow shape | runtime decision |
| Permissions | credentials are least-privilege | scope review |
| Safety | risky actions require approval | approval record |
| Observability | logs/traces/evals are reviewable | trace or log link |
| Rollback | owner can stop or revert the workflow | rollback note |
| Maintenance | dependencies and docs have an owner | owner field |

## Go / No-Go Questions

- Can the workflow be replayed with the same input?
- Does it fail closed on missing tools, rate limits, or provider errors?
- Are writes, external messages, and deployments approval-gated?
- Are secrets scoped to the narrowest useful permission set?
- Is there a clear owner for incidents and upgrades?

## Use With Templates

- [Pilot Plan](../templates/pilot-plan.md)
- [Risk Review](../templates/risk-review.md)
- [Security Review](../templates/security-review.md)
- [Rollout Readiness](../templates/rollout-readiness.md)
- [Post-Pilot Review](../templates/post-pilot-review.md)
