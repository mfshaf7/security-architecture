# Temporal Durable Orchestration Build Admission

## Summary

- date: 2026-07-31
- owner repo: `security-architecture`
- affected review subjects:
  - `components.temporal`
  - `repos.platform-engineering`
  - `repos.workspace-governance`
- ART feature: `openproject://work_packages/742`
- reviewed ART children:
  - `openproject://work_packages/743`
  - `openproject://work_packages/744`
  - `openproject://work_packages/745`
  - `openproject://work_packages/746`
  - `openproject://work_packages/747`
  - `openproject://work_packages/748`
  - `openproject://work_packages/749`
- prerequisite contract work: `openproject://work_packages/707`
- decision: `approved-with-findings`

This review approves bounded source implementation for the proposed Temporal
`dev-integration` profile. The profile may advance from `proposed` to
`build-admitted` after the workspace registry records this review and the
Platform acceptance reference.

This decision does not approve profile activation, self-serve launch, shared
workflow execution, stage, production, direct Console access, or either initial
workflow definition as active.

## Scope Delta

### Design Intent

The workspace has selected Temporal as a replaceable durable runtime behind
OOS for workflows that must survive restarts, external waits, controlled
retries, reconciliation, cancellation, or execution across multiple owners.

The accepted authority split is:

- OOS owns aggregate workflow policy, definitions, requests, controls,
  projection, correlation, and final receipts.
- Temporal owns durable scheduling, replay, timers, persisted waits, and
  activity retry dispatch.
- Platform owns the runtime and persistence lifecycle.
- each activity owner retains bounded domain authority.
- Security owns acceptance.
- Governance Operations Console calls OOS and never Temporal.

### Implemented Control

The reviewed implementation is contract-only:

- workspace intake classification and durable-orchestration contract
- proposed workspace profile registry entry
- Platform component architecture, access, operations, and release contracts
- accepted Platform ADR
- structurally complete proposed profile
- fail-closed profile commands

No Temporal namespace, service, UI, database, persistent volume, credential,
network policy, worker, workflow execution, or stage or production artifact
exists.

### Operating Evidence

Operating evidence is intentionally absent. The only accepted observations are:

- profile status reports `proposed`
- implementation is not present
- self-serve launch is denied before dispatch

Runtime activation requires a second security judgment against implemented and
operating evidence.

## Threat Model

Protected assets include:

- canonical backend records and mutation authority
- operator approval records
- workflow history and search attributes
- service and activity-owner credentials
- CGG packets, receipts, and raw artifact custody
- runtime persistence, backups, and forensic evidence

Primary failure modes are:

- secrets or raw context becoming durable workflow history
- one worker consuming another owner's task queue
- retries duplicating canonical side effects
- a stale approval being replayed against changed intent
- a model output or CGG packet being treated as authority
- direct Console or operator access bypassing OOS
- cancellation or rollback claims hiding partial effects
- destructive reset erasing incident evidence
- diagnostic UI, logs, metrics, or search attributes leaking payload data

## Review Areas

### Identity

Build implementation must use separate identities for:

- Temporal service and PostgreSQL
- OOS client and workflow worker
- each activity-owner worker
- human diagnostic access

Namespace and task-queue authorization must prevent cross-owner consumption.
Activity workers keep their own bounded backend credentials; Temporal does not
receive a general canonical-backend credential. Direct Console credentials,
anonymous namespace access, public UI ingress, and shared long-lived worker
credentials are denied.

The local diagnostic UI may be exposed only through the approved operator-local
access path. A future shared environment requires stronger workload identity
and a fresh review.

### Secrets

Temporal history, memo, search attributes, visibility records, logs, and error
details must not contain:

- secrets, tokens, credentials, or recovery material
- raw operational context or raw CGG artifacts
- unbounded logs or command output
- full duplicated business records
- raw prompts or unconstrained model output

Allowed history is reference-oriented: source refs and versions, definition and
run ids, bounded decisions and signals, status codes, digests, and receipt or
artifact refs.

Before activation, Platform must prove namespace-scoped secret delivery,
storage encryption, backup and restore custody, retention, deletion, and a
low-sensitivity search-attribute allowlist. Payload encryption beyond storage
encryption is required before higher-sensitivity data or governed stage use is
considered.

### Delivery

Build admission authorizes owner-repo source work only:

- Platform runtime and profile implementation under #708-#712
- OOS adapter and definition work under #721
- bounded WGCF activity work under #713
- bounded CGG adapter work under #728
- Console projection work under #735
- end-to-end proof under #750

