# Prototype Maturity Trust-Boundary Review

## Summary

- date: 2026-09-09
- owner repo: `security-architecture`
- delivery ref: `openproject://work_packages/1098`
- parent feature: `openproject://work_packages/920`
- parent initiative: `openproject://work_packages/892`
- governing architecture:
  `wgcf://artifacts/delivery-art/sha256/0ed37ee4c3dded47580518148eac4844c40b98d05e44c01aad4613604ad096dd`
- reviewed source:
  - Workspace Governance pull-request head:
    `workspace-governance@06a6afef6f705d1edc11d9e0c1e7204e80c01e7a`
  - Workspace Governance merge:
    `workspace-governance@3a7e73dfdc4d96593f98ad76f4792dc2ea45f349`
- source evidence:
  - Workspace Governance Review Packet:
    `wgcf://artifacts/delivery-art/sha256/417dfbf5186024653f16571c837193fd643f99f50e636b363ceeaccf634db922`
- prior reviews:
  - `docs/reviews/components/2026-05-06-workspace-prototype-studio-product-incubation-baseline.md`
  - `docs/reviews/components/2026-09-07-prototype-landing-trust-boundary.md`
  - `docs/reviews/components/2026-09-08-prototype-landing-normal-availability.md`
- decision: `approved-with-findings`

The authoritative Prototype maturity contract is acceptable as an inactive
implementation foundation. It separates Candidate Promotion from Baseline
Promotion, binds both to current Prototype Studio source truth, requires an
explicit operator decision, and denies cross-domain authority and success
before human-reviewed merge and canonical readback.

This decision permits the bounded implementation sequence under Feature
`#920`. It does not approve normal operator availability, a Prototype maturity
machine identity, live source mutation, automatic merge, Delivery admission,
runtime or release authority, source graduation, or Portfolio publication.
Final normal-availability judgment remains with ART `#1125` after composed
conformance evidence exists.

## Scope Delta

### Design Intent

Prototype maturity adds two local lifecycle transitions after Landing:

- Candidate Promotion moves an `exploring` Prototype to `candidate` after a
  bounded operator interview establishes objective, target user, expected
  proof, scope, boundaries, triggers, and owned issue disposition.
- Baseline Promotion moves a `candidate` Prototype to `baseline-approved`
  after existing design, workflow, state, review, boundary, and applicable
  executable evidence is assembled and accepted.

Neither transition changes project phase, source custody, runtime environment,
release posture, publication posture, security acceptance, or Delivery state.
A promotion prepares one reviewable non-default-branch source change. The
transition becomes true only after exact merged-source readback and a terminal
receipt agree.

Blocking a visible issue requires an issue reference, owner, and required fix.
Routing to closeout preserves maturity and delegates retirement to its separate
workflow. Leaving without a decision creates no no-op decision or receipt.

### Implemented Control

The reviewed Workspace Governance source provides:

- one product-neutral contract for Candidate and Baseline Promotion;
- strict schemas for request, packet, readiness, decision, readback, and
  receipt artifacts;
- immutable Prototype identity, source revision, record digest, correlation,
  idempotency, and cross-artifact digest bindings;
- exact lifecycle pairs and packet sections for both transitions;
- readiness checks for request and packet integrity, source lifecycle and
  freshness, evidence, boundaries, security triggers, and open issues;
- explicit block and closeout semantics that preserve current source maturity;
- non-default-branch mutation, authority locking, expected-state comparison,
  human review, merge, and merged-authority readback requirements;
- fail-closed replay conflict, stale-state retry, interruption reconciliation,
  rollback, and retained history rules; and
- semantic validation that rejects incomplete packets, non-ready promotion,
  invalid artifact bindings, and success without target-state readback.

### Operating Evidence

Workspace Governance pull request `#181` merged the reviewed contract after its
CI validation passed. The Review Packet records eight focused Prototype
maturity tests, all 180 Workspace Governance tests, repository and contract
validation, project lifecycle proof, stale-content audit, and source-causality
checks against the exact reviewed head.

This is contract, source, and local test evidence only. Prototype Studio
mutation, WGCF readiness, OOS workflow execution, a purpose-bound maturity
machine identity, Console composition, and cross-owner conformance do not exist
yet. No normal operating availability is established by this evidence.

