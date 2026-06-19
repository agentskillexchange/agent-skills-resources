# Skill Lifecycle

This diagram shows the lifecycle of a skill from idea to maintenance.

```mermaid
flowchart LR
  Idea["Workflow idea"] --> Source["Source and provenance check"]
  Source --> Draft["Draft skill"]
  Draft --> Setup["Install and setup validation"]
  Setup --> Safety["Permission and safety review"]
  Safety --> Pilot["Sandbox pilot"]
  Pilot --> Evidence["Evidence captured"]
  Evidence --> Decision{"Keep?"}
  Decision -->|Yes| Maintain["Maintain and refresh"]
  Decision -->|Revise| Draft
  Decision -->|No| Reject["Reject or archive"]
  Maintain --> Source
```

The lifecycle is intentionally review-heavy. A skill is not just an instruction
file; it is a workflow that should stay accurate as tools and policies change.
