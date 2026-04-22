# Operator Orchestration Shared Release Governance Review

## Summary

- date: 2026-04-22
- owner repos:
  - `platform-engineering`
  - `operator-orchestration-service`
- affected review subjects:
  - `components.operator-orchestration-service`
  - `repos.platform-engineering`
  - `repos.operator-orchestration-service`
- decision: `approved-with-findings`

This delta review covers the rollout of the standardized release-governance
model onto `operator-orchestration-service` as a shared control-plane
component.

The change adds:

- stage candidate, verification, and readiness records for the broker
- prod post-promotion verification record for the shared broker contract
- component-owned stage and prod verification catalogs
- source-side release metadata artifact expectations in the image build flow

## Scope Delta

`operator-orchestration-service` already shaped stage and prod-adjacent
workflow behavior, but its governed truth stopped at a manually pinned shared
deployment digest.

That left a serious control gap:

1. the shared broker could look healthy while its release state and verification
   truth were stale
2. stage and prod readiness had no explicit record proving which broker
   behavior was actually exercised
3. the platform repo had to infer component verification checks instead of
   using component-owned release expectations

This rollout fixes that by making the broker participate in release governance
as a shared control-plane component rather than a loosely pinned support
runtime.

## Review Areas

### Identity

- the change does not add new runtime identities directly
- it does create stronger accountability expectations for whoever records the
  broker candidate, verification, readiness, and prod verification state
- later automation must keep those write paths attributable and least-privileged

### Secrets

- the rollout does not change secret distribution paths by itself
- later release tooling must still avoid broadening access to the broker's
  OpenProject API token or caller shared secret just to record readiness state

### Delivery

- this is the correct delivery-control posture because stale broker behavior
  can invalidate both stage rehearsal and prod-facing workflow assumptions
- keeping the verification catalogs in the component repo is the right owner
  split; the platform should record release truth, not guess broker behavior
- using pending verification and readiness by default is correct until the
  exact shared contract is actually rehearsed and approved

### Runtime

- the current shared-runtime reality is still explicit: one shared deployment
  contract currently serves both stage rehearsal and prod-facing dependent
  workflows
- that is acceptable temporarily as long as the release objects point back to
  that exact shared contract and do not pretend a separate stage-only runtime
  already exists
- later maturity work may still choose to split the runtime, but that is not
  required for this governance step

### AI

- this broker can shape AI-adjacent or operator-assisted workflows later, so
  product-grade release governance is the correct baseline even before broader
  AI paths are activated

## Decision

`approved-with-findings`

Approved because the rollout closes a real trust and audit gap for a shared
control-plane component.

Required findings to carry forward:

- stage readiness must remain `pending` until a real candidate-specific broker
  rehearsal is recorded against the component-owned verification catalog
- prod verification must be reset or rerecorded whenever the shared deployment
  contract changes for prod-facing use
- later automation for candidate recording or readiness approval must preserve
  attributable least-privilege write paths

## Related Artifacts

- `platform-engineering/environments/shared/operator-orchestration-service/stage-candidate.yaml`
- `platform-engineering/environments/shared/operator-orchestration-service/stage-verification.yaml`
- `platform-engineering/environments/shared/operator-orchestration-service/stage-readiness.yaml`
- `platform-engineering/environments/shared/operator-orchestration-service/prod-verification.yaml`
- `platform-engineering/docs/components/operator-orchestration-service/release-governance.md`
- `operator-orchestration-service/verification-catalog.yaml`
- `operator-orchestration-service/prod-verification-catalog.yaml`
- `operator-orchestration-service/docs/architecture/release-governance.md`
- [`../security-delta-review-process.md`](../security-delta-review-process.md)
- [`../security-review-checklist.md`](../security-review-checklist.md)
