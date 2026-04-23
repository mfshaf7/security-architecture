# Environment-Complete Runtime Drill And Shared UI Catalog Review

## Summary

- date: 2026-04-24
- owner repo: `platform-engineering`
- affected review subjects:
  - `repos.platform-engineering`
  - `components.observability`
  - `components.operator-orchestration-service`
  - `components.vault`
  - `components.external-secrets`
  - `components.platform-postgresql`
  - `components.openclaw-host-bridge`
- decision: `approved-with-findings`

This delta review covers two related control changes:

- the drill authority now has a real `environment-complete-runtime-drill`
  profile instead of reserving estate-complete language for a workflow that did
  not yet exist
- the shared platform operator UI inventory is now platform-owned instead of
  living under the OpenClaw product path

## Scope Delta

### Design Intent

- `full-platform` wording should only map to an estate-complete drill when
  every admitted lane and product environment in scope is actually exercised
- the platform should own the shared UI inventory for Argo, Vault, Grafana,
  Prometheus, Alertmanager, and OpenProject instead of surfacing that shared
  catalog from a product-local path
- shared observability runtime identities should read as platform-owned, not
  OpenClaw-owned

### Implemented Control

- `platform-engineering` now carries:
  - `docs/runbooks/platform-operator-catalog.yaml`
  - `docs/runbooks/environment-complete-runtime-drill.md`
  - `environments/shared/runtime-drills/environment-complete-runtime-drill.yaml`
  - `environments/shared/runtime-drills/environment-complete-runtime-drill-evidence-template.yaml`
  - `scripts/platform_drill.py`
- the compatibility alias `full-platform-runtime-drill` now resolves to the
  estate-complete profile instead of the active-stack profile
- the prod and stage observability runtime identities now use platform-owned
  names instead of legacy OpenClaw-shaped names
- the shared OpenClaw `/platform` Telegram inventory remains read-only, but
  its source of truth is now the platform-owned runbook catalog rather than a
  product-local catalog file

### Operating Evidence

- platform validation passed for:
  - observability taxonomy
  - repo structure
  - governance docs
  - operational docs
  - OpenClaw stage and prod environment-contract validation
  - `platform_drill.py plan` against:
    - `active-stack-runtime-drill`
    - `environment-complete-runtime-drill`
    - `full-platform-runtime-drill` compatibility alias

## Review Areas

### Identity

- the runtime identity rename is the correct trust-boundary move because the
  shared observability stack no longer reads like an OpenClaw-owned control
  plane
- moving the shared UI catalog under platform-owned runbooks removes an
  ownership ambiguity that previously made one product appear to own shared
  operator surfaces

### Delivery

- the new estate-complete drill profile is acceptable because it narrows the
  difference between what the workflow claims and what it actually enumerates
- the alias change is correct because `full-platform` now maps to the
  environment-complete profile instead of overstating active-stack coverage

### Runtime

- the environment-complete drill remains acceptable only while the operator
  evidence really captures every declared lane and environment in scope
- if operators start using the environment-complete label while skipping one of
  the declared lanes without an explicit `not_applicable` or exception record,
  the workflow regresses back into the same overclaiming problem

### Host Control

- the host bridge remains an explicitly declared surface in the new
  environment-complete drill, which is the correct posture
- this remains acceptable only while `platform_drill.py` stays ledger-oriented
  and does not become a direct host-control mutation authority

### Operator Access

- the platform-owned shared UI catalog is acceptable only while it remains
  read-only, free of embedded credentials, and separate from mutation or
  approval paths
- continuing to surface the catalog through OpenClaw Telegram `/platform` is
  acceptable because the Telegram command remains an inventory surface rather
  than a new shared control plane

## Decision

`approved-with-findings`

Approved because the change makes estate-complete drill language honest and
removes product-owned ambiguity from the shared UI inventory without widening
shared runtime authority.

Findings and residual risk:

1. `environment-complete-runtime-drill` is acceptable only while operators
   record every declared lane honestly. Estate-complete naming is not a
   substitute for evidence.
2. The shared UI catalog remains acceptable only while it stays read-only and
   avoids embedded secrets, tokens, or mutation links.
3. `platform_drill.py` remains acceptable only while it stays a contract and
   ledger surface instead of becoming a hidden multi-plane mutation
   controller.

## Related Artifacts

- `platform-engineering/docs/runbooks/platform-operator-catalog.yaml`
- `platform-engineering/docs/runbooks/environment-complete-runtime-drill.md`
- `platform-engineering/environments/shared/runtime-drills/environment-complete-runtime-drill.yaml`
- `platform-engineering/environments/shared/runtime-drills/environment-complete-runtime-drill-evidence-template.yaml`
- `platform-engineering/scripts/platform_drill.py`
- `platform-engineering/environments/prod/argocd/observability-app.yaml`
- `platform-engineering/environments/stage/argocd/observability-app.yaml`
- `platform-engineering/environments/prod/observability-assets/operator-ui-auth-proxy.yaml`
- `platform-engineering/environments/stage/observability-assets/operator-ui-auth-proxy.yaml`
- [`../security-delta-review-process.md`](../security-delta-review-process.md)
- [`../security-review-checklist.md`](../security-review-checklist.md)
