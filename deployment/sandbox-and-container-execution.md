# Sandbox And Container Execution

Sandboxing matters when a skill-backed workflow runs generated code, shell
commands, repository automation, browser automation, or third-party tooling.

## What To Isolate

| Surface | Risk | Evidence to capture |
|---|---|---|
| Shell commands | destructive commands, credential leakage | command log and allowed path list |
| Generated code | unsafe imports, network calls | diff, test output, dependency list |
| Browser automation | account actions, form submits | screenshots, target URLs, approval records |
| Repository automation | branch writes, PR comments, merges | git diff, PR link, auth scope |
| External APIs | data exfiltration, side effects | API scopes, request logs, rollback path |

## Container Checklist

- Use a pinned base image or trusted runtime.
- Keep secrets outside the image.
- Mount only the paths needed for the task.
- Restrict network access when possible.
- Record dependency installation and test output.
- Clean up artifacts after the run.

## Sandbox Checklist

- Define allowed files, commands, and network destinations.
- Require approval before writes to production systems.
- Capture stdout/stderr and generated artifacts.
- Set timeout and resource limits.
- Treat downloaded code and generated scripts as untrusted until reviewed.

## Related Resources

- [Data And Secrets Handling](../security/data-and-secrets-handling.md)
- [Runtime Guardrails](../security/runtime-guardrails.md)
- [Security Review Template](../templates/security-review.md)
