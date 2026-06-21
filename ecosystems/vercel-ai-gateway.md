# Vercel AI Gateway

Vercel AI Gateway provides model routing and provider access for AI
applications.

## Where It Fits In Agent Operations

Vercel AI Gateway fits the model gateway and policy layer. It helps teams route
model calls, centralize provider access, and review operational controls.

## Skill-Adjacent Concepts

- model routing
- provider abstraction
- fallback
- usage and cost controls
- audit and operational visibility
- gateway-level policy

## Best Fit

- teams using multiple model providers
- hosted AI applications
- workflows that need provider failover or routing controls
- teams wanting model access separated from skill instructions

## When Not To Use It

- offline local workflows
- workflows using a single direct provider by design
- skill authoring without runtime model calls

## Safety And Rollout

- Define allowed models and providers.
- Track cost and latency.
- Keep gateway policy separate from skill wording.
- Review logs and provider failover behavior before production rollout.

## Source Links

- [Vercel AI Gateway docs](https://vercel.com/docs/ai-gateway)

## Relation To Skills

A skill can name gateway requirements and model constraints without embedding
provider secrets or routing policy in the skill body.
