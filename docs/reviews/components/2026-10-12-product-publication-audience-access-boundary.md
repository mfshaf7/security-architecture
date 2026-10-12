# Product Publication Audience And Access Security Delta

## Summary

- date: 2026-10-12
- owner repo: `security-architecture`
- delivery initiative: `openproject://work_packages/894`
- parent feature: `openproject://work_packages/923`
- security review item: `openproject://work_packages/1262`
- following OOS source item: `openproject://work_packages/1263`
- following Platform commissioning item: `openproject://work_packages/1264`
- decision URI:
  `security-architecture://product-publication/decisions/audience-internal-only-v1`
- governing architecture packet:
  `wgcf://artifacts/delivery-art/sha256/f31cf6c0a0d015345a0b286bf334719731e398337941591fb6c6143a2ef238ff`
- reviewed source:
  - Workspace Governance Product Publication contract:
    `workspace-governance@213b9fed48f8bd0e6e6fd658bfeae38cfd9e3784`
  - Workspace Governance Control Fabric readiness implementation:
    `workspace-governance-control-fabric@d12545242fed839df3bce65ad4dd5d6482e7854a`
  - Operator Orchestration Service audience capability:
    `operator-orchestration-service@a5c5fd5a8adc93b79e82d93abced31b65f055cd4`
  - Governance Operations Console audience projection:
    `governance-operations-console@79f95608c71fd4d74244e89324c6c5d45cd416f7`
  - existing internal-only Security decision:
    `security-architecture://product-publication/decisions/console-internal-v1`
- decision: `approved-with-findings`

The exact reviewed source safely supports the already commissioned `internal`
target. It also supports displaying all contract-defined tuples and rejecting
unapproved ones. It does not support widening the active target set.

The approved OOS target set therefore remains exactly `internal`. `unlisted`
remains valid as the owner manifest's current publication evidence and as a
Console-visible tuple, but it is not approved as a target transition. `client`,
`public`, and `archived` remain denied.

This is a bounded Security decision, not a claim that Portfolio grants product
access. It introduces no remote Console exposure, shared identity, ingress,
stage or production deployment, real client data, or product-access grant.

## Scope Delta

### Design Intent

Feature `#923` adds explicit audience, listing-scope, access-class, and posture
handling around the existing Product Publication workflow. Workspace
Governance continues to own the fixed tuples. WGCF continues to evaluate exact
owner-manifest and contract evidence. OOS continues to own the mutation journal
and receipt chain. The Console continues to submit reviewed intent and render
the authoritative result. Security decides which target subset may become
active, and Platform may commission only that subset.

The Console's owner-manifest binding is publication evidence. It is not a
verified access route, access credential, access decision, or product-access
grant. The product owner remains responsible for any actual product endpoint,
identity, authorization, and access enforcement.

### Implemented Control

OOS capability source recognizes the five closed contract tuples and validates
their fixed posture, listing scope, audience, and access class. It validates
action transitions before WGCF access or journal mutation. Its active source
manifest still allows only `internal` even though capability support exists for
the broader contract vocabulary.

The Console renders the exact current and target tuple and the exact
owner-manifest binding returned through the server-only OOS path. It rejects
altered target or manifest evidence during persisted-receipt reconciliation,
does not fall back to fixtures after live configuration begins, and keeps
`archived` outside the audience action. The Console remains private and
loopback-only.

The owner manifest currently records publication posture `unlisted`. WGCF
requires a request's current publication posture to equal that committed owner
lifecycle evidence. After an `unlisted` to `internal` publication, no reviewed
Feature `#923` owner step updates the manifest to `internal`. Consequently an
`internal` to `unlisted` target request would fail the WGCF current-posture
check. Security must not approve that transition as operable evidence.

### Operating Evidence

