# Context Governance Gateway Service Mode Admission Gates Security Delta

## Summary

- date: 2026-05-05
- owner repo: `security-architecture`
- affected review subjects:
  - `repos.context-governance-gateway`
  - `components.context-governance-gateway`
- ART items:
  - `openproject://work_packages/596`
  - `openproject://work_packages/597`
  - `openproject://work_packages/598`
- related upstream review:
  - [`2026-05-05-context-governance-gateway-phase-1-local-custody.md`](2026-05-05-context-governance-gateway-phase-1-local-custody.md)
- decision: `approved-with-findings`

This delta review establishes the security admission gates for
`context-governance-gateway` service-mode maturity. It approves the security
requirements and threat model that must govern later service implementation.
It does not approve API runtime activation, worker execution, shared artifact
storage, database-backed metadata, dashboard upload, broker adapters, scanner
execution, model invocation, or platform deployment.

The security decision is intentionally gate-first: CGG may continue toward
service mode only after identity, custody, retention, debug override,
tamper-evident ledger, and downstream projection controls are implemented in
the owning repos and revalidated through the matching platform gate.

## Scope Delta

### Design Intent

- CGG governs operational context before it reaches AI agents, operator
  workflows, CI, or automation.
- Service mode would move CGG from local-only artifact custody into a shared
  control-plane boundary with API, worker, metadata, artifact storage, and
  downstream packet-consumer surfaces.
- Raw operational context remains sensitive evidence. It must not become
  normal model context, dashboard payload, log output, or broker payload.
- Security gates must exist before implementation so later delivery work cannot
  normalize a partial runtime as an accepted enterprise design.

### Implemented Control

The reviewed slice is a security-governance artifact slice:

- service-mode threat model in this review
- reusable security requirements in
  [`../../architecture/components/context-governance-gateway/service-mode-security-requirements.md`](../../architecture/components/context-governance-gateway/service-mode-security-requirements.md)
- updated CGG component security view
- updated security review inventory

No CGG service process, shared database, object store, API listener, worker,
dashboard, broker adapter, scanner integration, or model path is implemented
or approved by this review.

### Operating Evidence

Operating evidence is intentionally pending because this review precedes
runtime implementation. Before service mode can be admitted, owner repos must
produce:

- CGG implementation evidence for the requirements in this review
- platform runtime profile and release-gate evidence
- storage custody, backup, restore, retention, and deletion evidence
- security validation proving raw context remains denied by default for model
  projection
- operator evidence showing debug override and retention deletion paths are
  attributable, time-bounded, and reviewable

## Threat Model

### Protected Assets

- raw operational artifacts, including terminal output, CI logs, repo content,
  environment-derived material, internal hostnames, private IP addresses, and
  incident evidence
- redacted artifacts and model-safe packets
- context manifests, receipts, digests, and ledger events
- policy/profile decisions and debug override records
- metadata store contents, artifact object references, and deletion records

### Trust Boundaries

- operator workstation or CI job to CGG capture boundary
- CGG API and worker runtime boundary
- artifact store and metadata store custody boundary
- packet projection boundary into operators, OOS, WGCF, CI, or model-facing
  tools
- platform deployment boundary owned by `platform-engineering`
- security acceptance boundary owned by `security-architecture`

### Threat Actors And Failure Modes

- accidental operator leakage of raw output into model-safe packets
- compromised or overprivileged caller projecting raw artifacts
- service worker or dashboard exposing raw context through logs, errors, or
  convenience views
- stale retention policy preserving sensitive artifacts longer than approved
- deletion request removing audit evidence without reviewable authorization
- debug override becoming permanent raw access
- tampering with receipts or ledger events after a sensitive projection
- downstream consumer treating CGG packets as approval authority
- scanner false negatives allowing secret-like material into projected context

### Required Mitigations

- fail closed on uncertain or secret-like material
- separate raw artifact custody from projected model-safe packets
- require caller identity, operator attribution, purpose, profile, artifact
  digest, and decision metadata for every projection
- keep debug override time-bounded, reason-bound, role-bound, and audited
- preserve append-only ledger semantics with hash chaining or equivalent
  tamper evidence
- make retention and deletion policy explicit, reviewable, and storage-backed
- prevent CGG from mutating ART, platform release state, security acceptance,
  workspace contracts, or governed model profiles

## Review Areas

### Identity

Service mode introduces a real caller boundary. Before runtime activation,
CGG must define:

- distinct service identity for API, worker, and any scheduled maintenance
  role
- caller identity for CLI, CI, OOS, WGCF, operator console, and future
  adapters
- operation-level authorization for capture, pack, project, inspect, retention
  deletion, debug override, and administrative policy changes
