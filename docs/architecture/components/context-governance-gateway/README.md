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
- full artifact custody remains local in the current approved slice
- service-mode runtime, shared storage, workers, dashboard upload, broker
  adapters, and downstream AI gateway adapters are not approved yet
- the proposed `dev-integration` profile is an admission contract only and must
  fail closed until platform and security gates approve service mode

## Current Admitted Shape

- owner repo: `context-governance-gateway`
- workspace authority owner: `workspace-governance`
- platform runtime owner: `platform-engineering`
- security owner: `security-architecture`
- current runtime lane: local CLI/source evidence plus proposed
  `dev-integration` profile
- stage/prod status: not admitted

## Security Model

### Identity

- Phase 1 has no service identity or network listener.
- Future API, worker, dashboard, broker, or adapter identity must be distinct
  from operator identity and attributable in receipts or audit metadata.
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

- Phase 1 is local CLI only.
- The proposed dev-integration profile may report status and run read-only
  static smoke, but `up` and `access` must fail closed.
- Persistent service-mode state requires approved storage, retention, deletion,
  encryption, access, audit, and rollback posture.

### AI

- CGG may produce packets for later AI-assisted or operator-assisted
  workflows.
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
