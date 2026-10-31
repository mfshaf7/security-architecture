# Console AI activity read scope

## Summary

Source-only review of the operator-approved Recent AI activity extension in
Operator Orchestration Service and Governance Operations Console. OOS remains
the durable request/evidence owner. Console remains a read projection. The
review inherits the existing Agent Console, native Work Design/Refinement,
provider connection and primary Console boundaries. It adds no model provider,
policy decision, canonical workflow action or deployment authority.

This review covers uncommitted local source candidates based on OOS
`1eceee2afaf34dbf2fbe4bb142bcff9fba7799e0`, Console
`0d7ce97709e7843ede8afd9c378f29a81a861f43` and Security
`554a32cc74d12673fbb339074fa4da4d336e138b`. It does not attest a merged,
commissioned or live-qualified composition.

## Scope Delta

- The reviewed UI batch also restores Proposal completion/history projection,
  Repository compact layout, Model Operations inspection and primary Console
  readability/resource containment. OOS exposes the existing nullable canonical
  Delivery reference in Proposal snapshots; Console composes existing authorized
  Delivery reads without creating links or closing source records. These changes
  introduce no new caller, credential, mutation, provider or authority. Retired
  outcomes remain distinct from implementation evidence; unavailable sources
  remain unavailable. Technical disclosures hide detail visually, not evidence
  or controls. Page/default/layout and agent-label changes preserve their APIs.
- OOS adds one bounded GET under the existing Agent Console caller/operator
  authentication. Caller ownership and operator binding are enforced before
  reading or using cached pages. Cursors bind the same caller/operator and
  cannot select another principal, endpoint or filesystem location.
- Retained Agent Console invocations project closed request kinds, optional
  record identity, state, timestamps and existing evidence references. Existing
  result bodies, prompts, context payloads, error messages and credentials are
  excluded. Legacy requests keep absent metadata explicit.
- Optional new request metadata is included in the existing invocation request
  digest. Replaying an invocation with different activity identity is rejected.
  Task kinds are closed; record identity is bounded and excludes paths, URLs,
  control characters and common credential prefixes.
- Native Work Design and Refinement retain their existing services, profiles,
  context admission and output validation. Their request outcomes are recorded
  in the existing private Agent Console store when that runtime is active.
  Recording for enrolled callers requires caller-specific authentication and
  the existing operator binding. Shared-secret-only caller claims cannot
  populate bound history. Other existing native callers retain their prior
  service path without entering this operator-scoped journal.
- New native records store safe metadata and governed evidence references,
  without model text or invented invocation receipts. A prior process's
  unfinished record projects as unconfirmed rather than falsely working.
- History reads do not invoke models or perform canonical mutations. A bounded
  metadata-page cache is invalidated by the existing private state's file
  identity/version, avoiding repeated full parsing when the state is unchanged.
- Console forwards only a fixed 10-row read and a bounded opaque cursor through
  its existing server-side configuration and attribution helper. It rejects
  identity mismatch, unexpected fields, oversized responses, duplicate request
  IDs, invalid state/timestamp/receipt combinations and unsupported task kinds.
- Record references remain inert data. Navigation selects admitted workspace
  targets through existing Console entry intents, never arbitrary URLs,
  commands, approvals or mutation handlers. Missing links remain absent.
- Explicit disconnected preview examples remain visibly labelled. Live errors
  cannot select them. Failed refresh retains recorded rows with a stale-source
  explanation. Earlier history replaces a bounded page and preserves its
  cursor after failure; no model request is retried by history controls.

## Review Areas

### Identity and confidentiality

The API retains the existing caller-specific credential and configured human
operator binding. Browser queries cannot change principal or owner scope.
Cross-owner cursor tests reject substitution. Native recording extends that
same requirement to the two existing advice adapters; no unauthenticated
activity-write API is introduced. Summary allowlists exclude raw model and
operator content. Same-origin responses are non-cacheable.

### AI and workflow authority

Activity completion means an assistance request completed. It never means
that its draft was accepted, that a workflow advanced or that a product was
delivered. CGG, model routing, provider profiles and canonical decision controls
remain with their existing owners. The UI shows actual evidence references;
missing legacy metadata, native invocation receipts and interrupted outcomes
remain explicit.

### Persistence, capacity and operations

The existing atomic digest-checked private store is reused, with backward
compatible optional metadata. New metadata and retained invocation records
survive a normal owner restart. No browser storage becomes history authority.
Query output, page-cache size and browser page retention are bounded. This
extension inherits the existing store's whole-file persistence implementation;
it does not claim to replace that store or qualify unlimited journal capacity.
The main agent retains security judgment and final landing/release closure.

## Decision

**approved** for the bounded source extension within the existing local
`dev-integration` boundary. The decision is source-scoped and carries no live
activation or production acceptance.

Evidence consists of owner contract/HTTP tests for caller/operator isolation,
read-only projection, stable paging, retained native outcomes, replay binding,
shared-secret denial, restart interpretation, cache invalidation and absence of
raw content; Console decoder tests for identity/data boundaries; native browser
history/cursor/record-navigation checks; and isolated composed OOS HTTP to
Console-decoder proof. Synthetic model stubs in composed proof establish
protocol behavior and do not claim real provider generation.

Before final batch release, bind the reviewed changes to the exact final source
commits, land OOS before its dependent Console, refresh the generated owner
change-record index from merged owner source, and use the existing Platform
commissioning/acceptance procedure. Canonical runtime, provider accounts and
live request records were not modified by this review.

## Final candidate source evidence

Console Gary PR158 selects `ebd86efb015be1469b881b91e5585293d71ec8c2`.
Its repository validation, architecture guards,845 tests, typecheck, production
build, zero-vulnerability production audit and all15 production-build browser
checks pass. Hosted validation41177802661 passed on that exact candidate.

OOS Gary PR399 merged as `cc6d6e341739851eaf5d86212b8f187540767927`;
PR400's published candidate is `ac36832a6cda4279efef10132c029e551e155686`.
The locally combined tree `aed19da6399b662c3f465b9d63f6893daaa654f1` at
validation-only Gary merge `0238b8972d46b4bae9b4e6676eebfb628026e14f`
passes1722 owner tests with2 existing skips. Full contract/OpenAPI/governance,
current-origin/main change-record and mutation checks pass. Both original
candidates passed API/worker image builds, health and execution-disabled smoke;
hosted41177809921 and41177927895 passed their original published candidates.
Final combined exact-head hosted validation and merged-tree equality are still
required before composed source selection. No provider inference or live
commissioning is inferred from these source checks.

The separate [October platform disposition](../../assessments/platform/2026-10-disposition.md)
records the overdue existing assessment/remediation checkpoints. It retains
open risks and does not expand this bounded source approval.
