# Evaluation And Benchmarks

Use this section to design practical evaluation evidence for agent skills,
skill-backed workflows, and team pilots.

Benchmarks are useful orientation tools, but they are not a substitute for
workflow-specific tests, traces, approval records, and regression checks.

## Start Here

| Need | Page |
|---|---|
| Understand the evaluation layer | [Evaluation Overview](evaluation-overview.md) |
| Compare public benchmarks | [Benchmark Landscape](benchmark-landscape.md) |
| Design workflow-specific evals | [Eval Design](eval-design.md) |
| Run regression checks | [Regression Testing](regression-testing.md) |
| Capture review evidence | [Evidence Capture](evidence-capture.md) |
| Compare tools and benchmark surfaces | [Evaluation Tool Matrix](evaluation-tool-matrix.md) |

## Evaluation Questions

- What task is the skill supposed to make repeatable?
- What does a correct result look like?
- Which failures matter most: wrong answer, unsafe action, missing citation,
  bad tool call, data leak, or slow/expensive run?
- What evidence can a reviewer inspect later?
- Which benchmark is relevant, and which benchmark would be misleading?

## Related Guides

- [Agent Ops](../ops/)
- [Security](../security/)
- [Deployment](../deployment/)
- [Quality Checklist](../examples/quality-checklist.md)
- [Post-Pilot Review Template](../templates/post-pilot-review.md)
