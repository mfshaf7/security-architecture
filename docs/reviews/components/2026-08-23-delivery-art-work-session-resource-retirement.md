# Delivery ART Work-Session Resource Retirement Security Delta

## Summary

- date: 2026-08-23
- owner repo: `security-architecture`
- affected review subjects:
  - `repos.operator-orchestration-service`
  - `components.operator-orchestration-service`
  - `repos.workspace-governance-control-fabric`
  - `components.workspace-governance-control-fabric`
- delivery initiative: `openproject://work_packages/958`
- implementation item: `openproject://work_packages/968`
- security evidence item: `openproject://work_packages/969`
- activation item: `openproject://work_packages/970`
- architecture-custody item: `openproject://work_packages/971`
- architecture packet:
  `wgcf://artifacts/delivery-art/sha256/7af7069136c871f1c6011892b7280333e5a2adf30af0be87951e8c0d3bf8f898`
- governing workspace contract:
  [`c1f2b7e5d7b297ce1b6bc8eb296c8210c771a5be`](https://github.com/mfshaf7/workspace-governance/commit/c1f2b7e5d7b297ce1b6bc8eb296c8210c771a5be)
- review triggers:
  - `delivery-art-destructive-resource-retirement`
  - `delivery-art-session-created-provenance`
  - `delivery-art-terminal-cleanup-evidence`
  - `delivery-art-architecture-v2-custody-validation`
  - `delivery-art-activation-sequencing`
- decision: `approved`

This review approves the exact Operator Orchestration Service and Workspace
Governance Control Fabric source revisions listed below for merge. The reviewed
changes add fail-closed retirement of session-created Git resources, durable
terminal cleanup evidence, and architecture-v2 custody validation without
moving canonical source, review, merge, Security, or ART authority into local
session state.

The approval does not activate the path in Workspace Governance and does not
claim dev-integration dogfood, stage, production, or general operating
readiness. Activation remains a separately governed step after both reviewed
implementation changes and this Security decision have merged.

### Exact Source And Evidence Binding

| Subject | Evidence | Exact revision or digest |
| --- | --- | --- |
| Operator Orchestration Service | [OOS PR #143](https://github.com/mfshaf7/operator-orchestration-service/pull/143) | head [`7f6b403bb5a218d5b13501c7606c747ebe8dadde`](https://github.com/mfshaf7/operator-orchestration-service/commit/7f6b403bb5a218d5b13501c7606c747ebe8dadde) |
| OOS CI | [Validate Governance Docs run 32615489945](https://github.com/mfshaf7/operator-orchestration-service/actions/runs/32615489945) | passed on exact head `7f6b403bb5a218d5b13501c7606c747ebe8dadde` |
| Workspace Governance Control Fabric | [WGCF PR #51](https://github.com/mfshaf7/workspace-governance-control-fabric/pull/51) | head [`e8287cd0044d2b48769a35158ed5c6ff616168b3`](https://github.com/mfshaf7/workspace-governance-control-fabric/commit/e8287cd0044d2b48769a35158ed5c6ff616168b3) |
| WGCF CI | [Governance Bootstrap run 32614150164](https://github.com/mfshaf7/workspace-governance-control-fabric/actions/runs/32614150164) | passed on exact head `e8287cd0044d2b48769a35158ed5c6ff616168b3` |
| Workspace Governance | governing Delivery ART contract | commit `c1f2b7e5d7b297ce1b6bc8eb296c8210c771a5be` |
| WGCF | durable architecture packet | `sha256:7af7069136c871f1c6011892b7280333e5a2adf30af0be87951e8c0d3bf8f898` |
| OOS | merge-ready Review Packet | `sha256:fec383c5fb3d624b729c2d7425f1bf5cff8a51ab5da01e7f863b9a145a3171d8` |
| WGCF | merge-ready Review Packet | `sha256:3cb20eb49dc85f245c29a5f7baa04e13d0c0178751fb865db881a93ee2183485` |

This decision is not reusable for another OOS or WGCF head, a broader cleanup
boundary, or a changed governing contract without a fresh delta assessment.

## Scope Delta

The previously approved work-session lifecycle could remove local coordination
state after closeout, but it did not own a complete, provenance-bound process
for retiring Git resources created by that session. The reviewed delta adds
that missing terminal boundary and updates WGCF to admit and validate the
architecture-v2 custody contract used by the lifecycle.

### Design Intent

- Retire only resources proven to have been created by the current work
  session; never infer ownership from naming alone.
- Bind cleanup to an exact finalized Review Packet and the current pull-request
  source head before deleting any branch or worktree resource.
- Use compare-and-delete semantics for both local and remote refs so a
  concurrent update survives rather than being deleted.
- Preserve the exact terminal resource manifest and a cleanup receipt after
  mutable session state is removed.
- Allow partial cleanup to be retried idempotently while retaining per-resource
  failure detail for the operator.
- Keep WGCF as durable artifact custodian and validator, not source mutation or
  cleanup authority.
- Keep activation, dogfood, and operating-readiness claims outside these
  source-only Landing Units.

### Implemented Control

The exact reviewed OOS head implements these controls:

- Session-created resource provenance is recorded at creation and checked again
  before retirement. Pre-existing or unproven resources are retained.
- Cleanup requires a finalized Review Packet whose content digest, WGCF custody
  URI and backend, operator, Delivery scope, Landing Unit decision, rollback
  boundary, branch, and base match the current session.
- Current pull-request URL, head, merge state, and exact source evidence must
  match that packet before any destructive action starts.
- Remote branch deletion uses an expected-object lease. Local branch deletion
  uses an expected-value `update-ref` transaction. A branch changed after the
  check is retained and reported rather than deleted.
- The exact terminal manifest is retained under deterministic cleanup-receipt
  storage before the mutable receipt index and session are removed. Its digest
  remains bound by the cleanup receipt.
- Cleanup is resumable. Already retired resources remain successful, unresolved
  resources retain `last_error`, and the terminal session is removed only when
  the complete retirement contract is satisfied.

The exact reviewed WGCF head implements these controls:

- Architecture-v2 packets are schema-validated and admitted through the same
  durable custody boundary as the existing architecture artifact family.
- Artifact retrieval verifies content-addressed identity before readiness or
  lifecycle consumers rely on the packet.
- The canonical Delivery ART contract bytes match the governing Workspace
  Governance revision identified above.

### Review Corrections Before Approval

Security inspection found defects in the pre-approval OOS candidate. The exact
approved head corrects all of them:

1. a remote branch check/delete race now uses expected-object lease deletion;
2. cleanup is bound to the current pull request and exact finalized Review
   Packet source evidence before any retirement begins;
3. a local branch check/delete race now uses expected-value ref deletion;
4. local Review Packet tampering now fails custody and content validation;
5. the exact terminal manifest is retained after session deletion instead of
   retaining only a digest of a deleted document; and
6. the operator projection preserves per-resource failure detail for bounded
   retry and diagnosis.

No unresolved Security finding remains within this source-only merge scope.

### Validation Evidence

The exact OOS head passed:

- the complete OOS test suite: `628` tests;
- the focused resource-retirement suite: `28` tests, including real local and
  remote concurrent-update preservation, pull-request mismatch denial, packet
  tamper denial, retained-manifest digest proof, and partial-cleanup retry;
- Delivery ART contract, API documentation, governance-document, orchestration
  bundle, and OpenAPI validation;
- base-aware change-record and OpenProject mutation-contract validation against
  fetched `origin/main`; and
- `git diff --check`.

GitHub repeated the repository CI-equivalent governance path successfully in
run `32615489945` on the exact reviewed head.

The exact WGCF head passed:

- the complete WGCF test suite: `314` tests;
- the focused artifact-registry and readiness suite: `36` tests;
- project validation, canonical contract-byte comparison, and
  `git diff --check`; and
- GitHub `governance-bootstrap` and `runtime-images` checks in run
  `32614150164` on the exact reviewed head.

These are source, contract, and custody-validation results. They are not
operating evidence for the later activated workspace path.

## Review Areas

### Delivery

The OOS and WGCF changes remain independent Landing Units with exact reviewed
heads, separate pull requests, and separate rollback boundaries. Security
acceptance is durable in this repository before activation. The activation item
must consume merged implementation evidence rather than local branches or
merge-ready packets.

The finalized Review Packet remains the source-landing authority. Cleanup may
retire only session-created resources after exact source and pull-request truth
matches that packet. It cannot approve a pull request, perform Security
acceptance, merge source, or close ART work.

### Runtime

The OOS change performs bounded local and Git-remote resource retirement from
an explicit operator command. It adds no continuously running worker, broker
route, Temporal workflow, deployment, ingress, privileged host service, or
production control plane.

Failures are fail-closed and retryable. Changed, ambiguous, pre-existing, or
unproven resources are retained. Partial completion remains visible through the
receipt and per-resource errors. Mutable session state is removed only after
terminal evidence has been persisted.

WGCF adds artifact validation and custody support only. It does not gain Git
mutation, OpenProject mutation, cleanup, or activation authority.

### Identity, Secrets, And AI

This delta introduces no new human or machine identity, credential, secret
delivery path, model call, prompt boundary, or AI-enabled action path. Recorded
operator identity remains attribution, not authentication. Existing GitHub,
WGCF, Security Architecture, and ART authorities remain unchanged.

## Expansion Gates

1. The exact reviewed Security Architecture change must merge before its
   decision is used as durable acceptance evidence.
2. OOS PR #143 and WGCF PR #51 must merge without changing their reviewed
   heads.
3. Workspace Governance activation under `#970` may begin only after both
   implementation merges and this Security decision are durable.
4. Activation must dogfood successful cleanup, retained-resource failure,
   partial retry, restart, and terminal evidence before operating readiness is
   claimed.
5. Automatic cleanup, a remote cleanup service, new credentials, privileged
   host execution, stage or production use, or automated approval and merge
   decisions require a fresh architecture and Security review.

## Decision

`approved`

Approval is limited to:

- OOS PR #143 at exact head
  `7f6b403bb5a218d5b13501c7606c747ebe8dadde`;
- WGCF PR #51 at exact head
  `e8287cd0044d2b48769a35158ed5c6ff616168b3`;
- Workspace Governance contract revision
  `c1f2b7e5d7b297ce1b6bc8eb296c8210c771a5be`;
- provenance-bound retirement of session-created Git resources;
- exact finalized Review Packet and current pull-request source binding;
- compare-and-delete protection for local and remote refs;
- durable terminal manifest and cleanup-receipt retention;
- retryable partial cleanup with bounded operator-visible errors; and
- architecture-v2 artifact validation and custody.

Approval excludes:

- any changed OOS, WGCF, or governing-contract revision;
- Workspace Governance activation before all reviewed source and Security
  changes merge;
- claims of completed dev-integration dogfood or operating readiness;
- deletion of pre-existing, changed, ambiguous, or unproven resources;
- cleanup authority in WGCF;
- stage, production, shared, public, or continuously automated cleanup; and
- new identity, secret, remote executor, privileged host, or AI scope.

## Related Artifacts

- [Prior work-session lifecycle review](2026-08-23-delivery-art-work-session-lifecycle.md)
- [OOS resource-retirement change record](https://github.com/mfshaf7/operator-orchestration-service/blob/7f6b403bb5a218d5b13501c7606c747ebe8dadde/docs/records/change-records/2026-08-23-delivery-art-work-session-resource-retirement.md)
- [Security delta review process](../security-delta-review-process.md)
- [Security review checklist](../security-review-checklist.md)
