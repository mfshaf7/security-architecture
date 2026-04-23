# Observability Baseline, Overlay, And Operator Access Review

## Summary

- date: 2026-04-24
- owner repo:
  - `platform-engineering`
- affected review subjects:
  - `repos.platform-engineering`
  - `components.observability`
- decision: `approved-with-findings`

This delta review covers the shift from an OpenClaw-shaped observability
identity toward a platform observability baseline with explicit shared and
product overlay boundaries, plus the follow-on hardening that moved the shared
UI catalog into a platform-owned path and renamed the live observability
runtime identities.

## Scope Delta

### Design Intent

- shared observability should be treated as a platform baseline rather than an
  OpenClaw-owned identity
- shared dashboard assets should be treated as an explicit overlay on that
  baseline
- product-specific overlay assets should move under product ownership instead
  of drifting back into shared platform paths
- operator access surfaces should stop implying OpenClaw ownership of the
  shared Grafana, Prometheus, or Alertmanager paths

### Implemented Control

- `platform-engineering` now records the baseline-versus-overlay model in:
  - `docs/decisions/adr/ADR-015-platform-observability-baseline-and-overlay-model.md`
  - `docs/components/observability/model.yaml`
- shared readiness and verification records now distinguish:
  - `layer: platform-baseline` for the observability stack
  - `layer: shared-component-overlay` for `platform-dashboards`
- shared operator runbooks and runtime-drill surfaces now describe:
  - platform baseline access
  - shared dashboard overlay access
  - platform-owned observability runtime identities
- OpenClaw-specific overlay ownership now has a product-local home under:
  - `products/openclaw/observability/`
- the shared UI inventory now lives under:
  - `docs/runbooks/platform-operator-catalog.yaml`
- the OpenClaw `/platform` catalog remains a read-only operator inventory
  surface, but it is now sourced from the platform-owned shared catalog rather
  than a product-local file

### Operating Evidence

- the shared platform runbooks now make the baseline-versus-overlay split
  explicit before an operator reaches the live endpoints
- the prod and stage readiness records now tie observability evidence to the
  correct layer instead of using one generic `observability healthy` claim
- the runtime-drill contract now distinguishes the platform baseline from the
  dashboard overlay in the shared drill surface

## Review Areas

### Identity

- the new model improves identity clarity because the shared observability UI
  and auth surfaces no longer read as if they belong to OpenClaw
- the platform-owned runtime names reduce the risk that operators mistake one
  product for the owner of the shared control-plane telemetry stack

### Runtime

- splitting baseline and overlay ownership is the correct runtime boundary
  because it prevents product-specific telemetry assets from silently defining
  the entire shared monitoring surface
- the runtime-drill and readiness surfaces are stronger now that they can name
  whether the platform baseline or the dashboard overlay actually moved

### Delivery

- product-local overlay ownership under `products/openclaw/observability/` is
  the correct delivery posture because it keeps product telemetry from
  re-entering shared paths without review
- shared component release governance remains in `platform-engineering`, which
  is correct because the Grafana host and shared auth proxy are still
  platform-owned

### Operator Access

- the OpenClaw `/platform` surface may continue to present the shared platform
  UI inventory because it is an operator inventory, not a delegated control
  plane
- this remains acceptable only while the platform-owned shared catalog stays
  read-only, keeps credentials out of the payload, and does not add mutating
  or secret-bearing actions for shared observability

## Decision

`approved-with-findings`

Approved because the change improves trust-boundary clarity and operator
understanding without widening runtime authority.

Findings and residual risk:

1. Product-local overlays are acceptable only while they do not introduce a
   parallel credential model, cross-product data exposure, or hidden control
   path around the shared Grafana and auth-proxy surfaces.
2. The OpenClaw `/platform` operator surface may remain the access index for
   shared platform UIs only while the underlying platform-owned catalog stays
   read-only and free of embedded credentials, tokens, or direct mutation
   paths.
3. Future work must reopen review if the platform baseline or overlay model
   expands into separate tenant-scoped Grafana organizations, additional human
   identities, writable operator actions, or new alert-routing destinations.

## Related Artifacts

- `platform-engineering/docs/decisions/adr/ADR-015-platform-observability-baseline-and-overlay-model.md`
- `platform-engineering/docs/components/observability/model.yaml`
- `platform-engineering/docs/components/observability/release-governance.md`
- `platform-engineering/docs/runbooks/access-platform-uis.md`
- `platform-engineering/docs/runbooks/access-grafana.md`
- `platform-engineering/docs/runbooks/environment-complete-runtime-drill.md`
- `platform-engineering/environments/shared/runtime-drills/environment-complete-runtime-drill.yaml`
- `platform-engineering/environments/prod/observability-release/`
- `platform-engineering/environments/stage/observability-release/`
- `platform-engineering/environments/prod/platform-dashboards-release/`
- `platform-engineering/environments/stage/platform-dashboards-release/`
- `platform-engineering/docs/runbooks/platform-operator-catalog.yaml`
- `platform-engineering/products/openclaw/observability/overlay-assets.yaml`
- [`../security-delta-review-process.md`](../security-delta-review-process.md)
- [`../security-review-checklist.md`](../security-review-checklist.md)
