# Temporal Chronology-Correct Commissioning Authorization

## Summary

- date: `2026-08-14`
- owner repo: `security-architecture`
- ART authorization: `openproject://work_packages/845`
- controlled execution: `openproject://work_packages/751`
- implementation evidence:
  `artifact://review-packets/delivery-698-work-item-843`
- canonical claims digest:
  `sha256:5908b6f18beb28ab5b9e47b7ff4e2555d955f310a0e3d99aed8bc7a0ff251a4e`
- immutable baseline digest:
  `sha256:aced40a209d0d0abc12f42c5cfbd203f579b8bea98a066ba729ded935ea04abb`
- authorization artifact:
  `records/controlled-proof-authorizations/delivery-698-845-temporal-commissioning-20260814-v7.json`
- decision: `approved-with-findings`

This review authorizes one chronology-correct, permit-bound Temporal
commissioning session after the v6 issuer rejected its impossible approval
chronology. It does not reuse v6 authority, activate Temporal, admit a general
workflow, or accept post-run evidence.

## Scope Delta

The v7 claims bind:

- session `delivery-698-751-temporal-commissioning-20260814-v7`
- Platform revision `e6ddc0545ca8e33b0b0ad0416b76e0fa84948854`
- OOS revision `f1f8a09561dd4667c188aea408695313a867501b`
- Workspace Governance revision
  `842943e949aff47e19835cc09ee24ed8c051723d`
- WGCF revision `6b8d65b7ba1df028e92c9d3f14eae14c481b5411`
- the reviewed OOS API, OOS worker, and WGCF worker image digests
- the `linux/amd64` runtime target and target-specific Temporal server manifest
- one operator-scoped namespace, fixed identities and queues, eleven ordered
  scenarios, and exact-baseline restoration
- issue time `2026-08-14T13:05:00Z` and expiry
  `2026-08-14T21:05:00Z`

The fresh baseline was captured before claims assembly with all controlled
runtime surfaces at `not-installed`. Security approval is recorded before the
declared issue time. Permit issuance must still wait for merged Security
provenance and a separate operator approval recorded before that issue time.

## Review Areas

- identity: unchanged fixed runtime identities and task queues
- secrets: ambient operator registry credentials remain excluded; the runtime
  declares no image-pull secret
- delivery: v6 chronology failed closed before permit creation and is not
  reusable; v7 restores the required baseline-to-approvals-to-issue order
- runtime: all seven image bindings remain subject to credential-free exact
  digest and `linux/amd64` validation before permit creation

## Findings

1. Runtime operating evidence does not yet exist for v7; producing it remains
   the bounded purpose of ART #751.
2. Platform must consume only the exact v7 permit during its declared window.
3. Any chronology, image-resolution, target-platform, source, baseline, or
   authorization mismatch must fail before runtime mutation.
4. Post-run Security review remains required before activation or wider reuse.

These findings are fail-closed gates, not accepted exceptions.

## Decision

`approved-with-findings`

Approved:

- the exact v7 canonical claims digest and validity window
- the exact source, image, target-platform, identity, queue, scenario,
  baseline, restore, and evidence bindings in that claims set
- one permit-bound local commissioning proof after merged Security provenance
  and the separate operator approval are validated

Not approved:

- v1 through v6, any consumed authority, or any other claims digest
- direct runtime launch outside the reviewed Platform issuer and executor
- profile activation, self-serve launch, stage, production, or general workflow
  admission
- treating this pre-run decision as post-run Security acceptance

## Related Artifacts

- [Rejected v6 chronology](2026-08-14-temporal-image-retrievability-commissioning-authorization.md)
- [Controlled commissioning proof contract](2026-08-01-temporal-controlled-commissioning-proof-contract.md)
- [Temporal security view](../../architecture/components/temporal/README.md)
