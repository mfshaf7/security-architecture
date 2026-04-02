# AI Security And Governance Standard

## Purpose

Define baseline security expectations for AI-enabled, model-assisted, and agentic systems on the platform.

## Scope

This applies to:

- LLM integrations
- copilots and agents
- model-assisted automation
- chat-driven action systems
- prompt, tool, and context pipelines

## Required Controls

### Identity And Authorization

- AI systems must not bypass normal authorization boundaries
- tool access must be explicitly scoped
- privileged actions require policy enforcement outside the model

### Prompt And Context Security

- untrusted input must be treated as potentially adversarial
- prompt injection paths must be identified and mitigated
- sensitive context should be minimized and justified

### Output And Action Safety

- model output must not be treated as trusted by default
- privileged or destructive actions require deterministic checks
- high-impact actions should support human review or approval

### Logging And Audit

- AI-triggered actions must be attributable
- prompts, tool calls, and policy decisions should be logged at an appropriate level
- exception paths must be reviewable after incidents

### Data Handling

- secrets must not be sent to models unless explicitly approved
- model context should avoid unnecessary confidential data
- data classification rules must apply to prompts and retrieved context

## Governance Expectations

- maintain an AI system inventory
- require architecture review for new agentic capabilities
- define model ownership and acceptable-use boundaries
