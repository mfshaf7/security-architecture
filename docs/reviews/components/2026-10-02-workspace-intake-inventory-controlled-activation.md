# Workspace Intake And Active Inventory Controlled-Activation Security Delta

## Summary

- date: 2026-10-02
- owner repo: `security-architecture`
- affected review subjects:
  - `repos.workspace-governance`
  - `repos.workspace-governance-control-fabric`
  - `repos.operator-orchestration-service`
  - `repos.governance-operations-console`
- delivery initiative: `openproject://work_packages/1203`
- parent feature: `openproject://work_packages/1205`
- security evidence item: `openproject://work_packages/1216`
- current architecture packet:
  `wgcf://artifacts/delivery-art/sha256/e31fd8cc44410fe88f1ee58f68944fe7a460c637e1d9396dc66290387a4af1fe`
- implemented-against architecture predecessor:
  `wgcf://artifacts/delivery-art/sha256/34022576c3cbcff6e3bf09d2ac0f5689e1b2255e82cc02a1233970b7fdc03bbe`
- decision: `approved-with-findings`

This review approves the exact merged Workspace Governance, WGCF, OOS, and
Console revisions below for controlled, single-operator, loopback
`dev-integration` activation by Platform work item `#1217`. It emits
`gate:intake-inventory-controlled-activation` for those exact revisions.

This is source acceptance, not operating proof. Platform must still prove the
configured composition, credential projection, restart, denial, rollback,
revocation, and teardown boundaries in `#1217`. OOS must then prove the
composed positive and negative path in `#1210` before the Feature may claim
routine operating readiness.

### Exact Source And Review-Packet Binding

