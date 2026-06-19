# Security And Permissions

Security guidance belongs inside the skill, not in a separate tribal-memory
document. The agent should know what it is allowed to touch before it acts.

## Permission Checklist

- Filesystem: read-only, workspace-only, or broader access?
- Repository: read, branch write, issue write, PR merge?
- Network: which domains or APIs?
- Secrets: required, optional, or prohibited?
- User data: customer, employee, medical, legal, financial, or public?
- Production systems: read-only, deploy, mutate, or delete?
- Human approval: when must the agent stop?

## Approval Gates

Require approval before:

- Publishing externally.
- Changing production configuration.
- Writing to protected branches.
- Running destructive commands.
- Sending user/customer communications.
- Expanding access scopes.
- Handling regulated or sensitive data.

## Good / Weak

| Weak | Better |
|---|---|
| "Use your credentials." | "Use a least-privilege token scoped to the sandbox project." |
| "Run the command." | "Run dry-run first; require approval before applying changes." |
| "Store logs." | "Redact secrets and avoid storing personal data in logs." |

## Evidence

Security review should leave evidence: scopes used, commands run, dry-run
output, approval decision, and known residual risks.