The OOS audience capability merged through PR
[#316](https://github.com/mfshaf7/operator-orchestration-service/pull/316)
after owner validation and exact-head review. The Console audience projection
merged through PR
[#66](https://github.com/mfshaf7/governance-operations-console/pull/66)
after focused tests, the full 497-test suite, type checking, production build,
repository validation, dependency audit, exact-head CI, and human review.

That is source evidence, not new operating proof. The prior Platform decision
still proves the existing internal-only composition. Platform `#1264` must
bind this review and the exact OOS activation revision, re-prove `internal`,
prove that every other target is denied before mutation, and prove replay,
restart, rollback, restoration, and final readback. No broader target may be
represented as commissioned.

## Review Areas

### Target Decision Matrix

| Posture | Security treatment | Reason |
| --- | --- | --- |
| `internal` | approved target | Existing exact-revision Security and Platform proof supports the private, workspace-authenticated, loopback-only path. |
| `unlisted` | evidence/display only; denied target | The committed owner manifest records it as current posture, but the reviewed workflow cannot durably establish `internal` as the later owner-manifest current state required for unpublish. |
| `client` | denied target | Owner-manifest evidence does not prove a product-specific client endpoint, client identity, authorization policy, or access approval. |
| `public` | denied target | The active Console product contract is explicitly not public/client-visible readiness and no public product endpoint or exposure review exists. |
| `archived` | denied target | Archive requires retired lifecycle evidence and belongs to deferred Feature `#924`, not the audience slice. |

### Identity And Authorization

The browser session principal, Console machine caller, configured operator,
OOS workflow authority, WGCF readiness caller, WGCF service identity, Security
reviewer, Platform activator, product owner, and human source reviewer remain
distinct. The Console cannot assert product access, Security approval, source
revisions, caller credentials, or WGCF identity from browser input.

The current model is acceptable only for the existing single-operator,
loopback-only `dev-integration` lane. Client, public, shared, remote, or
multi-user use would require product-specific identity and access evidence and
a fresh Security decision.

### Secrets And Data

Console-to-OOS and OOS-to-WGCF credentials remain server-side. Security
decision metadata is integrity evidence, not a credential. No secret may enter
owner manifests, browser payloads, packets, receipts, logs, review evidence, or
public repository content.

Commissioning must use synthetic operator-safe data. Real client data,
production exports, raw secrets, and client- or public-visible content remain
outside this decision.

### Delivery And Evidence Integrity

Every active authority must bind full Git revisions and exact digests. OOS must
continue to reject an unapproved target before WGCF access or journal mutation,
bind the issued and reread WGCF receipt, and preserve version, idempotency,
replay, and prior-receipt integrity. Console success must bind the exact OOS,
WGCF, owner-manifest, request, target, packet, and receipt evidence.

The governing architecture packet uses `owner-route` in three descriptive
fields. For this review and all downstream work, that phrase is constrained to
mean the exact owner-manifest evidence binding implemented by the Console. It
must not be interpreted as proof of an endpoint, access path, access decision,
or access grant. A corrected superseding packet must replace those stale terms
after this active work session closes and before `#1263` starts.

The positive real-Git conformance case is satisfied when this review binds the
exact merged OOS and Console revisions, records the exact approved target set,
and gives downstream activation and rollback conditions. The negative case is
satisfied by explicitly denying stale, contradictory, unauthorized,
replay-conflicting, cross-boundary, and unapproved target evidence without a
success claim.

### Runtime, Activation, And Rollback

OOS `#1263` may update the source manifest to bind this exact Security decision
and the current work-item sequence. It must keep
`allowed_target_postures` exactly `["internal"]`; capability support for other
tuples must remain inactive. Tests must prove that `unlisted`, `client`,
`public`, and `archived` are rejected before WGCF access or journal mutation.

Platform `#1264` may commission only the exact internal target. It must prove:

- the exact source and Security revisions are running;
- `unlisted` current owner evidence can publish to the fixed `internal` tuple;
- `unlisted`, `client`, `public`, and `archived` targets are denied;
- stale, contradictory, unauthorized, and replay-conflicting requests fail
  without false success;
- restart preserves durable history; and
- rollback, restoration, and final readback return the composition to the
  reviewed internal-only state.

Immediate rollback removes the `#1263` Security binding or restores its prior
manifest bytes and disables the corresponding Platform composition. Durable
readiness and publication history must not be deleted or rewritten.

### Visibility And Audit

The Console may display safe audience and owner-manifest references but does
not become an audit or authority store. OOS owns the terminal publication
journal, WGCF owns readiness, Security owns the target decision, and Platform
owns composition and operating-proof evidence. Source merge or Security review
alone must never display as live success.

### AI

No model selects the product, target posture, owner manifest, identity,
readiness result, Security decision, publication action, approval, or runtime
activation. No AI action path is introduced or approved by this review.

## Findings And Residual Constraints

1. **Owner evidence terminology: constrained.** `owner-route` in the current
   architecture packet means owner-manifest evidence only. The stale packet
   wording must be superseded before the next source work session.
2. **Unpublish target: not approved.** The static owner manifest cannot prove
   the post-publication `internal` current state that WGCF requires. This
   Feature may display `unlisted`; it may not activate it as a target.
3. **Client and public targets: not approved.** Neither exact product-access
   authority nor product-specific endpoint and identity evidence exists.
4. **Archive target: not approved.** Retired lifecycle evidence and Feature
   `#924` are prerequisites.
5. **Operating acceptance remains open.** Platform `#1264` owns the exact
   internal positive case and every required negative, replay, restart,
   rollback, restoration, and readback case.
6. **No new access authority.** Fixed publication metadata does not authorize
   access to the product or exposure of the Console.

## Decision

`approved-with-findings`

Security emits `gate:product-publication-audience-activation` only for the
existing `internal` target against exactly:

- `workspace-governance@213b9fed48f8bd0e6e6fd658bfeae38cfd9e3784`;
- `workspace-governance-control-fabric@d12545242fed839df3bce65ad4dd5d6482e7854a`;
- `operator-orchestration-service@a5c5fd5a8adc93b79e82d93abced31b65f055cd4`;
- `governance-operations-console@79f95608c71fd4d74244e89324c6c5d45cd416f7`;
- owner-manifest revision
  `governance-operations-console@83b0e20786bd6cd531e1043acf96df60ee5a3555`;
- owner-manifest digest
  `sha256:86f714e45ff092618558eb5649c9daa496e3f77e27ff3e90eafffc267650102f`;
- approved target set `["internal"]`; and
- a single-operator, loopback-only, synthetic-data `dev-integration` lane.

Not approved:

- widening OOS `allowed_target_postures` beyond `internal`;
- treating `unlisted` as an approved target transition;
- `client`, `public`, or `archived` targets;
- treating owner-manifest evidence as an endpoint or access grant;
- remote or shared Console exposure;
- stage, production, or real-client-data operation; or
- any source or runtime claim not bound to the exact reviewed revisions and
  final decision digest.
