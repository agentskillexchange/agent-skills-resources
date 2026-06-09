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

## Common Mistakes

- Persisting too much task-local context into memory.
- Blurring skill installation, skill execution, and agent reflection.
- Omitting rollback or cleanup guidance for long-running workflows.
