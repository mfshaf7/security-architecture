# OpenProject Runtime Sizing And Vault Single-Node Review

## Summary

- date: 2026-04-23
- owner repos:
  - `operator-orchestration-service`
  - `platform-engineering`
- affected review subjects:
  - `repos.platform-engineering`
  - `products.openproject`
  - `components.vault`
- decision: `approved-with-findings`

This delta review covers two related runtime posture changes on the single-host
platform:

1. bounding OpenProject to one Puma worker and GoodJob `maxThreads=10`
2. reducing the workload Vault set from three replicas to one and updating the
   Windows/bootstrap helper path to target only `vault-0`

## Scope Delta

### Design Intent

- OpenProject should keep enough concurrency for the current platform-managed
  and dev-integration ART workloads without reserving workstation memory for
  unused Rails workers
- Vault should stop claiming an in-cluster HA posture that does not produce
  meaningful host-level redundancy on a single workstation
- the Windows-hosted `PlatformCoreHostStack` bootstrap path must stay aligned
  with the actual workload Vault topology so startup does not wait on
  nonexistent peers

### Implemented Control

- `operator-orchestration-service` now renders the active
  `accepted-idea-delivery` profile with:
  - `OPENPROJECT_WEB__WORKERS=1`
  - `workers.default.maxThreads=10`
- `platform-engineering` now carries the same bounded OpenProject runtime
  settings in the governed OpenProject Helm values
- `platform-engineering` reduces `environments/shared/argocd/vault-app.yaml`
  to `ha.replicas: 1`
- the Windows/bootstrap source list for workload Vault pods now contains only
  `vault-0`, and the generated `platform-vault-unseal.ps1` helper was re-rendered
- platform Vault docs now describe the real single-node posture instead of an
  HA cluster

### Operating Evidence

- live proof in the existing devint OpenProject pod:
  - `OPENPROJECT_WEB__WORKERS=1 bundle exec rails runner "puts OpenProject::Configuration.web_workers"` returned `1`
- the generated workload Vault unseal helper now renders:
  - `$VaultPods = @('vault-0')`
- the scheduled-task bootstrap wrapper still invokes the same helper path:
  - `platform-vault-unseal.ps1`
- memory pressure reduction is the explicit operational goal for this change,
  but the control significance is the topology and startup-path alignment

## Review Areas

### Secrets

- reducing Vault to one replica does not widen who can read secrets, but it
  does reduce in-cluster availability margin
- on this single-host platform the previous three-pod shape did not provide
  true host-level redundancy, so the new singleton posture is more honest
  operationally
- the material control requirement is that recovery documentation, snapshots,
  and Windows/bootstrap helpers stay aligned with the singleton posture

### Runtime

- OpenProject runtime sizing is a bounded runtime adjustment, not a workflow or
  identity expansion
- lowering Puma workers and GoodJob threads is acceptable because the active
  workload is still workstation-scale and the change does not widen delivery
  authority
- startup-path alignment is required runtime hygiene; otherwise OpenClaw
  startup could hang waiting for `vault-1` and `vault-2`

### Delivery

- no new delivery mutation surface is introduced
- the active broker-owned ART execution path remains unchanged
- keeping devint and governed OpenProject sizing aligned reduces runtime drift
  between the two OpenProject lanes

### Identity

- no new human or machine identity is introduced
- existing Vault auth roles and OpenProject admin/token custody remain in the
  same owners and paths

## Decision

`approved-with-findings`

Approved because the change improves workstation fit and removes a false HA
assumption from the startup and recovery path.

Findings and residual risk:

1. `components.vault` now has an explicitly weaker in-cluster availability
   posture. This is acceptable on the current single-host platform, but it must
   not be described as HA.
2. Any future claim of governed stage/prod resilience for workload Vault must
   reopen the topology decision and restore a real multi-host trust and
   recovery story, not just a larger replica count on one machine.

Required follow-up:

- keep the generated Windows bootstrap artifacts in sync whenever
  `platform_vault_pod_names` changes
- keep Vault backup and recovery instructions anchored on the singleton
  workload pod until the topology changes again

## Related Artifacts

- [`../../architecture/components/vault/README.md`](../../architecture/components/vault/README.md)
- [`../../architecture/products/openproject/required-controls.md`](../../architecture/products/openproject/required-controls.md)
- [`../security-delta-review-process.md`](../security-delta-review-process.md)
