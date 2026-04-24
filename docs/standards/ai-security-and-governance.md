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

### Governed Model Profiles And Invocation Paths

- a raw upstream model name is not a governed control by itself
- a model invocation counts as governed only when it uses an approved
  model-profile plus a governed invocation path
- governed AI callers must use an internal AI gateway or another explicitly
  approved platform control plane rather than direct provider access
- direct provider credentials should not live in governed product workloads or
  operator-assist tools
- approved model profiles should define at least:
  - purpose
  - allowed callers
  - allowed data scope
  - structured output contract
  - human approval expectation
  - security review reference
  - lifecycle status such as `active`, `suspended`, `retired`, or `exception`

### Governed Model Access Contract

- a governed AI runtime foundation must define its model-access contract before
  runtime activation
- that contract must identify:
  - the approved profile registry
  - the governed invocation path
  - the caller identity boundary
  - the operator approval boundary
  - the required audit fields
- instruction bundles, prompts, skills, or `AGENTS.md` content do not replace
  the model-access contract and must not be treated as the runtime authority
- repo-local policy must not redefine governed model-access rules that already
  belong to the shared access plane or approved profile registry

### Governed AI Audit Minimum

- governed AI calls must emit reviewable audit metadata for at least:
  - caller identity
  - operator identity or acceptance reference when the decision requires human
    approval
  - approved profile id
  - invocation path
  - decision or correlation id
  - event time
  - outcome
  - override reason when an operator rejects or changes the suggested result
- the audit record should make it possible to distinguish:
  - workload identity from operator identity
  - suggestion generation from operator acceptance
  - governed invocation from exception-lane or direct-provider use

### AI-Assisted Operator Decisions

- AI may assist operator decisions only within a bounded reviewed purpose
- suggestion outputs must use a fixed, reviewable schema rather than free-form
  imperative text
- model output must not directly mutate active platform contracts or live
  runtime state
- operator approval remains required for governance decisions such as intake,
  admission, approval, or promotion
- every AI-assisted governance decision should emit attributable audit metadata
  for:
  - caller
  - profile
  - decision id
  - time
  - operator acceptance or override outcome

## Governance Expectations

- maintain an AI system inventory
- require architecture review for new agentic capabilities
- define model ownership and acceptable-use boundaries
- keep exception paths explicit and time-bounded instead of normalizing direct
  model access outside the governed path