## Review Areas

### Identity And Authorization

The stable Prototype identity and current source state are appropriate
authorization inputs, but neither authorizes a transition. Apply requires an
authenticated service caller, one accountable operator decision, current WGCF
readiness, the exact expected source revision and record digest, and the exact
reviewed source head.

The browser, Workspace Governance, WGCF, an advisor, packet content, evidence
content, or checklist completion cannot approve, merge, or complete a maturity
transition. Security Architecture reviews the boundary but does not operate the
workflow or hold source credentials.

The existing Prototype Landing GitHub App is purpose-bound to Landing branch
and path rules. Its repository scope and provider permissions do not authorize
Prototype maturity by implication. A maturity implementation may be built
inactive, but normal availability requires a Platform-owned, separately
reviewed identity definition or an explicit reviewed extension that names the
maturity branch pattern, exact write paths, caller, token custody, suspension,
revocation, and rollback behavior.

### Evidence, Secrets, And Untrusted Content

Operator-entered editable values, evidence references, Prototype source, and
advisor suggestions are untrusted inputs. Future implementations must accept
only fields named by the selected transition profile, impose bounded value and
collection sizes, normalize references, and reject unsupported schemes,
unsafe paths, and ambiguous source ownership.

Credentials, secret values, raw source, private logs, client-identifying data,
and unrestricted evidence bodies must remain outside requests, packets,
readiness findings, decisions, readbacks, receipts, browser responses, and ART
evidence. Evidence references are not proof merely because they are
well-formed; readiness must resolve them through the owning authority and apply
the Prototype data, visibility, and security-trigger rules.

Any model projection of Prototype or evidence content remains subject to the
admitted context-governance path. A model may summarize or suggest but cannot
classify evidence as sufficient, disposition risk, authorize apply, or claim
completion.

### Source Mutation And Custody

Workspace Prototype Studio remains the only maturity source authority. The
source implementation must restrict a promotion to the exact registry,
Candidate or Baseline record, and immutable Prototype history paths required
by that transition. It must not mutate referenced external source, project
phase, source custody, repository-provider state, Delivery ART, Platform
runtime, security acceptance, or Portfolio publication.

Promotions require a non-default branch, deterministic expected mutation set,
one authority lock, exact-head owner validation, human review and merge, and
digest-matching canonical readback. Block and route-closeout outcomes must not
create a source branch or write canonical source merely because the decision
schema carries source coordination metadata.

Changed source, changed reviewed head, lifecycle mismatch, identity collision,
merge denial, readback mismatch, or receipt failure remains visibly
non-successful. A workflow interruption cannot be treated as rollback or
success without current provider and canonical-source reconciliation.

### Readiness, Replay, And Recovery

WGCF readiness must bind the exact contract revision, this Security decision,
request and packet digests, current Prototype source revision and record digest,
policy inputs, and evidence authority used for evaluation. A policy, Security
decision, source, packet, or evidence change invalidates earlier readiness even
when the operator-facing values appear unchanged.

Promotion is denied unless every required check is ready for the exact current
state. A blocked result names one owner and actionable fix. A stale result
returns to editable workflow state and requires fresh readiness. Identical
idempotent replay returns the existing durable outcome; reuse against different
authority digests fails closed.

Cancellation, retry, restart, source-review wait, merge denial, receipt write
failure, and rollback must preserve one auditable chronology without duplicate
source mutation or a false terminal state.

### Visibility And Audit

Every attempt must retain value-safe references for request, packet, readiness,
operator decision, source base, branch, review head, merge, readback,
correlation, idempotency, recovery, and terminal outcome. Audit records expose
identifiers, digests, states, and exact next action, not secret or unrestricted
evidence values.

The Governance Operations Console remains a same-origin projection and command
adapter. It must show backend-derived lifecycle, blockers, review waits,
readback, receipts, history, and recovery. Fixture completion or browser-local
state cannot satisfy configured live mode.

## Findings And Activation Gates

1. **Candidate and Baseline source transitions are absent.** ART `#1094` and
   `#1095` must implement exact transition-specific fields and path allowlists,
   non-default branches, one authority lock, expected-state comparison, human
   review, canonical readback, immutable history, and unchanged-source block,
   closeout, stale, conflict, and failure paths.
