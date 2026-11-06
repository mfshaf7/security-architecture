# Proposal register, original history and submission recovery

## Summary

Review the existing Proposal maintenance batch across OOS and Governance
Operations Console. Extend the authenticated source-read boundary with bounded
register pages, retain original decision evidence, and make delayed or uncertain
submissions understandable. Workspace Proposals remains canonical; OOS remains
its mutation adapter. No identity, secret, database, provider grant, release
permission or new runtime control is introduced.

Inherit the unchanged account, private-project, provider, source-custody and
runtime boundaries from the [previous accepted review](2026-11-05-repository-account-routing.md).
This review concerns source and isolated local conformance. It does not replace
exact composed-source runtime acceptance or claim deployment.

The main agent retains Security judgment and final landing judgment. Gary authors
source; the standing delegated accountable human reviews and merges. This is not
an independent assessment.

## Scope Delta

The new read-only `/v1/proposals/register` route reuses authenticated callers,
configured Workspace Proposals scope, current source envelopes, audit and exact
revision/view binding. Each response has at most25matching summaries and scans
at most four native25-record pages. Selector-bound continuation, source totals,
explicit unavailable Delivery outcomes and exact candidate-ID metadata avoid
register-wide history and Delivery tree expansion. Summary history is explicitly
unloaded and cannot authorize a write. Sparse searches require continuation;
this is not an indexed search or a guarantee of a frozen source-wide snapshot.

Exact native Idea reads now prove the configured project and Idea type before
opening journals or reaching existing mutation logic. Foreign IDs fail closed.
The Console opens an exact selected snapshot before workflow actions and checks
Proposal/version identity before combining history pages. Authorization denial
clears retained source data; network failure retains only stale/read-only views.
No configured failure substitutes synthetic records.

New disposition events retain the accepted command's decision payload. Existing
journal records remain unchanged. Old events use original summaries, never
later notes or route. This adds no OpenProject machine field, lifecycle value,
command authority or cross-project disclosure. The original full notes were
already available to the same admitted callers through selected projections.

Capture recovery reuses the existing source-identity lookup and exact original
intent. Found identical captures are reused; unavailable prechecks do not send
creation. An uncertain response preserves details and offers a result check
before an identical retry. This does not assert global exactly-once creation
under concurrent clients. Ordinary workflow commands preserve their existing
stable IDs, version checks, approval and target-review gates. Pending dialogs
block repeat clicks; errors retain drafts and successful feedback names the
next action. Advisor draft lengths match the existing command limit, without
allowing advisor submission or silently truncating operator input.

## Review Areas

- Identity: existing authenticated caller/operator binding; exact Proposal
  project/type scope; clearing denied source data.
- Delivery: immutable original evidence, stable replay identity, unchanged
  repository readiness, target review and approval boundaries.
- Runtime: bounded read work, source revision binding, no new process or storage,
  isolated preview rather than live writes.

Secrets and AI custody remain inherited unchanged. A clearer UI does not grant
source access, model authority, repository admission or release permission.

## Evidence And Limits

Owner tests exercise bounded continuation beyond the first page, sparse search,
selector conflicts, malformed source metadata and exact linked Delivery reads.
Native HTTP tests check source envelopes and reject unauthorized/malformed reads
before accessing OpenProject. Native project/type tests reject foreign work
packages before their journals. Existing owner workflow tests preserve replay,
optimistic concurrency, custody and target gates. The Console adapter tests
verify native errors, source/version matching and capture precheck behavior.
Browser checks use isolated synthetic responses for paging, original history,
pending/error/result states, denied reads and interrupted capture recovery.
They do not create real Proposals, repositories or target records.

The source change does not modify writable OpenProject fields or their
allowedValues/form schema. Native adapter changes are read-only scope checks and
exact-ID metadata filters. Existing mutation-form regression tests remain in
the owner suite. A broad product-readiness or live performance claim is outside
this evidence.

## Decision

**approved** for this bounded source maintenance and isolated preview.

Operator preview review remains before publication. Land the OOS producer and
its indexed owner evidence before the dependent Console consumer, preserve the
existing prior composed runtime until normal exact acceptance/activation, then
verify authenticated readback. Rollback selects the prior paired sources; no
canonical event or proposal migration is required. This review does not
commission the new source or weaken any existing runtime pin check.
