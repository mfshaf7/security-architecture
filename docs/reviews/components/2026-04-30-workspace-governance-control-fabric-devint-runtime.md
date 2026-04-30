# Workspace Governance Control Fabric Dev-Integration Runtime Security Delta

## Summary

- date: 2026-04-30
- owner repo: `security-architecture`
- affected review subjects:
  - `repos.workspace-governance-control-fabric`
  - `components.workspace-governance-control-fabric`
- ART item: `openproject://work_packages/495`
- decision: `approved-with-findings`

This delta review covers activation of the `governance-control-fabric`
dev-integration runtime profile as a real local-k3s API Deployment, Service,
PostgreSQL StatefulSet, PVC, and migration Job. It supersedes the earlier
source-only posture for local runtime access, but it does not approve governed
stage or production deployment.

## Scope Delta

### Approved Dev-Integration Shape

- WGCF API runs as a local-k3s Deployment in
  `devint-governance-control-fabric-<operator>`.
- WGCF API is exposed through a ClusterIP Service and operator port-forward
  from `make devint-access PROFILE=governance-control-fabric`.
- WGCF metadata runs in a local-k3s PostgreSQL StatefulSet with a persistent
  volume claim in the same dev-integration namespace.
- The WGCF image runs `alembic upgrade head` as a Kubernetes Job before API
  rollout is accepted.
- Runtime image comes from
  `ghcr.io/mfshaf7/workspace-governance-control-fabric:sha-<source-sha>`.
- Shared smoke is read-only and covers health, readiness, status, graph query,
  validation-plan dry run, database migration evidence, and receipt metadata
  reads.
- The status path must fail closed on Kubernetes connection errors; only a
  verified absent namespace may return a clean `not-created` status.
- The worker runtime, governed stage/prod PostgreSQL, artifact custody store,
  and governed stage/prod path remain out of scope.

### Security Boundary

- No external ingress is approved.
- No shared static API key is introduced.
- No direct workspace contract, ART, platform release, or security finding
  mutation is introduced.
- The API surface remains read-oriented for the current implemented routes.
- The profile is local dev-integration evidence only, not governed rollout
  evidence.

## Review Areas

### Identity

The day-one runtime has Kubernetes workload identity only through its local
ServiceAccount. That is acceptable for local dev-integration because the API is
not exposed through ingress and does not mutate upstream authority stores.

Before stage or prod, WGCF must define caller authentication, authorization by
operation, audit identity propagation, and service-to-service identity.

### Secrets

The approved dev-integration slice introduces a local-only PostgreSQL password
stored as a Kubernetes Secret in the dev-integration namespace. It is not a
platform credential and must not be reused for stage/prod. The API image must
not embed credentials. Future platform secret delivery requires a separate
review.

### Delivery

The image build pipeline and local-k3s Deployment are acceptable as a fast
runtime lane because platform-engineering remains the runtime owner and
workspace-governance remains the profile lifecycle authority. The profile must
not be used as stage/prod evidence.

### Runtime

The local-k3s runtime is approved only for the current API surfaces and the
local PostgreSQL metadata dependency:

- `GET /healthz`
- `GET /readyz`
- `GET /v1/status`
- `GET /v1/graph`
- `GET /v1/graph/query`
- `POST /v1/validation-plans`
- `GET /v1/receipts`

The approved API Deployment and migration Job must preserve basic pod
hardening:

- non-root runtime
- no privilege escalation
- dropped Linux capabilities
- ClusterIP Service only

The approved PostgreSQL runtime is local dev-integration only. It must remain
inside the profile namespace, use a persistent volume claim for suspend/resume,
and be destroyed only through the explicit `devint-reset` path.

Future API-side validation execution, worker execution, governed stage/prod
PostgreSQL, artifact custody, ingress, or model-facing integration requires
fresh review.

### AI

This change does not activate AI behavior. Future Governance Operations
Console or model-consumption paths must still pass through governed context
admission and approved model-access controls.

## Decision

`approved-with-findings`

Findings and residual risk:

1. Dev-integration access is approved only for local-k3s API contract and
   console-consumption iteration.
2. No stage/prod deployment, external ingress, identity provider integration,
   or secrets path is approved.
3. API-side validation execution, worker execution, and governed stage/prod
   persistence remain blocked until reviewed.
4. Receipt and artifact custody risks remain open for future enterprise
   evidence storage.
5. Any path that lets WGCF mutate ART, platform release state, security
   acceptance, or workspace contracts is a security-significant regression.

## Related Artifacts

- `workspace-governance-control-fabric/Dockerfile`
- `workspace-governance-control-fabric/.github/workflows/build-image.yaml`
- `workspace-governance-control-fabric/dev-integration/profiles/governance-control-fabric/profile.yaml`
- `platform-engineering/docs/records/change-records/2026-04-30-wgcf-devint-runtime-access.md`
- `workspace-governance/contracts/developer-integration-profiles.yaml`
- [`2026-04-30-workspace-governance-control-fabric-operator-surface.md`](2026-04-30-workspace-governance-control-fabric-operator-surface.md)
