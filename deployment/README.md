# Deployment And Runtime Hosting

Use this section when a skill-backed workflow moves from local evaluation to a
hosted runtime, background job, sandbox, or team-facing service.

This is not a hosting ranking. It is a practical guide to choosing the right
runtime surface, keeping secrets controlled, and collecting rollout evidence.

## Start Here

| Need | Page |
|---|---|
| Understand the deployment layer | [Deployment Overview](deployment-overview.md) |
| Compare runtime hosting patterns | [Runtime Hosting](runtime-hosting.md) |
| Review sandbox and container execution | [Sandbox And Container Execution](sandbox-and-container-execution.md) |
| Plan secrets and environments | [Secrets And Environments](secrets-and-environments.md) |
| Check rollout readiness | [Deployment Readiness](deployment-readiness.md) |
| Compare providers and surfaces | [Provider Matrix](provider-matrix.md) |

## What Changes At Deployment Time

Local skill evaluation asks: does the workflow work?

Deployment asks:

- who owns the workflow
- where credentials live
- what inputs are trusted
- what actions can change external state
- how logs, traces, approvals, and rollback evidence are captured
- what fails closed when a model, tool, or provider is unavailable

## Related Guides

- [Agent Ops](../ops/)
- [Security](../security/)
- [Team Pilot Readiness](../checklists/team-pilot-readiness.md)
- [Rollout Readiness Template](../templates/rollout-readiness.md)
