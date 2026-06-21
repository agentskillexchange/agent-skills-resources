# AWS Bedrock Agents

AWS Bedrock Agents is a managed AWS service for building agents that can use
foundation models, action groups, APIs, and knowledge bases.

## Where It Fits

- AWS-native managed agents
- enterprise workflows with IAM and cloud governance
- action groups connected to APIs or Lambda
- knowledge-base-backed agent experiences

## Skill-Adjacent Concepts

- managed agent configuration
- action groups
- knowledge bases
- IAM permissions
- traces and invocation evidence by AWS service design

## Best Fit

- teams already operating in AWS
- workflows needing enterprise IAM and cloud controls
- agents that need managed access to AWS services

## When Not To Use It

- local coding-agent workflows
- simple skill documentation without hosted execution
- teams that cannot manage AWS IAM and audit requirements

## Safety And Rollout

- Scope IAM roles narrowly.
- Review every action group for external side effects.
- Keep test and production agents separate.
- Capture invocation logs and approval evidence for risky actions.

## Source Links

- [AWS Bedrock Agents docs](https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html)

## Relation To Skills

A skill can document how to configure, test, and verify a Bedrock Agent action
or workflow, including IAM scope and rollout evidence.
