# Temporal Security View

## Purpose

Temporal is the proposed platform-owned durable workflow runtime behind
`operator-orchestration-service` (OOS). It provides replay, timers, persisted
waits, and activity dispatch. It does not own business policy, operator
approval, domain decisions, or completion truth.

The current security decision permits bounded source implementation in
`dev-integration`. It does not approve an active runtime, self-serve launch,
stage, production, or direct Console access.

The controlled commissioning contract is also design-approved with findings.
That review permits the fail-closed contract and operator surface to land, but
it does not issue a run permit, authorize an executor, or approve runtime
activation. A fresh pre-run Security authorization and a separate post-run
review remain mandatory.

## Authority Boundary

- `workspace-governance` owns orchestration authority and admission contracts.
- OOS owns versioned definitions, request acceptance, controls, aggregate
  projection, correlation, and final receipts.
- `platform-engineering` owns Temporal topology, persistence, runtime
  lifecycle, access, observability, backup, restore, and promotion.
- activity owners keep their bounded business authority and credentials.
- `security-architecture` owns security acceptance.
- Governance Operations Console calls OOS only.

Temporal history is execution evidence. It is never approval authority or a
replacement source of truth.

## Data Boundary

Allowed workflow-history fields are limited to:

- definition id and immutable version
- request, run, correlation, and causation ids
- source record references and source versions
- bounded decisions, status codes, and control signals
- artifact, packet, event, log, and receipt references or digests
- low-sensitivity allowlisted search attributes

Prohibited fields include:

- secret values, credentials, tokens, or recovery material
- raw operational context or raw CGG artifacts
- unbounded logs, stack traces, attachments, or command output
- full duplicated business records
- raw prompts or unconstrained model output
- personal or confidential data that has not received explicit classification

Before activation, Platform and OOS must define history retention, visibility
retention, backup retention, deletion behavior, and the exact search-attribute
allowlist. Payload encryption beyond storage encryption is required before
higher-sensitivity data can be admitted or any governed stage runtime is
considered.

## Identity And Network Boundary

The implementation must separate:

- Temporal service and database identities
- OOS client and workflow-worker identity
- each activity-owner worker identity
- human diagnostic access

One worker must not consume another owner's task queue. Runtime credentials
must not grant direct canonical-backend authority unless that credential belongs
to the bounded activity owner. Shared long-lived worker credentials, anonymous
namespace access, public Temporal UI ingress, and direct Console credentials are
denied.

The first local profile must remain operator-scoped, namespace-scoped, and
reachable only through the approved local diagnostic path.

## Approval And Replay Boundary

An approval used by a durable workflow must bind:

- operator identity
- approved purpose and action
- immutable definition id and version
- source record and source version
- canonical intent digest
- decision time and freshness or expiry
- approval or decision record reference

Retry may reuse an approval only when the approved intent is byte-for-byte or
canonically equivalent, the definition and source versions are unchanged, and
the approval remains valid. A material signal or payload change requires a new
approval. A Temporal event or prior successful activity does not grant future
authority.

## Retry And Effect Boundary

- reads may use bounded retry with timeout and backoff
- writes require a stable logical-effect idempotency key
- activity receipts must correlate the external operation and workflow attempt
- an ambiguous write outcome enters blocked reconciliation instead of blind
  retry
- cancellation stops future effects but does not claim to undo completed ones
- compensation must be defined per effect; generic rollback claims are denied
- effect posture must remain visible as none, possible, partial, or verified

## CGG And AI Boundary

Temporal may persist CGG packet ids, artifact digests, admission outcomes,
suppression metadata, and receipt references. It must not persist raw artifact
bodies or normalize debug override as a workflow feature.

AI output may prepare bounded structured input only through an approved model
profile and governed invocation path. Model output cannot approve, activate,
promote, or directly mutate canonical state.

## Audit And Incident Boundary

Audit evidence must correlate:

- request, run, definition, workflow, and activity ids
- activity attempt and idempotency key
- caller, worker, and operator identities
- approval, CGG packet, source, event, and receipt references
- runtime and worker source or artifact versions
- outcome, effect posture, and event time

Logs and diagnostic UI must not expose payload bodies by default.

Incident response must stop new starts through OOS, preserve PostgreSQL and
workflow evidence, suspend the profile when necessary, and avoid destructive
reset. Backup and restore proof, replay compatibility, and evidence custody are
activation gates.

## Admission Posture

Build-admitted source implementation may include:

- version-pinned local runtime manifests
- owner commands that remain non-self-serve until activation
- identity, network, persistence, observability, and access controls
- OOS adapter and worker implementation
- tests for replay, idempotency, retry, cancellation, and evidence correlation

Still denied:

- profile lifecycle `active`
- self-serve `up`, `access`, or shared-runner smoke
- admitted business workflow execution
- stage or production deployment
- direct Console-to-Temporal access

Activation requires fresh review against implemented and operating evidence.

## Review

- [2026-07-31 Temporal durable orchestration build admission](../../../reviews/components/2026-07-31-temporal-durable-orchestration-build-admission.md)
- [2026-08-01 Temporal controlled commissioning proof contract](../../../reviews/components/2026-08-01-temporal-controlled-commissioning-proof-contract.md)
