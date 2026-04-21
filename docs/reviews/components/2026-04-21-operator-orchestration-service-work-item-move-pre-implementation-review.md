# Operator Orchestration Service Work-Item Move Pre-Implementation Review

## Summary

- date: 2026-04-21
- owner repos:
  - `operator-orchestration-service`
  - `platform-engineering`
- affected ART work:
  - `#61` `Brokerize core delivery control commands behind internal APIs`
  - `#63` `Brokerize delivery work-item move`
  - `#71` `Run security delta review for brokerized delivery work-item move`
- decision: `approved-with-findings`

This is the first live pre-implementation security delta review under the
strengthened global security-governance model.

It is intentionally triggered before implementation starts on `#63`, not after
the code lands.

## Scope Delta

The broker already owns bounded delivery read/update/create behavior for the
OpenProject delivery plane. `#63` would extend that authority into structure
mutation by allowing the broker to move a delivery work item under a different
parent inside `Workspace Delivery ART`.

That is a meaningful security delta because it changes:

- which backend mutation the broker may perform
- which OpenProject permission boundary the automation role must hold
- how much workflow authority the broker has over the canonical execution tree

Current state by control layer:

- design intent:
  - clear enough to review now
- implemented control:
  - not yet landed for this specific move command
- operating evidence:
  - not yet available for this specific move command

So this review is not a completion attestation. It is a bounded permission to
proceed with implementation under explicit constraints.

## Review Areas

### Identity

- the broker continues to act through a machine identity rather than human
  operator credentials
- this remains acceptable only if the new route stays bounded to intended ART
  structure-move semantics and does not become a generic arbitrary-parent
  mutation surface
- the OpenProject automation role must not expand past the minimum structure
  editing permission required for this route

### Secrets

- no new secret class is required for this change
- the existing OpenProject credential path remains acceptable if custody stays
  Vault-delivered and component-owned
- the security posture would worsen if this route encouraged direct credential
  reuse outside the broker boundary; that must not happen

### Delivery

- moving this operation behind the broker is the correct control direction
  because it keeps OpenProject internals out of outer operator surfaces
- the route must stay intent-shaped:
  - move one delivery work item under one allowed parent
  - preserve delivery-plane validation
  - reject generic structure editing outside the supported model
- platform wrappers should call the broker route rather than reintroducing
  direct backend mutation

### Runtime

- this route changes canonical execution state, so audit and caller identity
  remain mandatory
- the broker should continue to expose one bounded internal workflow surface,
  not a general admin API
- move operations should remain attributable in broker-side logs and in the
  OpenProject record trail

### AI

- no governed AI decision path is introduced by this specific route
- if later hierarchy mutation becomes model-shaped or approval-assisted, a new
  delta review is required before that expansion is treated as acceptable

## Decision

`approved-with-findings`

`#63` may proceed to implementation when all of these remain true:

1. the route is limited to delivery work-item move semantics, not generic
   OpenProject structure editing
2. the broker continues to validate parent/child placement against the delivery
   model
3. automation permissions stay minimally scoped
4. implementation proof is recorded before `#63` is marked `done`

Findings and required follow-up:

- implementation must prove that the route does not widen into arbitrary work
  package mutation
- completion evidence for `#63` should include live devint proof of:
  - broker route success
  - correct parent change in OpenProject
  - preserved auditability

## Related Artifacts

- [`../../architecture/components/operator-orchestration-service/README.md`](../../architecture/components/operator-orchestration-service/README.md)
- [`../../architecture/products/openproject/required-controls.md`](../../architecture/products/openproject/required-controls.md)
- [`../security-review-checklist.md`](../security-review-checklist.md)
- [`../security-delta-review-process.md`](../security-delta-review-process.md)
