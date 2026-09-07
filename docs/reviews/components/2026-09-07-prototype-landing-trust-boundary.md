# Prototype Landing Trust-Boundary Review

## Summary

- date: 2026-09-07
- owner repo: `security-architecture`
- delivery ref: `openproject://work_packages/1089`
- parent feature: `openproject://work_packages/919`
- parent initiative: `openproject://work_packages/892`
- governing architecture:
  `wgcf://artifacts/delivery-art/sha256/dc7d7c4be8301fcaf881f724fb976bd90aad9d375b152f831bb39d99c0d14270`
- reviewed source:
  - Workspace Governance pull-request head:
    `workspace-governance@eadb6247ddb751dec13a7cf33592f5ed3919c9d6`
  - Workspace Governance merge:
    `workspace-governance@015e5a7bcca98f752f7b4e3e25996f4af868d292`
- source evidence:
  - Workspace Governance Review Packet:
    `wgcf://artifacts/delivery-art/sha256/bb0e582a4741b0de0a7f57550159d76d62dcdc698b57acfb90bf019d254a3dfe`
- decision: `approved-with-findings`

The authoritative Prototype Landing contract is acceptable as an inactive
foundation. It separates contract, source, readiness, workflow, runtime,
security, and operator-projection authority; keeps editable naming separate
from stable identity; distinguishes incubation custody from referenced source
custody; and denies success before reviewed merge and canonical readback.

This decision permits the bounded implementation work already planned under
Feature `#919`. It does not approve normal operator availability, live source
mutation, runtime activation, external exposure, real-data use, or a model as
an authorization or completion authority.

## Scope Delta

### Design Intent

Prototype Landing converts direct, proposal-routed, existing-source, or
imported ingress into one governed Prototype record. The workflow must:

- normalize upstream material into an immutable Entry Packet;
- reserve one stable Prototype identity while allowing the proposed name and
  objective to be corrected before apply;
- resolve support needs without treating a support profile as project type or
  maturity;
- choose exactly one source-custody posture;
- prepare any source mutation on a non-default branch for human review;
- preserve external source authority for reference-only landings; and
- report `landed` only after merged source readback and terminal receipt agree.

Landing does not grant candidate status, baseline approval, Delivery work,
repository-provider custody, runtime activation, security acceptance, or
Portfolio publication.

### Implemented Control

The reviewed Workspace Governance source provides:

- strict contract and artifact schemas for Entry Packet, request, plan,
  readiness, apply, readback, and receipt;
- deterministic Entry and Prototype identity rules;
- explicit support profiles, dimensions, row states, and blocking conditions;
- source-custody mappings for create, update, reference-only, and import;
- exact request, plan, readiness, operator, source-version, correlation, and
  idempotency bindings;
- authority locking, expected-state comparison, non-default-branch mutation,
  source review, merge, and merged-authority readback requirements;
- fail-closed stale, conflict, denial, cancellation, interruption, retry, and
  reconciliation semantics; and
- semantic validation that rejects cross-artifact drift, invalid custody,
  apply-before-readiness, and success-before-merged-readback claims.

### Operating Evidence

The reviewed contract passed 171 Workspace Governance tests, 12 project
lifecycle proof scenarios, repository structure and contract validation, and
11 focused Prototype Landing positive and negative cases.

This is contract, source, and local test evidence only. Prototype source
mutation, WGCF readiness, OOS durable execution, Platform identity, Console
composition, and composed end-to-end operation do not exist yet. Normal
availability therefore remains denied.

## Review Areas

### Identity And Authorization

The stable Prototype identity is correctly independent from editable display
metadata. Every request and later artifact must bind the immutable Entry Packet
and reserved Prototype identity; names, objectives, source labels, profile
choices, and operator suggestions must never substitute for either identity.

Source mutation requires authenticated service-caller context, accountable
operator approval, current readiness, expected registry and source revisions,
and one authority lock. Browser input, proposal content, imported metadata, an
advisor, or a support profile cannot authorize apply, merge, custody transfer,
or completion.

The routine mutation identity must be dedicated and scoped to the exact
Prototype Studio source operation. Personal tokens, ambient `gh` credentials,
browser-held credentials, shared automation identities, and unrelated
repository-provider identities are not approved substitutes.

### Secrets And Untrusted Content

No new secret value is introduced by the contract. Future implementation must
keep credentials and sensitive source values out of Entry Packets, requests,
plans, readiness results, logs, errors, readbacks, receipts, browser responses,
fixtures, and Review Packets. Platform retains secret delivery and revocation
authority.

Imported or externally referenced source is untrusted evidence. Import must
bind origin and imported-content digests, normalize paths, reject traversal and
unsafe links, enforce bounded content limits, and avoid executing imported
hooks or source during inspection. Secret findings, unsupported content, or an
unresolved source owner block apply; they do not silently become `not-needed`.

### Delivery And Source Custody

Workspace Prototype Studio owns the Prototype record and incubation source.
It does not gain authority over referenced dedicated or shared owner source.
Reference-only Landing records an immutable source reference and revision but
performs no copy, write, transfer, branch creation, or provider mutation in the
external repository.

