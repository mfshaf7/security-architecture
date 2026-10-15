# Repository Custody Controlled-Activation Security Delta

## Summary

- date: 2026-10-15
- owner repo: `security-architecture`
- delivery initiative: `openproject://work_packages/1275`
- security acceptance item: `openproject://work_packages/1302`
- governing architecture packet:
  `wgcf://artifacts/delivery-art/sha256/8ad9c43664bb580a2eef7a23a8ddfa77c95bdea7bfc00efcb424d5008b71062a`
- activation gate: `gate:repository-custody-runtime-activation`
- reviewed source:
  - Workspace Governance authority:
    `workspace-governance@ec499fcbdd7d62687d704b9f9e50c87a601c48ee`
  - Workspace Governance Control Fabric readiness runtime:
    `workspace-governance-control-fabric@981aa6259b2dcc65d41dc739bddadbb395794973`
  - Operator Orchestration Service activation baseline:
    `operator-orchestration-service@c87d1fa7a242c495fae7c942b1437af78acfc094`
  - Platform Engineering identity baseline:
    `platform-engineering@068c6078755ec8a3df73e65f67131eb3e4cf07fa`
  - Governance Operations Console baseline:
    `governance-operations-console@9ae2edf5d5a4121ca198172225c65984494a3b72`
- prior activation work:
  - existing-repository identity: `openproject://work_packages/1044`
  - existing-repository Console composition: `openproject://work_packages/1045`
  - provisioning identity: `openproject://work_packages/1048`
  - provisioning Console composition: `openproject://work_packages/1049`
- decision: `approved-with-findings`

Security accepts one bounded OOS source change that advances the existing
repository-custody manifest from `contract-only` to active for local
`dev-integration`. The accepted change may refresh the pinned Workspace
Governance authority and bind this review, but it may not add an action,
provider, destination, permission, credential path, caller, or downstream
admission effect.

This decision is source-activation authority, not current operating proof.
The previously completed identity and Console work demonstrates that the
boundary was implemented, but GitHub installation tokens and runtime Secret
projections are intentionally short-lived. Platform work item `#1291` must
therefore commission fresh dedicated credentials, deploy the exact reviewed
owners, and prove the complete positive and negative Console journey before
repository custody can be called operating-ready.

## Scope Delta

### 2026-10-16 Retained-Request Readback Maintenance

Maintenance Landing Unit `maintenance-1275-repository-readback-security` uses
`child_isolated_landing_unit`: Security review and rollback are independent of
the two owner implementation landings. This is maintenance of the existing
acceptance path, not another ART child or provider action.

Security accepts the bounded readback delta at these exact candidate heads:

