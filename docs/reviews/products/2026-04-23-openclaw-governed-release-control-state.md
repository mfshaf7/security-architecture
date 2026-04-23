# OpenClaw Governed Release Control State Review

## Summary

- date: 2026-04-23
- owner repo:
  - `platform-engineering`
- affected review subjects:
  - `repos.platform-engineering`
  - `products.openclaw`
- decision: `approved-with-findings`

This delta review covers the reconciliation that aligns OpenClaw with the
standardized governed release model while keeping OpenClaw's deliberately
retained promotion-gate filename.

## Scope Delta

### Design Intent

- OpenClaw should follow the shared governed release vocabulary used by the
  broader platform model
- the product should keep its strongest existing release controls rather than
  weakening them to fit generic wording
- any retained OpenClaw-specific difference should be explicit and documented,
  not left as implied legacy behavior

### Implemented Control

- `platform-engineering` now makes the standardized model explicit for
  OpenClaw by:
  - switching the stage verification catalog to `requiredByDefault`
  - documenting `environments/stage/promotion-readiness.yaml` as the retained
    product-local filename for the standardized stage readiness decision
  - adding a product-owned OpenClaw release-governance runbook
  - updating the OpenClaw scripts and shared platform docs so operator-facing
    language uses the standardized stage-readiness terminology
- the stage readiness record itself now carries:
  - `schemaVersion`
  - `product`
  - `environment`

### Operating Evidence

- the OpenClaw product contract and runbooks now distinguish clearly between:
  - stage candidate
  - stage verification
  - standardized stage readiness decision
  - prod verification
  - prod lifecycle
- OpenClaw still keeps the promotion-gate file name
  `environments/stage/promotion-readiness.yaml`, but that difference is now
  reviewable instead of implicit
- the stage readiness helper still accepts the older
  `defaultRequiredForPromotion` field as a compatibility alias, which prevents
  accidental operator breakage while the product-owned catalog and docs now
  use the standardized field

## Review Areas

### Delivery

- this change improves delivery truth because the shared standards and the
  OpenClaw product docs now describe the same release model
- keeping the retained filename is acceptable because the difference is
  documented as an intentional promotion-gate label rather than hidden legacy
  drift
- the new product-owned release-governance runbook strengthens operator
  reviewability without widening the rollout authority boundary

### Runtime

- no new runtime authority is introduced
- the stage readiness record is now easier to audit because it identifies the
  product and environment explicitly
- the reconciled wording reduces the risk that operators treat a historic file
  label as proof of a different control model than the one the platform
  standards now require

### Identity

- no new human or machine identity is introduced
- the change does not widen any caller, workflow, or runtime principal

### Secrets

- no new secret class or custody path is introduced
- this tranche is about release-state clarity, not secret-delivery expansion

## Decision

`approved-with-findings`

Approved because the change reconciles a real release-governance drift without
weakening OpenClaw's existing gated promotion model.

Findings and residual risk:

1. OpenClaw still intentionally keeps `promotion-readiness.yaml` as a retained
   filename. That is acceptable only while the product docs continue to state
   clearly that it is the standardized stage readiness decision.
2. The stage readiness helper still accepts the older
   `defaultRequiredForPromotion` alias for compatibility. Reopen the review if
   new product artifacts start writing that field again instead of the
   standardized `requiredByDefault`.

Required follow-up:

- keep the retained filename explicitly documented in the OpenClaw product
  contract, runbooks, and shared workflow docs whenever those surfaces change
- treat any future attempt to expand OpenClaw's release model or approval
  automation beyond the current bounded path as a fresh delta-review trigger

## Related Artifacts

- [`../../architecture/products/openclaw/README.md`](../../architecture/products/openclaw/README.md)
- [`../../architecture/products/openclaw/required-controls.md`](../../architecture/products/openclaw/required-controls.md)
- [`../security-review-checklist.md`](../security-review-checklist.md)
- [`../security-delta-review-process.md`](../security-delta-review-process.md)
