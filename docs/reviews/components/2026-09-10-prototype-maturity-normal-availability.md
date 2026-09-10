# Prototype Maturity Normal-Availability Review

## Summary

- date: 2026-09-10
- owner repo: `security-architecture`
- delivery ref: `openproject://work_packages/1125`
- parent feature: `openproject://work_packages/920`
- parent initiative: `openproject://work_packages/892`
- governing architecture:
  `wgcf://artifacts/delivery-art/sha256/6b923ff94c8c0c2a4abdfbe1767307c1671dbc2be9fad1fe6f9d3664acf371c4`
- reviewed source:
  - Workspace Governance contract:
    `workspace-governance@3a7e73dfdc4d96593f98ad76f4792dc2ea45f349`
  - Workspace Prototype Studio:
    `workspace-prototype-studio@31a73628b0bfd5af1133bc3b633921a18e6e3941`
  - Workspace Governance Control Fabric:
    `workspace-governance-control-fabric@145e5e28c6933d0cd40fc45a0d01401c3e7af9aa`
  - Operator Orchestration Service:
    `operator-orchestration-service@f19d762a3cee52c7ee3185a0ba0014cc661a6177`
  - Governance Operations Console:
    `governance-operations-console@0707d42f7778782ab58027ed98a04dbd2e9ee356`
  - Platform identity definition:
    `platform-engineering@f2b3b5f0f96b13217487250fd16d59dc77496d16`
- immutable evidence:
  - composed conformance Review Packet:
    `wgcf://artifacts/delivery-art/sha256/1267af69967d433caea791dbadc600bef718b8489ddd9ac5778799431d86f01f`
  - identity-definition Review Packet:
    `wgcf://artifacts/delivery-art/sha256/1a1ec22ccd4456db99f67157c084a3c46ce4fb03ed1f4be820afadd60e676c45`
- prior review:
  [`2026-09-09-prototype-maturity-trust-boundary.md`](2026-09-09-prototype-maturity-trust-boundary.md)
- decision: `approved-with-findings`

Prototype Maturity may proceed toward normal operator availability in the
local `dev-integration` lane after the four activation findings in this review
are satisfied in order. The reviewed source and immutable evidence establish
the required contract, source authority, readiness, orchestration, Console,
identity, review, readback, replay, recovery, and audit boundaries.

This decision authorizes the bounded activation work. It does not activate the
workflow, commission a credential, approve a runtime, merge source, admit work
to Delivery, publish a Portfolio entry, or grant stage or production authority.

## Scope Delta

### Design Intent

The prior review accepted an inactive implementation foundation. The reviewed
delta completes that foundation and defines the dedicated machine identity
needed to make Candidate Promotion and Baseline Promotion available without
reusing Prototype Landing authority.

Prototype Maturity remains two local Workspace Prototype Studio transitions:

- Candidate Promotion moves `exploring` to `candidate` after an explicit,
  bounded operator decision.
- Baseline Promotion moves `candidate` to `baseline-approved` after exact
  evidence, boundary, and review checks pass.

Neither transition changes source custody, activates a preview runtime, creates
Delivery work, provisions a repository, publishes a Portfolio entry, or grants
Security or release authority.

### Implemented Control

The reviewed source provides:

- one canonical contract with transition-specific request, packet, readiness,
  decision, readback, and receipt schemas;
- exact Prototype identity, source revision, record digest, authority revision,
  session, execution, correlation, and idempotency binding;
- source-owned Candidate and Baseline mutations limited to the Prototype
  registry, maturity records, design baselines, and immutable history;
- WGCF readiness with current-authority, policy, evidence, expiry, and replay
  checks;
- durable OOS coordination, decision binding, cancellation, interruption
  reconciliation, source-review waiting, readback, and terminal receipts;
- same-origin Console request and projection routes that keep caller
  credentials server-side and reject disconnected success in configured live
  mode; and
- one dedicated, selected-repository GitHub App definition for Prototype
  Maturity with separate branch, path, secret, audit, revocation, and rollback
  boundaries from Prototype Landing.

The WGCF and OOS manifests and Platform identity remain inactive. App and
installation ids are unset, no credential is issued, and no provider or runtime
availability is claimed.

### Operating Evidence

The finalized #1100 Review Packet binds an isolated composed run to exact
Console, WGCF, OOS, and Prototype Studio revisions. Ten scenarios prove blocked
and successful Candidate and Baseline decisions, stale authority, cancellation,
caller isolation, replay conflict, restart recovery, changed review head,
readback mismatch, exact merged history, stable terminal receipts, and unchanged
canonical source outside successful promotions.

The finalized #1128 Review Packet proves the selected but inactive identity,
exact repository and permissions, separate Landing authority, bounded branch
and write paths, secret-safe validation, independent suspension and revocation,
rollback, and exact reviewed Git head. These are sufficient to authorize the
activation sequence, but they are not live commissioning evidence.

## Review Areas

### Identity And Authorization

The dedicated Prototype Maturity identity is appropriate. It is limited to the
immutable `mfshaf7/workspace-prototype-studio` repository and exactly Metadata
read, Contents write, Pull requests write, and Checks read. It cannot merge,
write `main`, bypass provider review, administer repositories, use unrelated
paths, or inherit Prototype Landing authority.