2. **Readiness enforcement is absent.** ART `#1096` must bind the exact merged
   contract and this review; resolve current Prototype, evidence, policy, and
   security-trigger authority; reject unbounded or unsafe values and
   references; and invalidate stale source, evidence, policy, or review state.
3. **Durable orchestration is absent.** ART `#1097` must bind caller and
   operator authority, exact current readiness, expected source head, review
   result, correlation, and idempotency; serialize mutation; reconcile restart
   and interruption; prevent source writes for non-promotion outcomes; and fail
   closed when a purpose-bound maturity source identity is unavailable.
4. **A Prototype maturity machine identity is not approved.** The existing
   Landing identity cannot be broadened implicitly. Source and orchestration
   implementations may land inactive, but ART `#1125` cannot approve normal
   availability until a Platform-owned identity definition or explicit
   reviewed extension proves exact repository, branch, path, permission,
   secret-delivery, rotation, suspension, revocation, audit, and rollback
   boundaries.
5. **The Console composition is absent.** ART `#1099` must keep credentials and
   authority server-side; distinguish suggestions, accepted values, readiness,
   decisions, source review, readback, and receipts; expose the exact blocker
   and next action; and deny fixture success in configured live mode.
6. **Composed conformance is absent.** ART `#1100` must prove both transitions
   through the Console and authoritative owners, including unauthorized and
   malformed input, missing evidence, stale source or policy, blocking issue,
   closeout routing, replay conflict, interruption, changed review head, merge
   denial, readback mismatch, receipt failure, cancellation, and rollback.
7. **Final normal availability remains unreviewed.** ART `#1125` must bind the
   exact merged revisions, maturity identity and runtime boundary, and `#1100`
   evidence before any routine operator availability is approved.

These findings are routed to existing Feature `#920` work and its final
Security gate. They are implementation and activation conditions, not accepted
risk.

## Decision

`approved-with-findings`

Approved:

- the exact merged Workspace Governance Prototype maturity contract as an
  inactive implementation foundation;
- separate Candidate and Baseline Promotion transitions with explicit
  operator decisions;
- digest-bound readiness, expected-state comparison, idempotent replay,
  non-default-branch review, merged-source readback, and terminal receipts;
- unchanged maturity for block and closeout routing outcomes;
- strict separation from Delivery admission, source custody, runtime, release,
  security acceptance, and Portfolio publication; and
- bounded implementation under ART `#1094`, `#1095`, `#1096`, `#1097`,
  `#1099`, and `#1100` subject to the findings above.

Not approved:

- normal Prototype maturity operator availability before ART `#1125`;
- implicit reuse or broadening of the Prototype Landing machine identity;
- personal, ambient, shared, browser-held, broad, or long-lived credentials;
- direct default-branch writes, automatic merge, provider bypass, force push,
  or mutation outside exact maturity-owned paths;
- source writes for block, route-closeout, stale, denied, cancelled, or failed
  outcomes;
- unbounded, unclassified, secret-bearing, or authority-free evidence;
- Console, WGCF, OOS, model, or checklist ownership of the maturity decision;
- Delivery admission, ART creation, source graduation, runtime activation,
  release approval, client exposure, or Portfolio publication by maturity; or
- success before exact human-reviewed merge, canonical readback, and durable
  terminal receipt.

Security Architecture retains final normal-availability judgment. Any
implementation that cannot preserve this boundary must stop and return for a
fresh delta review rather than weakening a gate locally.

## Related Artifacts

- [Security delta review process](../security-delta-review-process.md)
- [Prototype Studio product-incubation baseline](2026-05-06-workspace-prototype-studio-product-incubation-baseline.md)
- [Prototype Landing trust-boundary review](2026-09-07-prototype-landing-trust-boundary.md)
- [Prototype Landing normal-availability review](2026-09-08-prototype-landing-normal-availability.md)
- [Workspace Governance pull request #181](https://github.com/mfshaf7/workspace-governance/pull/181)
- [Prototype maturity contract](https://github.com/mfshaf7/workspace-governance/blob/3a7e73dfdc4d96593f98ad76f4792dc2ea45f349/contracts/prototype-maturity.yaml)
