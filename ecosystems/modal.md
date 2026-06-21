# Modal

Modal provides serverless compute for Python applications, jobs, and model or
data workloads. It is relevant for skill-backed workflows that need hosted
Python execution without managing servers directly.

## Where It Fits

- Python background jobs
- data processing workflows
- model-adjacent compute
- scheduled or triggered functions

## Skill-Adjacent Concepts

- hosted functions
- dependency images
- secrets
- scheduled jobs
- logs and execution results

## Best Fit

- Python-heavy skill-backed workflows
- compute jobs with clear input/output boundaries
- evaluation or enrichment tasks that need reproducible environments

## When Not To Use It

- browser-first app surfaces
- workflows that require a traditional web app platform
- tasks with unclear dependency or data boundaries

## Safety And Rollout

- Pin Python dependencies.
- Scope secrets per function or app.
- Record input/output artifacts for review.
- Set timeouts for jobs that call external tools.

## Source Links

- [Modal docs](https://modal.com/docs)

## Relation To Skills

A skill can explain how to run, verify, and audit a Modal-hosted function or job
that supports an agent workflow.
