# Lifecycle Context Controlled-Activation Review

## Summary

- date: 2026-09-24
- owner repo: `security-architecture`
- delivery ref: `openproject://work_packages/1166`
- parent feature: `openproject://work_packages/1159`
- parent initiative: `openproject://work_packages/1154`
- governing architecture:
  `wgcf://artifacts/delivery-art/sha256/f446b73abf7a9f07beee6bef3532a781a24fec81ee6e93570a39efe11d2b6905`
- reviewed source:
  - Context Governance Gateway PR #20, merge commit
    `f57423379aceb28d0072b977e43ee0f18590ae20`
  - Operator Orchestration Service PR #232, merge commit
    `041f167dfbb19c0da0b12707b035a4fa36ad96d9`
- reviewed CI:
  - CGG run `35931761450`, passed on PR #20
  - OOS run `35938503700`, passed on PR #232
- decision: `approved-with-findings`

This review permits Platform work item `#1167` to commission and prove the
exact lifecycle-context boundary in local `dev-integration`. It does not
activate the composition, establish normal availability, or approve stage or
production use. Platform must prove the configured identity, secret custody,
packet-first behavior, explicit raw fallback, restart, suspension, teardown,
and rollback boundaries before the composition may be described as operating.

## Scope Delta

### Design Intent

OOS derives authoritative lifecycle sources from the active Delivery work
session and asks CGG to admit, redact, budget, and preserve them as a bounded
packet. OOS remains the lifecycle authority. CGG cannot choose or execute an
action, invoke a model, mutate ART or source, or authorize a raw fallback.

The Governance Operations Console remains an authenticated OOS client. It must
not call CGG directly. Packet mode is the default. Raw fallback is a separate,
explicit OOS decision that requires a substantive reason and remains measured
against the exact work session.

### Implemented Control

The exact reviewed CGG source:

- accepts only the dedicated lifecycle caller allowlist and shared secret;
- has no usable default credential and fails closed while unconfigured;
- binds caller, operator, session, execution, Delivery item, Landing Unit,
  lifecycle state, source revisions, source digests, request time, and budget;
- validates one to sixteen typed ART, repository, validation, and runtime
  sources and rejects stale, oversized, malformed, or digest-mismatched input;
- stores raw input only through CGG custody while replay records and responses
  retain safe bindings, digests, packet references, and redacted content;
- returns explicit unavailable-source and truncation signals;
- replays an identical idempotent request across service restart and denies
  conflicting key reuse; and
- declares that it has no model, approval, Delivery mutation, lifecycle action,
  or raw-fallback authority.

The exact reviewed OOS source:

- derives all four source classes from current work-session truth;
- binds the request to the existing caller and operator identities before any
  projection;
- validates the complete CGG response, authority denials, source bindings,
  timeline, safety posture, budget, and receipt references before accepting a
  packet;
- records only references, digests, source summaries, and measurements in its
  lifecycle-context ledger, not packet or raw context content;
- records CGG denial and never silently downgrades a failed packet request to
  raw context;
- makes raw fallback an explicit request mode with a required reason, stable
  request identity, replay protection, and a separate counter; and
- reports whether the CGG client is commissioned without projecting its
  credential.

### Operating Evidence

The reviewed PRs are merged and their repository CI checks passed. Their tests
cover authentication denial, source and request digest checks, redaction,
budgeting, receipt binding, unavailable sources, identical replay, conflicting
replay, restart recovery, packet response drift, caller and operator mismatch,
explicit raw fallback, denial measurement, and secret-free ledger storage.

This is source and CI evidence. There is no configured end-to-end lifecycle
composition yet. No current evidence proves the dedicated credential is
projected only to OOS, that packet mode works through the composed services,
that raw fallback is operator-visible and measured in the live path, or that
restart, suspension, teardown, and rollback preserve the required receipts and
canonical state. Those are mandatory `#1167` proofs.

## Review Areas

### Identity And Authorization

Platform must provision one lifecycle-specific CGG caller binding for OOS.
The Console authenticates to OOS and must not receive the CGG credential or a
direct CGG route. OOS must preserve the caller and operator identities already
bound to the work session. Caller, operator, session, execution, work item,
Landing Unit, operation, source revisions, and idempotency identity must remain
consistent across the OOS request, CGG receipt, OOS ledger, and Console
projection.

A shared credential, implicit caller, changed binding, direct browser call, or
cross-session replay must fail closed. Local `dev-integration` attribution is
not authenticated production human identity and cannot support stage or
production claims.

### Secrets And Context Custody

The lifecycle shared secret must be generated and projected by Platform only
to the exact CGG and OOS consumers. It must not appear in source, persisted OOS
session state, packets, receipts, logs, metrics, traces, browser responses, or
ART evidence.

