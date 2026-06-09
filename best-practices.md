# Agent Skill Best Practices

## Write Skills Around Real Work

Good skills are workflow-shaped. They answer:

- What problem does this solve?
- Which tool, repo, API, or runtime does it use?
- What should the agent inspect first?
- What commands or steps are safe to run?
- How should the agent verify success?
- When should the agent stop and ask for approval?

## Source-Backed Metadata

Use source-backed fields. If you cannot prove a claim, omit it.

Recommended metadata:

```yaml
name: "Readable skill name"
slug: "stable-url-slug"
description: "One sentence about the workflow."
category: "Primary category"
framework: "Primary framework or Multi-Framework"
verification: "listed"
source: "https://github.com/example/project"
```

## Trust And Safety Checklist

- Prefer official docs and upstream repos.
- Label third-party material as `Community`.
- Avoid stale stars, downloads, or marketing numbers.
- Avoid generic copy-folder install instructions.
- Avoid unsafe install commands unless the risk is named and alternatives exist.
- Include a verification step that checks observable output.

## Multi-Framework Compatibility

Many skills can work across frameworks, but avoid claiming compatibility without
evidence. A multi-framework skill should rely on common primitives:

- shell commands
- HTTP APIs
- MCP servers
- documented config files
- repo-local instructions
- explicit verification steps

## Testing A Skill

At minimum, test that:

1. The source URL resolves.
2. Required tools are named.
3. Install/setup steps are actionable.
4. The main usage flow is reproducible.
5. The verification step catches failure.
6. The body does not contain generic placeholder text.

