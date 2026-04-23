# Platform Environment Readiness Aggregate Gate

## Summary

- date: 2026-04-23
- owner repo: `platform-engineering`
- affected review subjects:
  - `repos.platform-engineering`
  - `products.openclaw`
  - `products.openproject`
  - `components.operator-orchestration-service`
  - `components.vault`
  - `components.external-secrets`
  - `components.platform-postgresql`
  - `components.observability`
- decision: `approved-with-findings`

This delta review covers the new shared aggregate environment-readiness control
that evaluates stage and prod from the exact governed workload records instead
of leaving operators to infer readiness from health alone.

## Scope Delta

### Design Intent

- stage and prod should each have one shared fail-closed readiness verdict
- that verdict should consume the already-governed per-workload release-state
  records rather than invent a parallel health model
- product-specific semantics should stay in product adapters where they already
  exist, while the platform owns the aggregate decision path

### Implemented Control

- `platform-engineering` now carries:
  - `environments/stage/environment-readiness.yaml`
  - `environments/prod/environment-readiness.yaml`
  - `scripts/validate_environment_readiness.py`
  - `docs/runbooks/assess-environment-readiness.md`
- the shared validator:
  - reuses the OpenClaw product-owned readiness and prod-verification adapter
  - evaluates OpenProject and `operator-orchestration-service` through their
    recorded stage or prod release-state objects
  - evaluates supporting components through explicit support-readiness records
  - accepts `inactive` only where the current workload contract already says
    inactive is the correct posture

### Operating Evidence

- the aggregate `status` mode can now report which exact workload blocks stage
  or prod readiness
- the strict `validate` mode remains fail-closed because the current governed
  records are still largely `pending`
- no live trust boundary or secret path widened in this tranche; the control
  is an operator-facing decision surface over records already in Git

## Review Areas

### Delivery

- this is the correct control shape because environment readiness should be
  computed from exact governed workload records, not reconstructed from mixed
  health signals
- keeping OpenClaw on its existing product adapter avoids re-implementing
  product semantics in the shared platform layer
- the shared platform repo is the right owner because this verdict spans
  multiple workload tiers and products

### Runtime

- the new gate strengthens runtime truth by making stale or pending workload
  records visible at one aggregate seam
- allowing explicit `inactive` only where the contract already says so avoids
  forcing fake approval state for deliberately suspended surfaces
- the control still depends on the accuracy of the underlying workload records;
  it does not replace those lower-level checks

### Secrets

- the aggregate gate now makes shared secrets dependencies materially more
  reviewable because Vault, External Secrets, and PostgreSQL support-readiness
  can block environment readiness directly
- the validator does not need secret material itself; it consumes Git-tracked
  records and their references, which preserves least privilege

### Identity

- no new principal or credential path is introduced
- the operator surface is read-only with respect to the underlying workload
  records; it evaluates them rather than mutating backends

## Decision

`approved-with-findings`

Approved because the aggregate gate closes a real delivery and audit gap
without widening runtime or secret authority.

Findings and residual risk:

1. The aggregate gate is only as strong as the workload records it consumes. A
   `ready` verdict must never be treated as a substitute for missing
   workload-specific verification discipline.
2. `inactive` remains a bounded exception path. Reopen this review if the
   aggregate policy starts treating convenience suspensions as a normal success
   case rather than an explicit lifecycle posture.
3. The current validator is intentionally local-operator first. If later work
   adds remote workflow mutation or auto-approval behavior around this gate,
   require a fresh delta review before treating that expansion as safe.

## Related Artifacts

- `platform-engineering/environments/stage/environment-readiness.yaml`
- `platform-engineering/environments/prod/environment-readiness.yaml`
- `platform-engineering/scripts/validate_environment_readiness.py`
- `platform-engineering/docs/runbooks/assess-environment-readiness.md`
- `platform-engineering/docs/standards/governed-release-control-model.md`
- [`../../architecture/platform/trust-boundaries.md`](../../architecture/platform/trust-boundaries.md)
- [`../../architecture/domains/gitops-and-machine-trust.md`](../../architecture/domains/gitops-and-machine-trust.md)
- [`../../architecture/domains/secrets-and-recovery.md`](../../architecture/domains/secrets-and-recovery.md)
- [`../security-delta-review-process.md`](../security-delta-review-process.md)
- [`../security-review-checklist.md`](../security-review-checklist.md)
