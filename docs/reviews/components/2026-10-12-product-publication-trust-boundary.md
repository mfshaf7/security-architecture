# Product Publication Trust-Boundary Security Delta

## Summary

- date: 2026-10-12
- owner repo: `security-architecture`
- delivery initiative: `openproject://work_packages/894`
- parent feature: `openproject://work_packages/922`
- security review item: `openproject://work_packages/1257`
- following Platform activation item: `openproject://work_packages/1258`
- decision URI:
  `security-architecture://product-publication/decisions/console-internal-v1`
- governing architecture packet:
  `wgcf://artifacts/delivery-art/sha256/511401baf083e6530a294f364a4a8aedb71601e4d7e70690cb6035f2453d4a22`
- reviewed source:
  - Workspace Governance Product Publication contract:
    `workspace-governance@213b9fed48f8bd0e6e6fd658bfeae38cfd9e3784`
  - Workspace Governance Control Fabric readiness implementation:
    `workspace-governance-control-fabric@d12545242fed839df3bce65ad4dd5d6482e7854a`
  - Operator Orchestration Service corrected workflow:
    `operator-orchestration-service@8d197979f3cf8035f3822ede7b809fd98e274630`
  - Governance Operations Console and committed owner manifest:
    `governance-operations-console@83b0e20786bd6cd531e1043acf96df60ee5a3555`
- owner-manifest binding:
  - source snapshot:
    `governance-operations-console@9ef4e2f370439464afb0284131446d34abf4aa6d`
  - manifest revision:
    `governance-operations-console@83b0e20786bd6cd531e1043acf96df60ee5a3555`
  - manifest path: `product-publication/manifest.json`
  - manifest digest:
    `sha256:86f714e45ff092618558eb5649c9daa496e3f77e27ff3e90eafffc267650102f`