CGG owns raw artifact custody and redacted packet projection under its existing
local dev-integration findings. OOS may retain packet and receipt references,
digests, source summaries, fallback reasons, and counters, but not a second raw
context copy. Raw fallback output remains inside the authenticated OOS
operator boundary; it is not model-safe CGG output and must never be silently
selected or forwarded to a model.

### Delivery And Authority

CGG context evidence is not lifecycle approval. OOS alone projects the legal
next action and coordinates the existing Delivery work-session state machine.
Neither CGG nor the Console may mutate ART, source, review, merge, Security, or
release authority through this context path.

The Security gate binds only the two exact merged revisions above. A changed
caller, source taxonomy, fallback policy, credential path, custody model,
authority declaration, browser route, or runtime lane requires a fresh review
before activation.

### Runtime, Replay, And Recovery

Packet projection must fail closed on missing configuration, unavailable CGG,
authorization failure, stale context, digest mismatch, unsafe projection,
invalid receipts, or response-binding drift. Such failure must increment the
denied measurement and must not create packet success or raw fallback.

An identical retry may return the retained result. Conflicting reuse of either
CGG idempotency identity or OOS request identity must remain denied. Platform
must prove those semantics after API and OOS restart using the composed durable
state rather than only in-memory fixtures.

Suspension must stop new projection and revoke only the lifecycle binding.
Teardown and rollback must preserve ART, Git history, work-session state,
packet and redaction receipts, OOS ledger history, and unrelated CGG routes.
Cleanup must not delete shared CGG custody or unrelated Work Design and
Refinement state.

### Visibility And AI

The operator surface must distinguish packet, denied, and explicit raw-fallback
results and expose the cumulative measurements without exposing raw packet
content or credentials. A failed or denied projection cannot be rendered as a
successful packet.

This boundary introduces no model invocation. Lifecycle context remains input,
not approval. Any later model consumer, autonomous action, tool call, or raw
context projection requires its own reviewed authority and human-control path.

## Findings And Activation Gates

1. **Composition is not commissioned.** `#1167` must project the dedicated
   credential only to CGG and OOS, preserve Console-to-OOS routing, and prove
   successful authenticated packet projection through the configured services.
2. **Raw fallback has source controls but no composed operating proof.**
   `#1167` must show packet mode as the default, CGG failure as denied without
   downgrade, and raw fallback only after a separate authenticated request with
   a substantive reason and incremented measurement.
3. **Durable recovery is not proven in composition.** `#1167` must prove
   identical replay and conflicting replay across CGG and OOS restart while
   preserving source, receipt, and session bindings.
4. **Suspension, teardown, and rollback are not proven.** `#1167` must stop new
   requests, revoke the lifecycle credential, remove only composition-owned
   bindings, preserve evidence and canonical state, and restore the prior
   inactive posture without affecting other CGG workflows.
5. **The approval is local only.** Authenticated human identity, governed
   secret delivery, shared custody, stage, production, and model-driven use are
   outside this decision.

These findings are ordered activation conditions, not accepted risk. Failure
returns to Platform `#1167` and keeps the lifecycle composition inactive.

## Decision

`approved-with-findings`

Approved: the exact merged CGG and OOS source contracts and bounded Platform
commissioning work in `#1167` for local `dev-integration`.

Not approved: current operating readiness; normal availability; direct
Console-to-CGG access; implicit, automatic, or unmeasured raw fallback;
credential exposure; fixture-only activation claims; context-based lifecycle
approval; model invocation; broad cleanup; stage; or production.

The controlled-activation gate is satisfied only for Platform to begin the
bounded implementation and proof above. It is not evidence that the runtime
gate has already passed.

## Related Artifacts

- `context-governance-gateway/docs/operating-model/lifecycle-context-projection.md`
- `context-governance-gateway/contracts/schemas/lifecycle-context-projection-request.schema.json`
- `context-governance-gateway/contracts/schemas/lifecycle-context-projection-result.schema.json`
- `operator-orchestration-service/contracts/delivery-art-work-session/lifecycle-context-request.schema.json`
- `operator-orchestration-service/contracts/delivery-art-work-session/lifecycle-context-ledger.schema.json`
- `operator-orchestration-service/docs/records/change-records/2026-09-24-delivery-lifecycle-context-consumer.md`
- [`2026-05-05-context-governance-gateway-active-devint-runtime.md`](2026-05-05-context-governance-gateway-active-devint-runtime.md)
- [`2026-08-23-delivery-art-work-session-lifecycle.md`](2026-08-23-delivery-art-work-session-lifecycle.md)
