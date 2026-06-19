# Skill Evaluation Basics

Evaluate a skill before trusting it in a real workflow. The goal is not to make
every skill perfect; it is to know what the skill can safely do.

## Fast Review

| Question | Good signal | Weak signal |
|---|---|---|
| Is the source clear? | Links to official docs or a maintained repo | No source or a generic homepage |
| Is setup specific? | Commands, prerequisites, auth scope | "Install as usual" |
| Is usage bounded? | Clear workflow and stop conditions | Broad "automate everything" claims |
| Are permissions named? | Repo, filesystem, browser, network, secrets | No mention of access |
| Is verification present? | Tests, dry runs, logs, citations, screenshots | No evidence path |

## Evaluation Steps

1. Identify the workflow the skill claims to support.
2. Check the source and ownership.
3. Review install/setup instructions.
4. Look for permission and data access boundaries.
5. Run the smallest safe validation.
6. Decide: reject, revise, sandbox pilot, or approve for limited use.

## Trust Tiers Are Not A Substitute

A badge or label can help triage, but it does not replace reading the skill.
Always inspect high-impact skills that can run commands, touch production data,
write to repositories, or contact users.

## Evidence To Keep

- Skill version or commit.
- Source URL.
- Install command used.
- Permissions granted.
- Test result or dry-run output.
- Known limitations.
- Approval decision and owner.
