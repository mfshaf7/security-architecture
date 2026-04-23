# OpenProject Governed Release Control State Review

## Summary

- date: 2026-04-23
- owner repo:
  - `platform-engineering`
- affected review subjects:
  - `repos.platform-engineering`
  - `products.openproject`
- decision: `approved-with-findings`

This delta review covers the new governed release-state model for the
platform-managed OpenProject contract.

## Scope Delta

### Design Intent

- OpenProject should gain explicit candidate, verification, readiness, and
  prod-verification records for the platform-owned deployment contract
- those records should make release truth inspectable and fail closed when the
  exact contract has not been verified
- the change must improve governed release control without overstating product
  maturity or claiming a separate OpenProject-owned `source -> stage -> prod`
  rail already exists

### Implemented Control

- `platform-engineering` now carries:
  - OpenProject stage candidate, stage verification, stage readiness, and prod
    verification records under
    `environments/prod/openproject-release/`
  - product-owned verification catalogs for OpenProject stage and prod checks
  - an operator-facing release-governance runbook for the platform-managed
    OpenProject contract
  - updated OpenProject product docs that describe the governed release surface
    while keeping the product classified as `platform-integrated`

### Operating Evidence

- the initial release objects were recorded against the current OpenProject
  contract:
  - `openproject/openproject@13.4.4`
  - `docker.io/openproject/openproject:17.2.3-slim`
- the product contract surfaces remained reviewable at the time the records
  were added:
  - Argo `openproject` `Synced Healthy`
  - Argo `openproject-secrets` `Synced Healthy`
  - `openproject-admin-secret` `SecretSynced`
  - `openproject-postgresql-credentials` `SecretSynced`
- the new release objects intentionally remain `pending` where no governed
  verification or readiness evidence exists yet

## Review Areas

### Delivery

- this change materially improves GitOps and release-governance truth because
  OpenProject can no longer be treated as stage-ready or prod-verified from
  health alone
- the operator runbook keeps the approval boundary reviewable and anchored on
  explicit evidence instead of hidden operator memory
- the control remains appropriately bounded because it governs a
  platform-managed product contract rather than introducing a new autonomous
  product promotion rail

### Runtime

- OpenProject remains a conventional web runtime with database dependency and
  operator-access concerns; this tranche does not widen runtime authority
- the new catalogs and release records make the runtime contract easier to
  audit because they bind verification expectations to exact contract files
- runtime maturity is still intentionally limited: OpenProject is
  `platform-integrated`, and the release objects must not be described as proof
  that a separate governed stage runtime already exists

### Identity

- no new human or machine identity was introduced by this tranche
- the existing OpenProject admin and automation identities remain under their
  prior bounded control model

### Secrets

- no new secret class or custody path was introduced
- the release-governance model correctly treats secret sync as one verification
  signal, not as a sufficient release-readiness proof by itself

## Decision

`approved-with-findings`

Approved because the change strengthens delivery and runtime governance for a
real platform-managed product without widening authority or inventing a false
rollout maturity.

Findings and residual risk:

1. OpenProject still lacks a distinct governed stage runtime. The new stage
   candidate, verification, and readiness objects are valid controls, but they
   must stay evidence-bound and must not be described as a full product-owned
   stage lane.
2. The current OpenProject release records are intentionally fail-closed.
   Future contract changes still need real verification and readiness evidence
   recorded in Git before the product can be treated as governed stage-ready or
   prod-verified.

Required follow-up:

- keep `stage-verification.yaml`, `stage-readiness.yaml`, and
  `prod-verification.yaml` synchronized with the exact OpenProject contract when
  that contract changes
- reopen the product review if OpenProject later gains a distinct stage runtime
  or an independent source-owned promotion rail

## Related Artifacts

- [`../../architecture/products/openproject/README.md`](../../architecture/products/openproject/README.md)
- [`../../architecture/products/openproject/required-controls.md`](../../architecture/products/openproject/required-controls.md)
- [`../security-review-checklist.md`](../security-review-checklist.md)
- [`../security-delta-review-process.md`](../security-delta-review-process.md)
