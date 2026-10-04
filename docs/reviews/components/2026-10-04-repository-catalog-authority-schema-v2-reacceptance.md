# Repository Catalog Authority-Schema v2 Re-Acceptance

## Summary

- date: 2026-10-04
- owner repo: `security-architecture`
- affected review subject: `repos.operator-orchestration-service`
- predecessor review:
  [`2026-10-04-repository-catalog-authority-digest-reacceptance.md`](2026-10-04-repository-catalog-authority-digest-reacceptance.md)
- delivery initiative: `openproject://work_packages/1203`
- consuming operating-proof item: `openproject://work_packages/1231`
- Landing Unit Decision: `child_isolated_landing_unit`; this Security judgment
  has a distinct owner, review path, revision pin, and rollback from the WGCF
  owner-maintenance repair and the dependent Platform commissioning change
- decision: `approved-with-findings`

The first live repository-readiness request using the corrected exact-content
digest failed closed with `authority-contract-invalid`. The mounted Workspace
Governance authority was current and byte-exact, but WGCF still hard-coded the
legacy `repos.yaml` schema-v1 shape and its tests generated only v1 fixtures.
Canonical `repos.yaml` has used schema v2 since 2026-09-06.

This review accepts only WGCF merge
[`3d04ccaa8a751dfcb743c06b253299ee028c8f46`](https://github.com/mfshaf7/workspace-governance-control-fabric/commit/3d04ccaa8a751dfcb743c06b253299ee028c8f46)
from human-approved [PR #97](https://github.com/mfshaf7/workspace-governance-control-fabric/pull/97).
The repair pins the canonical v2 authority schema commit and digest, validates
the complete authority document before evaluation, updates the unit authority
to the v2 record envelope, and proves legacy v1 and schema tampering fail
closed. It adds no identity, permission, secret, route, readiness authority, or
Catalog mutation authority.

The source set accepted for the next architecture refresh is:

- Workspace Governance:
  `9718ce9eea04049541a1fb44f0b7cdc0ac823687`;
- Workspace Governance Control Fabric:
  `3d04ccaa8a751dfcb743c06b253299ee028c8f46`;
- Operator Orchestration Service:
  `7ea390c28ac95d64a8fee285f212585bf7863cf6`;
- Governance Operations Console:
  `f7e1db75739e5fbeb8d7a5ad0d9a7858f2289aac`;
- Platform Engineering:
  `7b0058a7a605871125dd5d9147e557dd9bc4ecb9`; and
- this Security review's eventual merged revision.

Architecture packet v13 is now durably persisted at
`wgcf://artifacts/delivery-art/sha256/ef13022a4fb930086617781eda0727217d3cae0d17e23cde7c82276e0da10db7`
with custody receipt digest
`sha256:ed0d2b0906757b3c4a9d2b0a04b6800428ea6743bdfd1584a8b3725dfa8c2a45`.
It explicitly supersedes v12, binds WGCF
`3d04ccaa8a751dfcb743c06b253299ee028c8f46` and the prior merged phase of this
review at `cbb78d6e67097e3375ad983fca8408b491ac892a`, and preserves all 35 covered
children, approved owner boundaries, rollback boundaries, and conformance
outcomes. The only structural change is the replacement of terminal Platform
Landing Unit identity
`delivery-1203-repository-catalog-platform-recovery-2` with
`delivery-1203-repository-catalog-platform-recovery-3` after OOS recovery
receipt
`work-session-recovery:work-session:delivery-1203:delivery-1203-repository-catalog-platform-recovery-2`
archived the clean unmerged session. The receipt proves no remote branch, pull
request, Review Packet, or readiness receipt existed and retains local source
for deliberate reconciliation. This follow-up source change is the exact
architecture-binding phase of the same `child_isolated_landing_unit` Security
judgment. Architecture packets v11 and v12 remain historical evidence, not
current activation authority. No replacement ART Defect or child is
authorized.

Commissioning later exposed one product-local repeat-edit conflict in the
already accepted Console source. The original idempotency digest represented
only the effective Catalog draft, while each later deliberate operator
acceptance carried a new request body. OpenProject correctly rejected that
different body under the reused key. Console owner-maintenance
[PR #51](https://github.com/mfshaf7/governance-operations-console/pull/51)
binds the idempotency digest to the stable operator acceptance: same-acceptance
retries still replay, while a later reviewed acceptance gets a distinct key.
It adds no credential, role, permission, route, backend authority, or browser
authority. Agent Gary authored the change; `mfshaf7` approved and squash-merged
it as `f7e1db75739e5fbeb8d7a5ad0d9a7858f2289aac` after all 466 semantic tests,
typecheck, production build, repository validation, dependency audit, and
strict branch-lifecycle cleanup passed.

Architecture packet v14 is durably persisted at
`wgcf://artifacts/delivery-art/sha256/e834d9b9823ce1e0db357e0fbbbbf5b287e9e95c6e4aab18beb5e255fc556591`
with custody receipt digest
`sha256:65687bd75a926cf5fbb0ba90d504a84ad871b552507c85828cc9962dd007c19b`.
It supersedes v13 and changes only the Console source snapshot to that merged
repair plus the Security snapshot to this review's prior merge. All 35 covered
children, the active `delivery-1203-repository-catalog-platform-recovery-3`
Landing Unit, owner boundaries, dependencies, security posture, rollback
boundaries, and conformance outcomes are preserved. Packets v11 through v13
are historical evidence rather than current activation authority.

Architecture packet v15 is durably persisted at
`wgcf://artifacts/delivery-art/sha256/1f17cc327aa7bbb730ab80877421f6d3d4a459b9e66d528c49e8d36bebb031ff`
with custody receipt digest
`sha256:51949b4ad017ba9bf66c881fc7bab373d26c22754653323f3070ab869b59bc96`.
It supersedes v14 and changes only the terminal Platform Landing Unit identity
from `delivery-1203-repository-catalog-platform-recovery-3` to
`delivery-1203-repository-catalog-platform-recovery-4`. OOS recovery receipt
`work-session-recovery:work-session:delivery-1203:delivery-1203-repository-catalog-platform-recovery-3`
with digest
`sha256:b33fc840d6e49b47e4d50268ef12ade5ae44cee4f788547941e2847faa635e23`
proves the superseded session was clean, unmerged, and had no remote branch,
pull request, Review Packet, or readiness receipt; its retained source is
eligible for deliberate reconciliation into recovery 4. All 35 covered
children, source revisions, owner boundaries, dependencies, security posture,
rollback boundaries, and conformance outcomes are preserved. Packets v11
through v14 are historical evidence rather than current activation authority.

Architecture packet v16 is durably persisted at
`wgcf://artifacts/delivery-art/sha256/3a4b5edb6bc54ff47a45f610b41f75bc57dd9d1ab56e9475518100d75ff72ab0`
with custody receipt digest
`sha256:8621a894e31626b24a4abc66ac489fe96c9f1fa127b54155ff51d042b13f5dae`.
It supersedes v15, binds merged Platform PR 264 at
`7b0058a7a605871125dd5d9147e557dd9bc4ecb9` and the OOS configured-path
transport repair at `7ea390c28ac95d64a8fee285f212585bf7863cf6`, and replaces only the incomplete
terminal Platform Landing Unit identity with
`delivery-1203-repository-catalog-platform-recovery-5`. Evidence-preserving OOS
recovery receipt
`work-session-recovery:work-session:delivery-1203:delivery-1203-repository-catalog-platform-recovery-4`
with digest
`sha256:9f8dc621b8b1ce28a1170bec73eed7d665c6b96e5ac2d5b1c60d336f8425b568`
proves PR 264 is merged, preserves its durable merge-ready Review Packet at
`sha256:38b0924a4fdc2eea8bf587d15b4e67a3793d542f42eff51cba896b84144af8c8`,
and confirms no readiness receipt or finalized packet exists. Recovery 5 must
use the complete accepted-base profile and cannot claim the archived packet as
its own evidence. All 35 covered children, owner boundaries, dependencies,
security posture, rollback boundaries, and conformance outcomes are preserved.
Packets v11 through v15 are historical evidence rather than current activation
authority.

## Scope Delta

### Design Intent

- Preserve Workspace Governance as repository-authority owner.
- Preserve WGCF as an independent, non-mutating readiness evaluator.
- Require the evaluator to understand the exact canonical authority contract,
  not an approximate synthetic fixture.
- Keep unrecognized schema versions, malformed records, stale source bytes,
  and mismatched repository rules fail-closed.

### Implemented Control

WGCF's repository-readiness contract manifest now pins the canonical
`contracts/schemas/repos.schema.json` source path, source commit
`3b89d0f6f50823ada8b9694327692440d10f428e`, and SHA-256
`fe8cf65f9d04dc4d246477cb3eb0c2bdc5b351e859e5376e3a610acd2df443c6`.
The contract loader verifies that bundled schema before constructing a JSON
Schema validator, and the evaluator rejects the complete authority document if
validation fails.

Agent Gary authored WGCF PR #97; `mfshaf7` approved and merged it after the
482-test delivery evidence suite, project validation, base-aware diff check,
and a local exact-authority proof all passed. The proof evaluated current
Workspace Governance authority digest
`sha256:94aeb6a58b5bcea176b629546df1577971c94c69516c7b8be544e676cc9fc342`
and returned `ready` with a repository-readiness reference for
`openclaw-runtime-distribution`. The source credential, branch, remote branch,
and worktree were retired after merge.

### Operating Evidence

The prior live rejection remains valid negative evidence: it proved the
authority contract failed closed and no Catalog mutation occurred. The local
exact-authority result proves source compatibility, not deployed behavior.
Positive first-use mutation, readback, reuse, restart, denial, rollback,
cleanup, and final status remain assigned to item `#1231` after exact
architecture, Security, and Platform pin refresh.

## Review Areas

### Delivery And Runtime Integrity

The change narrows drift by replacing a hand-written version check with a
digest-pinned canonical schema. The runtime still reads the exact mounted
Workspace Governance file and compares its byte digest to the OOS request
before evaluating the repository. A schema upgrade now requires an explicit
WGCF contract update rather than failing late behind an apparently green v1
fixture.

Platform must deploy only an image attributable to WGCF merge
`3d04ccaa8a751dfcb743c06b253299ee028c8f46` and must update both the
repository-catalog commissioning policy and Workspace Intake identity source
set. Architecture and Security bindings must name the same exact revisions.

### Identity, Secrets, AI, And Mutation Authority

No identity or secret definition changes. The existing Workspace Intake caller
and short-lived credential path remains unchanged. No model is invoked, no AI
decision is introduced, and no browser receives control credentials. WGCF
continues to issue readiness evidence only; OOS remains the bounded Catalog
mutation owner and OpenProject remains canonical Catalog state.

## Findings And Activation Conditions

1. Architecture packet v16 satisfies the successor-packet condition by binding
   WGCF `3d04ccaa8a751dfcb743c06b253299ee028c8f46`, Security
   `e392abe55fbec947431aeba75c9daccf56cc0dee`, Console
   `f7e1db75739e5fbeb8d7a5ad0d9a7858f2289aac`, OOS
   `7ea390c28ac95d64a8fee285f212585bf7863cf6`, Platform
   `7b0058a7a605871125dd5d9147e557dd9bc4ecb9`, the unchanged approved Epic 1203
   scope and evidence outcomes, and the fresh
   `delivery-1203-repository-catalog-platform-recovery-5` source-intent identity.
2. The merge containing this paragraph must land before Platform activation so
   the Platform policy can pin the exact architecture-binding Security
   revision.
3. Start the replacement Platform Landing Unit for existing item `#1231` with
   the exact OOS recovery receipt chain, fresh branch, and exact WGCF, Security,
   and architecture revisions; do not create another ART child.
4. Rebuild the exact `refinement-catalog` composition and require the live
   readiness response to report `repository-ready` with a current durable
   reference before any Catalog mutation.
5. Complete the already-planned positive and negative live-backend cases,
   bounded rollback, cleanup, and final active status before closing `#1231`.
6. Keep the cross-repo fixture/authority escape in the active improvement
   candidate until a stronger acceptance control is separately approved and
   landed.

No exception or accepted risk is created.

## Decision

`approved-with-findings`

Approved:

- exact WGCF merge `3d04ccaa8a751dfcb743c06b253299ee028c8f46`;
- exact Console repair merge
  `f7e1db75739e5fbeb8d7a5ad0d9a7858f2289aac`;
- exact architecture packet v16
  `sha256:3a4b5edb6bc54ff47a45f610b41f75bc57dd9d1ab56e9475518100d75ff72ab0`;
- complete validation against the digest-pinned canonical repository-authority
  v2 schema;
- the exact source set listed above as input to the successor architecture
  packet; and
- continuation under existing item `#1231` after architecture and Security
  binding refresh.

Not approved:

- activating WGCF `3d04ccaa8a751dfcb743c06b253299ee028c8f46` under stale architecture v11
  through v15, a terminal recovered Landing Unit identity, or stale
  Platform/Security pins;
- accepting arbitrary or unpinned authority schemas;
- treating the local source proof as deployed operating evidence;
- fixture, cached, synthetic, or stale readiness evidence as Catalog mutation
  authority;
- any new identity, secret, permission, mutation owner, public route, stage,
  production, or multi-user scope; or
- machine approval or merge, browser-held credentials, or direct-main writes.

## Related Artifacts

- [Authority-digest predecessor](2026-10-04-repository-catalog-authority-digest-reacceptance.md)
- [Security delta review process](../security-delta-review-process.md)
- [WGCF owner change record](https://github.com/mfshaf7/workspace-governance-control-fabric/blob/3d04ccaa8a751dfcb743c06b253299ee028c8f46/docs/records/change-records/2026-10-04-repository-readiness-v2-authority.md)
- [WGCF pull request #97](https://github.com/mfshaf7/workspace-governance-control-fabric/pull/97)
- [Console pull request #51](https://github.com/mfshaf7/governance-operations-console/pull/51)
- Architecture packet v16:
  `wgcf://artifacts/delivery-art/sha256/3a4b5edb6bc54ff47a45f610b41f75bc57dd9d1ab56e9475518100d75ff72ab0`