Create, update, and import may prepare Prototype Studio source only on a
non-default branch. Pull-request review, exact-head validation, provider merge,
and digest-matching canonical readback remain distinct gates. Repository
provisioning or existing-repository custody may satisfy a source plan, but
neither action admits a Prototype or transfers source authority by implication.

Stale source, changed custody, identity collision, changed reviewed head,
merge denial, readback mismatch, or receipt failure must remain visibly
non-successful and leave canonical registry state unchanged.

### Runtime, Data, Visibility, Audit, And Recovery

Support-profile selection may prepare a runtime-profile request, but Landing
cannot activate a runtime, issue a credential, expose a route, or assert stage
or production readiness. Runtime, data, integration, visibility, evidence, and
recovery rows must be evaluated from current authority state, not accepted as
truth because an upstream source suggested them.

Every attempt must preserve Entry Packet, request, plan, readiness, approval,
source revision, execution, correlation, idempotency, branch, review, merge,
readback, receipt, and outcome evidence. Exact replay returns prior evidence;
conflicting replay fails. Interrupted mutation requires fresh readback before
retry and cannot claim rollback merely because the workflow stopped.

Rollback disables new Landing execution and runtime projection while retaining
source history and all denied, blocked, failed, replayed, and landed evidence.

### AI And Agentic Influence

An advisor may explain support choices or draft operator input, but a model is
not an identity, policy, readiness, source, merge, custody, security, or
completion authority. Untrusted proposal, import, or source content must not be
projected to a model outside the admitted context-governance path. All mutable
actions remain subject to deterministic validation and explicit human gates.

## Findings And Activation Gates

1. **Prototype source records and mutation are not implemented.** ART `#1086`
   must implement the exact artifact chain, stable identity, custody postures,
   bounded import handling, non-default-branch mutation, canonical readback,
   immutable history, and no-source-mutation failure paths.
2. **Readiness enforcement is not implemented.** ART `#1087` must bind the
   exact contract and this review; resolve authoritative source ownership and
   freshness; evaluate data, exposure, import safety, support blockers, and
   expected mutation scope; and reject stale or unresolved inputs.
3. **Durable workflow enforcement is not implemented.** ART `#1088` must bind
   caller and operator authority, serialize mutation, preserve idempotency,
   reconcile interrupted outcomes, require exact-head review and merged
   readback, and emit value-safe terminal receipts.
4. **The runtime identity is not commissioned.** ART `#1090` must define and
   prove the least-privileged Prototype Landing identity, secret custody,
   destination and repository scope, token rotation, suspension, revocation,
   audit, and rollback without exposing credential values.
5. **The Console composition is absent.** ART `#1091` must keep the browser
   projection-only, prevent client-supplied authority or credentials, preserve
   suggestion-versus-accepted-data cues, expose blockers and exact next action,
   and avoid fixture success in configured live mode.
6. **Composed conformance is absent.** ART `#1092` must prove positive and
   negative direct, proposal-routed, existing-source, and imported paths,
   including identity collision, stale revision, custody mismatch, malicious
   import shape, secret finding, denial, cancellation, replay conflict,
   interruption, changed review head, merge denial, and readback mismatch.

These findings are routed to existing Feature `#919` children. No separate
remediation item is required.

## Decision

`approved-with-findings`

Approved:

- the exact merged Workspace Governance Prototype Landing contract;
- the separation of contract, source, readiness, workflow, runtime, security,
  and Console authority;
- stable identity with editable pre-apply metadata;
- explicit incubation, external-reference, and import custody postures;
- fail-closed readiness, idempotency, recovery, review, readback, and receipt
  requirements; and
- bounded follow-on implementation under ART `#1086`, `#1087`, `#1088`,
  `#1090`, `#1091`, and `#1092`.

Not approved:

- normal Prototype Landing operator availability;
- direct registry or default-branch mutation;
- mutation of referenced external source or implicit custody transfer;
- importing or executing unvalidated external content;
- personal, ambient, shared, browser-held, or long-lived credentials;
- runtime activation, external exposure, real-mutable data, candidate or
  baseline promotion, Delivery creation, or Portfolio publication by Landing;
- model authorization, security acceptance, merge, or success projection; or
- success before exact reviewed merge and canonical readback.

Security Architecture retains normal-availability judgment. This review
permits only the existing bounded implementation and evidence sequence.

## Related Artifacts

- [Security delta review process](../security-delta-review-process.md)
- [Prototype Studio product-incubation baseline](2026-05-06-workspace-prototype-studio-product-incubation-baseline.md)
- [Workspace Intake authority-boundary review](2026-09-06-workspace-intake-authority-boundary.md)
- [Repository custody provider-identity review](2026-08-29-repository-custody-provider-identity-boundary.md)
- [Workspace Governance pull request #178](https://github.com/mfshaf7/workspace-governance/pull/178)
- [Prototype Landing contract](https://github.com/mfshaf7/workspace-governance/blob/015e5a7bcca98f752f7b4e3e25996f4af868d292/contracts/prototype-landing.yaml)
