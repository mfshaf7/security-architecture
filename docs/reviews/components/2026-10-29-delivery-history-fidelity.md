# Delivery history fidelity security review

## Summary

- date: 2026-10-29
- decision: `approved`
- classification: operator-approved owner maintenance
- composition: [finite source decision](2026-10-24-configurable-ai-routing.yaml)

Approve the existing authenticated history-read correction and original Console
inspection interfaces. This extends the [completed-work lock review](2026-10-28-native-completed-work-lock.md).
It introduces no workflow, identity, account, credential, model, persistence
service or approval authority. Original absence and partial coverage remain
explicit; missing historical artifacts are not recreated as evidence.

## Scope Delta

Gary OOS candidate `74f7e6181f8b0f7bc3f8207639a51d978e82c631` merged as
`d219e37c02170c9ecf7900fbd8b2a0561f3dfea7` in
[PR392](https://github.com/mfshaf7/operator-orchestration-service/pull/392).
Gary Console candidate `47f71bdcfea39e5077c4fe8eecce0bf882bc0f9e` merged as
`eea99305ba7ee06fff7755162e0b82051954e53f` in
[PR144](https://github.com/mfshaf7/governance-operations-console/pull/144).
Both candidate/merge trees are identical. Local and exact-head hosted checks
passed: OOS1,681passing/two existing skips and Console805passing, including
architecture/types/production build. The Console production audit found zero
vulnerabilities. OOS exact API/worker builds and health/fail-closed smoke passed.
Only OOS and Console advance in the finite paired decision. Platform tree, other
reviewed sources, original durable manifest, generation and worker digest remain
unchanged. Candidate/merge tree equality was verified before selecting these revisions.

OOS scopes the selected target by configured Delivery project, root and Epic type
before reading history. Intake, Work Design, Refinement and closeout evidence are
independent. Refinement does not require a currently authorable packet to inspect
verified original runs and trusted activity receipts. Run/event target binding,
trusted actor validation and distinct original receipt digest identities remain.

OpenProject's selected-item activity endpoint returns an unpaginated collection.
The existing adapter consumes it once with truthful collection metadata; the
Console read slices logical pages, rather than claiming native server pagination.
It adds no project-wide archive scan or cross-request cache. Original creation,
change, comment, actor reference and time are retained. Raw structured workflow
payloads are not exposed in the activity excerpt. Missing coverage is explicit.

The Console retains the same active-work components with completed-work edits,
advice, finalization, approval, apply and autosave locked. Pure navigation and
snapshot inspection/zoom remain available. Selected retained versions supply
board, note and full brief when present. Older missing fields and wholly absent
artifacts remain explicit; current metadata and unaccepted autosave cannot fill
original history. Refinement and Execution preserve verified independent sections
when another stage or current packet cannot be read.

## Review Areas

### Identity, secrets and scope

No new endpoint authority or identity is introduced. Existing caller, source and
admission checks precede the existing authenticated GET. Exact target project,
parent and type checks precede evidence access; optional schema availability
cannot broaden scope. Current command eligibility is not granted by a history
projection. Original actor refs are retained when the provider omits names.
Public source contains synthetic tests only, without private journals or tokens.

### Delivery, runtime and evidence

Original stage records retain IDs, actors, times, digests and references. The
retained native activity event digest is not relabelled as a durable run receipt.
Independent failures produce explicit partial coverage, rather than suppressing
readable evidence or presenting a fabricated success. OpenProject HTML is reduced
to bounded plain text and rendered as text. No backend business writes are added.
The read-only UI remains a product lock, not server authorization.

### Validation and operating limits

Committed OOS tests, owner governance/API/bundle gates, base-aware mutation and
change-record checks and exact API/worker image smoke are required before merge.
Console tests, architecture checks, types and production build are required.
Native pre-landing OpenProject reads verified distinct logical pages, creation
and change details, original actor refs and zero business writes. Browser proof
has passed genuine missing-original Work Design and legacy/modern Refinement
inspection, including the late-packet navigation correction. The separately
labelled synthetic retained-version/zoom case and final commissioned readback
remain required operating checks with zero write attempts or saved-session changes. Final actual-source
readback follows accepted normal commissioning; that later evidence is not
invented as a prerequisite of this source review.

A browser-local artifact never retained cannot be recovered from terminal
receipts. Selected-item collection reads can grow with that item's activity;
logical paging is not a server-side scalability claim. Existing API bounds,
owner timeout and explicit read errors remain. This repair does not add storage
or a new indexing subsystem.

## Decision

`approved` for the exact sources selected in the paired finite decision within
existing local dev-integration. No waiver, new architecture or release authority.
Commissioning must prove actual served revisions, original interfaces, independent
legacy/modern owner reads, creation/edit activity, locked business controls, zero
history writes and unchanged saved sessions. Existing normal Platform rollback
restores the previous OOS/Console selection and paired source acceptance while
preserving ART, receipts, local drafts, accounts and valid durable generation.