| Owner | Reviewed source | Landing evidence | Scope |
| --- | --- | --- | --- |
| Workspace Governance | [`e3864940dd6961426de93fa5cdb2215a86a5aca1`](https://github.com/mfshaf7/workspace-governance/commit/e3864940dd6961426de93fa5cdb2215a86a5aca1) | [PR #215](https://github.com/mfshaf7/workspace-governance/pull/215), [PR #217](https://github.com/mfshaf7/workspace-governance/pull/217), Review Packet `sha256:a89d3bdab7930f71e5b376db51f27bce708d5db18569fbac18d626aa7766866a` | Canonical activation contract, validation, and current owner-evidence closure |
| Workspace Governance Control Fabric | [`0d0b686ea78397d91f64b498d78a4aa6651e1c05`](https://github.com/mfshaf7/workspace-governance-control-fabric/commit/0d0b686ea78397d91f64b498d78a4aa6651e1c05) | [PR #93](https://github.com/mfshaf7/workspace-governance-control-fabric/pull/93), Review Packet `sha256:6a81fb1a51ebd17b3f247483e540c144840d6a36ac51f990ab47a3a2a089e2e1` | Exact-contract readiness, failure mapping, and custody receipts |
| Operator Orchestration Service | [`ce061b456c44f52d327908729db3b1e934f26acf`](https://github.com/mfshaf7/operator-orchestration-service/commit/ce061b456c44f52d327908729db3b1e934f26acf) | [PR #257](https://github.com/mfshaf7/operator-orchestration-service/pull/257), Review Packet `sha256:aa1eab4aac6980eb4d2c34f4f30d69803acdeea5e87f403cc7692aa31c0ca5b1` | Durable Intake and Inventory orchestration bound to the reviewed authority chain |
| Governance Operations Console | [`d17912691a6dd99335c327637eda98c4105d98eb`](https://github.com/mfshaf7/governance-operations-console/commit/d17912691a6dd99335c327637eda98c4105d98eb) | [PR #48](https://github.com/mfshaf7/governance-operations-console/pull/48), Review Packet `sha256:a6627a715587533a0c4c07855835999be503044f22afed0f3eeeeca39aa16036` | Server-only operator adapter, state projection, denied paths, and activation sequencing |

The current architecture packet is the Security and Platform review snapshot.
Its predecessor is the packet OOS implemented against. The current packet
records that predecessor in `custody.supersedes`, keeps the same artifact id,
landing topology, authority sequence, human gates, and rollback model, and
states that the supersession refreshes source revisions without changing the
architecture. This two-packet lineage is accepted to avoid a self-referential
requirement for merged source to embed a packet created after that source.
Platform must verify both exact digests and this supersession relationship; it
must not treat an arbitrary stale packet as compatible.

## Scope Delta

### Design Intent

- Keep Workspace Governance as the only canonical classification and active
  inventory source authority.
- Keep WGCF non-mutating: it evaluates exact authority and issues immutable,
  caller-bound readiness and custody evidence.
- Keep OOS as the durable command, idempotency, retry, recovery, source-review,
  merged-readback, and terminal-receipt authority.
- Keep the Console as a server-side operator projection and submission surface;
  it must not infer success or become a competing source of record.
- Require exact-head human review and merge before canonical success.
- Separate source acceptance, Security acceptance, Platform activation, and
  composed operating proof.

### Implemented Control

Workspace Governance defines one ordered operating contract for Intake
classification, active-inventory promotion, and inventory lifecycle. The
contract denies direct-main mutation, automatic merge, source-complete claims
of operating readiness, premature runtime activation, and broad cleanup.

WGCF consumes exact canonical contract and schema digests. Its readiness
surfaces reject stale authority, malformed input, replay conflict, inactive
posture, and premature activation. Its result is evidence; it cannot mutate
the canonical register or grant runtime authority.

OOS binds requests to authenticated application callers, deterministic request
and idempotency identities, exact authority revisions, WGCF receipts, bounded
source changes, review branches, exact-head checks, human merge, canonical
readback, and terminal receipts. Existing Intake conformance evidence from ART
`#1069` proves that browser-altered source, target, requested-record, and
evidence fields are rejected and that interrupted and replayed requests remain
recoverable without false success. The dedicated Workspace Governance identity
evidence from ART `#1082` proves repository scope, minimum permissions,
credential isolation, denied merge authority, revocation, and teardown.

The Console keeps OOS endpoints and caller credentials server-side. Canonical
Workspace Intake and Workspace Registry mutations pass through the existing
private Platform session boundary. Missing configuration, invalid session
truth, malformed owner response, conflict, dependency failure, or source
failure remains unavailable and never falls back to fixture mutation. The
Console projects OOS state and next action; it does not own workflow success.

### Operating Evidence

All four exact revisions have finalized Review Packets and merged readback.
The owner evidence covers contract and schema validation, stale and premature
activation denial, WGCF readiness tests, OOS workflow and recovery tests,
Console architecture guards and semantic tests, TypeScript validation,
production build, public-source validation, and source-diff validation.

The earlier completed Intake proof adds 29 source-authenticity cases and seven
real-Git/process-recovery scenarios covering authenticated candidates,
browser alteration, review-only mutation, changed-head denial, human merge,
canonical readback, interruption, cancellation, retry, and replay. The earlier
identity proof covers exact App, installation, repository, permissions, token,
runtime delivery, provider mismatch, revocation, and teardown.

This remains source and prior bounded operating evidence. It does not prove
the new `#1203` composition is configured at the approved revisions. That
evidence belongs to `#1217` and `#1210` and cannot be replaced by this review.

## Review Areas

### Identity And Authorization

No new human identity is approved. The Console inherits the approved
single-operator, loopback Platform session boundary. The local operating-system
account remains the trust root. Shared, remote, or multi-user operation remains
outside this decision.

The Console caller identity, WGCF caller identity, and dedicated Workspace
Governance GitHub App remain distinct. A valid Console session does not grant
owner mutation by itself; OOS authorization, expected-state checks, WGCF
readiness, provider controls, exact-head human review, merge, and readback all
remain mandatory. Machine identities may not approve or merge their own work.

### Secrets And Custody

Platform retains custody of caller secrets and the GitHub App private key.
OOS may receive only the bounded runtime credentials required for its exact
workflow. The Console receives only its server-side OOS credential and private
session projection. WGCF receives its own caller binding.

Credential values, private projection contents, raw owner payloads, and private
filesystem paths must remain absent from browser output, source, ART text,
Review Packets, receipts, and logs. Receipts expose bounded identities,
digests, references, outcomes, and timestamps only.

### Replay, Failure, And Evidence Integrity

Caller, operator, request, idempotency, authority revision, readiness receipt,
source head, review, merge, readback, and terminal result must remain bound.
Conflicting identity reuse, stale authority, changed review head, malformed or
partial evidence, replay conflict, interrupted work, dependency failure, and
readback mismatch must remain visibly non-successful.

The current architecture packet and its exact predecessor relationship are
part of that binding. A different current packet, predecessor, source revision,
or landing topology requires another Security delta review.

### Delivery, Runtime, Rollback, And Cleanup

Platform may activate only the exact source revisions above and only after this
decision. `#1217` must prove exact revision selection, private credential
projection, service health, dependency denial, restart, rollback, revocation,
and teardown. `#1210` must prove the composed positive, stale, unauthorized,
replayed, interrupted, owner-unavailable, rollback, and cleanup paths.

Rollback must be owner-bounded: disable new requests, revoke runtime
credentials, remove the Console/OOS composition, and revert only the affected
Landing Unit when source rollback is required. Canonical Git history, Review
Packets, readiness and custody receipts, denied and failed evidence, Security
decisions, and runtime teardown evidence must be preserved.

### AI

This delta adds no model call, prompt boundary, model-selected action, tool
authority, or AI approval path. AI suggestions remain non-authoritative and
cannot supply identity, accept their own recommendation, select credentials,
authorize source mutation, merge a review, or establish completion.

## Findings And Activation Conditions

1. **The local operating-system account remains the human trust root.** This is
   accepted only for controlled, single-operator, loopback `dev-integration`.
   Federated identity, MFA, browser-session binding, remote revocation, shared
   access, stage, and production require separate architecture and review.
2. **The packet lineage must be verified, not guessed.** Platform must bind the
   current packet digest, its recorded predecessor, and the exact approved
   owner revisions. Any different or incompatible packet fails closed.
3. **Source evidence is not current composition evidence.** `#1217` must prove
   the exact configured runtime and secret boundary; `#1210` must prove the
   complete composed positive and negative workflow before routine readiness.
4. **Configured live mode may not fall back to fixtures.** Missing, stale,
   malformed, unauthorized, partial, conflicting, or unavailable owner truth
   remains unavailable or blocked.
5. **Human review remains mandatory.** The Workspace Governance App and other
   machine identities cannot merge, approve, bypass protected `main`, broaden
   repository scope, or replace canonical merged readback.

These are activation limits and accepted residual risks for the bounded local
lane. Failure of any condition blocks `#1217` or returns the result to its owner;
it does not justify widening identity, bypassing evidence, or claiming partial
success.

## Decision

`approved-with-findings`

Approved:

- the exact source revisions and finalized Review Packets bound above;
- the current architecture packet and its exact compatible predecessor lineage;
- the ordered Workspace Governance, WGCF, OOS, Console, Security, Platform,
  and operating-proof authority chain;
- distinct machine identities, server-only credential custody, replay and
  stale-state denial, exact-head review, human merge, and canonical readback;
- controlled, single-operator, loopback `dev-integration` activation by `#1217`;
  and
- subsequent composed operating proof by `#1210`.

Not approved:

- routine operating readiness based on this source review alone;
- any source revision or architecture lineage not bound above;
- shared, remote, multi-user, stage, production, ingress, or public exposure;
- browser, fixture, UI state, or AI output as authorization or source truth;
- shared, ambient, personal, long-lived, or browser-held credentials;
- machine approval or merge, direct-main writes, protected-branch bypass, or
  success before canonical merged readback;
- fixture fallback after live configuration is selected; or
- deletion of canonical history or evidence during rollback and cleanup.

## Related Artifacts

- [Workspace Intake authority-boundary review](2026-09-06-workspace-intake-authority-boundary.md)
- [Governance Console identity activation review](2026-09-27-governance-operations-console-identity-activation.md)
- [Governance Console runtime operability review](2026-09-27-governance-operations-console-runtime-operability.md)
- [Identity and access architecture](../../architecture/domains/identity-and-access.md)
- [Secrets and recovery architecture](../../architecture/domains/secrets-and-recovery.md)
- [GitOps and machine trust architecture](../../architecture/domains/gitops-and-machine-trust.md)
- [AI and agentic architecture](../../architecture/domains/ai-and-agentic.md)
- [Security delta review process](../security-delta-review-process.md)
- [Security review checklist](../security-review-checklist.md)
