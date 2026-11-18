# Finalized brief presentation and complete advisor replies

## Summary

Review the approved maintenance batch for complete finalized-brief presentation,
a larger controlled note editor, the Build Tree selected-item request mapping,
and bounded transport of valid structured advisor replies. Landing Unit Decision:
`child_isolated_landing_unit`, `brief-advisor-acceptance-20261118`.
The separate Security review/acceptance boundary justifies this unit. The main
agent exercises standing delegated operator review; this is not independent
assurance. No ART items or project-runtime implementation are added.

## Scope Delta

- Retained collections show one diagram per preview with the original complete
  export. Navigation, keyboard/touch access and zoom preserve retained versions.
- Pending and finalized briefs share their complete review layout. Unsaved work
  cannot silently substitute an older snapshot. A larger note editor shares the
  current controlled field, length, read-only state and explicit save semantics.
- Build Tree reads selected identity from the existing versioned context's
  observations. Exact source, package, operator and selected-item validation remain.
- OOS validates typed native replies before encoding the existing compatibility
  field. Both OOS response contracts and the Console decoder now admit a bounded
  128,000-character structured transaction rather than smaller human-text limits.
  The native decoder rejects an oversized aggregate; messages remain limited to
  12,000 characters and individual field/operation limits remain unchanged.

## Review Areas

AI/data: replies remain inert local drafts. The selected role, fields, source
revision, read-only state and complete transaction are validated. Canonical Apply,
source execution, approval and model/provider configuration are unchanged. The
actual retained native reply was structurally valid; compatibility size checks
caused rejection. It was validated offline through the repaired consumers,
without another inference, browser injection or canonical mutation.

UI/data: full notes render as text in the existing dialog system. Previews reuse
the existing renderer and retained snapshot; no new remote image origin, HTML
execution, storage authority or mutable history is introduced. Explicit Save and
Finalize remain separate actions; preview/navigation/expansion do not finalize.
Tree application and undo preserve prior finalized versions and unrelated work.

Delivery/runtime: Gary authors both owner PRs; delegated human review verifies
exact heads and passing checks. The Security decision must name their merged
revisions before normal activation. No credential scope, provider timeout,
privilege, service family, persistent storage or Stage/Prod authority is added.
Current account custody, CGG admission, provider journals, recovery controls and
prior accepted runtime remain. Known hardware instability is unchanged.

## Evidence

Console: all 1,155 semantic tests, architecture, type checking, optimized build,
repository validation and production dependency audit pass. Browser tests cover
full/pending/retained/multi-view review, notes and current-versus-old snapshot,
selected-item request mapping, large complete tree application and exact undo.
Finalized history is unchanged. Synthetic replies are not model-quality proof.

OOS: 2,021 tests pass with two existing skips. Generated Work Design/Agent Console
OpenAPI and the full 262-route API documentation checks pass; governance and
committed base-aware record/mutation checks pass. The actual retained 52,248-
character compatibility reply passes the native decoder, both repaired OOS
contracts, Console parser and atomic tree transaction offline. Its human message
is within the unchanged limit. Oversized aggregates/messages still fail.
Exact hosted checks and candidate/merged tree equality precede acceptance.

## Decision

`approved` for this bounded source delta, subject to the exact merged-source
composition recorded below and the existing normal activation. This grants no
autonomous final decisions, new provider scope or broader product-readiness
claim. Source tests are distinct from current operating proof. A completed
provider result must not be regenerated merely because transport rejected it.

## Rollback And Operating Qualification

Restore the prior accepted composition through the existing owner procedure.
Retain private drafts, finalized versions, saved conversations and original
completed/unconfirmed provider records. No reset or inference replay is part of
rollback. After activation inspect actual source/process bindings and native
Console loading, preview/note history and advisor request delivery. Do not claim
all advisor behaviors, hardware reliability or project runtime work complete.

## Exact Merged Sources

Gary [OOS418](https://github.com/mfshaf7/operator-orchestration-service/pull/418)
merged at `1df4a93e93b5c987595056c9060f0d0b203bde56`; Gary
[Console184](https://github.com/mfshaf7/governance-operations-console/pull/184)
merged at `35fe587b0b77fd0aea2cc2a7a974464c6cbdb43b`. Both exact candidate heads passed hosted
checks and delegated approval; each merged tree matches its reviewed candidate.
The [current composed decision](2026-10-24-configurable-ai-routing.md) and its
machine-readable companion accept these revisions with the unchanged other
owners, Platform tree, architecture, durable capability manifest and policies.
Normal activation and actual current operating verification remain separate.
