# Prototype Closure Implementation-Admission Review

## Summary

- date: 2026-09-12
- owner repo: `security-architecture`
- delivery ref: `openproject://work_packages/1106`
- parent feature: `openproject://work_packages/921`
- parent initiative: `openproject://work_packages/892`
- reviewed contract: `workspace-governance@1b7952ba180a3a52a997253e840b769574efd632`, `contracts/prototype-closure.yaml`
- reviewed inactive identity definition: `platform-engineering@2cd3efcccf74a7aacd5071971ff768f52e6eaa40`, `security/prototype-closure-identity.yaml`
- architecture packet: `sha256:0aabf80c5c81a3b349c851761a4181b0798a0d09e4ce97a71d42ea8fabc8295a`
- decision: `approved-with-findings`

The closure contract and inactive, purpose-bound identity definition are
acceptable inputs for bounded implementation. This is an implementation gate,
not an approval to activate Closure or to claim that any future source transfer,
runtime cleanup, or independent review has occurred.

## Scope Delta

### Design Intent

Delivery acceptance advances project phase without graduating Studio source.
Graduation requires an accepted durable custodian and proof of the exact source
transfer or already-owned source. Retirement ends local incubation without
retiring accepted Delivery work or deleting durable source. Reopen returns a
retained retired Prototype to exploration with new history. Portfolio
publication and governed release are separate decisions.

### Implemented Control

Workspace Governance defines four actions, action-specific request, receipt,
and history schemas, a semantic validator, target-route restrictions, receipt
bindings, replay and recovery rules. Platform defines a separate Closure GitHub
App identity limited to the selected Studio repository, closure branches, and
closure-owned paths. That identity is `defined-inactive`: no app installation,
private key, projected token, or enabled workflow exists. The Landing and
Maturity identities are not Closure credentials.

### Operating Evidence

The reviewed contract and identity definition are merged source, not composed
runtime proof. There is no implemented Studio Closure mutation, WGCF Closure
readiness, OOS Closure workflow, Console live projection, commissioned Closure
credential, or cross-owner conformance at this gate. The source PRs were
operator-approved through a delegated Codex session; that is not evidence of
independent human review for any future Closure source mutation.

## Review Areas

### Authority And Custody

Studio alone may write Prototype lifecycle and append-only history. OOS may
coordinate but not unilaterally accept Delivery, select a durable owner, approve
its custody, merge Studio source, or publish to Portfolio. A selected route or
repository request is not a durable-owner acceptance. The owning target must
issue an exact accepted receipt before Studio records the corresponding exit.

Implementations must bind an authenticated caller and accountable operator to
the action, observed lifecycle, exact Studio source revision and record digest,
correlation, idempotency key, and accepted target receipts. Human approval must
cover the exact mutation set and review head. No browser, advisor, fixture,
checklist, or broker acknowledgement may substitute for that authority.

### Source And Receipt Integrity

One authority lock, expected-state comparison, non-default branch, exact-head
owner validation, provider-enforced review and merge, canonical merged readback,
and terminal receipt are required for source-changing outcomes. Receipt and
history digests must bind the prior event, target authority, source revision,
and observed post-merge state. Denied or failed attempts must not project a
completed transition or silently overwrite prior custody.

Identical replay returns the existing terminal outcome; the same key against
changed authority inputs fails closed. Stale source, missing or revoked target
acceptance, changed review head, interrupted merge, receipt failure, or readback
mismatch require reconciliation before any retry. Reconciliation cannot invent
rollback after a merge or success before target and Studio readback agree.

### Data, Runtime, And Revocation

Operator notes, source references, advisor output, and target receipts are
untrusted until resolved against their owners. Implementations must bound
fields and collections, validate reference schemes and exact owner identity,
exclude credentials and unrestricted evidence bodies from packets and logs, and
enforce the Prototype's data and visibility posture. A model may assist with
wording but cannot decide custody, evidence sufficiency, risk, or completion.

Platform alone owns exact active preview-resource cleanup and Closure token
custody. Retirement requires cleanup or absence proof before a completed
retirement receipt. Graduation must not leave active incubation resources
unaccounted for: bind an exact cleanup/disposition outcome to closure before
terminal completion. Reopen must not restore old runtime credentials or erase
retirement history. Suspension and revocation must affect only the exact
Closure identity and active resources, preserving Landing, Maturity, durable
owner source, and canonical audit history.

## Findings And Activation Gates

1. **Owner implementation is absent.** ART `#1102` and `#1103` must implement
   action-specific Studio writes and history with path allowlists, expected
   state, accepted target proof, merge/readback ordering, replay, denial, and
   recovery. No target application may mark source graduated by itself.
2. **Readiness and durable coordination are absent.** ART `#1104` and `#1105`
   must resolve current source, target, identity, policy, and evidence authority;
   bind exact digests; reject stale and malformed requests; serialize mutation;
   reconcile interruption; and fail closed while the Closure identity is
   inactive. A parsed reference is not evidence of target acceptance.
3. **Operator projection and composed proof are absent.** ART `#1108` and
   `#1109` must prove all four actions through authoritative owners, including
   unauthorized, missing-receipt, conflicting replay, stale source, denied
   target, changed review head, merge denial, readback mismatch, cleanup
   failure, cancellation, and restart paths. A fixture or a generated packet
   cannot prove live completion.
4. **The machine identity is inactive.** ART `#1140` must perform the final
   Security review of exact implementation, provider rules, reviewer
   independence, composed conformance, token custody, suspension, and
   revocation. ART `#1107` may commission only after that decision; its
   absence or failure keeps normal availability disabled.
5. **Contract-level fields are intentionally broad.** Source implementations
   must enforce action-specific fields, bounded values, trusted reference
   resolution, and exact owner/path restrictions. If these cannot be enforced
   without changing the shared contract, return the proposed delta for review
   before widening the boundary locally.

These are implementation and activation conditions, not accepted risk.

## Decision

`approved-with-findings`

Approved: bounded, inactive implementation under Feature `#921` using the
reviewed contract and dedicated inactive identity definition.

Not approved: normal operator availability, implicit Landing or Maturity
credential reuse, direct default-branch writes, agent self-approval, automatic
or bypassed merge, custody transfer without durable-owner acceptance, runtime
cleanup without exact Platform proof, source deletion, Portfolio publication,
Delivery completion by Prototype, or success before canonical readback and a
durable terminal receipt.

If implementation cannot preserve these constraints, stop and return for a
fresh Security delta review. Final normal-availability authority remains with
ART `#1140` after the composed proof exists.
