# Temporal Post-Installation-Fix Commissioning Authorization

## Summary

- date: `2026-08-14`
- owner repo: `security-architecture`
- ART authorization: `openproject://work_packages/847`
- controlled execution: `openproject://work_packages/751`
- implementation evidence:
  `artifact://review-packets/delivery-698-work-item-846`
- canonical claims digest:
  `sha256:1b9f339fc12367310d7e75ade3c459662ebd19caa30c01463f3320f0ec6b266e`
- immutable baseline digest:
  `sha256:91134c6d8c004b4b74098ca732a97c6869650d4d5345960d8d720649764facaf`
- authorization artifact:
  `records/controlled-proof-authorizations/delivery-698-847-temporal-commissioning-20260814-v8.json`
- decision: `approved-with-findings`

This review authorizes one fresh permit-bound Temporal commissioning session
after ART #846 corrected the chart-generated Kubernetes name boundary. It does
not reuse v7 authority, activate Temporal, admit a general workflow, or accept
post-run evidence.

## Scope Delta

The v8 claims bind:

- session `delivery-698-751-temporal-commissioning-20260814-v8`
- Platform revision `abeb7632a5e19d5c9300b63a331b91bcc188f8c2`
- OOS revision `f1f8a09561dd4667c188aea408695313a867501b`
- Workspace Governance revision
  `842943e949aff47e19835cc09ee24ed8c051723d`
- WGCF revision `6b8d65b7ba1df028e92c9d3f14eae14c481b5411`
- the reviewed OOS API, OOS worker, and WGCF worker image digests
- the `linux/amd64` runtime target and target-specific Temporal server manifest
- operator-scoped Temporal namespace
  `governance-operator-workspace-own-8b38e48f3544`, fixed identities and
  queues, eleven ordered scenarios, and exact-baseline restoration
- issue time `2026-08-14T14:40:00Z` and expiry
  `2026-08-14T22:40:00Z`

The immutable baseline was captured before claims assembly with all controlled
runtime surfaces at `not-installed`. Security approval is recorded before the
declared issue time. Permit issuance must still wait for merged Security
provenance and a separate operator approval recorded before that issue time.

## Review Areas

- identity: unchanged fixed runtime identities and task queues; the readable
  namespace prefix is shorter while its operator digest suffix remains bound
- secrets: ambient operator registry credentials remain excluded; the runtime
  declares no image-pull secret
- delivery: v7 is terminal and not reusable; v8 binds the merged ART #846
  correction and finalized implementation evidence
- runtime: all seven image bindings remain subject to credential-free exact
  digest and `linux/amd64` validation before permit creation

## Findings

1. Runtime operating evidence does not yet exist for v8; producing it remains
   the bounded purpose of ART #751.
2. Platform must consume only the exact v8 permit during its declared window.
3. Any chronology, image-resolution, target-platform, source, baseline,
   namespace, or authorization mismatch must fail before runtime mutation.
4. Post-run Security review remains required before activation or wider reuse.

These findings are fail-closed gates, not accepted exceptions.

## Decision

`approved-with-findings`

Approved:

- the exact v8 canonical claims digest and validity window
- the exact source, image, target-platform, identity, queue, scenario,
  baseline, restore, and evidence bindings in that claims set
- one permit-bound local commissioning proof after merged Security provenance
  and the separate operator approval are validated

Not approved:

- v1 through v7, any consumed authority, or any other claims digest
- direct runtime launch outside the reviewed Platform issuer and executor
- profile activation, self-serve launch, stage, production, or general workflow
  admission
- treating this pre-run decision as post-run Security acceptance

## Related Artifacts

- [Prior v7 authorization](2026-08-14-temporal-chronology-correct-commissioning-authorization.md)
- [Controlled commissioning proof contract](2026-08-01-temporal-controlled-commissioning-proof-contract.md)
- [Temporal security view](../../architecture/components/temporal/README.md)
