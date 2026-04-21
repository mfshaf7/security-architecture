# OpenProject Broker Create Role And Assignable Principal Review

## Summary

- date: 2026-04-21
- owner repos:
  - `platform-engineering`
  - `operator-orchestration-service`
- affected review subject: `products.openproject`
- decision: `approved`

This delta review covers the product-facing correction to the broker-backed
OpenProject create path after live devint proof exposed role drift and assignee
contract ambiguity.

## Scope Delta

The current product operating model already includes a broker-owned delivery
create surface. The new delta tightens the product boundary in three ways:

- the accepted-idea-delivery lane now provisions the broker identity with the
  structure-edit permissions the create path actually requires
- broker create preserves markdown-backed SAFe custom fields as product truth
- assignee selection is now explicitly limited to assignable principals in the
  target project or work item

This keeps the product on an intent-shaped broker surface while avoiding hidden
runner-only behavior.

## Review Areas

### Identity

- the reviewed automation role now matches the real create-path capability
  requirement
- the product still separates machine automation from human admin identity

### Secrets

- no new secret class is introduced
- existing token custody remains the relevant control boundary

### Delivery

- product truth is stronger because create now preserves the structured SAFe
  fields that the ART depends on
- assignee behavior is safer because the product no longer implies arbitrary
  user assignment through the broker

### Runtime

- the product remains platform-integrated, but the local devint lane now
  carries the correct reviewed role set for this workflow

### AI

- no AI-governance boundary changed in this slice

## Decision

`approved`

Approved because the product boundary is now more truthful and more durable:
the broker create path is aligned to the reviewed automation role and to the
backend's assignable-principal model.

Required follow-up: None.

## Related Artifacts

- [`../../architecture/products/openproject/README.md`](../../architecture/products/openproject/README.md)
- [`../../architecture/products/openproject/required-controls.md`](../../architecture/products/openproject/required-controls.md)
- [`../security-delta-review-process.md`](../security-delta-review-process.md)
