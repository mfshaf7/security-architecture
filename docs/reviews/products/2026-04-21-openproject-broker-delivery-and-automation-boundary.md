# OpenProject Broker Delivery And Automation Boundary Review

## Summary

- date: 2026-04-21
- owner repos:
  - `platform-engineering`
  - `operator-orchestration-service`
- affected review subject: `products.openproject`
- decision: `approved-with-findings`

This delta review covers the current OpenProject security boundary after the
delivery-plane operating model and broker workflow expansion.

## Scope Delta

OpenProject is no longer just a platform-integrated web product with proposal
capture automation. The current model now includes:

- broker-owned delivery execution summary and bounded delivery mutation routes
- stronger automation identity provisioning for broker workflow access
- ART-first delivery operation as the canonical work-state truth
- production hygiene that allows a vetted seeded ART baseline instead of an
  empty plane requirement

That makes the product boundary more explicit and more powerful at the same
time. The baseline review is therefore not sufficient on its own.

## Review Areas

### Identity

- the broker automation role is now part of the real product operating model
- least privilege remains acceptable only when permissions stay mapped to
  delivery intent and do not become a generic work-package admin lane
- human admin and machine automation identities must stay clearly separated

### Secrets

- broker-to-OpenProject credential custody remains acceptable when Vault stays
  the owner path and runtime delivery is reviewable
- no new secret class is introduced, but the impact of compromise is larger now
  that the broker can perform more delivery operations

### Delivery

- the broker boundary is the correct long-term delivery seam because it hides
  OpenProject-specific field and permission quirks from higher-level operators
- seeded production ART history is acceptable only when the imported baseline
  is explicitly approved and clearly distinguishable from rehearsal noise
- direct platform-side mutation paths should continue to shrink rather than
  regrow

### Runtime

- OpenProject remains the canonical execution backend and retains standard web
  application and database runtime concerns
- the security story still depends heavily on platform-managed controls because
  the product is platform-integrated rather than fully self-governed

### AI

- no governed AI mutation path is part of this tranche
- any future model-shaped delivery operation or approval routing must receive a
  dedicated delta review

## Decision

`approved-with-findings`

Approved because the broker boundary is a security improvement over exposing
raw OpenProject semantics. The approval depends on these continuing controls:

- no generic OpenProject passthrough API
- explicit provenance review before seeded ART history enters prod
- automation role growth remains bounded and reviewable
- each later broker migration slice receives its own delta review before it is
  treated as security-complete

Residual findings:

- OpenProject still depends on platform-managed controls for a large part of
  its runtime security story
- prod seeding policy needs continued operational discipline to avoid mixing
  vetted history with rehearsal-only noise

## Related Artifacts

- [`../../architecture/products/openproject/README.md`](../../architecture/products/openproject/README.md)
- [`../../architecture/products/openproject/threat-model.md`](../../architecture/products/openproject/threat-model.md)
- [`../../architecture/products/openproject/required-controls.md`](../../architecture/products/openproject/required-controls.md)
- [`../security-review-checklist.md`](../security-review-checklist.md)
- [`../security-delta-review-process.md`](../security-delta-review-process.md)
