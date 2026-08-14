# Temporal Image-Retrievability Commissioning Authorization

## Summary

- date: `2026-08-14`
- owner repo: `security-architecture`
- ART authorization: `openproject://work_packages/844`
- controlled execution: `openproject://work_packages/751`
- implementation evidence:
  `artifact://review-packets/delivery-698-work-item-843`
- canonical claims digest:
  `sha256:3586fc68041d2e7464f4eb737dc02c7c261c82522ebaf0d22ad436d7db7f0a8c`
- immutable baseline digest:
  `sha256:640c9386a16286954c4d14a7f4c17b158ca4cc1b772599101ba22068ebfd0668`
- authorization artifact:
  `records/controlled-proof-authorizations/delivery-698-844-temporal-commissioning-20260814-v6.json`
- decision: `approved-with-findings`

This review authorizes one fresh, permit-bound Temporal commissioning session
after exact runtime-image retrievability and target-platform validation landed.
It does not reuse v5 authority, activate Temporal, admit a general workflow, or
accept post-run evidence.

## Scope Delta

The v6 claims bind:

- session `delivery-698-751-temporal-commissioning-20260814-v6`
- Platform revision `e6ddc0545ca8e33b0b0ad0416b76e0fa84948854`
- OOS revision `f1f8a09561dd4667c188aea408695313a867501b`
- Workspace Governance revision
  `842943e949aff47e19835cc09ee24ed8c051723d`
- WGCF revision `6b8d65b7ba1df028e92c9d3f14eae14c481b5411`
- the reviewed OOS API, OOS worker, and WGCF worker image digests
- the `linux/amd64` runtime target and target-specific Temporal server manifest
- one operator-scoped namespace, fixed identities and queues, eleven ordered
  scenarios, and exact-baseline restoration
- issue time `2026-08-14T11:20:00Z` and expiry
  `2026-08-14T19:20:00Z`

The baseline was captured before claims assembly with all controlled runtime
surfaces at `not-installed`. Permit issuance now resolves every exact image
binding through an isolated credential-free Docker configuration before a
single-use permit can be created.

## Review Areas

- identity: unchanged fixed runtime identities and task queues
- secrets: ambient operator registry credentials are excluded from image
  validation; the runtime still declares no image-pull secret
- delivery: exact image and target-platform checks fail before permit creation
  or consumption
- runtime: the Temporal server lock now selects the reviewed `linux/amd64`
  manifest and all seven image bindings must resolve for that target

## Findings

1. Runtime operating evidence does not yet exist for v6; producing it remains
   the bounded purpose of ART #751.
2. Platform must consume only the exact v6 permit during its declared window.
3. Any image-resolution, target-platform, source, baseline, or authorization
   mismatch must fail before runtime mutation.
4. Post-run Security review remains required before activation or wider reuse.

These findings are fail-closed gates, not accepted exceptions.

## Decision

`approved-with-findings`

Approved:

- the exact v6 canonical claims digest and validity window
- the exact source, image, target-platform, identity, queue, scenario,
  baseline, restore, and evidence bindings in that claims set
- one permit-bound local commissioning proof after merged Security provenance
  and the separate operator approval are validated

Not approved:

- v1 through v5, any consumed authority, or any other claims digest
- direct runtime launch outside the reviewed Platform issuer and executor
- profile activation, self-serve launch, stage, production, or general workflow
  admission
- treating this pre-run decision as post-run Security acceptance

## Related Artifacts

- [Prior v5 authorization](2026-08-14-temporal-diagnostic-correction-commissioning-authorization.md)
- [Controlled commissioning proof contract](2026-08-01-temporal-controlled-commissioning-proof-contract.md)
- [Temporal security view](../../architecture/components/temporal/README.md)
