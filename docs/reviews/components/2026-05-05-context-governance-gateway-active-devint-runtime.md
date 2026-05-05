# Context Governance Gateway Active Dev-Integration Runtime Security Delta

## Summary

- date: 2026-05-05
- owner repo: `security-architecture`
- affected review subjects:
  - `repos.context-governance-gateway`
  - `components.context-governance-gateway`
- ART items:
  - `openproject://work_packages/639`
  - `openproject://work_packages/640`
  - `openproject://work_packages/646`
- related upstream reviews:
  - [`2026-05-05-context-governance-gateway-phase-1-local-custody.md`](2026-05-05-context-governance-gateway-phase-1-local-custody.md)
  - [`2026-05-05-context-governance-gateway-service-mode-admission-gates.md`](2026-05-05-context-governance-gateway-service-mode-admission-gates.md)
- related implementation evidence:
  - `context-governance-gateway` PR #12
  - `platform-engineering` PR #187
  - `security-architecture` PR #80
- decision: `approved-with-findings`

This delta review approves CGG active local `dev-integration` runtime
activation only. It does not approve governed `stage` or `prod`, model
invocation, downstream adapters, broad shared custody, debug override, or raw
artifact projection.

## Scope Delta

### Design Intent

CGG remains the context-admission control-plane component. The immediate target
is not enterprise shared service maturity; it is a local-k3s dev-integration
runtime that proves API, worker, packet, receipt, manifest, metrics, trace, and
safe dashboard metadata behavior before any governed rollout.

The active profile must remain a local iteration lane:

- workspace registry controls self-serve launch
- platform accepts the local runtime shape and suspend/reset behavior
- security approves the local custody boundary with findings
- stage and production stay blocked until later platform and security gates

### Implemented Control

The reviewed implementation and platform evidence provide:

- active-only local-k3s API, worker, PostgreSQL, MinIO, Services, and PVCs
- local profile secrets generated under ignored `.dev-integration` state
- owner-repo lifecycle scripts for `up`, `status`, `access`, `smoke`, `down`,
  `reset`, and `promote-check`
- shared runner lifecycle gating that refuses `up`, `access`, and `smoke`
  while the workspace registry lifecycle is not `active`
- read-only smoke against a seeded safe packet, receipt, manifest, dashboard,
  metrics, and trace set
- raw projection denial when secret-like material is detected
- redaction marker and raw-secret non-leakage proof
- `devint-down` suspend behavior that preserves PVCs and local secrets
- `devint-reset` destructive local reset behavior
- platform docs that explicitly deny stage/prod overclaim

### Operating Evidence

Operating evidence reviewed:

- owner-repo active smoke reported `runtime_ready=true`
- raw projection was denied
- seeded secret-like material did not appear in the model-safe excerpt
- receipt digest matched manifest digest
- dashboard, metrics, and traces exposed safe metadata only
- platform shared runner `status` resolved the build-admitted profile and
  reported `launchable=false`
- platform shared runner `up` and `smoke` failed closed before workspace
  activation
- platform PR #187 recorded local dev-integration acceptance and stage/prod
  denial
- security PR #80 refreshed generated security change-record evidence after
  platform main contained the platform acceptance record

## Review Areas

### Identity

Approved for local dev-integration:

- profile-local runtime secrets and local operator attribution through the
  shared dev-integration session manifest
- no production service identity
- no shared enterprise caller identity
- no downstream adapter identity

Findings:

1. Local dev-integration secrets are acceptable only because the profile is
   local, non-governed, and gated by workspace lifecycle.
2. A future stage or production runtime still requires distinct API, worker,
   maintenance, caller, and operator identities with operation-level
   authorization.

### Secrets

Approved for local dev-integration:

- deterministic redaction and raw projection denial in the active smoke path
- local MinIO/PVC-backed custody for raw and redacted artifacts
- reference-based packet and receipt evidence
- no raw artifact bodies in platform release records or ART completion notes

Findings:

1. Local raw custody can accumulate sensitive operational context. Operators
   must treat `devint-reset` as destructive and avoid copying raw artifacts
   into chat, tickets, release records, dashboards, or model prompts.
2. Scanner integrations, encryption posture, retention deletion, legal hold,
   backup, and restore are still not approved for governed shared custody.

### Delivery

Approved for local dev-integration:

- platform acceptance of local runtime shape and operator docs
- workspace lifecycle registry as the launch authority
- security review as acceptance authority for the local custody boundary
- no direct ART, platform release-state, workspace contract, or security
  finding mutation by CGG

Findings:

1. CGG evidence remains context evidence only. It is not approval authority.
2. Workspace activation must reference this review and the platform acceptance
   record; otherwise the launch control story is incomplete.

### Runtime

Approved for local dev-integration:

- API Deployment and ClusterIP Service
- worker Deployment with safe heartbeat behavior
- PostgreSQL and MinIO local dev-integration dependencies
- PVC-backed CGG state
- local port-forward access through the active profile
- read-only smoke
- suspend by scaling deployments to zero while preserving PVCs and local secrets
- reset by deleting local namespace and local profile state

Not approved:

- governed stage or production runtime
- Argo application
- production image pinning
- production secrets
- broad scanner execution in a shared runtime
- dashboard raw browsing
- broker, WGCF, CI, or model-facing adapters
- debug override

### AI

Approved for local dev-integration:

- model-safe packet generation and safe metadata inspection
- default denial of raw projection when secret-like material appears

Not approved:

- model invocation
- raw context projection to any model
- treating packets as delivery or security approval authority
- downstream adapter consumption without a later review

## Decision

`approved-with-findings`

Approved because the active local dev-integration runtime now has implemented
owner-repo controls, platform acceptance, read-only smoke proof, raw projection
denial, and explicit stage/prod denial. The residual findings are acceptable
for local dev-integration only.

Required follow-up before workspace activation:

1. `workspace-governance` must set the CGG profile lifecycle to `active` only
   after referencing this review and the platform acceptance record.
2. Shared runner proof must be rerun after workspace activation.
3. If raw context appears in packet, dashboard, metric, trace, ART note, or
   model context, treat it as a security blocker.

Required follow-up before governed `stage` or `prod`:

1. Define production identity and authorization.
2. Define encrypted custody, retention, deletion, legal hold, backup, restore,
   and support readiness.
3. Define debug override with operator, reason, scope, expiry, approval, and
   ledger evidence.
4. Define image provenance, migration, network, and rollback controls.
5. Refresh security review against the governed candidate.

## Risk Disposition

ART risk `openproject://work_packages/646` is mitigated for local
dev-integration by:

- read-only smoke
- raw projection denial
- local-only custody
- platform docs denying stage/prod overclaim
- `devint-down` suspend behavior
- destructive `devint-reset` boundary

The broader enterprise shared-custody risk remains outside this active local
dev-integration activation and must be reviewed again before governed stage or
production.

## Related Artifacts

- [`../../architecture/components/context-governance-gateway/README.md`](../../architecture/components/context-governance-gateway/README.md)
- [`../../architecture/components/context-governance-gateway/service-mode-security-requirements.md`](../../architecture/components/context-governance-gateway/service-mode-security-requirements.md)
- [`2026-05-05-context-governance-gateway-service-mode-admission-gates.md`](2026-05-05-context-governance-gateway-service-mode-admission-gates.md)
- `context-governance-gateway/docs/operating-model/dev-integration-service.md`
- `platform-engineering/docs/components/context-governance-gateway/access.md`
- `platform-engineering/docs/records/change-records/2026-05-05-cgg-devint-platform-activation-acceptance.md`
