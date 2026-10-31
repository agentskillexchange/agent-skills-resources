# Hermes

Hermes Agent is an open-source agent from Nous Research with skills, memory, and
agent-managed workflows. Its skill model is useful for understanding how agents
can learn and reuse operational patterns over time.

## Role In The Skills Ecosystem

- Self-improving agent runtime with skill management.
- Strong fit for memory-backed workflows, persistent operations, and
  agent-managed skill libraries.
- Skills should be explicit about what should be persisted and what should stay
  task-local.

## Source-Backed Resources

| Label | Resource | Why it matters |
|---|---|---|
| Official | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | Official Hermes Agent repository. |
| Official | [Hermes skills feature docs](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/skills.md) | Skill management and usage documentation. |
| Official | [Hermes bundled skills catalog](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/reference/skills-catalog.md) | Reference for bundled Hermes skills. |
| ASE | [Hermes-related ASE skills](https://agentskillexchange.com/browse-skills/?q=Hermes) | Live ASE search for Hermes-related skills. |

## Skill Guidance

Hermes-oriented skills should include:

- memory boundaries
- skill installation or tap instructions
- safe delegation patterns
- verification and rollback guidance

## Skill Patterns That Fit Hermes

- self-improvement workflows
- persistent memory management
- personal agent routines
- reusable skill libraries
- reflection and learning loops

## Representative ASE Examples

- `run-a-self-improving-personal-agent-with-hermes-agent`

## Next Artifact To Open

If you are evaluating a Hermes skill for persistent operations or
self-improvement, compare it with the
[OpenClaw Runtime Ops completed evaluation](../examples/completed-evaluations/openclaw-runtime-ops-evaluation.md)
first, then copy the evidence shape into the
[Skill Evaluation Worksheet](../templates/skill-evaluation-worksheet.md).
For a Hermes skill you are drafting, use the
[First Skill Review](../checklists/first-skill-review.md) checklist before
asking for broader review.

Carry forward:

- the read-only scope and memory/configuration paths to inspect
- what may persist versus what must remain task-local
- allowed commands, data access, and human approval boundaries
- the expected evidence, cleanup or rollback step, and unresolved risks before
  any persistent or self-improving write action

The completed evaluation is an evidence pattern for a bounded runtime workflow,
not an endorsement of Hermes or a particular skill.

## Common Mistakes

- Persisting too much task-local context into memory.
- Blurring skill installation, skill execution, and agent reflection.
- Omitting rollback or cleanup guidance for long-running workflows.
