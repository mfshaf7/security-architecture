# Temporal Post-Correction Commissioning Authorization

## Summary

- date: 2026-08-14
- owner repo: `security-architecture`
- affected review subjects:
  - `components.temporal`
  - `components.operator-orchestration-service`
  - `components.workspace-governance-control-fabric`
  - `repos.platform-engineering`
  - `repos.operator-orchestration-service`
  - `repos.workspace-governance`
  - `repos.workspace-governance-control-fabric`
- review triggers:
  - `temporal-controlled-runtime-proof-authorization`
  - `temporal-component-commissioning-runtime-drill`
  - `temporal-baseline-attestation-and-exact-restore`
  - `temporal-bounded-worker-and-payload-boundary`
- ART authorization: `openproject://work_packages/836`
- blocked execution: `openproject://work_packages/751`
- post-correction implementation evidence:
  `artifact://review-packets/delivery-698-work-items-832-833-temporal-commissioning-corrections`
- post-correction implementation packet digest:
  `sha256:4a83056c5224a771691c50199c1ceb5a034eb034c7fcd1e2b0545ffc313da7d8`
- canonical claims digest:
  `sha256:3989f5157e02c9f1a091499cc57bb60972f594d5cfa9f196475cf2366aa1d46b`
- authorization artifact:
  `records/controlled-proof-authorizations/delivery-698-836-temporal-commissioning-20260814-v1.json`
- decision: `approved-with-findings`

This review authorizes Security's side of one new, unconsumed Temporal
commissioning claims set after the final Platform corrections and durable
evidence-custody work landed. It does not supply operator approval, issue or
consume a Platform permit, launch runtime, activate Temporal, accept post-run
evidence, or authorize reuse of either earlier terminal session.

## Scope Delta

### Design Intent

The commissioning proof retains split authority. Security approves one
immutable claims digest, the operator separately approves that same digest,
Platform issues and atomically consumes one permit, OOS owns the aggregate
workflow, WGCF owns the bounded readiness activity, and Platform owns runtime
installation and exact-baseline cleanup.

The two earlier commissioning sessions are terminal evidence. Their approvals,
permits, and cleanup records are not reusable authority. This decision binds a
new session, baseline, claims digest, validity window, final corrected Platform
revision, and durable correction Review Packet.

### Implemented Control

The reviewed claims bind:

- commissioning session
  `delivery-698-751-temporal-commissioning-20260814-v1`
- final corrected Platform revision
  `20143d4624ffa3f41b81400916f8c16f018c0499`
- OOS revision `f1f8a09561dd4667c188aea408695313a867501b`
- Workspace Governance revision
  `842943e949aff47e19835cc09ee24ed8c051723d`
- WGCF revision `6b8d65b7ba1df028e92c9d3f14eae14c481b5411`
- the post-correction implementation Review Packet and digest named in the
  summary
- immutable baseline digest
  `sha256:6533f5fca315ae06c781030516ffd72bfe085dc4b5be4a7b1be7257c921cc78a`
- one `validation-readiness-run` definition, one operator-scoped namespace,
  three runtime identities, and two owner-specific task queues
- exact Temporal, PostgreSQL, OOS API, OOS worker, and WGCF worker image
  digests
- eleven ordered positive and negative commissioning scenarios
- atomic single-use consumption before first mutation
- the fixed permitted-action list, fail-stop conditions, bounded diagnostic
  evidence, and exact-baseline cleanup-only authority
- issue time `2026-08-13T23:26:05Z` and expiry
  `2026-08-14T10:26:05Z`

The final corrected Platform source resolves the durable correction Review
Packet through its content-addressed custody path and binds that reviewed
source truth to permit issuance. Direct or symlink-resolved control inputs
under the canonical run deletion scope remain rejected before consumption.
Read-only status does not create absent operator state. Runtime command
failures retain only bounded executable, return-code, digest, and byte-count
evidence. Cleanup retries remain limited to the consumed session's immutable
approvals, receipt, execution claim, lease, executor snapshot, and captured
restore scope.

Platform validation and an independent Node implementation reproduced the same
RFC 8785-subset claims digest.

### Operating Evidence

The baseline was captured at `2026-08-13T22:21:24.217Z` from clean,
revision-pinned worktrees and found all three controlled surfaces absent. No
permit has been issued or consumed for this session, and no namespace,
database, worker, workflow, or activity has been launched.

## Review Areas

### Identity

The claims preserve distinct OOS API, OOS workflow-worker, and WGCF
activity-worker identities and separate owner queues. Wrong identity and queue
use remain negative proof scenarios; this authorization does not treat claim
declarations as operating evidence.

### Secrets

The claims remain reference- and digest-oriented. Secret values, raw context,
unbounded logs, command output, and duplicated business records remain denied
in Temporal history and promoted evidence. The bounded diagnostic path stores
hashes and byte counts rather than command output.

### Delivery

The machine authorization is usable only after its exact bytes are merged to
`security-architecture` `main`. Platform must independently resolve the merged
Security revision, normalized source path, artifact reference, and digest when
issuing a permit. The claims intentionally exclude the Security artifact's
containing commit to avoid a self-reference cycle.

### Runtime

The approved scope is one local `component-commissioning-proof`. Any expiry,
source or image drift, target mismatch, identity denial failure, missing
baseline, unexpected side effect, evidence failure, or restore failure stops
new proof actions. Once execution starts, only the permit-bound terminal
cleanup path may remove scoped runtime, restore the exact baseline, or record a
governed exception.

## Findings

1. Runtime identity, secret, queue, network, persistence, replay, backup,
   restore, and payload-boundary evidence does not yet exist for this session.
   Producing it is the bounded purpose of ART #751.
2. Explicit operator approval of the same canonical claims digest is absent.
   Platform must not issue a permit until that separate approval exists.
3. This authorization is valid only for the stated session and window. If the
   proof cannot start and finish within that window, a new baseline, claims
   set, and Security decision are required.
4. ART #791 must review the completed evidence and exact-baseline restoration
   before profile lifecycle change or broader reuse.

These findings are fail-closed gates, not accepted exceptions.

## Decision

`approved-with-findings`

Approved:

- the exact canonical claims digest named in this review
- the exact source, artifact, image, identity, queue, namespace, scenario,
  action, baseline, restore, and validity bindings in that claims set
- use of the merged source-controlled approval as Security's independent input
  to later Platform permit issuance
- one permit-bound local commissioning proof after separate operator approval

Not approved:

- either earlier terminal commissioning session or any other claims digest,
  source revision, image, namespace, identity, queue, definition, scenario set,
  action set, baseline, or validity window
- permit issuance without separate operator approval
- direct runtime launch outside the reviewed Platform issuer and executor
- profile activation, self-serve launch, stage, production, or general workflow
  admission
- treating this pre-run decision as post-run Security acceptance

## Related Artifacts

- [Previous commissioning reauthorization](2026-08-14-temporal-commissioning-reauthorization.md)
- [Temporal controlled commissioning proof contract](2026-08-01-temporal-controlled-commissioning-proof-contract.md)
- [Temporal approval provenance source review](2026-08-13-temporal-approval-provenance-source-review.md)
- [Temporal durable orchestration build admission](2026-07-31-temporal-durable-orchestration-build-admission.md)
- [Temporal security view](../../architecture/components/temporal/README.md)
- [Security delta review process](../security-delta-review-process.md)
