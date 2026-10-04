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
  `968643ad3dca86366ae417ebe77a23ba7c2c2cb6`;
- Governance Operations Console:
  `9347794a138f3649bb6ef5b7db057524d1c1e26d`; and
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

1. Architecture packet v13 satisfies the successor-packet condition by binding
   WGCF `3d04ccaa8a751dfcb743c06b253299ee028c8f46`, Security
   `cbb78d6e67097e3375ad983fca8408b491ac892a`, the unchanged approved Epic 1203
   scope and evidence outcomes, and the required fresh Platform source-intent
   identity.
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
- exact architecture packet v13
  `sha256:ef13022a4fb930086617781eda0727217d3cae0d17e23cde7c82276e0da10db7`;
- complete validation against the digest-pinned canonical repository-authority
  v2 schema;
- the exact source set listed above as input to the successor architecture
  packet; and
- continuation under existing item `#1231` after architecture and Security
  binding refresh.

Not approved:

- activating WGCF `3d04ccaa8a751dfcb743c06b253299ee028c8f46` under stale architecture v11 or
  v12, a terminal recovered Landing Unit identity, or stale Platform/Security
  pins;
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
- Architecture packet v13:
  `wgcf://artifacts/delivery-art/sha256/ef13022a4fb930086617781eda0727217d3cae0d17e23cde7c82276e0da10db7`