- operator attribution when a human approves projection, override, deletion,
  or exceptional access
- audit correlation across request, artifact, packet, receipt, and ledger
  event

Shared static caller secrets are not approved as the enterprise target. If a
temporary dev-integration secret is used later, it must be local, profile-bound,
rotatable, non-production, and explicitly superseded by the platform identity
plan.

### Secrets

Raw artifacts may contain secrets even after deterministic detection. The
service-mode custody rule is:

- preserve raw artifacts only in an approved custody store
- deny raw projection into model-safe packets by default
- store redacted artifacts separately from raw artifacts
- keep manifests and receipts reference-based instead of copying raw sensitive
  context
- never log raw artifact bodies, scanner excerpts, or unredacted environment
  values from API, worker, dashboard, or adapter paths
- require approved encryption, retention, deletion, access control, and backup
  posture before shared storage is admitted

Scanner integrations may improve detection, but they do not replace context
admission policy, receipts, or custody controls.

### Delivery

The authority split remains mandatory:

- `workspace-governance` owns context admission standards and contracts.
- `context-governance-gateway` owns implementation.
- `platform-engineering` owns deployment state, version pinning, runtime
  profiles, promotion, backup, and restore gates.
- `security-architecture` owns security acceptance.
- OOS and WGCF may consume CGG outputs only through reviewed adapters; they do
  not receive raw context by default.

CGG evidence is not approval authority. It must not directly mutate ART,
platform release state, security findings, workspace contracts, or governed AI
profiles.

### Runtime

Approved by this review:

- security requirements and threat model for future service-mode runtime
- fail-closed service-mode admission gate
- requirement that #587 and later service implementation work remain blocked
  until security and platform gates have evidence

Not approved by this review:

- API listener activation
- worker execution
- database-backed metadata
- shared object storage
- dashboard upload or browsing
- broker or WGCF adapters
- model gateway or LLM invocation
- stage or production deployment
- broad scanner execution in a shared runtime

When runtime implementation begins, basic pod and process hardening must be
defined by the platform gate, including non-root execution, dropped Linux
capabilities, no privilege escalation, explicit network exposure, and
readiness/health behavior that does not leak raw context.

### AI

CGG may produce packets that later feed AI-assisted workflows, but this review
does not approve model invocation. A downstream AI path remains governed only
when it uses an approved model profile, governed invocation path, structured
output contract, audit metadata, and human approval where required.

Model-safe packets must remain budgeted, redacted, purpose-bound, and
reference-based. Raw context must not be projected to models unless a future
security review explicitly approves a bounded exception with compensating
controls.

## Decision

`approved-with-findings`

Approved because the review establishes concrete security gates before CGG
service-mode implementation begins and keeps the runtime blocked until the
requirements are implemented and evidenced.

Findings and residual risk:

1. Service-mode runtime remains blocked. This review is not runtime admission.
2. Shared raw artifact custody is not approved until platform storage,
   encryption, backup, restore, retention, deletion, and access-control gates
   exist.
3. Caller identity and authorization are not implemented yet and must be
   proven before API or worker activation.
4. Debug override and retention deletion require explicit operator
   attribution, reason, expiry, and ledger evidence before they are safe.
5. Scanner false negatives remain possible, so packet projection must fail
   closed when findings or uncertainty exist.
6. Downstream AI or automation consumers remain separate approval surfaces and
   must not inherit authority from CGG packets.

## Acceptance Gates Before Service Mode Implementation

Before #587 or any equivalent service-mode implementation slice starts, the
delivery workflow must show one of these:

- this security gate and the platform gate are complete with matching evidence
- or an explicit accepted waiver records owner, scope, expiry, risk treatment,
  and rollback boundary

Before runtime activation, the owner repos must prove:

- identity and authorization contract
- artifact custody contract
- retention and deletion contract
- debug override contract
- tamper-evident ledger contract
- packet projection contract
- platform deployment and rollback contract
- security revalidation against the implemented runtime

## Related Artifacts

- [`../../architecture/components/context-governance-gateway/README.md`](../../architecture/components/context-governance-gateway/README.md)
- [`../../architecture/components/context-governance-gateway/service-mode-security-requirements.md`](../../architecture/components/context-governance-gateway/service-mode-security-requirements.md)
- [`2026-05-05-context-governance-gateway-phase-1-local-custody.md`](2026-05-05-context-governance-gateway-phase-1-local-custody.md)
- `context-governance-gateway/AGENTS.md`
- `context-governance-gateway/docs/threat-model/phase-1-local-custody.md`
- `workspace-governance/contracts/developer-integration-profiles.yaml`
- `workspace-governance/contracts/components.yaml`
