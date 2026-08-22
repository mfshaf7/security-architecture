# Delivery ART Work-Session Lifecycle Security Delta

## Summary

- date: 2026-08-23
- owner repo: `security-architecture`
- affected review subjects:
  - `repos.operator-orchestration-service`
  - `components.operator-orchestration-service`
- delivery initiative: `openproject://work_packages/958`
- security evidence item: `openproject://work_packages/962`
- implementation item: `openproject://work_packages/963`
- activation and dogfood item: `openproject://work_packages/964`
- architecture packet:
  `wgcf://artifacts/delivery-art/sha256/879527d9905bfd4a9108c51dec5d1d875118c1fd7e5d82f4deaabdf0cb87814a`
- governing workspace contract:
  [`fa8df763333990bb84256184cfd050e7c5c099ee`](https://github.com/mfshaf7/workspace-governance/commit/fa8df763333990bb84256184cfd050e7c5c099ee)
- review triggers:
  - `delivery-art-work-session-state-custody`
  - `delivery-art-historical-freshness`
  - `delivery-art-human-gate-preservation`
- decision: `approved`

This review approves the exact Operator Orchestration Service source revision
listed below for merge. It adds a reconstructable local coordination session
around the existing Delivery ART lifecycle without moving canonical work,
source, artifact, review, merge, or closeout authority into that session.

The approval does not activate the path in Workspace Governance and does not
claim dev-integration dogfood, stage, production, or general operating
readiness. Those claims remain blocked on work item `#964` after the reviewed
source has merged.

### Exact Source And Evidence Binding

| Subject | Evidence | Exact revision or digest |
| --- | --- | --- |
| Operator Orchestration Service | [OOS PR #142](https://github.com/mfshaf7/operator-orchestration-service/pull/142) | base [`833ddc8b38e79238957bd813c6a3a2acc4f1276c`](https://github.com/mfshaf7/operator-orchestration-service/commit/833ddc8b38e79238957bd813c6a3a2acc4f1276c); head [`f50fcc4c44e96aebaa81c6be9728f559b0c0a15e`](https://github.com/mfshaf7/operator-orchestration-service/commit/f50fcc4c44e96aebaa81c6be9728f559b0c0a15e) |
| OOS CI | [Validate Governance Docs run 32588144090](https://github.com/mfshaf7/operator-orchestration-service/actions/runs/32588144090) | passed on exact head `f50fcc4c44e96aebaa81c6be9728f559b0c0a15e` |
| Workspace Governance | governing operator-path contract | commit `fa8df763333990bb84256184cfd050e7c5c099ee` |
| WGCF | durable architecture packet | `sha256:879527d9905bfd4a9108c51dec5d1d875118c1fd7e5d82f4deaabdf0cb87814a` |

This decision is not reusable for another OOS head, a broader runtime boundary,
or a changed workspace contract without a fresh delta assessment.

## Scope Delta

The existing Delivery ART lifecycle had durable artifact transitions and
human gates, but normal operation still required a caller-managed plan file.
The reviewed delta adds one operator path for starting, inspecting, continuing,
and closing a source-backed Landing Unit after process restart or worktree
relocation.

### Design Intent

- Keep the session as local coordination state, not a canonical backend or
  evidence store.
- Reconstruct source work from the operator-approved Landing Unit and exact Git
  base instead of persisting an absolute worktree path.
- Keep one session for all covered work-item aliases in a Landing Unit.
- Separate immutable material architecture truth from ordinary ART progress so
  progress does not invalidate an approved historical decision.
- Preserve explicit human authority for architecture, Landing Unit selection,
  exceptions, pull-request review, merge, Security acceptance, and ART
  closeout.
- Project one bounded next action and fail closed when state, source, artifact,
  or authority evidence is inconsistent.

### Implemented Control

The exact reviewed OOS head implements these controls:

- Work-session decisions and stored state are closed, schema-validated machine
  contracts. Coordination validation rejects absolute paths and secret-shaped
  fields before persistence.
- The default XDG state root lives outside Git worktrees in private
  directories. Directories are created with mode `0700`, files with mode
  `0600`, and JSON replacement uses an atomic write-and-rename boundary. An
  explicit state-root override remains operator-controlled.
- Session and alias storage names use reversible percent encoding rather than
  lossy normalization. Distinct valid Landing Unit identifiers therefore
  cannot overwrite one another.
- Alias-index entries are validated, inherited object properties are not
  treated as aliases, durable session files can recover a torn index, and
  conflicting aliases fail closed.
- Session creation is serialized across the complete Landing Unit scope.
  Continue and close mutations are serialized by shared session identity, so
  different covered work-item aliases cannot mutate one session concurrently.
- Source reconstruction resolves an exact base commit and planned branch.
  Repository names, relative paths, traversal, and symlink escape are checked
  before architecture content is read.
- Candidate artifacts still require exact freshness. Historical architecture
  and work-start artifacts remain usable only while their material decision
  fields match current authority; material structural drift fails closed.
- Local session deletion occurs only after the close adapter reports complete
  ART closeout. Deleting coordination state does not delete Git, WGCF,
  OpenProject, pull-request, or Review Packet evidence.
- Compatibility lifecycle-plan commands remain available as recovery tools,
  while the bounded `work` command family becomes the normal operator surface.

### Review Corrections Before Approval

Security inspection found defects in the pre-approval candidate. The exact
approved head corrects all of them:

1. lossy filesystem naming that could collapse distinct valid identifiers;
2. overlapping concurrent starts through different work-item aliases;
3. concurrent continue or close mutations through aliases of one session;
4. inherited object-property names being interpreted as alias-index entries;
5. missing explicit private-directory permissions;
6. missing negative tests for repository traversal and symlink escape; and
7. an incorrect architecture-packet digest in the OOS change record.

No unresolved Security finding remains within this source-only merge scope.

### Operating Evidence

The exact committed head passed:

- the complete OOS test suite: `614` tests;
- the focused work-session and CLI-adapter suite: `15` tests;
- orchestration bundle, Delivery ART contract, Proposal and orchestration
  OpenAPI, API documentation, and governance-document validation;
- base-aware change-record and OpenProject mutation-contract validation against
  fetched `origin/main`;
- API and orchestration-worker image builds; and
- API health and fail-closed worker-status smoke checks.

GitHub repeated the repository CI-equivalent path successfully in run
`32588144090` on the exact reviewed head.

This is source and build evidence, not operating evidence for the activated
workspace path. Restart, relocation, cleanup, and closeout dogfood remain
required under `#964` after merge.

## Review Areas

### Identity And Authorization

This delta introduces no new human or machine identity and no new credential.
The stored operator identifier and decision source are attribution fields, not
authentication. Existing OOS caller authentication and canonical ART authority
remain outside the local session.

Human gates are preserved in the lifecycle projection. OOS stops at the next
required gate; it does not approve architecture, exceptions, pull requests,
merge, Security acceptance, or ART closeout. GitHub, Security Architecture,
WGCF, and Workspace Delivery ART remain the enforcement or decision authorities
for those boundaries.

### Secrets And Local State

The session is intentionally secret-free. Schema and recursive coordination
validation reject secret-shaped keys and absolute host paths. Private local
permissions reduce accidental same-host disclosure, but the session is not a
secret store and must not be extended into one.

The local XDG-style state is coordination only. It is reconstructable from
canonical sources and cannot be cited as durable work, approval, merge, or
closeout evidence. An explicit state-root override must preserve the same
outside-worktree boundary.

### Delivery And Human Gates

The source boundary remains one owner-repo Landing Unit with an explicit branch
and exact base commit. Pull-request identity and head freshness are checked by
the existing lifecycle before merge-ready evidence can advance. Rollback is
preserved by reverting the OOS source change and leaving canonical artifacts
untouched.

The implementation projects Security and merge gates but does not prevent a
privileged human from bypassing external GitHub or ART policy. This review does
not reclassify projection as enforcement; branch protection, review authority,
and ART mutation controls remain separately governed.

### Runtime And Failure Behavior

The delta adds no Temporal workflow, broker, network endpoint, deployment,
privileged host action, or control plane. It adds local CLI coordination and
source-worktree reconstruction inside OOS.

Corrupt state, ambiguous aliases, conflicting active sessions, live mutation
locks, missing durable artifacts, material architecture drift, source-path
escape, and unavailable closeout authority fail closed with one bounded next
action. A lock owned by a dead local process is recoverable. Ordinary ART
progress does not falsely invalidate immutable material decisions.

### Visibility And Audit

Operators receive one session status and one next action. Canonical audit truth
remains distributed by ownership:

- OpenProject for ART work state and closeout;
- Git and GitHub for source, review, and merge;
- WGCF for durable artifact custody and readiness receipts;
- Security Architecture for the exact-head decision; and
- the finalized Review Packet for landing evidence.

The local session links these authorities but does not replace any of them.

### AI

This delta adds no model call, model-derived decision, prompt boundary, or
AI-enabled action path.

## Expansion Gates

The source decision is approved, but the following remain explicit gates:

1. OOS PR #142 must merge without changing the reviewed head.
2. Workspace Governance capability parity and operator guidance must activate
   only after the OOS merge through `#964`.
3. The activated path must dogfood restart, worktree relocation, cleanup,
   multi-item alias resume, and closeout before being described as the normal
   workspace operating path.
4. Shared runtime, stage, production, new credentials, remote state, or
   automated human-gate decisions require a fresh architecture and Security
   review.

## Decision

`approved`

Approval is limited to:

- OOS PR #142 at exact head
  `f50fcc4c44e96aebaa81c6be9728f559b0c0a15e`;
- local, secret-free, reconstructable work-session coordination;
- exact-base source reconstruction and bounded artifact reads;
- collision-free aliases and serialized session mutation;
- material historical-freshness evaluation;
- preservation of existing external human and machine authorities; and
- source merge before the separately governed activation and dogfood item.

Approval excludes:

- any changed OOS source revision;
- Workspace Governance activation before the OOS merge;
- claims of completed dev-integration dogfood or operating readiness;
- stage, production, shared, or public runtime use;
- durable evidence or approval authority in local session state;
- new identity, secret, remote storage, Temporal, or privileged runtime scope;
  and
- automated approval, merge, Security acceptance, or ART closeout.

## Related Artifacts

- [OOS work-session change record](https://github.com/mfshaf7/operator-orchestration-service/blob/f50fcc4c44e96aebaa81c6be9728f559b0c0a15e/docs/records/change-records/2026-08-23-delivery-art-work-session-lifecycle.md)
- [OOS Delivery ART lifecycle capability contract](https://github.com/mfshaf7/operator-orchestration-service/blob/f50fcc4c44e96aebaa81c6be9728f559b0c0a15e/contracts/delivery-art-lifecycle/capabilities.json)
- [Delivery ART evidence custody review](2026-08-09-art-evidence-custody-and-source-provenance.md)
- [Security delta review process](../security-delta-review-process.md)
- [Security review checklist](../security-review-checklist.md)
