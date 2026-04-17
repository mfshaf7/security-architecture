# Governed AI Intake Assist And Model Profile Review

## Scope

Review the proposed governed AI control pattern for workspace intake assistance:

- `platform-engineering` owns the approved model-profile registry and the future
  AI access plane
- `workspace-governance` may record `ai-suggested` intake entries only when the
  suggestion is backed by an approved governed profile
- operator acceptance remains the final authority for recording the workspace
  intake decision

This is a platform-scoped review of the control model, not approval for direct
provider access or a live gateway rollout.

## Decision

Approved as the current governed AI intake control model with staged
activation.

The control is acceptable while all of these remain true:

- a governed AI decision is defined by approved profile plus governed
  invocation path, not by raw model name alone
- `workspace-governance` accepts `ai-suggested` intake entries only when the
  referenced profile is `active`, purpose-bound for intake assistance, and
  human approval remains required
- the approved intake-classifier profile stays `suspended` until the internal AI
  gateway, caller identity, audit emission, and direct-provider egress block
  exist
- direct provider keys are not normalized into governed product or workspace
  control paths
- operator acceptance or override remains attributable and reviewable

## Review Areas

### Identity

- the governed path introduces a machine-identity requirement for the future AI
  gateway and its approved callers
- operator identity must remain distinct from machine invocation identity
- the intake suggestion path is acceptable only if workload or operator-tool
  identity can be attributed at the gateway boundary

### Secrets

- provider credentials should live only in the governed AI access plane, not in
  `workspace-governance` or product-local scripts
- this review does not approve any direct provider secret distribution into
  governed workloads

### Delivery

- the platform owns the approved profile registry and the future enforcement
  path
- `workspace-governance` consumes that registry as a dependency for intake
  validation instead of inventing repo-local model policy
- the operator decision is still explicit and reviewable in the intake register

### AI

- the output contract is suggestion-only and bounded to intake classification
- the model may recommend `out-of-scope`, `proposed`, or `admitted`, but it may
  not directly change active repo, product, or component contracts
- human approval remains required even when the model output is valid
- this control is intentionally narrower than a general-purpose agent or tool
  caller

### Visibility

- operators must be able to identify which approved profile generated the
  suggestion, which decision id was recorded, and whether the suggestion was
  accepted or overridden
- if the invocation path cannot emit that metadata, the intake suggestion path
  should not be treated as governed

## Residual Risk

- the registry and validation foundation can be merged before the live AI
  gateway exists, so the currently defined intake profile must remain
  non-active until the runtime path is real
- the broader platform still lacks the internal AI gateway, egress block, and
  runtime audit path needed for a fully live governed AI system
- operator exception use of external AI tools remains a temporary governance gap
  until the governed access plane is real

## Related Artifacts

- [`../../standards/ai-security-and-governance.md`](../../standards/ai-security-and-governance.md)
- [`../../architecture/domains/ai-and-agentic.md`](../../architecture/domains/ai-and-agentic.md)
- [`../security-review-checklist.md`](../security-review-checklist.md)
