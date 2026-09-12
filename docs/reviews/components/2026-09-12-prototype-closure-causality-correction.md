# Prototype Closure Causality Correction Review

## Summary

- date: 2026-09-12
- owner repo: `security-architecture`
- delivery ref: `openproject://work_packages/1143`
- parent feature: `openproject://work_packages/921`
- parent initiative: `openproject://work_packages/892`
- reviewed contract: `workspace-governance@eb9ec14e9191535a358bc80418aa0a14ad8b8609`, `contracts/prototype-closure.yaml` and its version-2 schemas
- prior review: `2026-09-12-prototype-closure-implementation-admission.md`
- decision: `approved-with-findings`

The corrected source-event and terminal-receipt order is acceptable for bounded, inactive Closure implementation. This updates the causality judgment in the prior review; it does not activate the Closure identity or prove that Studio, OOS, WGCF, Platform, or Console implementations exist.

## Scope Delta

### Design Intent

The prior contract allowed a circular interpretation: a Studio source event could appear to require the terminal OOS receipt, while that receipt required a merged Studio event. Version 2 orders the evidence instead. The accepted request and action-specific target authority evidence precede the Studio event. The event binds the request digest, exact expected source revision, prior history digest, and relevant accepted evidence, never a future terminal receipt. After provider-reviewed merge, Studio readback proves the exact merged event, lifecycle, and custody. Only then may OOS issue a completed terminal receipt binding the event and readback digests.

### Implemented Control

Workspace Governance merged the version-2 contract, request, history-event, merged-readback, and receipt schemas, plus semantic validation in PR #187. Source-event and receipt fields now express the acyclic order. The dedicated Platform Closure identity remains defined but inactive. OOS, Studio, WGCF, and Console Closure implementations are not established by this contract merge. Separately, OOS PR #209 now rejects an Architecture Packet whose declared ART graph differs from live ART during admission; that planning guard does not provide Closure mutation authority.

### Operating Evidence

Contract tests and merged source prove schema and semantic behavior only. The missing ART #1101 to #1142 dependency was restored through the bounded OOS route as OpenProject relation #313; #1143 then reached `implementation-ready`. This establishes work-order coherence, not Closure runtime readiness. No commissioned Closure credential, real Studio Closure mutation, target acceptance, merged Studio readback, or terminal Closure receipt is evidenced here.

## Review Areas

### Authority And Source Custody

The corrected order preserves separate authorities. Studio owns incubation source and append-only lifecycle history. Target Delivery or durable owner acceptance must be resolved from that owner before an event claims the corresponding transition. OOS coordinates and issues its own terminal receipt only after canonical Studio readback. Applying Delivery changes project phase, not source custody; graduation requires one accepted durable source custodian and exact transfer or already-owned proof. Retirement and reopen cannot erase source history or revive old runtime authority.

Implementation must bind the authenticated caller, accountable operator, action, expected lifecycle, source revision, record digest, correlation, idempotency key, prior event digest, and action-specific accepted evidence. A selected route, UI confirmation, advisor output, or syntactically valid reference is not target acceptance.

### Event, Merge, And Receipt Integrity

The source event must be reviewable on a non-default branch and must not contain or require the future OOS terminal receipt. Source preparation and merge require one authority lock, current expected-state comparison, exact-head validation, provider-enforced review and required checks, and a canonical merged readback. The readback must identify the event digest, merged source revision, observed lifecycle, and custody before OOS records a completed receipt. A receipt cannot retrospectively authorize the event it cites.

Identical replay under the same authority digests returns the same terminal outcome; changed authority input under the same idempotency key is denied. Denied or failed pre-merge attempts may have a terminal finding and next action but no Studio transition event. A merge whose result or readback is uncertain remains pending reconciliation, not terminal failure or an unguarded retry. Post-merge receipt failure must reconcile against the merged event rather than creating a second event or inventing rollback.

This review does not authorize the Closure machine identity to approve or merge its own source. An authorized human PR-only bypass of a repository update restriction, where separately permitted, does not waive human review, trusted CI, exact-head proof, or canonical readback and is not a general Closure merge permission.

### Runtime, Data, And Revocation

Target receipts, notes, source references, and advisor output remain untrusted until resolved against their owners. Implementations must bound fields and references, keep credentials and unrestricted evidence bodies out of source events and logs, and preserve the Prototype data and visibility posture. Platform owns exact active incubation-resource cleanup and Closure token custody. Retirement needs cleanup or absence proof; graduation needs explicit resource disposition. Suspension and revocation must affect only the Closure identity and resources, not Landing, Maturity, accepted target source, or audit history.

## Findings And Gates

1. `#1102` and `#1103` must implement the version-2 Studio event/readback and source custody boundary with exact branch, history, replay, denial, and recovery behavior. No source event may cite a future terminal receipt.
2. `#1104` and `#1105` must implement readiness and OOS coordination that resolves target authority before event creation, issues the terminal receipt only after exact merged readback, and leaves uncertain post-merge outcomes pending reconciliation. WGCF custody alone is not Studio source mutation.
3. `#1108` and `#1109` must prove the four actions and failure paths against composed owners, including pre-merge denial, conflicting replay, changed review head, merge uncertainty, readback mismatch, receipt failure, cleanup failure, and restart. Fixtures alone are insufficient operating evidence.
4. `#1140` remains the final Security gate for the actual implementation, provider rules, reviewer separation, token custody, composed proof, suspension, and revocation. `#1107` may commission only after that decision. Until then the Closure identity and normal operator availability remain inactive.

These are implementation and activation conditions, not accepted risk.

## Decision

`approved-with-findings`

Approved: version-2 causality contract as the source for bounded inactive implementation under Feature #921.

Not approved: live Closure availability, source mutation without accepted target authority, a source event dependent on its future terminal receipt, success without exact merged Studio readback, false terminal failure after uncertain merge, agent self-approval, bypass of required review or checks, reuse of Landing/Maturity credentials, or implicit Portfolio publication or governed release.

If implementation cannot preserve this order, return a concrete contract delta for review before expanding local authority. Final normal-availability judgment remains at #1140.