The profile remains non-self-serve. A source merge, ART completion note, or
Temporal workflow receipt cannot activate the profile or approve a release.
Platform activation, Security revalidation, and workspace lifecycle mutation
remain separate gates.

### Runtime

Approval records must bind operator, purpose, immutable definition version,
source ref and version, canonical intent digest, decision time, freshness or
expiry, and decision ref. Retry may reuse approval only while all bound
material remains unchanged and valid.

Reads may use bounded retry. Canonical writes require stable logical-effect
idempotency keys and receipt correlation. Ambiguous outcomes must enter blocked
reconciliation rather than blind retry. Cancellation stops future effects but
does not erase completed ones. Compensation is effect-specific and must not
claim generic rollback for irreversible operations.

Before activation, the implementation must prove:

- pinned runtime and worker versions
- PostgreSQL persistence, migration, backup, restore, suspend, and reset
- worker and runtime restart survival
- deterministic replay compatibility
- idempotency, timeout, retry, cancellation, and partial-effect projection
- namespace, task-queue, identity, and network isolation
- metrics, logs, traces, retention, and redaction
- read-only shared smoke behavior
- stop-start and incident evidence preservation

### AI

No model invocation is part of the proposed Temporal profile.

Future AI assistance may prepare only bounded structured input through an
approved model profile and governed invocation path. Model output remains
untrusted, receives deterministic validation, and cannot approve, activate,
promote, or mutate canonical state directly.

### Context And Evidence

Temporal may persist CGG packet ids, artifact digests, admission decisions,
suppression metadata, and receipt refs. Raw artifact bodies and debug override
are denied by default. CGG evidence does not become workflow approval.

Audit evidence must correlate request, run, definition, workflow, activity,
attempt, idempotency, caller, worker, operator, approval, CGG, source, event,
and receipt references. Logs and diagnostic views must avoid payload bodies.

Incident response must:

1. stop new workflow starts through OOS
2. preserve PostgreSQL and workflow evidence
3. suspend the profile or affected workers without destructive reset
4. classify the failure by runtime, definition, activity, identity,
   persistence, approval, or projection boundary
5. resume, retry, or reconcile only through admitted OOS controls

## Findings

1. Workflow-history classification, search-attribute allowlisting, retention,
   backup, and payload-protection evidence are not implemented. Owners:
   Platform and OOS. ART: #708, #710, #711, #712, #721.
2. Namespace, task-queue, identity, secret, UI-access, and network controls are
   not implemented. Owner: Platform. ART: #709 and #710.
3. Approval binding, idempotency, retry, cancellation, compensation, and
   partial-effect projection are contract intent only. Owners: OOS and activity
   owners. ART: #713 and #721.
4. CGG packet-only handoff is not implemented. Owners: CGG and OOS. ART: #728
   and #721.
5. Correlated audit, incident, backup, restore, restart, and replay evidence
   does not exist. Owners: Platform and OOS. ART: #710-#712 and #750.
6. The first definitions remain unadmitted. `validation-readiness-run` and
   `delivery.refinement.apply` must not be shown as active until their
   definition and runtime gates pass.

These are gated implementation findings, not accepted runtime defects. They
remain open through the referenced ART work and require refreshed security
review before activation.

## Decision

`approved-with-findings`

Approved now:

- record this review as the Temporal component baseline
- advance the profile to `build-admitted`
- implement the bounded local profile and owner-repo source controls
- keep all runtime commands and shared-runner launch fail closed until active

Not approved:

- profile lifecycle `active`
- self-serve runtime launch or diagnostic access
- execution of an admitted durable workflow
- direct Console-to-Temporal access
- raw CGG context or secret-bearing workflow payloads
- AI approval or mutation authority
- stage or production deployment

Activation requires Platform acceptance of the implemented runtime, complete
owner commands, read-only smoke, restart and replay proof, correlated receipts,
and a fresh Security review against operating evidence.

## Related Artifacts

- [Temporal security view](../../architecture/components/temporal/README.md)
- [Workspace durable orchestration contract](https://github.com/mfshaf7/workspace-governance/blob/main/contracts/durable-orchestration.yaml)
- [Workspace Temporal profile registry](https://github.com/mfshaf7/workspace-governance/blob/main/contracts/developer-integration-profiles.yaml)
- [Platform Temporal component](https://github.com/mfshaf7/platform-engineering/blob/main/docs/components/temporal/README.md)
- [Platform Temporal profile](https://github.com/mfshaf7/platform-engineering/blob/main/dev-integration/profiles/temporal/profile.yaml)
- [Platform ADR-017](https://github.com/mfshaf7/platform-engineering/blob/main/docs/decisions/adr/ADR-017-temporal-durable-workflow-runtime.md)
