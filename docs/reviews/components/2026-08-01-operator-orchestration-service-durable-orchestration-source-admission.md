# Operator Orchestration Service Durable Orchestration Source Admission

## Summary

- date: 2026-08-01
- owner repo: `operator-orchestration-service`
- affected review subjects:
  - `repos.operator-orchestration-service`
  - `components.operator-orchestration-service`
- review trigger: `broker-runtime-and-caller-surface`
- ART initiative: `openproject://work_packages/698`
- source feature: `openproject://work_packages/721`
- implementation PR: `operator-orchestration-service` PR #117, merged as
  `7659047a2671135066c17e8b1ae64eb2a2be5bc7`
- runtime source revision:
  `e6a29e86bca1cf0eea53b92a8cbb62212960788c`
- decision: `approved-with-findings`

This review admits the merged OOS durable-orchestration source and its
fail-closed API and worker artifacts. It does not approve Temporal activation,
workflow execution, self-serve launch, shared runtime access, stage, or
production.

## Scope Delta

### Design Intent

OOS now owns a versioned durable-orchestration boundary for
`validation-readiness-run`. Temporal remains a replaceable scheduling and
history runtime behind OOS; it does not gain business authority, approval
authority, canonical-backend credentials, or direct Console access.

The accepted authority split remains:

- OOS authenticates callers, admits requests and controls, owns workflow
  policy, and projects aggregate receipts.
- Platform owns Temporal topology, persistence, runtime lifecycle, identity,
  network policy, observability, backup, restore, and activation manifests.
- WGCF owns the bounded validation-readiness activity result.
- Security owns activation acceptance.
- Governance Operations Console calls OOS only.

### Implemented Control

The merged source provides:

- strict versioned request, control, workflow-input, run-binding, projection,
  activation-evidence, registration, and generation-retirement contracts
- canonical request, control, and projection schemas projected recursively
  into OpenAPI, with CI rejecting top-level or nested drift
- authenticated caller mode as an activation prerequisite
- digest-pinned activation manifests and evidence records bound to the exact
  Temporal target, namespace, identity, source, and profile
- activation-generation-derived task queues, immediate pre-poll
  revalidation, periodic revocation checks, and fail-stop worker behavior
- deterministic generation-registration and seal Update identities, a
  512-registration capacity bound, and stable capacity-exhaustion semantics
- acknowledged authorization-bound registry sealing, exact workflow-id
  reconciliation, terminal projection verification, and Ed25519 retirement
  receipts over a published canonical byte vector
- separate API and workflow-worker images, with the worker profile retained at
  zero replicas and every activation switch disabled
- reference-oriented Temporal inputs and projections rather than raw context,
  secrets, command output, or full canonical business records

The implementation does not give Temporal direct OpenProject, Console,
Platform, Security, or WGCF authority.

### Source And Build Validation

Accepted source and build validation is limited to:

- 425 passing OOS tests
- deterministic workflow-bundle validation
- full-depth canonical OpenAPI synchronization and 56-route API parity
- exact-source API image
  `oos-api:698-e6a29e8` at
  `sha256:02e7408b02a3145eb1a56ec3c3a6a45f777885ce6c7c77db71646df5eb1d0db5`
- exact-source worker image
  `oos-orchestration-worker:698-e6a29e8` at
  `sha256:706bbfb7e81192a38ad7f5a7b5de73b804a1105a2b88d73ebfd507f17fe311d3`
- API health returning live while worker status reported `enabled: false`,
  `execution_authorized: false`, `activation_ready: false`, and
  `run_allowed: false`
- paired Platform protocol acceptance merged as
  `6082cda443c3b5c3a684b39278078ce4b5776624`
- paired WGCF source evidence at
  `c59f34b6893a763df82184fc54c6c6dc1982c38e`

### Operating Evidence

Operating evidence is absent. No live Temporal namespace, worker poll,
workflow execution, activity dispatch, durable history, database, network
path, credential delivery, restart, replay, backup, restore, or
incident-response proof is claimed. Source tests, local image builds, and local
health or fail-closed status checks cannot satisfy a runtime activation gate.

## Review Areas

### Identity

Source admission is acceptable because caller authentication is an activation
gate, Platform evidence binds the Temporal target and OOS identity, and worker
task queues are generation-specific. Separate service, database, OOS worker,
activity-owner, and human diagnostic identities still require operating proof
before activation.

### Secrets

The source contracts admit references and digests, not secret values or raw
context. Runtime secret custody, delivery, rotation, storage encryption,
backup custody, and diagnostic redaction remain Platform activation gates.

### Delivery

PR #117 is source admission only. Its merge, local images, Review Packet, or a
Temporal receipt cannot activate the profile or authorize stage or production.
Rollback remains a source revert while all runtime replicas and activation
switches stay disabled.

### Runtime

The implementation closes the source-level replay, stale-generation,
registration-history, retirement, authorization-expiry, and contract-drift
gaps found during exact-head review. Live namespace isolation, worker
identity, network policy, persistence, restart, replay, observability,
retention, backup, restore, and incident fencing are not yet operating
controls.

### AI

No model invocation, model authority, or AI-shaped mutation path is introduced.

## Findings

1. No live Temporal operating evidence exists. Platform and OOS must prove
   namespace, identity, network, persistence, restart, replay, observability,
   retention, backup, restore, and incident behavior before activation. This
   remains in the separate runtime-proof work under ART `#726` and its
   dependent Platform/Security gates.
2. `validation-readiness-run` is source-admitted but not runtime-admitted. A
   fresh Security activation review must verify the exact deployed OOS,
   Platform, WGCF, identity, network, secret, and evidence revisions before
   the profile can become active.
3. Stage and production remain outside this decision. They require governed
   promotion evidence after dev-integration operating proof succeeds.

These are explicit future activation gates, not accepted live defects.

## Decision

`approved-with-findings`

Approved:

- the merged OOS durable-orchestration source and canonical API contracts
- local API and fail-closed worker image construction
- retention of the worker at zero replicas with all activation controls off
- downstream indexing of the source-admission change record

Not approved:

- Temporal profile lifecycle `active`
- workflow or activity execution
- self-serve launch or shared diagnostic access
- direct Console-to-Temporal access
- stage or production deployment
- treating workflow history or receipts as approval authority

The main Security review authority retains activation and final landing
judgment. Runtime activation requires the separate operating-evidence review;
this source review cannot be replayed as that approval.

## Related Artifacts

- [Temporal durable orchestration build admission](2026-07-31-temporal-durable-orchestration-build-admission.md)
- [Temporal security view](../../architecture/components/temporal/README.md)
- [OOS security view](../../architecture/components/operator-orchestration-service/README.md)
- [Security delta review process](../security-delta-review-process.md)
- [OOS source-admission record](https://github.com/mfshaf7/operator-orchestration-service/blob/main/docs/records/change-records/2026-07-31-oos-durable-orchestration-source-admission.md)