The accountable operator still owns the maturity decision and exact source-head
review. The Console, WGCF, OOS, an advisor, packet content, evidence content,
or the GitHub App cannot authorize merge or completion.

### Secrets And Data

The future private key remains Platform-owned in a dedicated Vault path. OOS
may receive only a short-lived installation token through a read-only Secret
mount and a separate WGCF caller binding. Private keys, tokens, caller secrets,
authorization headers, unrestricted evidence, and source bodies remain outside
browser responses, logs, errors, receipts, ART evidence, and Console
projections.

Operator input, Prototype content, evidence references, and advisor output are
untrusted. Readiness must resolve current authority and enforce bounded values,
references, and evidence rather than trusting their shape or origin.

### Source, Delivery, And Machine Trust

Promotion prepares one deterministic non-default branch and requires exact-head
validation, human review and merge, canonical ancestry, and byte-identical
readback before success. Block, closeout route, cancellation, stale authority,
review denial, or failed readback cannot mutate canonical maturity or fabricate
a successful receipt.

Prototype Studio remains source authority. WGCF cannot mutate source, OOS
cannot merge, Platform cannot decide maturity, and the Console cannot become a
parallel workflow. Source candidates are not live authority, and this workflow
does not perform Delivery intake or environment promotion.

### Runtime, Replay, And Recovery

Runtime activation currently remains false in both WGCF and OOS, and the
Platform identity is selected but inactive. #1129 and #1130 must activate their
existing capabilities independently only after this review. #1131 must then
commission the identity and compose the exact reviewed revisions in one bounded
runtime profile.

Identical retry returns retained state. A changed authority, caller, payload,
review head, policy, evidence set, or idempotency binding fails closed. Restart
and interruption reconcile from durable state, provider truth, and canonical
source. Suspension prevents new work; rollback disables both workflow gates,
revokes token projection, preserves evidence and Git history, and does not
affect Prototype Landing.

### Visibility, Audit, And AI

The operator projection must distinguish acknowledgement, blocked readiness,
decision required, review required, cancellation, stale state, failure,
readback, and terminal success. Receipts expose value-safe identifiers, digests,
source revisions, review and merge references, caller, session, execution,
action, outcome, and recovery references without secret values.

An advisor may explain choices or draft bounded input. It is not identity,
readiness, security, source, merge, custody, or completion authority. Any model
projection of Prototype or evidence content remains subject to the admitted
context-governance path and deterministic output validation.

## Findings And Activation Gates

1. **WGCF activation is pending.** ART `#1129` must pin this merged review and
   the exact identity and conformance revisions, enable only Prototype Maturity
   readiness, and prove unauthorized, stale, expired, tampered, and
   replay-conflicting requests remain denied.
2. **OOS activation is pending.** ART `#1130` must pin this merged review and
   current WGCF implementation, enable only Prototype Maturity orchestration,
   and preserve caller binding, durable restart, cancellation, exact-head
   review, readback, receipt, and Landing-identity separation.
3. **Platform commissioning is pending.** ART `#1131` must start only after
   #1129 and #1130, verify the exact App, installation, repository, permissions,
   provider rules, token lifetime, Vault custody, runtime projection, restart,
   suspension, revocation, and rollback, and retain value-free receipts.
4. **Normal Console operating proof is pending.** ART `#1132` must complete the
   normal Candidate and Baseline path through the configured Console and prove
   blocked, stale, unauthorized, replayed, interrupted, review-denied,
   readback-mismatched, suspended, and revoked paths remain visibly
   non-successful. Fixtures or disconnected local receipts cannot satisfy it.

These are activation conditions, not accepted risk. Prototype Maturity remains
unavailable until all four complete. A failed condition returns to its owning
work item; it must not be bypassed or weakened locally.

## Decision

`approved-with-findings`

Approved:

- the reviewed Candidate and Baseline authority and trust-boundary model;
- bounded activation work for local `dev-integration` under #1129 through
  #1132;
- the dedicated one-repository Prototype Maturity GitHub App definition;
- human-review-only merge with exact-head and canonical-readback proof;
- content-addressed readiness, durable coordination, idempotent recovery,
  value-safe audit, independent suspension, revocation, and rollback; and
- the Console as a same-origin server-mediated operator client.

Not approved:

- claiming normal availability before all four activation findings close;
- partial WGCF, OOS, identity, runtime, or Console activation;
- reuse or expansion of Prototype Landing identity or authority;
- stage or production operation, external exposure, or release authority;
- automatic or machine-authorized merge, direct `main` write, or provider
  bypass;
- browser-held, personal, ambient, shared, broad, or long-lived credentials;
- secret or unrestricted evidence values in source, logs, receipts, ART, or
  Console projections;
- Delivery admission, repository provisioning, runtime activation, source
  graduation, Portfolio publication, or Prototype closeout by a maturity
  transition; or
- model authorization, readiness, security acceptance, merge, or success
  projection.

Security Architecture retains authority over later trust-boundary changes. If
activation cannot preserve this exact boundary, the affected unit must stop and
return for a fresh delta review.
