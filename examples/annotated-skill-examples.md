# Annotated Skill Examples

These examples are representative public ASE skills. They are not copied here in
full; the goal is to show what each one teaches future skill authors.

## Coding And Review

**Slug:** `staff-engineer-mode`

- **Why it is a good example:** It turns broad engineering judgment into a
  reusable routing skill instead of a vague persona prompt.
- **Workflow encoded:** Design review, delivery planning, reliability,
  security, operations, and maintenance routing.
- **Strong metadata:** `Developer Tools`, `Multi-Framework`,
  `security_reviewed`.
- **Setup/usage/verification pattern:** Useful as a review-mode skill where the
  agent should classify the engineering problem before acting.
- **What authors can copy:** Start with the decision surface, then route to
  specialized guidance instead of mixing every concern into one flat checklist.

## MCP Tool Connection

**Slug:** `postgresql-mcp-server`

- **Why it is a good example:** It connects a concrete tool surface to agent
  access through MCP.
- **Workflow encoded:** Database access and query workflows through an MCP
  server.
- **Strong metadata:** `Data Extraction & Transformation`, multi-framework
  compatibility including `MCP`, `security_reviewed`.
- **Setup/usage/verification pattern:** A strong MCP skill should name the
  server, the client context, and how to verify connectivity.
- **What authors can copy:** Treat MCP as a tool bridge, not the whole workflow.

## SRE And Incident Ops

**Slug:** `investigate-production-incidents-across-kubernetes-and-cloud-signals-with-holmesgpt`

- **Why it is a good example:** It is framed around an on-call investigation
  loop, not just a tool name.
- **Workflow encoded:** Pull alerts, logs, metrics, and infrastructure context
  into an incident investigation.
- **Strong metadata:** `Runbooks & Diagnostics`, `Custom Agents`,
  `security_reviewed`.
- **Setup/usage/verification pattern:** Good incident skills should separate
  evidence collection, hypothesis, and remediation.
- **What authors can copy:** Make the operational state explicit before
  recommending action.

## Security And Guardrails

**Slug:** `route-risky-coding-agent-work-through-human-approval-checkpoints-with-humanlayer`

- **Why it is a good example:** It encodes a safety boundary for high-risk
  coding-agent work.
- **Workflow encoded:** Pause, collect a human decision, then resume or block
  risky work.
- **Strong metadata:** `Security & Verification`, `Multi-Framework`,
  `security_reviewed`.
- **Setup/usage/verification pattern:** The approval checkpoint is part of the
  workflow, not an afterthought.
- **What authors can copy:** Put approval rules close to the risky action.

## Data Platform

**Slug:** `query-and-inspect-postgres-databases-through-mcp-with-pgedge-postgres-mcp`

- **Why it is a good example:** It scopes database work to schema discovery,
  safe querying, and inspection.
- **Workflow encoded:** Agent-safe Postgres inspection through MCP.
- **Strong metadata:** `Data Extraction & Transformation`, `MCP`,
  `security_reviewed`.
- **Setup/usage/verification pattern:** Data skills should be explicit about
  read/write boundaries and query validation.
- **What authors can copy:** Start with inspection and scope before execution.

## Content And Research

**Slug:** `draft-cited-research-reports-with-storm`

- **Why it is a good example:** It centers cited research and human review.
- **Workflow encoded:** Research a topic, build a multi-perspective outline, and
  draft a cited report.
- **Strong metadata:** `Research & Scraping`, `Multi-Framework`,
  `security_reviewed`.
- **Setup/usage/verification pattern:** Strong research skills separate source
  collection, synthesis, and review.
- **What authors can copy:** Keep citations and claim verification visible.

## OpenClaw Runtime Ops

**Slug:** `run-day-2-openclaw-operations-with-production-runbooks-and-reusable-prompt-patterns-from-openclaw-runbook`

- **Why it is a good example:** It treats runtime operations as repeatable
  runbooks, not one-off troubleshooting.
- **Workflow encoded:** Stabilize long-running deployments, tune worker
  patterns, and apply monitoring/security prompts.
- **Strong metadata:** `Runbooks & Diagnostics`, `OpenClaw`,
  `security_reviewed`.
- **Setup/usage/verification pattern:** Runtime skills should include health
  checks and recovery guidance.
- **What authors can copy:** Include operational success criteria, not just
  commands.

## Hermes / Emerging Runtime

**Slug:** `run-a-self-improving-personal-agent-with-hermes-agent`

- **Why it is a good example:** It shows a persistent agent workflow with memory,
  scheduled work, and skill learning.
- **Workflow encoded:** Deploy Hermes Agent as a personal agent that learns from
  experience and coordinates work.
- **Strong metadata:** `Templates & Workflows`, `Multi-Framework`,
  `security_reviewed`.
- **Setup/usage/verification pattern:** Emerging-runtime skills should explain
  persistence, memory, and boundaries.
- **What authors can copy:** Be clear about what the agent should remember and
  what should remain task-local.