- `operator-orchestration-service@dbe33dad90f3a11e5516478d81a0513061a6bd6f`
  ([OOS PR #344](https://github.com/mfshaf7/operator-orchestration-service/pull/344));
- `governance-operations-console@926a6c87256efd0b9d8932094373fbb4fbde58b1`.

Design intent is to recover retained custody requests after a browser reload,
not create a Console-owned register or infer admission from provisioning.
OOS exposes a paginated read of the same records already available by request
identity. It requires the existing caller-bound credential, admits only a
SHA-256 cursor and a page limit of 1–25, validates stored request identities
and artifact integrity, and performs no provider action. A corrupt record
fails the read instead of silently omitting evidence.

Console reads this collection only through its server-held OOS identity and
validates the canonical source envelope, request digest, bounded page shape,
and each existing workflow result. The browser receives only the established
safe result projection. Register recovery is capped at ten pages; duplicate
request identities, repeated cursors, malformed data, or unavailable owner
truth fail closed. Polling is bounded to visible pages. An authoritative
refresh replaces the previous snapshot, and an older in-flight refresh cannot
overwrite a subsequently completed command result. Loading and unavailable
states do not select fixtures or claim current owner availability.

Provider custody and provisioning receipts remain distinct from Workspace
Intake, inventory, Catalog, and product lifecycle decisions. No action,
permission, credential, caller, provider destination, mutation authority, or
network exposure is added. Existing-link and provisioning still use separate
Platform-held GitHub App identities. The read surface is accepted only inside
the existing single-operator, loopback `dev-integration` boundary.

Implemented-source evidence includes OOS focused store reconstruction,
pagination, corruption, authentication, and no-provider-effect cases; full
owner tests and API-contract validation; and Console canonical-envelope,
cold-read, linked-record reconstruction, malformed-pagination, and unavailable
readback cases, architecture guards, semantic tests, type checking, and build.
Exact-head owner CI and human approval remain required before merge. This
review is not live operating evidence.

The decision remains `approved-with-findings`: it permits only these bounded
owner source landings. The machine-readable composed Platform decision is
unchanged by this maintenance review. The final merged OOS and Console
revisions and the pending Platform composition repair require a fresh exact
composition decision before activation. Existing final journey work must
prove browser reload recovery, provider identity/readback, credential failure,
restart, and restoration without fixture or CLI substitution. Rollback removes
the collection adapter and restores the previous read behavior while retaining
owner records; it does not delete repositories or evidence. Security judgment
and delegated human approval remain with the primary operator agent, not the
implementation identity.

### Design Intent

- let the Console invoke the already implemented `link-existing` and
  `provision-new` custody actions only through authenticated OOS;
- keep policy in Workspace Governance, readiness in WGCF, orchestration and
  terminal evidence in OOS, provider identity custody in Platform, and final
  operator projection in the Console;
- preserve separate least-privilege GitHub App identities for read-only
  existing-repository lookup and organization repository creation;
- make missing, expired, revoked, mismatched, or stale identity and policy
  evidence a visible denial, never a fixture or ambient-credential fallback;
  and
- leave Workspace Intake, active inventory, Delivery Catalog, product
  admission, release, archive, transfer, and deletion outside this action.

### Implemented Control

The reviewed OOS baseline already provides exact request and idempotency
binding, WGCF decision reread, caller authentication, action-specific
credentials, GitHub destination pinning, redirect denial, bounded responses,
immutable numeric repository identity, create-at-most-once provisioning,
uncertain-outcome recovery, separate settings readback, terminal receipts, and
fail-closed behavior when runtime activation or credentials are absent.

The Platform baseline already provides separate identity contracts and
operator commands for the read-only and provisioning GitHub Apps. Private keys
remain in distinct Vault paths. Runtime receives only short-lived installation
tokens through distinct Kubernetes Secrets. Commission, delivery, rotation,
revocation, permission, installation-owner, repository-scope, organization,
destination, expiry, and secret-free receipt checks are implemented.

The reviewed Workspace Governance authority now records dated operating truth
instead of treating source presence as current live availability. That control
prevents this activation decision from being misreported as a functioning
Console path before Platform produces fresh operating evidence.

### Current Evidence

ART `#1044`, `#1045`, `#1048`, and `#1049` are complete with valid completion
narratives. They close the findings routed by the 2026-08-29 custody and
provisioning reviews as implementation history; they do not make expired
runtime credentials current.

At the exact OOS baseline, 30 focused repository-custody tests pass. They cover
contract and OpenAPI integrity, activation denial, caller and credential
denial, provider destination and redirect containment, existing-repository
readback, provisioning, replay, stale authorization, provider mismatch,
readback mismatch, changed-intent conflict, and uncertain-outcome recovery.

At the exact Platform baseline, 21 focused identity tests pass. They cover both
identity contracts, exact permissions, application and installation ownership,
repository and organization scope, local-cluster delivery, token expiry,
value-free credential binding, redirect denial, revocation, and runtime Secret
projection. The source contracts still declare normal activation false, which
is correct before the OOS activation Landing Unit and Platform commissioning
run in their required order.

## Security Boundary

### Identity And Authorization

The existing-repository action uses a dedicated selected-repository GitHub App
with repository `Metadata: read` only. Provisioning uses a separate
organization installation with repository `Administration: write`,
`Contents: read`, and implicit `Metadata: read`. Personal, operator, ambient
`gh`, OAuth-user, shared automation, deploy-key, browser-held, and long-lived
credentials remain denied.

The Console carries accountable operator intent but no provider credential or
provider authority. OOS binds the authenticated caller, operator approval,
request, decision, action, target, credential reference, correlation, and
idempotency identity. Platform alone mints and projects installation tokens.

### Secrets, Provider Trust, And Disclosure

Private keys remain in Platform Vault custody and may not enter source,
browser state, command arguments, logs, errors, requests, decisions, readbacks,
receipts, Review Packets, or ART text. Installation tokens are short-lived,
server-only runtime material and use different Secret projections for read and
provision actions.

Normal provider traffic remains pinned to `https://api.github.com`; explicit
loopback HTTP remains sandbox-only. Redirects cannot forward credentials.
Provider responses remain size-bounded and schema-validated, and downstream
error bodies cannot become Console or durable workflow truth.

### Replay, Recovery, Rollback, And Audit

Existing-link success requires immutable provider identity readback.
Provisioning persists intent before mutation, creates at most once, reconciles
an uncertain result before any retry, and proves the provider id and exact
settings through separate readback. Neither action can infer success from an
accepted request, HTTP create response, workflow state, or Console projection.

Rollback disables the OOS source activation or removes the Platform runtime
projections, revokes issued tokens, and retains request, decision, readback,
receipt, denial, audit, and source history. It does not delete, transfer,
archive, admit, or release a repository.

## Findings And Activation Conditions

1. **Fresh runtime identity is still required.** Platform `#1291` must
   commission and deliver currently valid tokens from the two dedicated GitHub
   App identities. Historic tokens or an unrelated read-only App cannot be
   reused.
2. **Source activation must land before commissioning.** OOS `#1288` may make
   only the bounded manifest and authority-pin change accepted here, with
   focused and full owner validation, exact-head human review, protected
   merge, and finalized Review Packet evidence.
3. **Configured failure cannot fall back.** Missing credentials, missing live
   owner routes, stale WGCF decisions, provider mismatch, unavailable
   dependencies, or Console fixture state must remain visible non-success.
4. **Operating readiness remains downstream evidence.** Platform `#1291`,
   composed Security acceptance `#1303`, and the fixture-free Console journey
   `#1298` must prove provider permission, delivery, denial, revocation,
   restart, rollback, canonical readback, and normal restoration.
5. **The authority set is closed.** A new action, permission, provider,
   identity, destination, credential path, caller, remote exposure, or
   downstream mutation requires fresh Security review.

These conditions are already assigned to existing Epic `#1275` children. They
do not require a new defect, story, control plane, or credential mechanism.

## Decision

`approved-with-findings`

Approved:

- `gate:repository-custody-runtime-activation` for the bounded OOS `#1288`
  source-activation Landing Unit;
- reuse of the implemented repository-custody and provisioning workflows and
  the two existing Platform identity mechanisms;
- a refresh of the exact Workspace Governance authority pin and a durable
  reference to this review in the OOS manifest;
- local, single-operator, loopback `dev-integration` commissioning by Platform
  `#1291`; and
- live proof using one real, approved organization repository target under the
  final Console journey.

Not approved:

- claiming current operating readiness from completed historical work, source
  tests, this review, or a manifest flag alone;
- fixture, mock, synthetic, personal-token, ambient-credential, or direct-CLI
  substitution for the Console journey;
- browser access to provider, WGCF, Vault, Kubernetes, or Platform credentials;
- automatic Workspace Intake, inventory, Catalog, product, release, archive,
  transfer, or deletion effects;
- broad organization management or any provider permission outside the two
  reviewed identity contracts; or
- stage, production, shared, remote, public, or multi-user operation.

## Related Artifacts

- [Repository Custody Provider Identity Boundary Review](2026-08-29-repository-custody-provider-identity-boundary.md)
- [Repository Provisioning Authority Review](2026-08-29-repository-provisioning-authority.md)
- [OOS Platform Operation Adapter Security Delta](2026-10-15-oos-platform-operation-adapter-boundary.md)
- [Security delta review process](../security-delta-review-process.md)
- [Security review checklist](../security-review-checklist.md)
