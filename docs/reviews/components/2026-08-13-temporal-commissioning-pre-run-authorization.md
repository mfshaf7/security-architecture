# Temporal Commissioning Pre-Run Authorization

## Summary

- date: 2026-08-13
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
- ART authorization: `openproject://work_packages/790`
- upstream evidence preparation: `openproject://work_packages/799`
- reviewed implementation: `openproject://work_packages/825`
- canonical claims digest:
  `sha256:373d0035a9a1f8f8aa8d3cea6987ac9ab4e188cc82830e0a90fecd7ee88d9fd5`
- authorization artifact:
  `records/controlled-proof-authorizations/delivery-698-790-temporal-commissioning-20260813-v2.json`
- decision: `approved-with-findings`

This review authorizes Security's side of one bounded, unconsumed Temporal
commissioning claims set. It does not issue the Platform permit, supply the
operator's separate approval, launch any runtime, activate the Temporal
profile, accept post-run evidence, or authorize reuse for another digest.
The machine approval binding uses the schema's binary `approved` decision for
this exact digest; this review retains `approved-with-findings` because permit,
execution, restoration, and post-run acceptance remain fail-closed gates.

## Scope Delta

### Design Intent

The build-admitted Temporal profile needs one controlled run to collect the
operating evidence required for a later lifecycle judgment. The reviewed path
keeps authority split: Security approves one immutable claims digest, the
operator separately approves the same digest, Platform issues and consumes one
permit, OOS owns the aggregate workflow, WGCF owns the bounded readiness
activity, and Platform owns runtime installation and exact-baseline cleanup.

### Implemented Control

The authorization binds:

- commissioning session
  `delivery-698-799-temporal-commissioning-20260813-v2`
- Platform revision `9085c7a76616979713a9120635233030a55f7dc2`
- OOS revision `f1f8a09561dd4667c188aea408695313a867501b`
- Workspace Governance revision
  `842943e949aff47e19835cc09ee24ed8c051723d`
- WGCF revision `6b8d65b7ba1df028e92c9d3f14eae14c481b5411`
- finalized implementation Review Packet
  `artifact://review-packets/delivery-698-work-item-825-v3`
- immutable baseline digest
  `sha256:324f8f2a2dae2dfc9f8ead2cba5910110a9dfafb513ef34c8cee75f3e8333b2f`
- one `validation-readiness-run` definition, namespace
  `governance-mfshaf7`, three runtime identities, and two owner-specific task
  queues
- exact Temporal, PostgreSQL, OOS API, OOS worker, and WGCF worker image
  digests
- eleven ordered positive and negative commissioning scenarios
- atomic single-use consumption before first mutation
- the fixed permitted-action list, ten fail-stop conditions, and
  exact-baseline cleanup-only authority
- issue time `2026-08-13T13:00:00Z` and expiry
  `2026-08-14T13:00:00Z`

Platform's validator accepted the claims and an independent Node implementation
reproduced the same RFC 8785-subset digest. OOS and WGCF image provenance is
bound to GitHub Actions release metadata for their reviewed source revisions.

### Operating Evidence

The baseline was captured at `2026-08-13T10:52:17.864Z` from clean,
revision-pinned owner worktrees. It records `not-installed` for the Temporal
runtime, OOS validation-readiness worker, and WGCF readiness activity worker.

No permit has been issued, no approval has been consumed, no namespace,
database, worker, workflow, or activity has been launched, and no runtime
mutation is accepted as evidence by this review.

## Review Areas

### Identity

The claims use distinct OOS API, OOS workflow-worker, and WGCF activity-worker
identities and separate owner queues. The controlled run must prove denial of
wrong identity or queue use. This authorization does not convert identity names
in a claim into operating proof.

### Secrets

The permitted proof remains reference- and digest-oriented. Secret values, raw
context, unbounded logs, command output, and duplicated business records remain
denied in Temporal history and promoted evidence. Runtime credential custody
and diagnostic redaction must be proven during the bounded run and reviewed
afterward.

### Delivery

The Security artifact becomes usable only after merge to `main`, because the
Platform issuer requires the exact artifact bytes at a clean Security revision
contained in `refs/remotes/origin/main`. A local commit or open branch is not
authorization provenance. Operator approval and permit issuance remain later,
separate gates.

### Runtime

The approved scope is one local `component-commissioning-proof`. Any expiry,
source or image drift, target mismatch, identity denial failure, missing
baseline, unexpected side effect, evidence failure, or restore failure stops
new proof actions. Once a run has started, only the permit-bound cleanup path
may remove scoped runtime, restore the exact baseline, or record a governed
exception.

## Findings

1. Runtime identity, secret, queue, network, persistence, replay, backup,
   restore, and payload-boundary evidence does not exist yet. That is the
   bounded purpose of ART #751, not evidence supplied by this authorization.
2. Explicit operator approval of the same claims digest is still absent.
   Platform must not issue a permit until that independent artifact exists.
3. The authorization expires at `2026-08-14T13:00:00Z`. If the permit cannot
   be issued and the proof completed within that window, the run must not start;
   a new baseline, claims set, and Security decision are required.
4. ART #791 must review the completed operating evidence and exact-baseline
   restoration before any profile lifecycle change or broader reuse.

These are fail-closed execution gates, not accepted exceptions.

## Decision

`approved-with-findings`

Approved:

- the exact canonical claims digest named in this review
- the exact source, artifact, image, identity, queue, namespace, scenario,
  action, baseline, restore, and validity bindings contained in that claims set
- use of the source-controlled approval artifact as Security's independent
  input to later Platform permit issuance
- one permit-bound local commissioning proof after separate operator approval

Not approved:

- another claims digest, source revision, image, namespace, identity, queue,
  definition, scenario set, action set, baseline, or validity window
- permit issuance without the separate operator approval
- direct runtime launch outside the reviewed Platform issuer and executor
- profile activation, self-serve launch, stage, production, or general workflow
  admission
- treating this pre-run decision as post-run Security acceptance

## Related Artifacts

- [Temporal controlled commissioning proof contract](2026-08-01-temporal-controlled-commissioning-proof-contract.md)
- [Temporal approval provenance source review](2026-08-13-temporal-approval-provenance-source-review.md)
- [Temporal durable orchestration build admission](2026-07-31-temporal-durable-orchestration-build-admission.md)
- [Temporal security view](../../architecture/components/temporal/README.md)
- [Security delta review process](../security-delta-review-process.md)
