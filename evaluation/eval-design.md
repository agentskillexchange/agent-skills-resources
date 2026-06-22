# Eval Design

Design evals from the workflow backward. Start with the decision the team needs
to make, then choose the smallest evidence that supports that decision.

## Eval Brief

| Field | Prompt |
|---|---|
| Workflow | What repeatable work should the skill perform? |
| User | Who depends on the result? |
| Input set | What examples represent normal, edge, and risky cases? |
| Expected result | What counts as correct, useful, and safe? |
| Tools | Which tools may be called? |
| Blockers | Which actions require approval or refusal? |
| Evidence | What trace, log, artifact, or reviewer note will be saved? |

## Rubric Shape

Use a small rubric before adding complex scoring.

| Criterion | Example question |
|---|---|
| Correctness | Did the workflow produce the requested artifact or answer? |
| Grounding | Are claims backed by sources, files, logs, or tool output? |
| Tool use | Were the right tools used with the right scope? |
| Safety | Were risky writes, messages, or deployments gated? |
| Reproducibility | Can another reviewer rerun or inspect the evidence? |

## Avoid

- only testing happy paths
- treating model benchmark scores as skill approval
- mixing prompt changes, model changes, and tool changes in one eval run
- hiding failures in aggregate scores
- using production secrets or customer data in early evals