- corrective review evidence:
  - [OOS exact Security decision binding PR #312](https://github.com/mfshaf7/operator-orchestration-service/pull/312)
  - [OOS internal-only target-scope PR #313](https://github.com/mfshaf7/operator-orchestration-service/pull/313)
  - [Console owner-manifest PR #64](https://github.com/mfshaf7/governance-operations-console/pull/64)
- decision: `approved`

The reviewed design keeps product identity, owner evidence, readiness,
workflow mutation, Console projection, Security acceptance, and Platform
activation under separate owners. It is acceptable only for one
single-operator, loopback-only `dev-integration` path that moves the existing
Governance Operations Console record from `unlisted` to `internal` using
synthetic operating evidence.

The initial architecture packet correctly separates owner capabilities and
places this review before Platform activation, but it did not expose the two
embedded source activation gates or the required product-owner manifest as
separate prerequisites. Security inspection also found that the original OOS
implementation accepted only the shape of a Security decision and did not
constrain that decision to the intended target posture. Those implementation
gaps are repaired at the exact revisions above. The remaining OOS and WGCF
`runtime_activation` flags must be changed in their owner repositories after
this decision and before Platform `#1258` may commission the path.

## Scope Delta

### Design Intent

- publish only an already active Workspace Governance product; publication
  must not create product identity, change lifecycle, activate runtime, approve
  a release, or transfer source custody;
- accept one exact product-owner manifest from merged owner-repository truth;
- let WGCF evaluate the exact authority, manifest, lifecycle, target, and
  freshness binding and issue a durable, short-lived readiness receipt;
- let OOS bind the operator decision, Security decision, readiness readback,
  idempotency/version chain, terminal packet, and immutable owner receipt;
- let the Console submit reviewed intent through its same-origin server-only
  adapter and render the exact owner result without receiving private runtime
  credentials; and
- keep source activation, Platform composition, live proof, and any broader
  audience as later, independently controlled decisions.

### Implemented Control

Workspace Governance defines closed schemas and fixed tuples for product-owner
manifests, publication requests, packets, and receipts. The active product
inventory fixes the Console product record, classification, lifecycle, runtime
owner, and source owners. The owner manifest binds source snapshot
`9ef4e2f370439464afb0284131446d34abf4aa6d`, current `unlisted` posture,
dedicated source custody, and loopback local-preview evidence. Its separate
manifest revision and digest allow WGCF to verify committed bytes without a
self-referential commit hash.

WGCF reads Workspace Governance and the owner repository from merged
`origin/main` truth. It verifies exact authority-file digests, product
inventory, owner and source ancestry, committed manifest bytes and digest, all
five lifecycle axes, the requested target tuple, request identity, replay,
version, and timestamps. Only the admitted OOS caller may evaluate readiness;
the actor-scoped read path returns the same durable receipt. The ledger binds
the WGCF service identity and implementation revision and expires readiness
after fifteen minutes.

OOS validates closed schemas, caller-to-operator binding, request and
idempotency identity, exact Security URI/digest/revision, exact WGCF issuer and
implementation, issued-plus-read readiness equality, previous receipt and
version, and all cross-boundary grants. PR #312 changed the Security check from
namespace-shaped input to the exact independently configured decision. PR
#313 made `internal` the only source-approved target posture and rejects
`client`, `public`, `unlisted`, and `archived` targets before WGCF access or
journal mutation. Durable journal locking and canonical digests preserve replay
and conflict behavior.

The Console mutation and read routes require the verified private Platform
session, `Operator` role, `Workspace owner` authority, and the exact configured
operator binding. OOS and Security credentials remain server-only. The Console
validates the command, readiness, packet, receipt, manifest, authority,
revision, timeline, target, version, and digest bindings before projecting
success. Configured failure does not fall back to fixtures, and synthetic
fixture records cannot enter the live path.

### Operating Evidence

The Workspace Governance, WGCF, OOS, and Console source Landing Units passed
their owner validation, exact-head review, protected merge, and source
evidence paths. The corrective OOS revisions passed 1,273 tests, API and
governance-document validation, exact-head CI, human review, and protected
merge. The owner-manifest revision passed the Workspace Governance manifest
validator, Console repository validation, 493 tests, type checking, production
build, dependency audit, exact-head CI, human review, and protected merge.

This is source and review evidence, not live operating proof. OOS and WGCF are
still source-inactive. No Product Publication service, route, credential,
journal, readiness ledger entry, or portfolio mutation has been activated by
this review. Platform `#1258` remains responsible for a fresh synthetic
positive publication, negative authorization and mismatch cases, durable
readback, restart behavior, rollback, and clean teardown against the exact
activated revisions.

## Review Areas

### Identity And Authorization

The browser session principal, Console machine caller, bound operator, OOS
workflow authority, WGCF readiness caller, WGCF service identity, Security
reviewer, Platform activator, and human source reviewer remain distinct. The
browser cannot assert caller credentials, operator identity, Security
acceptance, WGCF issuer identity, source revisions, or trusted correlation.
Neither OOS nor the Console can create product identity or grant runtime,
release, lifecycle, source, or Security authority.

This identity model is acceptable only for the existing local single-operator
lane. Trusted shared human identity is absent, so remote, shared, or multi-user
exposure is not approved.

### Secrets And Data

Console-to-OOS and OOS-to-WGCF caller secrets remain server-side and must be
delivered by Platform through the existing private runtime boundary. Security
decision configuration is integrity metadata, not a credential. No secret may
enter source, browser payloads, owner manifests, packets, receipts, review
evidence, logs, or public repository content.

Platform proof must use synthetic product and operator-safe data only. Real
client data, production exports, raw secrets, and client- or public-visible
content are outside this decision.

### Delivery, Replay, And Evidence Integrity

Every admitted authority uses full Git revisions and exact digests. WGCF must
prove that the manifest revision descends from the owner source snapshot and
that the committed bytes equal the submitted digest. OOS must issue and reread
the same WGCF readiness receipt and reject issuer, implementation, expiry,
manifest, request, target, or ledger drift. Conflicting idempotency reuse and
stale publication versions fail closed.

The Security decision binding is the exact merged bytes of this review. The
runtime decision revision is this review's merge commit and the runtime
decision digest is the SHA-256 digest of this file at that commit. OOS and
Console Platform configuration must carry the same decision URI, digest, and
revision; namespace-shaped or partially matching values are insufficient.

### Runtime, Activation, And Rollback

Both embedded runtime gates are currently false:

- `operator-orchestration-service/contracts/product-publication/manifest.json`;
- `workspace-governance-control-fabric/contracts/product-publication/manifest.json`.

This decision authorizes narrowly scoped owner-repository maintenance that
changes those two Product Publication gates to true after this review merges.
The activation changes must preserve the reviewed contract digests,
internal-only OOS target scope, caller authorization, readiness ledger,
Security binding, and all tests. They must not add routes, callers, target
postures, credentials, network exposure, or deployment state.

Platform `#1258` may compose the path only after both activation changes merge.
It must bind the exact activated OOS and WGCF revisions, this exact Security
decision, owner-manifest revision `83b0e20786bd6cd531e1043acf96df60ee5a3555`,
and manifest digest
`sha256:86f714e45ff092618558eb5649c9daa496e3f77e27ff3e90eafffc267650102f`.
Immediate rollback disables the Console capability, removes runtime
credentials, and stops the dedicated composition. If source-level revocation is
required, reviewed follow-up changes restore the owner gates to false. Neither
rollback path may delete durable receipts or rewrite publication history.

### Visibility And Audit

The Console capability projection distinguishes disconnected, invalid, and
live state without exposing endpoints, credentials, private paths, or operator
identity. OOS owns the terminal publication journal; WGCF owns the readiness
ledger; Platform owns composition and operating-proof receipts. The Console
may render safe references but must not become an audit or authority store.

Platform proof must show exact running revisions, service identities, manifest
revision and digest, Security decision revision and digest, readiness and owner
receipt references, negative-case outcomes, rollback, and teardown. A source
merge or Security approval alone must never display as live success.

### AI

No model selects the product, target posture, identity, manifest, readiness
decision, Security decision, publication action, approval, or activation. No
AI action path is introduced or approved by this review.

## Closed Findings And Residual Constraints

1. **Exact Security acceptance binding: closed.** OOS PR #312 rejects a
   different URI, digest, or revision before WGCF access or journal mutation.
2. **Initial target scope: closed.** OOS PR #313 admits only `internal` and
   rejects every other target posture before side effects.
3. **Product-owner evidence: closed.** Console PR #64 provides a committed
   manifest with an exact earlier source snapshot, lifecycle evidence, and
   digest-verifiable merged revision.
4. **Activation ownership: sequenced.** The original packet omitted the OOS
   and WGCF source-gate Landing Units. They are required as corrective
   owner-repository maintenance after this decision and before Platform
   commissioning; no additional ART child is required.
5. **Operating acceptance remains open.** Source and review evidence do not
   prove the composed runtime. Platform `#1258` owns the live positive,
   negative, restart, rollback, cleanup, and exact-revision evidence.
6. **Expansion remains blocked.** Client, public, archived, shared, remote,
   multi-user, stage, production, real-client-data, and AI-driven operation
   require a new Security delta and any corresponding owner-source changes.

## Decision

`approved`

Security emits `gate:product-publication-controlled-activation` for the two
bounded owner-source activation changes and subsequent Platform commissioning
against exactly:

- `workspace-governance@213b9fed48f8bd0e6e6fd658bfeae38cfd9e3784`;
- `workspace-governance-control-fabric@d12545242fed839df3bce65ad4dd5d6482e7854a`
  before its gate-only activation change;
- `operator-orchestration-service@8d197979f3cf8035f3822ede7b809fd98e274630`
  before its gate-only activation change;
- `governance-operations-console@83b0e20786bd6cd531e1043acf96df60ee5a3555`;
- owner source snapshot
  `governance-operations-console@9ef4e2f370439464afb0284131446d34abf4aa6d`;
- owner manifest digest
  `sha256:86f714e45ff092618558eb5649c9daa496e3f77e27ff3e90eafffc267650102f`;
- target posture `internal`; and
- a single-operator, loopback-only, synthetic-data `dev-integration` lane.

Not approved:

- Platform commissioning while either exact owner source remains inactive;
- any target posture other than `internal`;
- a different or partially matching Security decision URI, digest, or revision;
- stale, malformed, missing, contradictory, unauthorized, expired,
  replay-conflicting, cross-product, or cross-boundary evidence as success;
- direct browser access to OOS or WGCF, or browser-supplied authority fields;
- real client data, remote or public exposure, shared or multi-user operation;
- stage, production, release, or governed public/client publication; or
- treating this decision or a source merge as live operating proof.

Any change to target posture, identity, credential custody, product or manifest
binding, owner repository, authority revision, readiness or journal behavior,
network exposure, environment, data classification, or action authority
requires another Security delta review.

## Related Artifacts

- [Product Publication contract](https://github.com/mfshaf7/workspace-governance/blob/213b9fed48f8bd0e6e6fd658bfeae38cfd9e3784/contracts/product-publication.yaml)
- [WGCF readiness implementation](https://github.com/mfshaf7/workspace-governance-control-fabric/blob/d12545242fed839df3bce65ad4dd5d6482e7854a/packages/control_fabric_core/src/control_fabric_core/product_publication_readiness.py)
- [OOS Product Publication operator surface](https://github.com/mfshaf7/operator-orchestration-service/blob/8d197979f3cf8035f3822ede7b809fd98e274630/docs/operations/product-publication-operator-surface.md)
- [Console Product Publication integration](https://github.com/mfshaf7/governance-operations-console/blob/83b0e20786bd6cd531e1043acf96df60ee5a3555/docs/product/product-publication-live-integration.md)
- [Security delta review process](../security-delta-review-process.md)
- [Security review checklist](../security-review-checklist.md)
