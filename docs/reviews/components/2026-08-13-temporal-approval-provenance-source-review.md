# Temporal Approval Provenance Source Review

## Summary

- date: 2026-08-13
- owner repo: `security-architecture`
- affected review subjects:
  - `components.temporal`
  - `repos.platform-engineering`
  - `repos.workspace-governance`
- review triggers:
  - `temporal-controlled-runtime-proof-authorization`
  - `temporal-component-commissioning-runtime-drill`
  - `temporal-baseline-attestation-and-exact-restore`
  - `temporal-bounded-worker-and-payload-boundary`
- ART security review: `openproject://work_packages/824`
- ART Platform correction: `openproject://work_packages/825`
- reviewed Workspace Governance merge:
  `842943e949aff47e19835cc09ee24ed8c051723d`
- reviewed Workspace Governance PR:
  [#145](https://github.com/mfshaf7/workspace-governance/pull/145)
- reviewed Platform head:
  `12b6375b51e88912239cba467c8c951269e7f854`
- reviewed Platform PR:
  [#203](https://github.com/mfshaf7/platform-engineering/pull/203)
- decision: `approved`

This review approves the exact Platform source head above to merge after this
Security decision is merged. It confirms that controlled-proof claims bind
only executable source revisions while the final permit separately binds the
exact merged Security approval revision, normalized source path, artifact
reference, and digest.

This decision is source acceptance only. It does not issue a controlled-proof
permit, satisfy the future per-run Security authorization, authorize Temporal
commissioning, activate the Temporal profile, or claim operating evidence.

## Scope Delta

### Design Intent

The earlier authorization design required the future Security approval
artifact to prove a claims digest that included the Security commit containing
that same artifact. That dependency was circular: the final Security commit
could not exist before the artifact was committed, while the artifact could not
name that final commit before it existed.

The corrected authority split is:

- canonical claims bind only executable source revisions from Platform, OOS,
  Workspace Governance, and WGCF
- the claims digest is final before either approval is attached
- the operator and Security each approve that same immutable claims digest
- permit issuance loads the Security artifact from its exact historical Git
  revision and normalized path
- the Security revision must be contained in the local
  `refs/remotes/origin/main` tracking ref
- the permit approval envelope records the Security revision, path, artifact
  reference, and digest without changing the claims digest
- every use of the permit revalidates both approval content and source
  provenance before runtime mutation

This removes the Git-provenance cycle without making Security an executable
source owner or weakening the independent approval boundary.

### Implemented Control

The exact Platform PR head implements and proves the following controls:

- authorization schema v4 renames the claims collection to
  `execution_source_revisions` and rejects the former mixed source shape
- the approval envelope requires
  `security_authorization_source_repo`,
  `security_authorization_source_revision`,
  `security_authorization_source_path`,
  `security_authorization_ref`, and
  `security_authorization_digest`
- only `security-architecture` is accepted as the approval source repo
- source paths are normalized and constrained before historical Git-object
  reads
- the Security checkout must be clean at the expected revision
- the exact Security revision must be an ancestor of
  `refs/remotes/origin/main`; a clean pushed review branch is denied until it
  is merged and the tracking ref contains it
- the artifact bytes loaded from the permit-bound historical revision must
  match the supplied approval object, artifact reference, and digest
- claims remain byte-stable while approval provenance is attached
- absent, dirty, unmerged, substituted, stale, wrong-revision, wrong-path,
  digest-mismatched, Platform-drifted, and legacy inputs fail closed
- the permit and execution claim are revalidated before every controlled
  runtime mutation

The canonical Workspace Governance schema and the Platform vendor copy are
byte-identical at SHA-256
`8c41760d409a000aeaef9b32fed76e09b8eea1ac5d44c99c742517a305bac89b`.
The reviewed Platform implementation file has SHA-256
`d6d4fb6acced7d4597742bdb46112c13d65c356c0552ff3f6d979e2edbeca27f`,
and its controlled-proof test source has SHA-256
`2d69d170cb476d24fd3c38178355969943f398bde2d2f56e1deec4ffc6292c67`.

Validation against the exact Platform head passed:

- 62 controlled-proof authorization and execution tests
- the isolated real-Git approval-provenance positive and negative case
- 13 Platform dev-integration regression tests
- source-manifest, commissioning-plan, repository-structure, schema-parity,
  and patch-format checks
- Platform pull-request `validate` and `repo-posture` checks

### Operating Evidence

Operating evidence is intentionally absent. No controlled-proof permit was
issued, no Security per-run authorization exists, no Temporal runtime or
worker was started, no namespace or database was created, and no commissioning
workflow or activity ran.

The real-Git suite is source conformance evidence. It proves merge-containment
and historical-object behavior in isolated repositories; it does not prove a
live Security approval, live identity, runtime isolation, persistence, backup,
restore, or post-run evidence custody.

## Review Areas

### Delivery

The merge sequence is mandatory:

1. Workspace Governance PR #145 is already merged.
2. This exact Security review must merge.
3. Platform PR #203 may merge only if its head remains exactly
   `12b6375b51e88912239cba467c8c951269e7f854`.

Any Platform head change invalidates this decision and requires a fresh delta
review. A local Security branch, clean commit, or pushed but unmerged branch is
not approval provenance. The future permit issuer must operate against a
freshly fetched Security repository whose `refs/remotes/origin/main` contains
the permit-bound revision.

The source Review Packets remain separate by owner and rollback boundary. This
Security review must not be folded into the Platform commit or treated as
evidence that the commissioning runtime ran.

### Runtime

The correction preserves the existing fail-closed runtime boundary. Every
controlled mutation revalidates the consumed permit and the Security source
binding. Missing or changed provenance stops the action before mutation.

The profile remains `build-admitted`. Normal Temporal launch, access, smoke,
backup, restore, workflow, and activity commands remain denied. The later
per-run review must still bind current source, immutable artifacts, identities,
queues, namespace, baseline, expiry, and owner-image provenance before a permit
may be issued.

### Identity And Secrets

This delta introduces no new identity, credential, secret-delivery path, or
data-retention scope. The identity, queue-isolation, secret-custody, payload,
and evidence-minimization findings from the 2026-08-01 contract review remain
future commissioning gates; they are not satisfied or weakened here.

## Findings

No new source finding blocks this correction. Existing future gates remain:

- ART #790 owns the fresh per-run Security authorization
- ART #751 owns the bounded commissioning execution after authorization
- ART #791 owns post-run Security review of operating evidence

Those gates are outside this source-only decision and must not be inferred from
an `approved` result here.

## Decision

`approved`

Approved:

- the exact Workspace Governance merge and exact Platform PR head identified
  above
- separation of executable source claims from Security approval provenance
- exact historical Security revision, normalized path, reference, and digest
  binding in the approval envelope
- denial of clean but unmerged Security review branches
- immutable claims across approval attachment
- fail-closed source, path, digest, merge-containment, substitution, drift,
  replay, and legacy-shape validation
- Security merge before the unchanged Platform head

Not approved:

- use of this review as a per-run `security_authorization_ref`
- issuance or consumption of a controlled-proof permit
- Temporal, OOS worker, or WGCF worker commissioning
- profile activation, self-serve launch, stage, or production
- any operating-evidence or production-readiness claim

If Platform PR #203 changes after this review, the approval is stale and the
changed head must receive another exact delta review.

## Related Artifacts

- [Temporal controlled commissioning proof contract](2026-08-01-temporal-controlled-commissioning-proof-contract.md)
- [Temporal durable orchestration build admission](2026-07-31-temporal-durable-orchestration-build-admission.md)
- [Temporal security view](../../architecture/components/temporal/README.md)
- [Security delta review process](../security-delta-review-process.md)
- [Workspace Governance PR #145](https://github.com/mfshaf7/workspace-governance/pull/145)
- [Platform PR #203](https://github.com/mfshaf7/platform-engineering/pull/203)
