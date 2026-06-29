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

## Anti-Patterns

- Stale popularity claims.
- Generic placeholder body text.
- Category-only skills with no workflow.
- Long copied documentation without an agent-specific procedure.
- Tool links with no install, usage, or verification guidance.
