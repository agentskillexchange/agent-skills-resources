# OpenAI Agents SDK

The OpenAI Agents SDK is a code-first framework for applications that need to
run agents with tools, handoffs, guardrails, and tracing. It fits when the
application—not a coding-agent runtime—owns deployment, state, credentials,
and approval decisions.

## Role In The Skills Ecosystem

- Agent application framework for Python and TypeScript.
- Strong fit for tool-using workflows, specialist handoffs, and app-owned
  orchestration.
- Skills should make the agent's tool boundary, approval behavior, state, and
  observable evidence explicit rather than treating an SDK integration as a
  self-contained safety control.

## Source-Backed Resources

| Label | Resource | Why it matters |
|---|---|---|
| Official | [Agents SDK guide](https://developers.openai.com/api/docs/guides/agents/sdk) | Chooses a starting path for agent definitions, tools, orchestration, guardrails, state, and observability. |
| Official | [Agents SDK quickstart](https://developers.openai.com/api/docs/guides/agents/quickstart) | Builds one working agent before adding more workflow complexity. |
| Official | [Guardrails and human review](https://developers.openai.com/api/docs/guides/agents/guardrails-approvals) | Distinguishes automatic checks from human approval before sensitive actions. |
| Official | [Agents SDK repositories](https://github.com/openai/openai-agents-python) | Provides SDK source, examples, issues, and language-specific documentation routes. |
| ASE | [OpenAI-related skills on ASE](https://agentskillexchange.com/browse-skills/?q=OpenAI) | Live ASE search for representative, separately maintained catalog entries. |

## Skill Guidance

An Agents SDK-oriented skill should name:

- the one job each agent owns, including its instructions and expected output;
- which tools, MCP servers, data, and credentials that agent may use;
- the handoff trigger and what state or context is allowed to cross it;
- which actions must pause for human approval or fail closed;
- the trace, evaluation, or test signal a reviewer can inspect; and
- the bounded outcome and stop condition.

Start with one agent and one observable workflow. Add a handoff only when a
second specialist has a distinct job and permission boundary; add tools only
when their inputs, side effects, and failure behavior can be reviewed.

## Skill Patterns That Fit The Agents SDK

- function or hosted-tool workflows with explicit input and output checks;
- specialist routing with bounded handoff criteria;
- approval-gated actions that can pause and resume;
- trace-backed regression or evaluation loops; and
- application-owned MCP integrations with scoped credentials.

## Next Artifact To Open

If the workflow can call tools, hand off work, or cause a side effect, compare
it with the [HumanLayer Approval Workflow completed evaluation](../examples/completed-evaluations/humanlayer-approval-workflow-evaluation.md)
before building a broader pilot. Then copy the evidence shape into the
[Skill Evaluation Worksheet](../templates/skill-evaluation-worksheet.md).

Carry forward the owner of each tool and credential, allowed inputs and data
scope, approval or denial behavior, trace or test evidence, rollback path, and
the condition that ends the run. The example is an evidence pattern, not an
endorsement of a particular SDK or catalog skill.

## Common Mistakes

- Adding multiple agents before one agent has a reviewed contract and evidence.
- Treating guardrails as a substitute for tool permissions or human approval.
- Letting a handoff widen access without naming the new agent's tool scope.
- Shipping tool calls without a trace, test, or auditable outcome.
