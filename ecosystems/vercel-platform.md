# Vercel Platform

Vercel is a hosted platform for web applications, serverless functions,
deployments, environment variables, and observability. In the agent skills
ecosystem, it is most relevant when a skill-backed workflow becomes an app,
endpoint, or team-facing service.

## Where It Fits

- AI web apps and chat interfaces
- tool-calling endpoints
- serverless functions
- deployment previews and production releases
- environment variable management

## Skill-Adjacent Concepts

- hosted execution for AI app workflows
- deployment previews for review
- managed environment variables
- request logs and observability
- model/provider usage through app code or Vercel AI SDK

## Best Fit

- teams building AI workflows into web products
- skill-backed review tools with a browser/API surface
- workflows that need preview deployments before rollout

## When Not To Use It

- long-running jobs that exceed function/runtime limits
- workflows that only need local coding-agent execution
- untrusted code execution without a separate sandbox design

## Safety And Rollout

- Keep production secrets out of preview deployments unless required.
- Separate read-only and write-capable credentials.
- Use preview deployments for human review.
- Capture logs and rollback notes for each production rollout.

## Source Links

- [Vercel docs](https://vercel.com/docs)
- [Vercel deployments docs](https://vercel.com/docs/deployments)
- [Vercel functions docs](https://vercel.com/docs/functions)

## Relation To Skills

A skill can describe how to deploy, verify, and roll back a Vercel-hosted agent
workflow without becoming the hosting platform itself.
