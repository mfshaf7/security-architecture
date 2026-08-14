# Temporal Valid-Chronology Commissioning Authorization

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
- ART authorization: `openproject://work_packages/839`
- blocked execution: `openproject://work_packages/751`
- implementation evidence:
  `artifact://review-packets/delivery-698-work-item-837`
- canonical claims digest:
  `sha256:84ddc2920decb3191f628d808b434a584d81f3cb38b1cfd5b92fc63b0c53b322`
- authorization artifact:
  `records/controlled-proof-authorizations/delivery-698-839-temporal-commissioning-20260814-v3.json`
- decision: `approved-with-findings`

This review replaces the unusable v2 pre-run authorization with one fresh,
unconsumed Temporal commissioning claims set whose approval chronology matches
the Platform permit contract. It does not issue or consume the permit, launch
runtime, activate Temporal, accept post-run evidence, or authorize any other
session.

## Scope Delta

### Design Intent

The commissioning proof retains split authority. Security and the operator
separately approve one immutable claims digest before the claims-declared permit
issue time. Platform then issues and atomically consumes one permit for the
single outer commissioning session. OOS owns the aggregate workflow, WGCF owns
the bounded readiness activity, and Platform owns runtime installation and
exact-baseline cleanup.

### Implemented Control

The reviewed v3 claims bind:

- session `delivery-698-751-temporal-commissioning-20260814-v3`
- Platform revision `5186d1be601f68ff7324994b9866a513a99f7a98`
- OOS revision `f1f8a09561dd4667c188aea408695313a867501b`
- Workspace Governance revision
  `842943e949aff47e19835cc09ee24ed8c051723d`
- WGCF revision `6b8d65b7ba1df028e92c9d3f14eae14c481b5411`
- finalized readiness-fix Review Packet
  `artifact://review-packets/delivery-698-work-item-837`
- immutable baseline digest
  `sha256:962edcf0a64b90efd11243ac016c47804eab68b788b728990c4a7aebc6fd9d06`
- the fixed image, identity, queue, namespace, scenario, action, bounded
  diagnostic, and exact-baseline restoration set from the reviewed executor
- issue time `2026-08-14T02:45:00Z` and expiry
  `2026-08-14T11:45:00Z`

The baseline was captured at `2026-08-14T02:24:28.653Z`. Explicit operator
approval was recorded at `2026-08-14T02:26:55Z`, and this Security decision was
recorded at `2026-08-14T02:28:19Z`. Both therefore follow the immutable baseline
and precede the declared permit issue time, satisfying the fail-closed
chronology required by the issuer.

### Operating Evidence

The prior v2 issuance attempts stopped before permit creation because the v2
Security approval postdated its claims-declared issue time. No v2 permit was
issued or consumed and no runtime mutation occurred. The fresh v3 baseline
reports Temporal runtime, the OOS controlled worker, and the WGCF controlled
worker as `not-installed`.

## Review Areas

### Identity

The v3 claims preserve distinct OOS API, OOS workflow-worker, and WGCF
activity-worker identities and separate owner queues. Runtime readiness must
prove each exact admitted poller identity.

### Secrets

The claims remain reference- and digest-oriented. Secret values, raw context,
unbounded logs, command output, and duplicated business records remain denied
in Temporal history and promoted evidence.

### Delivery

Platform may resolve this authorization only from its exact merged
`security-architecture` source path and containing revision. The permit remains
single-use and cannot be consumed before the declared issue time or after
expiry.

### Runtime

The approved scope is one local `component-commissioning-proof`. Any source,
image, identity, baseline, evidence, expiry, side-effect, or restore mismatch
stops new proof actions. After consumption, only the permit-bound terminal
cleanup path may restore the exact baseline or record a governed exception.

## Findings

1. Runtime operating evidence does not yet exist for v3. Producing it is the
   bounded purpose of ART #751.
2. Platform must not consume the permit before `2026-08-14T02:45:00Z` or after
   `2026-08-14T11:45:00Z`.
3. ART #791 must review completed evidence and exact-baseline restoration before
   profile activation or broader reuse.

These findings are fail-closed gates, not accepted exceptions.

## Decision

`approved-with-findings`

Approved:

- the exact v3 canonical claims digest and validity window named above
- the exact reviewed source, image, identity, queue, namespace, scenario,
  action, baseline, restore, and evidence bindings in that claims set
- use of the merged authorization as Security's input to Platform issuance
- one permit-bound local commissioning proof after the declared issue time

Not approved:

- v1, v2, any terminal session, or any other claims digest or validity window
- permit issuance without the separate operator approval
- direct runtime launch outside the reviewed Platform issuer and executor
- profile activation, self-serve launch, stage, production, or general workflow
  admission
- treating this pre-run decision as post-run Security acceptance

## Related Artifacts

- [Previous unusable v2 authorization](2026-08-14-temporal-post-readiness-fix-commissioning-authorization.md)
- [Temporal controlled commissioning proof contract](2026-08-01-temporal-controlled-commissioning-proof-contract.md)
- [Temporal approval provenance source review](2026-08-13-temporal-approval-provenance-source-review.md)
- [Temporal security view](../../architecture/components/temporal/README.md)
- [Security delta review process](../security-delta-review-process.md)
