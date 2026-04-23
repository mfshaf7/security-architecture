# Supporting Component Release Readiness Contracts Review

## Summary

- date: 2026-04-23
- owner repo:
  - `platform-engineering`
- affected review subjects:
  - `repos.platform-engineering`
  - `components.vault`
  - `components.external-secrets`
  - `components.platform-postgresql`
  - `components.observability`
  - `components.platform-dashboards`
- decision: `approved-with-findings`

This delta review covers the rollout of explicit verification and
support-readiness records for the shared `supporting component` tier.

## Scope Delta

### Design Intent

- shared supporting services should no longer look stage-ready or prod-ready
  from health alone
- stage and prod should both carry reviewable release truth for the exact
  contract each supporting service exposes
- intentionally suspended stage support surfaces should stay explicitly
  `inactive`, not quietly implied-ready

### Implemented Control

- `platform-engineering` now carries operator-facing release-governance docs
  for:
  - `vault`
  - `external-secrets`
  - `platform-postgresql`
  - `observability`
- the platform repo now records:
  - stage and prod verification plus support-readiness for shared `vault`
  - stage and prod verification plus support-readiness for shared
    `external-secrets`
  - stage and prod verification plus support-readiness for the current
    prod-managed `platform-postgresql` contract
  - prod verification plus support-readiness for `observability`
  - prod verification plus support-readiness for `platform-dashboards`
  - stage verification plus support-readiness for `observability` and
    `platform-dashboards`, both intentionally marked `inactive` while the stage
    surfaces remain suspended

### Operating Evidence

- the current contract paths remain reviewable in Git for each supporting
  service
- the new records intentionally remain `pending` or `inactive` because this
  tranche adds the governance objects, not fresh rehearsal evidence
- stage observability and stage dashboard surfaces are still intentionally
  suspended, so `inactive` is the correct current posture for those records

## Review Areas

### Delivery

- this is the correct control move because shared dependencies can otherwise
  invalidate product or control-plane readiness while still appearing healthy
- splitting verification from support-readiness preserves fail-closed posture
  for later aggregate readiness automation
- the platform repo is the correct owner because these are platform-managed
  contracts, not independent product promotion lanes

### Secrets

- this tranche materially improves reviewability around Vault and External
  Secrets because secret delivery can no longer hide behind vague shared-health
  claims
- `platform-postgresql` also benefits because credential delivery is now part
  of the governed support-readiness story instead of an implicit runtime
  assumption
- later verification tooling must still avoid widening access to Vault or
  database credentials merely to record evidence

### Runtime

- marking suspended stage observability and dashboard surfaces `inactive` is
  the right bounded use of the lifecycle vocabulary
- the prod-managed PostgreSQL contract remains an explicit shared dependency
  for stage-facing OpenProject rehearsal; that shared-runtime reality is
  acceptable only while it stays documented and reviewable

### Identity

- no new human or machine identities were introduced by this tranche
- later automation that writes verification or support-readiness records must
  keep those write paths attributable and least-privileged

## Decision

`approved-with-findings`

Approved because the change closes a real audit and delivery-governance gap for
shared dependencies without widening runtime authority.

Findings and residual risk:

1. Every supporting component record is still intentionally fail-closed. The
   platform must not describe these services as governed-ready until exact
   contract-specific verification evidence is recorded.
2. The prod-managed `platform-postgresql` contract is currently reused for
   stage-facing OpenProject rehearsal. That is acceptable only while it stays
   explicit. Reopen the review if a separate stage database contract is
   introduced.
3. `inactive` is acceptable for stage observability and stage dashboard
   records only while their suspension is deliberate and documented. When those
   surfaces resume, the records must move back to real pending verification and
   support-readiness state.
4. The later aggregate readiness workflow must consume these exact records
   rather than bypassing them through generic health summaries.

## Related Artifacts

- `platform-engineering/docs/components/vault/release-governance.md`
- `platform-engineering/docs/components/external-secrets/release-governance.md`
- `platform-engineering/docs/components/platform-postgresql/release-governance.md`
- `platform-engineering/docs/components/observability/release-governance.md`
- `platform-engineering/environments/shared/vault-release/`
- `platform-engineering/environments/shared/external-secrets-release/`
- `platform-engineering/environments/prod/platform-postgresql-release/`
- `platform-engineering/environments/stage/observability-release/`
- `platform-engineering/environments/prod/observability-release/`
- `platform-engineering/environments/stage/platform-dashboards-release/`
- `platform-engineering/environments/prod/platform-dashboards-release/`
- [`../security-delta-review-process.md`](../security-delta-review-process.md)
- [`../security-review-checklist.md`](../security-review-checklist.md)
