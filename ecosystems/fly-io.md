# Fly.io

Fly.io runs applications and containers close to users. In the agent skills
ecosystem, it is relevant when a workflow needs a containerized service rather
than a short serverless function.

## Where It Fits

- custom agent services
- APIs with native dependencies
- containerized background workers
- globally distributed app services

## Skill-Adjacent Concepts

- container runtime
- app deployment
- secrets and environment variables
- regional placement
- logs and operational checks

## Best Fit

- workflows that need container packaging
- agent services with custom binaries or dependencies
- long-lived services where regional placement matters

## When Not To Use It

- simple static docs or catalog pages
- edge-only routing logic
- unreviewed generated code without sandbox boundaries

## Safety And Rollout

- Pin dependencies and base images.
- Keep secrets in the platform secret store.
- Review logs for sensitive payloads.
- Document rollback commands before production rollout.

## Source Links

- [Fly.io docs](https://fly.io/docs/)

## Relation To Skills

A skill can capture the deployment, verification, and rollback steps for a
containerized agent workflow hosted on Fly.io.
