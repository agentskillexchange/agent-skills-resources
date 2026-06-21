# Policy And Governance

Policy and governance turn individual reviews into repeatable team decisions.
They should define who owns a workflow, what risk is allowed, and what evidence
is required before broader rollout.

## Governance Questions

- Who owns the skill-backed workflow?
- Which systems and data can it access?
- Which actions require approval?
- What logs, traces, and evals are retained?
- What policy applies to model/provider choice?
- Who can change the workflow?
- When is the next review?

## Risk Framework Fit

Use public risk frameworks as orientation, not as a substitute for local review:

- [NIST AI RMF](../ecosystems/nist-ai-rmf.md) for AI risk management vocabulary
- [OWASP LLM Top 10](../ecosystems/owasp-llm.md) for LLM application risk categories

## Practical Governance Artifact

For every production candidate, save:

- owner
- workflow scope
- data classification
- tool permissions
- approval gates
- rollback path
- evidence links
- review date
