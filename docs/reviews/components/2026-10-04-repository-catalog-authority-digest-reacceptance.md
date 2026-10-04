# Repository Catalog Authority-Digest Re-Acceptance

## Summary

- date: 2026-10-04
- owner repo: `security-architecture`
- affected review subject: `repos.operator-orchestration-service`
- predecessor review:
  [`2026-10-04-repository-catalog-controlled-activation.md`](2026-10-04-repository-catalog-controlled-activation.md)
- delivery initiative: `openproject://work_packages/1203`
- consuming operating-proof item: `openproject://work_packages/1231`
- Landing Unit Decision: `child_isolated_landing_unit`; this exact Security
  judgment has a distinct owner, review path, revision pin, and rollback from
  the OOS maintenance repair and the Platform commissioning change
- decision: `approved-with-findings`

The first real cross-repository readiness call exposed an input-definition
mismatch before any Catalog mutation: OOS supplied the canonical semantic
Workspace Inventory digest, while WGCF independently verified SHA-256 over the
exact `contracts/repos.yaml` source bytes. Both implementations failed closed,
but the handoff could never become ready.

This review accepts OOS merge
[`968643ad3dca86366ae417ebe77a23ba7c2c2cb6`](https://github.com/mfshaf7/operator-orchestration-service/commit/968643ad3dca86366ae417ebe77a23ba7c2c2cb6)
from human-approved [PR #279](https://github.com/mfshaf7/operator-orchestration-service/pull/279).
It accepts no other source successor. The change distinguishes the two digest
controls, keeps the semantic digest for Inventory projections, and sends the
exact source-content digest to WGCF. No identity, permission, caller, secret,
repository scope, readiness authority, or mutation authority changes.

The required source-binding refresh is now durably represented by architecture
packet v11:
`wgcf://artifacts/delivery-art/sha256/115056ba9f888c8ee08de78a17bcea5dd8df40c4a3624eeecbdc7b79148deb17`.
It supersedes v10, binds the exact OOS repair and this review's first merged
Security acceptance, preserves the approved Epic scope and owner map, and
assigns `#1231` to one fresh evidence-preserving Platform recovery Landing
Unit. This follow-up review change is the exact architecture-binding phase of
the same `child_isolated_landing_unit` Security judgment.

The complete commissioning source set accepted with v11 is:

- Workspace Governance:
  `9718ce9eea04049541a1fb44f0b7cdc0ac823687`;
- Workspace Governance Control Fabric:
  `f296a8bf91bcc22272f0079cf2b0aec6fe431fdf`;
- Operator Orchestration Service:
  `968643ad3dca86366ae417ebe77a23ba7c2c2cb6`; and
- Governance Operations Console:
  `9347794a138f3649bb6ef5b7db057524d1c1e26d`.

This remains source and architecture acceptance, not operating proof. Platform
must pin the eventual merge containing this exact v11 binding and complete the
existing `#1231` commissioning path. No replacement ART Defect or child is
authorized.

## Scope Delta

### Design Intent

- Preserve Workspace Governance as the repository-authority owner and WGCF as
  the independent Repository readiness evaluator.
- Preserve OOS as the bounded orchestration layer, not a readiness decision
  authority.
- Represent the semantic inventory identity and the exact source-file identity
  as separate, named digests so consumers cannot silently substitute one for
  the other.
- Keep any authority race fail-closed: WGCF compares the supplied exact digest
  to the authority bytes it reads and returns stale when they differ.

### Implemented Control

OOS now computes `active_inventory_content_digest` from the exact
`contracts/repos.yaml` bytes in the same one-revision source checkout used for
the active repository record and semantic Inventory projection. The service
validates both digests and sends only the source-content digest as WGCF's
`expected_authority_digest`. The existing semantic `active_inventory_digest`
remains unchanged for Inventory workflow comparisons.

The merged owner evidence includes exact-byte and whitespace-sensitivity unit
coverage, outbound-request binding, 12 real-Git Inventory source checks, the
full 1,207-test OOS suite with no failures, CI-equivalent generated-contract
and governance validation, and a security-tagged owner change record. Agent
Gary authored the source, `mfshaf7` approved and merged it, and the source
credential and branch residue were retired after merge.

### Operating Evidence

The failed live call is valid negative evidence: it proved independent WGCF
verification, stale rejection, and no Catalog mutation. Positive readiness,
Catalog mutation and readback, retry, restart, denial, rollback, cleanup, and
final activation remain assigned to Platform `#1231` after exact pin refresh.

## Review Areas

### Delivery And Evidence Integrity

The correction binds the producer to the consumer's already-reviewed digest
definition without moving authority. Platform must not reuse the predecessor
OOS pin or the earlier architecture source snapshot. Its next architecture
packet and activation policy must identify OOS
`968643ad3dca86366ae417ebe77a23ba7c2c2cb6` and the eventual merged revision
containing this review.

The semantic digest and source-content digest must remain separately named in
code, tests, audit evidence, and operator-facing diagnostics. A future
normalization, serialization, or checkout transformation must produce a stale
result rather than an accepted readiness reference when WGCF observes
different authority bytes.

### Runtime And Failure Behavior

The accepted source preserves non-mutation during readiness preparation. OOS
still requires an active exact Repository record and validates WGCF's subject,
scope, receipt, generation, timestamp, authority digest, and linking decision.
WGCF still independently reads current authority and owns the readiness
decision and ledger. Catalog mutation remains a later, separately accepted
OOS action with mutation-time revalidation and canonical readback.

Configured live mode may not fall back to the semantic digest, fixtures, a
locally synthesized decision, or a previously ready receipt after an authority
change. The existing single-operator, loopback `dev-integration` limit remains
unchanged.

### Identity, Secrets, And AI

No App, installation, token, caller, reviewer, merge authority, credential
path, secret projection, model call, or AI authority changes. The Console
browser remains outside Workspace Governance, WGCF, and Catalog-control
credentials and cannot supply either digest as policy input.

## Findings And Activation Conditions

1. Platform must replace the predecessor OOS and Security pins with the exact
   merged successors before reactivating the composition.
2. The Delivery architecture packet consumed by `#1231` must be refreshed so
   its source snapshot and validation plan describe this maintenance repair;
   the prior packet remains historical evidence, not current authority.
3. `#1231` must exercise the real OOS-to-WGCF call and require the returned
   authority digest to equal the source-content digest derived from current
   Workspace Governance authority before Catalog mutation.
4. The final proof must still cover positive first use, current-reference
   reuse, stale and unauthorized denial, dependency failure, restart, bounded
   rollback, cleanup, and final active status.
5. The absent pre-merge cross-repo conformance case remains a control-system
   improvement candidate; it does not justify another ART Defect or permit
   source-only evidence to close `#1231`.

No exception or accepted risk is created.

## Decision

`approved-with-findings`

Approved:

- exact OOS merge `968643ad3dca86366ae417ebe77a23ba7c2c2cb6`;
- exact architecture packet
  `wgcf://artifacts/delivery-art/sha256/115056ba9f888c8ee08de78a17bcea5dd8df40c4a3624eeecbdc7b79148deb17`
  with the Workspace Governance, WGCF, OOS, and Console revisions listed
  above;
- separate semantic and exact source-content Inventory digests;
- use of the exact source-content digest for WGCF
  `expected_authority_digest`;
- a dependent Platform-only source-pin, Security-pin, architecture-packet, and
  commissioning refresh under existing item `#1231`; and
- continuation of the predecessor review's exact Console, Workspace
  Governance, WGCF, identity, secret, mutation, rollback, and scope limits.

Not approved:

- any other OOS successor or unreviewed Platform source;
- semantic and source-content digest substitution;
- OOS or the Console making the readiness decision locally;
- fixture, cached, synthetic, or stale evidence as operating success;
- mutation success inferred from readiness preparation;
- machine approval or merge, browser-held credentials, or direct-main writes;
  or
- shared, remote, multi-user, stage, production, ingress, or public exposure.

## Related Artifacts

- [Controlled-activation predecessor](2026-10-04-repository-catalog-controlled-activation.md)
- [Security delta review process](../security-delta-review-process.md)
- [OOS owner change record](https://github.com/mfshaf7/operator-orchestration-service/blob/968643ad3dca86366ae417ebe77a23ba7c2c2cb6/docs/records/change-records/2026-10-04-repository-readiness-content-digest.md)
- [OOS pull request #279](https://github.com/mfshaf7/operator-orchestration-service/pull/279)
