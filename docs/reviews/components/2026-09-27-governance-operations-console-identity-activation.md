# Governance Operations Console Identity Activation Security Delta

## Summary

- date: 2026-09-27
- owner repo: `security-architecture`
- affected review subject: `repos.governance-operations-console`
- delivery initiative: `openproject://work_packages/898`
- security evidence item: `openproject://work_packages/1181`
- parent feature: `openproject://work_packages/928`
- architecture packet:
  `wgcf://artifacts/delivery-art/sha256/b7b8806ba161003ba87d62de5d4851d1ae750bd86789a7fae3f5f0a4174b99cb`
- decision: `approved-with-findings`

This review approves the exact merged Platform and Console source boundary for
bounded, single-operator, loopback `dev-integration` activation. It does not
approve normal availability, shared access, federated identity, stage, or
production use. Configured operating proof remains downstream work.

### Exact Source Binding

| Owner | Pull request | Merged source | Reviewed evidence |
| --- | --- | --- | --- |
| Platform Engineering | [platform-engineering#248](https://github.com/mfshaf7/platform-engineering/pull/248) | [`f4475dbd0129961302ff48aea10b751b6b85512a`](https://github.com/mfshaf7/platform-engineering/commit/f4475dbd0129961302ff48aea10b751b6b85512a) | `products/governance-operations-console/runtime-contract.md`, `session-projection-policy.yaml`, and `runbooks/manage-session-projection.md` |
| Platform Engineering | [platform-engineering#249](https://github.com/mfshaf7/platform-engineering/pull/249) | [`604a91c4237ecc27e589defb31d16a3fe50a7a0a`](https://github.com/mfshaf7/platform-engineering/commit/604a91c4237ecc27e589defb31d16a3fe50a7a0a) | `docs/records/change-records/2026-09-27-governance-console-session-projection.md` |
| Governance Operations Console | [governance-operations-console#33](https://github.com/mfshaf7/governance-operations-console/pull/33) | [`7dbf37cbbfcfc4d7285f3656258eb18286ce86d5`](https://github.com/mfshaf7/governance-operations-console/commit/7dbf37cbbfcfc4d7285f3656258eb18286ce86d5) | `docs/product/surface-contracts/identity-and-authorization.md` and `docs/security-and-data-boundaries.md` |
| Operator Orchestration Service | architecture snapshot | [`c52294332681da3345b3366a37f1cf1f8537c314`](https://github.com/mfshaf7/operator-orchestration-service/commit/c52294332681da3345b3366a37f1cf1f8537c314) | Existing authenticated application-caller and workflow-authorization boundary; no new human-session acceptance is claimed |

The architecture packet defines the owner order. Platform supplies private
session truth, the Console consumes it and enforces mutable routes, OOS keeps
workflow authorization, and Security Architecture approves the combined trust
boundary. A different source revision requires a new delta review.

## Scope Delta

### Design Intent

- Replace browser fixtures and visible profile labels as mutation authority
  with a private Platform-owned session projection.
- Keep authentication/session issuance in Platform and business authorization
  in each OOS workflow owner.
- Make Console mutations fail closed when identity, authority, freshness, or
  configuration is absent or conflicting.
- Carry display-safe operator attribution and a server-generated correlation
  reference toward OOS without exposing projection contents or caller secrets
  to the browser.
- Preserve a bounded local path now without presenting it as federated or
  shared-runtime identity.

### Implemented Control

Platform issues `console-operator-identity/v1` only from an active admitted
local session. Policy fixes the operator, source profile, roles, named
authority, lifetime, and environment. Publication is atomic; the projection
is an operator-owned `0600` regular file. Missing, malformed, stale, expired,
stopped, conflicting, or unadmitted session truth fails closed. Receipts carry
references and hashes rather than projection values.

The Console reads the projection only on the server through
`GOVERNANCE_CONSOLE_SESSION_PROJECTION_PATH`. It rejects relative paths,
symlinks, non-regular files, wrong ownership or mode, oversized input, unknown
schema fields, wrong source authority, non-live or non-current posture,
unordered timestamps, expiry, missing role or named authority, and mismatch
with `GOVERNANCE_CONSOLE_OPERATOR_ID`.

Every canonical Proposal, Delivery, Prototype, Repository, Workspace Intake,
and Workspace Registry POST route enters the shared authorization boundary
before its owner adapter. Accepted requests receive a server-generated UUID.
Only display-safe identity and correlation headers are added by the server;
browser-supplied values cannot override them. Read, preparation, advice, and
local Agent Console routes remain outside this mutation boundary by explicit
classification and architecture guard.

OOS remains the authenticated application-caller and workflow-authorization
owner. This review does not claim that OOS durably consumes every new human
attribution header. A valid Platform projection alone cannot authorize a
domain mutation or replace expected-state, approval, idempotency, readback, or
receipt controls.

### Operating Evidence

Platform source tests cover policy and schema validation, issuance,
inspection, deterministic same-session behavior, conflicting sessions,
expiry, revocation, owner and mode checks, and fail-closed source states.
Console validation covers malformed, stale, expired, conflicting, and missing
projection input; route coverage; browser-header replacement; operator
matching; exception preservation; architecture; semantics; TypeScript;
production build; and dependency audit.

Those results prove source behavior at the exact commits above. They do not
prove a configured Console-to-OOS operating session, durable downstream human
attribution, restart and revocation behavior across the combined runtime, or
normal availability. The ordered downstream activation and operating-proof
items remain required.

## Review Areas

### Identity And Authorization

The boundary is materially stronger than fixture or browser-derived identity.
The Console server independently validates current Platform session truth and
then delegates business authorization to OOS. Role and named-authority claims
come from reviewed Platform policy, not editable Console profile state.

The trust root is still the local operating-system account. An operator who
controls that account remains inside the local `dev-integration` trust
boundary, including the ability to influence files owned by that account.
File custody and source validation prevent accidental or cross-account misuse;
they are not federated identity, MFA, or protection from the admitted local
account itself.

The projection is server-global for the bounded local process rather than
bound to a browser session. The reviewed Console source does not establish a
complete same-origin or anti-CSRF request gate for every mutation. Until that
control and its negative proof exist, activation is restricted to a controlled
single-operator loopback browser. Shared, remote, or multi-user access remains
blocked.

`GOC-SEC-02` is therefore narrowed, not closed globally. Trusted server-side
route enforcement exists for the exact local boundary, while federated login,
browser-session binding, request-origin enforcement, account switching, MFA,
remote revocation, and shared-runtime authorization remain expansion gates.

### Secrets And Data Handling

The projection is identity evidence, not a credential, but it remains private
server-side data. Its configured path and contents must not enter browser
bundles, `NEXT_PUBLIC_*` variables, logs, fixtures, ART descriptions, or Review
Packets. Platform receipts may expose only bounded references and digests.

The OOS caller secret remains a separate server credential. This review does
not authorize moving it into the projection, browser, source, or identity
headers. Revoking the projection must deny Console mutations without changing
or disclosing the OOS machine credential.

### Replay, Expiry, And Failure

Projection expiry and source-issued timestamp ordering are enforced on every
canonical mutation. A new server correlation ID is created per accepted
request. These controls prevent stale session authority and ambiguous request
attribution, but the projection is not a one-time request token. Domain-level
replay, concurrent mutation, expected-state, and idempotency remain OOS and
owner-workflow controls.

Missing configuration, missing authority, stale or expired projection,
operator mismatch, owner-adapter failure, and malformed evidence must remain
denied. No fixture, UI state, advisor result, cached browser value, or
unverified header may turn those outcomes into success.

### Delivery, Rollback, And Availability

The source order is complete: Platform projection contract and evidence landed
before Console enforcement, and this review follows both. Rollback remains
separable:

1. revoke the Platform projection or stop the admitted local session;
2. remove the Console projection-path configuration;
3. disable the bounded Console runtime; and
4. revert the Console or Platform Landing Unit in owner order if source
   rollback is required.

OOS workflow state and owner records are not deleted by identity rollback.
No ingress, shared endpoint, stage, production, or public route is approved.
Normal local availability still requires configured positive and negative
operating evidence after this source review.

### Visibility And Audit

The Console forwards a server-generated correlation ID and display-safe
principal, role, authority, expiry, source, and owner references. This is a
sound attribution seam, not proof of durable audit. Downstream work must show
which fields OOS accepts, persists, returns in receipts, and correlates to the
canonical mutation without allowing browser override.

Console logs, browser state, and UI labels are not audit authority. Platform
issuance and revocation receipts, OOS workflow receipts, and owner readback
must provide the durable operating chain.

### AI

This delta adds no model call, AI decision authority, tool invocation, or
governed-model change. Existing `GOC-SEC-01` and `GOC-SEC-04` remain unchanged
and outside this approval.

## Findings And Activation Gates

1. **Browser request-origin binding is not complete.** The configured runtime
   must remain single-operator and loopback-only. Before shared or normal
   trusted availability, canonical mutation routes must reject absent,
   malformed, or cross-origin request context and retain architecture coverage.
2. **Durable human attribution is not yet proven.** The Console emits bounded
   headers, but downstream operating proof must bind principal, session,
   correlation, approval, command, owner receipt, and readback without treating
   unconsumed headers as audit evidence.
3. **The local operating-system account remains the trust root.** Federated
   authentication, MFA, browser-session issuance, remote revocation, and
   shared-runtime authorization need separate architecture and Security review.
4. **Configured operating evidence is absent.** Activation must prove positive,
   missing, malformed, stale, expired, conflicting, replayed, revoked,
   interrupted, owner-unavailable, and rollback cases through the actual
   configured owner path. Source tests alone do not establish availability.

These findings do not require a new remediation item for this bounded source
approval. They are mandatory conditions on the already ordered activation and
operating-proof work. A failed condition keeps the Console mutation path
inactive or returns it to the owning work item.

## Decision

`approved-with-findings`

Approved:

- the exact source revisions bound above
- the Platform-owned private session projection contract
- Console server-side fail-closed enforcement for canonical mutation routes
- a controlled, single-operator, loopback `dev-integration` activation step
- server-generated request correlation and display-safe attribution forwarding
- independent Platform, Console, OOS, and Security ownership

Not approved:

- normal availability based on source evidence alone
- shared, remote, multi-user, stage, production, or public exposure
- federated identity, MFA, browser-session authority, or remote revocation
- mutation without request-origin protection outside the bounded local posture
- browser, fixture, profile preference, or visible role as authorization truth
- treating forwarded but unconsumed headers as durable audit evidence
- storing projection contents or OOS caller secrets in source or evidence
- bypassing OOS workflow authorization or owner readback

## Related Artifacts

- [Prototype Closure controlled-activation review](2026-09-19-prototype-closure-controlled-activation.md)
- [Governance Console Proposal live-integration review](2026-08-16-governance-operations-console-proposal-live-integration.md)
- [Governance Console source-graduation review](2026-07-31-governance-operations-console-source-graduation.md)
- [Identity and access architecture](../../architecture/domains/identity-and-access.md)
- [Identity and access standard](../../standards/identity-and-access.md)
- [Security delta review process](../security-delta-review-process.md)
- [Security review checklist](../security-review-checklist.md)
