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
product overlay boundaries.

## Scope Delta

### Design Intent

- shared observability should be treated as a platform baseline rather than an
  OpenClaw-owned identity
- shared dashboard assets should be treated as an explicit overlay on that
  baseline
- product-specific overlay assets should move under product ownership instead
  of drifting back into shared platform paths
- operator access surfaces should explain the compatibility-phase naming truth
  without implying OpenClaw ownership of the shared Grafana, Prometheus, or
  Alertmanager paths

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
  - compatibility-phase legacy OpenClaw-shaped app and service names
- OpenClaw-specific overlay ownership now has a product-local home under:
  - `products/openclaw/observability/`
- the OpenClaw `/platform` catalog remains a read-only operator inventory
  surface, but its shared observability entries are now labeled as
  platform-owned instead of looking product-owned

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
  and auth surfaces are no longer described as if they belong to OpenClaw
- the compatibility phase is acceptable because the operator-facing runbooks
  now say explicitly that legacy names such as `openclaw-observability` remain
  implementation artifacts, not ownership truth

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

- the OpenClaw `/platform` catalog may continue to surface shared platform UIs
  because it is an operator inventory, not a delegated control plane
- this is acceptable only while the catalog stays read-only, keeps credentials
  out of the catalog payload, and does not add mutating or secret-bearing
  actions for shared observability

## Decision

`approved-with-findings`

Approved because the change improves trust-boundary clarity and operator
understanding without widening runtime authority.

Findings and residual risk:

1. Compatibility-phase legacy names such as `openclaw-observability` are
   acceptable only while the primary runbooks, readiness records, and access
   surfaces continue to identify those paths as platform-baseline surfaces.
2. Product-local overlays are acceptable only while they do not introduce a
   parallel credential model, cross-product data exposure, or hidden control
   path around the shared Grafana and auth-proxy surfaces.
3. The OpenClaw `/platform` operator catalog may remain the access index for
   shared platform UIs only while it stays read-only and free of embedded
   credentials, tokens, or direct mutation paths.
4. Future work must reopen review if the platform baseline or overlay model
   expands into separate tenant-scoped Grafana organizations, additional human
   identities, writable operator actions, or new alert-routing destinations.

## Related Artifacts

- `platform-engineering/docs/decisions/adr/ADR-015-platform-observability-baseline-and-overlay-model.md`
- `platform-engineering/docs/components/observability/model.yaml`
- `platform-engineering/docs/components/observability/release-governance.md`
- `platform-engineering/docs/runbooks/access-platform-uis.md`
- `platform-engineering/docs/runbooks/access-grafana.md`
- `platform-engineering/docs/runbooks/full-platform-runtime-drill.md`
- `platform-engineering/environments/shared/runtime-drills/full-platform-runtime-drill.yaml`
- `platform-engineering/environments/prod/observability-release/`
- `platform-engineering/environments/stage/observability-release/`
- `platform-engineering/environments/prod/platform-dashboards-release/`
- `platform-engineering/environments/stage/platform-dashboards-release/`
- `platform-engineering/products/openclaw/platform-operator-catalog.yaml`
- `platform-engineering/products/openclaw/observability/overlay-assets.yaml`
- [`../security-delta-review-process.md`](../security-delta-review-process.md)
- [`../security-review-checklist.md`](../security-review-checklist.md)
