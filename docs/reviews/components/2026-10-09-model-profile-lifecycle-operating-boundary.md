# Model-Profile Lifecycle Operating-Boundary Security Delta

## Summary

- date: 2026-10-09
- owner repo: `security-architecture`
- delivery initiative: `openproject://work_packages/1203`
- parent feature: `openproject://work_packages/1214`
- security review item: `openproject://work_packages/1243`
- governing gate: `gate:model-operations-controlled-activation`
- governing architecture packet:
  `wgcf://artifacts/delivery-art/sha256/3a4b5edb6bc54ff47a45f610b41f75bc57dd9d1ab56e9475518100d75ff72ab0`
- reviewed source:
  - Operator Orchestration Service request-workflow merge:
    `operator-orchestration-service@147e50191a747bad3c0d8129a6f2817d4551d345`
  - Operator Orchestration Service activation candidate:
    `operator-orchestration-service@340d3a0609275af82fc107cbd63b7599b677a584`
  - Platform Engineering lifecycle-workflow merge:
    `platform-engineering@4df06f09e6960b94235be48a9afb2976b24d9eb6`
  - Governance Operations Console integration merge:
    `governance-operations-console@5cb579fcff7e77396e5701242b057e5be4ee7e51`
- source review:
  - [OOS request workflow PR #293](https://github.com/mfshaf7/operator-orchestration-service/pull/293)
  - [OOS bounded activation PR #294](https://github.com/mfshaf7/operator-orchestration-service/pull/294)
  - [Platform lifecycle workflow PR #279](https://github.com/mfshaf7/platform-engineering/pull/279)
  - [Console Model Operations integration PR #60](https://github.com/mfshaf7/governance-operations-console/pull/60)
- decision: `approved`

The exact revisions are approved for single-operator, loopback-only
`dev-integration` composition and operating proof. This decision permits OOS
PR #294 to merge before Platform work item `#1241` performs that proof. It does
not approve stage or production, shared or remote access, real client data,
direct provider access, or activation of an individual model profile without
its own exact Security decision.

## Scope Delta

### Design Intent

- let an operator request and review a governed model-profile lifecycle change
  through the Console and OOS;
- keep the canonical profile registry and lifecycle mutation in Platform;
- keep provider and model selection out of the Console and OOS;
- require a separate Security decision for `activate` and `exception` intent;
- make new and amended profiles remain suspended; and
- bind source, review, application, readback, operating evidence, and rollback
  without treating one layer's receipt as another layer's authority.

### Implemented Control

OOS owns request identity, caller/operator binding, revision ordering, review
state, replay protection, Platform fulfillment acknowledgement, and receipts.
Its activation candidate enables runtime construction only when both the
feature flag and `OOS_RUNTIME_PROFILE=dev-integration` are present. OOS cannot
choose a provider or model, write the Platform registry, or claim that a
profile lifecycle changed.

Platform validates the exact OOS source bundle before applying a reviewed
request. It owns registry source, provider/model references, suspended default
state, activation configuration, atomic apply and rollback, authoritative
readback, and private operating evidence. Activation and exception requests
must carry an exact Security decision reference. The workflow rejects secret-
shaped registry values and direct caller-controlled provider invocation.

The Console uses server-only adapters. The browser submits bounded intent to
OOS and receives safe request and operating projections; it receives no OOS
secret, Platform file path, provider credential, raw private artifact, or
registry mutation capability. Its Platform adapter reads only configured
private artifacts, requires owner-only file mode, and fails closed on stale,
malformed, mismatched, or incomplete evidence.

### Operating Evidence

OOS passed its focused model-profile tests, API and governance validators, and
the complete serialized owner suite with 1,238 passing tests and two explicit
skips. Parallel execution produced a host-level `SIGSEGV` and transient parse
corruption; the same committed source passed serially, so heavy proof remains
serialized on this resource-constrained host.

Platform PR #279 passed the lifecycle source, schema, contract, and owner-repo
validation at its reviewed head. Console PR #60 passed architecture guards,
489 semantic tests, type checking, production build, and exact-head review.
These results are source evidence. Platform `#1241` must still compose the
exact merged OOS activation revision and produce current positive, negative,
rollback, cleanup, and cross-layer readback evidence before operating
completion can be claimed.

## Review Areas

### Identity And Authorization

The Console machine caller, bound operator, OOS reviewer, Platform fulfiller,
Security decision authority, and human source reviewer remain distinct roles.
OOS rejects missing or mismatched caller/operator bindings and keeps Platform
fulfillment callers separate from operator-bound callers. No reviewed machine
identity can approve or merge its own source change.

This is acceptable only for the existing single-operator local lane. Shared or
multi-user exposure requires trusted user identity and a new delta review.

### Secrets And Data

OOS caller secrets and Platform artifact paths remain server-side. Private
operating artifacts must be owner-readable only and stay outside browser
responses and source. Registry input rejects secret-shaped keys; provider
credentials and direct provider calls are outside this workflow. Real client
data is not approved.

### Delivery And Source Integrity

Each owner revision is exact and reviewed. OOS activation is deliberately
sequenced after this Security decision and before Platform commissioning.
Platform source application requires the exact approved OOS request, pinned
source digests, clean expected source, atomic write, authoritative readback,
and rollback. Dirty, detached, stale-base, wrong-head, unreviewed, or unmerged
source cannot satisfy completion.

### Runtime, Replay, And Failure Integrity

Runtime construction remains off by default and fails closed outside
`dev-integration`. OOS rejects stale revision, unauthorized caller, malformed
input, invalid transition, and conflicting replay. Console rejects stale OOS
envelopes, same-sequence conflicts, unsafe Platform artifacts, and incomplete
reconciliation. Platform rejects out-of-order state, digest drift, missing
decisions, false readback, and incomplete proof.

### AI And Profile Lifecycle

This workflow governs profile metadata and lifecycle; it does not invoke a
model or approve model use. `create` and `amend` result in suspended profiles.
Every `activate` or `exception` request still requires a separate exact
Security decision covering the provider, model, route, data, and use boundary.

## Decision

`approved`

Security emits `gate:model-operations-controlled-activation` for OOS PR #294
and subsequent operating proof against exactly:

- `operator-orchestration-service@340d3a0609275af82fc107cbd63b7599b677a584`;
- `platform-engineering@4df06f09e6960b94235be48a9afb2976b24d9eb6`;
- `governance-operations-console@5cb579fcff7e77396e5701242b057e5be4ee7e51`;
- the `dev-integration` runtime profile;
- operator-private OOS state and Platform evidence paths; and
- the loopback-only, single-operator boundary described above.

Not approved:

- stage, production, shared, remote, public, or client-visible operation;
- direct browser registry mutation, provider selection, model selection, or
  credential access;
- direct OOS or Console provider invocation;
- real client data or secrets in requests, source, receipts, or projections;
- activating or excepting a profile without its separate exact Security
  decision;
- stale, malformed, incomplete, synthetic-substitute, unreviewed, or
  mismatched source and operating evidence; or
- treating source activation or Security review as completed Platform
  commissioning.

Any change to identity, credential custody, provider reachability, registry
authority, evidence privacy, network exposure, data classification, runtime
profile, or lifecycle decision ownership requires another delta review.

## Related Artifacts

- [Security delta review process](../security-delta-review-process.md)
- [Security review checklist](../security-review-checklist.md)
- [Governed AI access model](../../standards/governed-ai-access-model.md)
- [Governed AI Gateway component](../../architecture/components/governed-ai-gateway/README.md)
