# Context Governance Gateway

## Role

`context-governance-gateway` is the implementation component for Operational
Context Governance and Context Admission Control. It captures raw operational
context, normalizes and classifies it, redacts risky material, budgets and
projects safe excerpts, then emits model-safe/operator-safe packets, receipts,
digests, and local ledger events.

It does not own workspace contracts, Workspace Governance Control Fabric
readiness, Workspace Delivery ART mutation, platform deployment authority,
security acceptance, custom scanners, custom object storage, or model gateway
policy.

## Trust Boundary

CGG sits at the boundary before operational context reaches AI agents,
operators, CI, or automation:

- raw artifacts can contain secrets, internal hostnames, private IPs, command
  output, repo contents, or runtime evidence
- model-safe packets must contain only redacted, sliced, budgeted, and
  policy-admitted context
- full artifact custody remains local in the current approved slices
- active local `dev-integration` runtime is approved only after workspace
  lifecycle activation and only for local-k3s service-shape proof
- the provider-neutral governed AI gateway handoff is approved as a dormant
  source contract only
- governed service-mode runtime, shared stage/prod storage, dashboard raw
  browsing, downstream handoff activation, and model invocation are not
  approved yet

## Current Admitted Shape

- owner repo: `context-governance-gateway`
- workspace authority owner: `workspace-governance`
- platform runtime owner: `platform-engineering`
- security owner: `security-architecture`
- current runtime lane: local CLI/source evidence plus security-approved
  local-k3s `dev-integration` after workspace lifecycle activation
- stage/prod status: not admitted

## Service Mode Admission Gate

The next maturity boundary after local `dev-integration` is governed shared
service mode. That boundary is not approved yet.

Before service implementation or runtime activation, CGG must satisfy the
service-mode security requirements for:

- caller identity and authorization
- raw and redacted artifact custody
- retention and deletion
- debug override
- tamper-evident ledger events
- model-safe and operator-safe packet projection
- downstream consumer attribution and denial metadata

The current security decisions approve active local dev-integration and the
dormant provider-neutral handoff source contract only. They keep governed
shared metadata storage, governed shared artifact storage, dashboard raw
browsing, downstream handoff activation, scanner execution, model invocation,
stage, and production blocked until implementation, platform, and security
evidence exist for those boundaries.

## Security Model

### Identity

- Phase 1 local CLI has no service identity or network listener.
- Active local dev-integration may use local profile secrets only.
- Future governed API, worker, dashboard, broker, or adapter identity must be
  distinct from operator identity and attributable in receipts or audit
  metadata.
- CGG outputs must not become autonomous approval or mutation authority.

### Secrets

- Raw artifacts are sensitive local evidence.
- Default projection posture is deny raw model projection when sensitive or
  uncertain material is detected.
- Scanner integrations may improve detection later, but they do not remove the
  need for packet admission, receipt, and custody controls.

### Delivery

- Source implementation lands in `context-governance-gateway`.
- Workspace contracts and profile registry truth stay in `workspace-governance`.
- Platform deployment state, version pinning, and promotion stay in
  `platform-engineering`.
- Security review and acceptance stay in `security-architecture`.

### Runtime

- Phase 1 local CLI remains local-only.
- Active local dev-integration may run API, worker, PostgreSQL, MinIO, PVC-backed
  state, read-only smoke, and access through the active profile only.
- Persistent governed service-mode state still requires approved identity,
  storage, retention, deletion, encryption, access, debug override,
  tamper-evident audit, backup, restore, and rollback posture.

### AI

- CGG may produce packets for later AI-assisted or operator-assisted
  workflows.
- CGG may project the reviewed provider-neutral three-field gateway handoff as
  dormant source behavior after packet and receipt integrity agree.
- It does not approve model invocation or replace governed model-access
  controls.
- Downstream AI consumers must preserve attribution, output validation, and
  human approval for security or delivery decisions.

## Principal Risks

- raw operational context leaking into model-safe packets
- false negatives in deterministic redaction before scanner integrations land
- local raw artifact custody being mistaken for enterprise shared custody
- service-mode runtime starting before identity, storage, and security review
  are complete
- CGG being mistaken for WGCF, an LLM gateway, a scanner, or an approval
  authority

## Required Companion Artifacts

- Service-mode security requirements:
  [`service-mode-security-requirements.md`](service-mode-security-requirements.md)
- Service-mode admission gates security delta:
  [../../../reviews/components/2026-05-05-context-governance-gateway-service-mode-admission-gates.md](../../../reviews/components/2026-05-05-context-governance-gateway-service-mode-admission-gates.md)
- Active dev-integration runtime security delta:
  [../../../reviews/components/2026-05-05-context-governance-gateway-active-devint-runtime.md](../../../reviews/components/2026-05-05-context-governance-gateway-active-devint-runtime.md)
- Provider-neutral context handoff security delta:
  [../../../reviews/components/2026-08-22-context-governance-gateway-provider-neutral-context-handoff.md](../../../reviews/components/2026-08-22-context-governance-gateway-provider-neutral-context-handoff.md)
- Phase 1 local custody security delta:
  [../../../reviews/components/2026-05-05-context-governance-gateway-phase-1-local-custody.md](../../../reviews/components/2026-05-05-context-governance-gateway-phase-1-local-custody.md)
- AI security and governance standard:
  [../../../standards/ai-security-and-governance.md](../../../standards/ai-security-and-governance.md)
- AI and agentic domain:
  [../../domains/ai-and-agentic.md](../../domains/ai-and-agentic.md)
- component inventory:
  [../../platform/component-inventory.md](../../platform/component-inventory.md)
- workspace governance active component contract:
  `workspace-governance/contracts/components.yaml`
- dev-integration profile registry:
  `workspace-governance/contracts/developer-integration-profiles.yaml`
