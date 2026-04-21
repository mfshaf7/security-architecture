# Operator Orchestration Service Delivery Workflow Broker Expansion Review

## Summary

- date: 2026-04-21
- owner repo: `operator-orchestration-service`
- affected review subjects:
  - `repos.operator-orchestration-service`
  - `products.openproject`
- decision: `approved-with-findings`

This delta review covers the first expansion of the broker from proposal-plane
handoff into delivery-plane execution operations:

- delivery execution summary read surface
- bounded delivery work-item update command
- bounded delivery work-item create command
- stronger OpenProject adapter and broker runtime boundary documentation

## Scope Delta

The baseline runtime-admission review approved a bounded shared broker with
capture and proposal-plane workflows. The new slice adds delivery-plane
OpenProject mutation and readback paths behind the broker boundary.

That changes the security posture in three meaningful ways:

1. the broker now mediates additional OpenProject work-package operations
2. the OpenProject automation role requires broader but still bounded
   permissions
3. platform-side operator wrappers can now depend on the broker for real
   delivery execution behavior rather than direct local OpenProject runners

The change does not introduce public ingress, direct human operator execution
inside the broker, or governed AI automation. It does widen the shared internal
workflow authority and therefore requires a fresh security decision.

## Review Areas

### Identity

- the broker keeps a distinct machine identity and caller-auth boundary
- additional OpenProject permissions are acceptable only when they remain tied
  to the broker automation role and do not become a generic administrator lane
- no new human identity is introduced in this slice

### Secrets

- OpenProject token custody remains component-owned and Vault-delivered
- the change does not introduce a new secret class
- the stronger broker role still depends on tight secret-path ownership and
  clear separation from Telegram runtime credentials

### Delivery

- shifting delivery workflow commands behind the broker is the correct control
  direction because it removes OpenProject-specific semantics from outer
  operator surfaces
- the route set remains bounded and intent-shaped rather than generic
  CRUD-through to OpenProject
- audit correlation now matters more because the broker is becoming a stronger
  workflow authority

### Runtime

- the broker remains an internal runtime with explicit health and readiness
  surfaces
- OpenProject stays the canonical execution backend rather than being replaced
  by the broker
- the allowed route set is still narrow enough for phase-by-phase admission

### AI

- no governed AI decision path is introduced in this tranche
- that boundary must remain explicit if later workflow slices introduce
  model-shaped mutation or approval behavior

## Decision

`approved-with-findings`

Approved because the change strengthens the workflow boundary and keeps the
broker route set bounded. The expansion is acceptable when all of these remain
true:

- no generic OpenProject passthrough route is introduced
- automation permissions stay narrowly tied to delivery workflow needs
- platform wrappers keep the broker as the delivery workflow seam instead of
  reintroducing direct backend mutation paths
- each later brokerized delivery surface receives its own delta review when it
  widens the trust boundary materially

Current findings to route back into ongoing work:

- remaining broker migration slices must continue to avoid generic CRUD
- caller/auth and audit evidence should stay explicit as the route set grows

## Related Artifacts

- [`../../architecture/components/operator-orchestration-service/README.md`](../../architecture/components/operator-orchestration-service/README.md)
- [`../../architecture/products/openproject/required-controls.md`](../../architecture/products/openproject/required-controls.md)
- [`../security-review-checklist.md`](../security-review-checklist.md)
- [`../security-delta-review-process.md`](../security-delta-review-process.md)
