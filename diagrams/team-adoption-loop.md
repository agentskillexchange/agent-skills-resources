# Team Adoption Loop

Teams should move from learning to production through a small evidence loop.

```mermaid
flowchart LR
  Learn["Learn concepts"] --> Pick["Pick low-risk workflow"]
  Pick --> Evaluate["Evaluate skill"]
  Evaluate --> Sandbox["Sandbox run"]
  Sandbox --> Risk["Risk review"]
  Risk --> Pilot["Limited pilot"]
  Pilot --> Metrics["Measure usefulness and safety"]
  Metrics --> Decision{"Adopt?"}
  Decision -->|Adopt| Rollout["Roll out with owner and monitoring"]
  Decision -->|Revise| Evaluate
  Decision -->|Stop| Archive["Archive decision and evidence"]
  Rollout --> Refresh["Freshness review"]
  Refresh --> Evaluate
```

The loop keeps adoption reversible. Each step should leave enough evidence for a
future reviewer to understand why the team continued or stopped.
