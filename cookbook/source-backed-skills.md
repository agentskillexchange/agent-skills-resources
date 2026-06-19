# Source-Backed Skills

A source-backed skill tells the reader where its claims come from. That matters
because agent workflows often depend on external tools, permissions, APIs, and
security behavior that can change.

## Checklist

- Link to the official tool docs or maintained repository.
- Distinguish official docs from community examples.
- Avoid star, download, or popularity claims unless they are fetched and dated.
- Explain what the source proves.
- Remove claims that cannot be verified.

## Good / Weak

| Weak | Better |
|---|---|
| "This is the best way to run browser tasks." | "Use this when the workflow needs browser state that an API cannot expose." |
| "Install the tool." | "Install from the official package or source repo linked below." |
| "Works with all agents." | "The workflow is framework-neutral; adapters may be needed for each runtime." |

## Source Notes

When adding a resource, record the owner and label:

- `Official`: project or vendor-owned.
- `Lab`: model provider, research lab, or frontier-lab material.
- `Community`: third-party material.
- `ASE`: Agent Skill Exchange material.

If ownership is unclear, use `Community` or skip the resource.
