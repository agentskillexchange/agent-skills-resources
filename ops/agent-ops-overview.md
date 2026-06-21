# Agent Ops Overview

Agent ops is the operating layer around skill-backed workflows. It answers a
different question from skill authoring: not only "can the agent do this?", but
"can a team run, review, monitor, and stop this safely?"

## Why Skills Need Operational Evidence

Skills encode repeatable behavior. Once a skill touches repositories, customer
data, workflows, external tools, or production systems, teams need evidence that
the behavior is observable and bounded.

Operational evidence usually includes:

- trace or run log
- tool call record
- eval or regression result
- approval evidence
- rollback plan
- owner and review date
- monitoring or alert path

## Authoring vs Running

| Activity | Main question | Evidence |
|---|---|---|
| Authoring a skill | Is the instruction/source/setup clear? | source URL, setup notes, verification steps |
| Piloting a workflow | Does it work safely for one bounded case? | sandbox run, trace, reviewer notes, risks |
| Running with a team | Can the team operate it repeatedly? | owner, monitoring, approval gate, rollback |

## Connect To Existing Artifacts

- Use [First Skill Review](../checklists/first-skill-review.md) before deeper evaluation.
- Use [Team Pilot Readiness](../checklists/team-pilot-readiness.md) before a pilot.
- Use [Pilot Plan](../templates/pilot-plan.md) to define owner, scope, and success criteria.
- Use [Rollout Readiness](../templates/rollout-readiness.md) before expanding usage.

## Practical Rule

If a workflow can write, deploy, message a user, change billing, expose data, or
take security-sensitive action, it needs an approval gate and saved evidence.
