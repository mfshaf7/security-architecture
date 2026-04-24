# Governed AI Model Access And Audit Contract Review

## Summary

- date: 2026-04-24
- owner repo: `security-architecture`
- affected review subjects:
  - `repos.workspace-governance`
  - `repos.platform-engineering`
- decision: `approved-with-findings`

This review evaluates the control-plane architecture work that turns the
governed AI runtime foundation into an explicit model-access and audit contract
instead of leaving it as loose repo-local doctrine.

## Scope Delta

### Design Intent

- the workspace control plane should separate reusable governance-engine logic
  from tenant-instance state
- runtime work should stay blocked until the model-access and audit boundary is
  explicit
- `workspace-governance` should consume governed model-access truth rather than
  inventing repo-local AI runtime policy

### Implemented Control

- `workspace-governance` now carries:
  - `docs/governance-engine-foundation.md`
  - `contracts/governance-engine-foundation.yaml`
- the workspace contract now states that runtime activation depends on:
  - approved profile plus governed invocation path
  - workload caller identity distinct from operator acceptance identity
  - explicit audit-field requirements
  - sequencing behind the governance-engine boundary and shadow-parity path
- the security standard now requires an explicit governed model-access contract
  and minimum audit metadata for governed AI calls

### Operating Evidence

- the new workspace contract is schema-validated
- contract validation proves the model-access references point at real
  `platform-engineering` and `security-architecture` artifacts
- the workspace bootstrap docs now expose the governance-engine and runtime
  foundation as first-class architecture truth instead of depending on handoff
  prose

## Review Areas

### Identity

- separating workload caller identity from operator acceptance identity is the
  correct trust boundary for governed AI decisions
- this remains acceptable only while a future invocation plane preserves both
  identities instead of collapsing them into one service credential

### Delivery

- keeping the runtime track blocked behind the governance-engine split is the
  correct sequencing decision
- `workspace-governance` is acceptable as the architecture owner for the
  control-plane boundary, but it must keep consuming platform-owned model
  profiles instead of cloning model-policy logic locally

### Runtime

- the instruction bundle model is acceptable only while it remains an
  authoring-layer truth rather than an implicit execution authority
- future runtime packaging may materialize those layers, but it should not
  redefine the governed access boundary or operator approval semantics

### AI

- the governed model-access contract is acceptable because it requires:
  - approved profile plus governed invocation path
  - structured output contract
  - explicit human approval for governance decisions
  - attributable audit emission
- this review does not approve a live governed AI runtime yet
- activation remains blocked until the actual invocation plane exists and is
  reviewed against the same contract

## Decision

`approved-with-findings`

Approved because the change tightens the control model and makes the runtime
sequencing honest without activating a new AI path prematurely.

Findings and residual risk:

1. The contract is still architectural. A future live invocation plane needs a
   fresh delta review before any governed profile becomes active.
2. `workspace-governance` must keep consuming platform-owned profile and access
   truth rather than re-implementing governed AI policy in repo-local
   validators.
3. Audit-field requirements are necessary but not sufficient. The future access
   plane still needs real audit retention, review, and exception handling.

## Related Artifacts

- `workspace-governance/docs/governance-engine-foundation.md`
- `workspace-governance/contracts/governance-engine-foundation.yaml`
- `platform-engineering/docs/standards/governed-ai-access-model.md`
- `platform-engineering/security/governed-ai-model-profiles.yaml`
- [`../security-delta-review-process.md`](../security-delta-review-process.md)
- [`../security-review-checklist.md`](../security-review-checklist.md)
