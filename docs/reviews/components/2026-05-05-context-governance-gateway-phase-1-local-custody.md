# Context Governance Gateway Phase 1 Local Custody Security Delta

## Summary

- date: 2026-05-05
- owner repo: `security-architecture`
- affected review subjects:
  - `repos.context-governance-gateway`
  - `components.context-governance-gateway`
- ART item: `openproject://work_packages/581`
- related implementation evidence:
  - `https://github.com/mfshaf7/context-governance-gateway/pull/1`
  - `openproject://work_packages/574`
  - `openproject://work_packages/575`
  - `openproject://work_packages/576`
  - `openproject://work_packages/577`
  - `openproject://work_packages/578`
  - `openproject://work_packages/579`
  - `openproject://work_packages/580`
- decision: `approved-with-findings`

This delta review evaluates the Phase 1 local-only security posture for
Context Governance Gateway. The reviewed slice captures raw operational
context locally, redacts and budgets a projected packet, emits an operator
receipt, and appends a local ledger event.

The approval is limited to local CLI/source use. It does not approve API
service mode, worker execution, shared artifact storage, database-backed
metadata, dashboard upload, broker adapters, model invocation, or cross-repo
runtime behavior.

## Scope Delta

### Design Intent

- `context-governance-gateway` implements context admission before operational
  context reaches AI agents, operator workflows, CI, or automation.
- Raw artifacts are preserved locally so operators retain forensic evidence.
- Model-safe packets receive redacted, sliced, and budgeted context only.
- Operator receipts explain captured, redacted, included, denied, stored, and
  policy-profile decision evidence.
- `dev-integration` admission is required before shared runtime surfaces exist.

### Implemented Control

The reviewed implementation in `context-governance-gateway` PR #1 provides:

- local `cgg init`, `run`, `pack`, `project`, and `inspect` commands
- local `.cgg/` output structure for raw artifacts, redacted artifacts,
  manifests, packets, receipts, and `ledger.jsonl`
- deterministic masking for secret-like environment values, JSON secret
  fields, bearer tokens, JWTs, GitHub tokens, AWS access keys, private keys,
  private IPs, and internal hostnames
- repeated-log collapse, failure-window extraction, and token budgeting
- profile behavior for `casual`, `developer`, and `enterprise`
- default denial of raw projection when sensitive indicators are found
- local docs, ADR, and threat model stating the service/runtime boundary

### Operating Evidence

Current evidence is local/source evidence only:

- PR #1 merged with passing validation workflow
- local unit tests cover init, redaction, command capture, packet generation,
  receipt generation, ledger append, repeated-log collapse, directory packing,
  and artifact projection
- CLI smoke commands generated packets and receipts locally
- no dev-integration profile exists or is required for this local-only slice

## Review Areas

### Secrets

Raw artifacts may contain secrets, internal hostnames, private IPs, command
output, repository contents, or CI/runtime evidence. The accepted Phase 1
posture is:

- raw artifacts remain local under `.cgg/artifacts/raw/`
- raw projection into model-safe packets is denied when findings exist
- packets include redacted excerpts and metadata, not raw sensitive output
- receipts record where the full artifact is stored and why raw projection was
  denied

Residual risk remains because deterministic matching is not complete DLP.
External scanner integrations and approved shared custody are not approved by
this review.

### Runtime

Phase 1 is local CLI/source behavior only. No service identity, network
listener, central worker, object store, database, dashboard, broker adapter, or
cross-repo runtime is approved.

Any API, worker, database-backed storage, dashboard, downstream adapter, broker
adapter, or shared runtime behavior requires a registered dev-integration
profile and a fresh security review.

### Delivery

The authority split remains acceptable:

- `workspace-governance` owns context admission standards and workspace
  contracts.
- `context-governance-gateway` owns implementation.
- `platform-engineering` owns deployment state and profile admission.
- `security-architecture` owns security acceptance.

The local CLI implementation is evidence-producing, not an approval authority.
It must not mutate ART, platform release state, security decisions, workspace
contracts, or governed AI profiles.

### AI

This slice does not approve model invocation. It approves generation of
model-safe packets for later consumption by operators or approved downstream
tools.

If packets are consumed by an AI workflow, that workflow still needs governed
model-access approval, output validation, auditability, and human approval for
security or delivery decisions.

## Decision

`approved-with-findings`

Approved because the Phase 1 implementation keeps raw artifacts local, denies
raw model projection by default when findings exist, emits receipts and ledger
events, and explicitly blocks service/runtime expansion until dev-integration
admission.

Findings and residual risk:

1. Deterministic redaction is not complete DLP. It reduces obvious leakage but
   does not replace Presidio, Gitleaks, TruffleHog, or custom recognizer
   integration.
2. Raw artifact custody is local-only. Shared custody needs approved storage,
   encryption, retention, deletion, access control, and audit posture.
3. Local file permissions and operator workstation hygiene are outside the
   current implementation control. Operators must treat `.cgg/artifacts/raw/`
   as sensitive local evidence.
4. Enterprise profile behavior suppresses raw excerpts when findings exist,
   but false negatives remain possible until scanner/policy integrations land.
5. API, worker, database, dashboard, broker adapter, and cross-repo runtime
   work remain blocked until dev-integration admission and fresh security
   review.

## Acceptance Gates Before Runtime Expansion

Before CGG can move beyond local CLI/source use:

- a dev-integration profile must be proposed and admitted
- runtime identity and caller attribution must be defined
- artifact storage custody must define encryption, retention, deletion, access,
  and audit
- scanner/policy integrations must be selected and bounded
- downstream packet consumers must preserve the authority split and avoid raw
  context projection
- security review must be refreshed for the new runtime boundary

## Related Artifacts

- `context-governance-gateway/README.md`
- `context-governance-gateway/AGENTS.md`
- `context-governance-gateway/docs/adr/0001-context-governance-gateway.md`
- `context-governance-gateway/docs/architecture/phase-1-local-pipeline.md`
- `context-governance-gateway/docs/operating-model/local-cli.md`
- `context-governance-gateway/docs/threat-model/phase-1-local-custody.md`
- `context-governance-gateway/contracts/schemas/model-safe-packet.schema.json`
- `context-governance-gateway/contracts/schemas/operator-receipt.schema.json`
- `context-governance-gateway/contracts/schemas/redaction-report.schema.json`
