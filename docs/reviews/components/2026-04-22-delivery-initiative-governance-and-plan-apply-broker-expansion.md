# Delivery Initiative Governance And Plan Apply Broker Expansion Review

## Summary

- date: 2026-04-22
- owner repos:
  - `operator-orchestration-service`
  - `platform-engineering`
- affected review subjects:
  - `repos.operator-orchestration-service`
  - `repos.platform-engineering`
  - `products.openproject`
- affected ART work:
  - `#61` `Enabler: Brokerize core delivery control commands behind internal APIs`
  - `#67` `Enabler: Brokerize delivery initiative governance update`
  - `#70` `Enabler: Brokerize delivery plan apply and reconciliation`
- decision: `approved`

This delta review covers two new broker-owned delivery surfaces:

- `POST /v1/delivery-initiatives/{delivery_id}/governance`
- `POST /v1/delivery-initiatives/{delivery_id}/plan/apply`

The corresponding OpenProject operator scripts now call those broker routes
instead of mutating the delivery initiative and plan-reconcile path directly in
platform-side Rails runners.

## Scope Delta

Earlier reviews approved bounded broker ownership for:

- delivery execution summary reads
- delivery work-item update, create, move, blocker, parking, and dependency
  behavior

This slice extends that authority one level higher:

- the broker may now update initiative-only governance fields that belong on
  the top-level Epic
- the broker may now apply a bounded execution plan rooted at that Epic,
  including controlled reconcile behavior for omitted descendants

The change is material because it centralizes more of the canonical delivery
workflow behind the broker boundary. It also increases the importance of
keeping the surface intent-shaped and preventing drift into generic OpenProject
CRUD.

## Review Areas

### Identity

- the broker still acts through a machine identity with the reviewed delivery
  project permissions
- no human operator credential is reused in the new routes
- the new routes remain acceptable only because they are:
  - initiative-scoped
  - field-bounded
  - limited to the delivery project
- this review does not approve arbitrary Epic patching or general project
  structure administration

### Secrets

- no new secret class is introduced
- the existing broker caller-auth and OpenProject token custody remain the
  relevant secret controls
- platform wrappers continue to consume the broker route rather than exposing
  backend credentials in a wider operator surface

### Delivery

- initiative governance is the correct workflow boundary for PM² and top-level
  delivery controls; it should not remain as a raw platform-side field patch
- plan/apply is acceptable because it stays bounded to:
  - `schema_version=1`
  - initiative-rooted plan items
  - controlled `ignore|park` and `retire|defer` reconcile semantics
  - existing delivery completion rules, which still reject `status=done`
    inside plan payloads
- retaining a dedicated completion workflow and dedicated parking/retirement
  model prevents the route from collapsing into unconstrained lifecycle CRUD

### Runtime

- the broker now becomes the single bounded runtime seam for two additional
  high-value delivery operations
- platform wrappers are reduced to broker adapters, which is the desired
  runtime posture
- live proof is still required for closure because these routes mutate
  canonical ART state

### AI

- no autonomous AI decision authority is added here
- any future AI-authored initiative governance or plan generation that bypasses
  explicit operator ownership would require a fresh delta review

## Decision

`approved`

Approved because the new routes improve the control-plane boundary without
expanding into a generic admin API.

This approval depends on the following continuing to hold:

1. initiative governance remains limited to initiative-only fields
2. plan/apply remains rooted at the delivery Epic and keeps reconcile behavior
   bounded to the documented `parked` / `retired` model
3. completion still requires the evidence-backed completion workflow
4. platform operator commands continue to call the broker route instead of
   reintroducing direct backend mutation

Required follow-up:

- record live devint proof for both routes before `#67` and `#70` are marked
  `done`

## Related Artifacts

- [`../../architecture/components/operator-orchestration-service/README.md`](../../architecture/components/operator-orchestration-service/README.md)
- [`../../architecture/products/openproject/required-controls.md`](../../architecture/products/openproject/required-controls.md)
- [`../security-delta-review-process.md`](../security-delta-review-process.md)
