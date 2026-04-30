# Workspace Governance Control Fabric Operator Surface Security Delta

## Summary

- date: 2026-04-30
- owner repo: `security-architecture`
- affected review subjects:
  - `repos.workspace-governance`
  - `repos.workspace-governance-control-fabric`
- ART item: `openproject://work_packages/429`
- decision: `approved-with-findings`

This delta review evaluates the pre-implementation operator surface for the
Workspace Governance Control Fabric. It covers the identity, audit, approval,
evidence-custody, future API/runtime, and AI-adjacent boundaries created by
the #428 contract and runtime operator surface.

This is not a live-runtime approval. It approves the framing and required
control posture that later implementation slices must preserve.

## Scope Delta

### Design Intent

- `workspace-governance` remains the authority for contracts, schemas, routing
  rules, maturity rules, and workspace-root guidance.
- `workspace-governance-control-fabric` becomes the runtime implementation
  layer for source snapshots, validation planning, readiness evaluation,
  control receipts, ledger events, API, worker, and CLI.
- The fabric should make governance validation faster and more observable
  without becoming a hidden approval system or direct mutation path.
- Operator-visible success should cite receipts and ledger events instead of
  raw terminal output or chat-only memory.

### Implemented Control

- `workspace-governance` now defines:
  - `contracts/governance-control-fabric-operator-surface.yaml`
  - `contracts/schemas/governance-control-fabric-operator-surface.schema.json`
  - `docs/governance-control-fabric-operator-surface.md`
- the contract defines:
  - minimum CLI and API meanings
  - record contracts for source snapshots, plans, runs, receipts, readiness
    decisions, authority references, escalation records, and ledger events
  - profiles for `local-read-only`, `dev-integration`, and `governed-stage`
  - denied actions for authority mutation, platform deployment approval,
    security acceptance, direct ART mutation, autonomous AI governance
    decisions, and chat-only evidence hiding
  - blocker triggers for unknown authority, stale snapshots, failed parity,
    missing owner boundaries, security deltas, and platform release gates
- `workspace-governance-control-fabric` now has a primary operator instruction
  surface at `docs/operations/operator-surface.md`.

### Operating Evidence

- #428 landed the workspace-governance contract and the control-fabric
  operator surface through PR-backed Review Packet evidence.
- The contract validation in `workspace-governance` enforces the required
  command, API, record, profile, blocker, denied-action, phase, and
  no-authority-mutation constraints.
- No central service, dashboard, model invocation path, or deployment state is
  approved by this slice.

## Review Areas

### Identity

- The fabric must distinguish at least four identities once runtime exists:
  - human operator
  - control-fabric workload or service identity
  - broker/OOS caller identity for ART workflow mutation
  - platform deployment or promotion authority
- The operator surface is acceptable because it denies direct mutation of
  workspace contracts, platform deployment state, security acceptance, and ART
  work state.
- Future service runtime must define authentication and authorization before
  `dev-integration` or governed-stage API use. The CLI-only local posture is
  lower risk but still needs attributable operator records for meaningful
  actions.

### Secrets

- This slice introduces no provider credential, platform secret, or service
  token placement.
- Future source snapshots, receipts, validation output, and ledger references
  can carry sensitive operational context by accident. Implementation must
  classify, suppress, redact, or reference sensitive artifacts instead of
  emitting raw secret-like material in compact output.
- If the fabric later stores artifacts outside local files, storage custody,
  retention, encryption, access control, and deletion posture require a fresh
  review before activation.

### Delivery

- The authority split is correct: workspace contracts stay in
  `workspace-governance`; deployment approval stays in `platform-engineering`;
  security acceptance stays in `security-architecture`; ART mutation stays in
  `operator-orchestration-service`.
- Readiness decisions are evidence, not approval. They may support a human or
  platform gate, but they must not replace that gate.
- The new workspace-governance metadata should treat
  `workspace-governance-control-fabric` as a security review subject because
  it will own validation planning, admission/readiness, receipts, ledger, CLI,
  API, worker, and runtime surfaces.

### Runtime

- Day-one CLI-first implementation is acceptable only while it preserves the
  source-snapshot to plan to run to receipt to ledger flow.
- A future API/service boundary must define:
  - caller authentication
  - authorization by operation and profile
  - audit retention
  - request and response size controls
  - failure posture for stale or unknown authority
  - clear separation between read-only receipts and mutating owner-system
    workflows
- `dev-integration` and governed-stage profiles remain blocked until platform
  adoption and security evidence are explicit.

### AI

- This slice does not activate governed AI behavior.
- Future AI integration must treat fabric output as governed context or
  evidence, not as direct action authority.
- If a model consumes source snapshots, validation output, receipts, or
  readiness decisions, the context must pass through an approved context
  admission path and still preserve human approval for governance decisions.
- Autonomous AI governance decisions remain denied.

## Decision

`approved-with-findings`

Approved because the operator surface explicitly separates authority,
implementation, review, and evidence boundaries before runtime code starts.
The design is conservative: it denies direct authority mutation, blocks unknown
or stale sources, and requires receipts and ledger events for operator claims.

Findings and residual risk:

1. Runtime implementation remains blocked until it preserves the identity split
   and emits attributable audit records for source snapshots, validation runs,
   readiness decisions, and escalations.
2. Evidence custody is the main residual risk. Receipts and ledger events must
   not become a new channel for leaking raw operational context, secrets, or
   oversized validation output.
3. The API/service posture is not approved yet. It requires a future delta
   review covering authn/authz, retention, network exposure, storage custody,
   and deployment profile before activation.
4. Readiness decisions must remain evidence-only. Any implementation that lets
   the fabric approve platform release, security acceptance, ART mutation, or
   workspace contract mutation is a security-significant regression.
5. AI integration remains deferred. Any model-consumption path for fabric
   context, receipts, or decisions requires governed context admission,
   approved model-access profile, output validation, audit, and human
   approval.

## Related Artifacts

- `workspace-governance/contracts/governance-control-fabric-operator-surface.yaml`
- `workspace-governance/contracts/schemas/governance-control-fabric-operator-surface.schema.json`
- `workspace-governance/docs/governance-control-fabric-operator-surface.md`
- `workspace-governance/docs/governance-engine-foundation.md`
- `workspace-governance-control-fabric/docs/operations/operator-surface.md`
- `workspace-governance-control-fabric/README.md`
- `workspace-governance-control-fabric/AGENTS.md`
- [`../security-delta-review-process.md`](../security-delta-review-process.md)
- [`../security-review-checklist.md`](../security-review-checklist.md)
