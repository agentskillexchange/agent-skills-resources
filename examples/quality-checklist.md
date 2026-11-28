# Skill Quality Checklist

Use this checklist when reviewing a skill for usefulness and trust.

## What Good Looks Like

| Review area | Weak pattern | Strong pattern |
|---|---|---|
| Setup | "Install the tool and run it." | Names the upstream package, account or API prerequisites, auth steps, and the expected local or hosted runtime. |
| Permissions | "Use the CLI to fix the issue." | Starts read-only, names which commands can write or touch production, and adds approval checkpoints before risky actions. |
| Evidence | "Check that it works." | Defines observable proof such as test output, logs, traces, screenshots, citations, or reviewed records. |
| Verification | "Run the workflow." | Gives concrete pass/fail checks and explains what to do when the check fails or data is missing. |

## Source Provenance

- The skill points to a real upstream repo, package, API, or documented source.
- Official claims are backed by source ownership.
- Community resources are labeled as community.

## Install And Setup Clarity

- Install steps describe the upstream tool, not only how to copy the skill file.
- Prerequisites are named.
- Authentication, secrets, or provider setup are explicit.

## Usage Specificity

- The skill describes a concrete workflow.
- The agent knows what to inspect first.
- Inputs, outputs, and handoff expectations are clear.

## Verification Steps

- The skill names observable checks.
- Tests, scans, commands, or evidence are included where appropriate.
- Failure conditions are clear.

## Safety And Permissions

- Dangerous commands, writes, secrets, and production access are called out.
- Approval checkpoints are included for risky actions.
- Read-only exploration is preferred before mutation.

## Metadata Quality

- `name`, `slug`, `description`, `category`, `framework`, `verification`, and
  `source` are consistent.
- Category describes the primary skill type.
- Framework claims are supported by setup or usage details.

## Multi-Framework Claims

- The skill uses common primitives if it claims multi-framework use.
- Client-specific setup is documented when needed.
- Compatibility is not assumed from popularity alone.

## Draft To Review Handoff

Use the checklist as a repair pass before opening a formal review. If any
section depends on guesses, fix the draft before review. If every section has a
source, setup path, permission note, workflow step, and observable check, carry
the same evidence into the
[First Skill Review Checklist](../checklists/first-skill-review.md).

## Repair Before First Review

Use this table to turn checklist gaps into a review-ready evidence block:

| If this area is weak | Repair the draft by adding | Carry into first review |
|---|---|---|
| Source provenance | Official repo, package, API docs, or clearly labeled community source. | Source URL and ownership note. |
| Install and setup | Concrete install command, account requirement, auth step, or hosted runtime. | Setup proof a reviewer can try. |
| Permissions and safety | Minimum role, token, data access, write action, or approval checkpoint. | Permission note and safety-sensitive action. |
| Usage specificity | First object to inspect, bounded workflow, expected output, and handoff. | Repeated workflow summary. |
| Verification | Pass signal, failure signal, blocked path, and saved artifact or log. | Observable check and open risk. |

If a row cannot be repaired, mark the first review as `Revisit with fixes`
rather than sending a weak draft into deeper evaluation.

## Worked Quality Repair

Use this small before-and-after when a first draft sounds plausible but is not
yet reviewable. It shows the level of evidence to add; it is not a template for
claiming a tool or integration was tested.

| Review area | Thin draft | Review-ready repair |
|---|---|---|
| Source and setup | “Use the vendor CLI to summarize incidents.” | Link the official CLI documentation; name the install command, required account, and the exact authenticated environment. |
| Permissions and safety | “The agent updates the incident.” | Start by reading the incident. Name the role allowed to post an update, identify the write command, and require approval before it runs. |
| Workflow | “Summarize and update.” | Inspect one incident record, extract the named fields, draft a summary, request approval, then post only the approved text. |
| Verification | “Check the update worked.” | Save the draft and command result; pass only if the posted text matches the approved draft. If access or approval is missing, stop and hand off without writing. |

Before opening the [First Skill Review Checklist](../checklists/first-skill-review.md),
translate the repair into one short evidence block: upstream source, setup
proof, minimum permission and approval boundary, bounded workflow, observable
pass signal, and any open risk. A reviewer should be able to trace every claim
in that block without guessing from the skill title.

## Anti-Patterns

- Stale popularity claims.
- Generic placeholder body text.
- Category-only skills with no workflow.
- Long copied documentation without an agent-specific procedure.
- Tool links with no install, usage, or verification guidance.
