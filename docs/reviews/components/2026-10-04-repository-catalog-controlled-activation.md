# Repository And Delivery Catalog Controlled-Activation Security Delta

## Summary

- date: 2026-10-04
- owner repo: `security-architecture`
- delivery initiative: `openproject://work_packages/1203`
- parent feature: `openproject://work_packages/1211`
- security evidence item: `openproject://work_packages/1230`
- governing architecture packet:
  `wgcf://artifacts/delivery-art/sha256/8bdc926a0ec2f591110480edda9516074fd9610906de7b9ca03c03b60b4d7d80`
- reviewed source:
  - Operator Orchestration Service reviewed head:
    `operator-orchestration-service@7e8f62b425f0e7f64337ec5b4d2e8fb02ddfaad4`
  - Operator Orchestration Service merge:
    `operator-orchestration-service@92f0967242f535b46aad9e585c72694c6ff1863b`
  - Governance Operations Console reviewed head:
    `governance-operations-console@4c7b4da1c65eb4018aff0297ea09fc15e0f910ac`
  - Governance Operations Console merge:
    `governance-operations-console@9347794a138f3649bb6ef5b7db057524d1c1e26d`
  - Workspace Governance authority baseline:
    `workspace-governance@9718ce9eea04049541a1fb44f0b7cdc0ac823687`
  - Workspace Governance Control Fabric readiness baseline:
    `workspace-governance-control-fabric@f296a8bf91bcc22272f0079cf2b0aec6fe431fdf`
- finalized source evidence:
  - OOS Review Packet:
    `wgcf://artifacts/delivery-art/sha256/9ec2308ade2e5ee1825893f94ff42a47702ae9810720ede4e7aacdcd597db327`
  - Console Review Packet:
    `wgcf://artifacts/delivery-art/sha256/9687d40324fb3ba4b9d9a60ef63359554d7e0bec8ff5c59361668b59121b614f`
- decision: `approved-with-findings`

This review accepts the exact merged first-use Repository-to-Catalog source for
bounded, single-operator, loopback `dev-integration` commissioning by Platform
work item `#1231`. It emits
`gate:repository-catalog-controlled-activation` for those exact revisions.

The decision is source acceptance, not operating proof. Platform must still
prove the configured OOS, Workspace Inventory, WGCF, Catalog-control, Console,
credential, restart, denial, rollback, and cleanup boundaries before the
Feature can claim routine availability. The architecture packet intentionally
captures the OOS predecessor used to start `#1228`; this review binds the exact
merged OOS successor above and does not permit any other unreviewed successor.

## Scope Delta

### Design Intent

- let an admitted active Workspace Inventory repository become an exact Owner
  Repo Catalog candidate without granting the Console direct WGCF or backend
  authority;
- keep Workspace Governance as repository-authority owner, WGCF as readiness
  decision and receipt owner, OOS as orchestration and Catalog mutation owner,
  and the Console as the same-origin operator surface;
- make first-use readiness issuance and later mutation-time revalidation one
  continuous, fail-closed identity chain;
- preserve reviewed operator acceptance, deterministic retry, canonical
  readback, durable receipts, human source review, and owner-bounded rollback;
  and
- commission only the existing accepted-idea-delivery local composition after
  exact-revision Security acceptance.

### Implemented Control

OOS adds an authenticated repository-readiness preparation route. It reads the
active repository and the whole current `contracts/repos.yaml` digest through
the Workspace Inventory authority boundary, rejects inactive or inconsistent
records, and asks WGCF to issue or replay the readiness decision for the exact
repository identity and authority digest. OOS accepts only a ready,
linking-allowed, non-mutating, durable, content-addressed decision whose
subject, Catalog value, target scope, receipt identity, generation, evaluation
time, ledger reference, and authority digest agree.

The route neither changes Repository nor Catalog state. Existing Catalog
mutation remains a separate reviewed action and revalidates readiness before
the bounded backend mutation and canonical readback. A changed authority
digest therefore becomes stale instead of silently reusing old evidence.

The Console calls only its same-origin server route. The server obtains the
readiness reference from OOS for the exact selected active Repository when
canonical Catalog truth does not already carry it. The browser cannot supply
OOS credentials, call WGCF or OpenProject, synthesize a receipt, broaden the
repository identity, or convert navigation and draft creation into mutation.
Catalog mutation and Delivery work-item linking remain distinct receipts, and
partial failure retains the OOS reconciliation action.

### Operating Evidence

The OOS source evidence covers 1,208 tests with no failures, 41 focused Catalog
and Workspace Inventory protocol tests, 12 real-Git authority checks,
base-aware governance and contract validators, generated API/schema checks,
and a production dependency audit with no reported vulnerability. Positive
and negative cases include active, inactive, inconsistent, stale, malformed,
unauthorized, replayed, and mismatched authority or receipt evidence.

The Console source evidence covers its Repository protocol check at the exact
reviewed head and binds same-origin navigation, first-use readiness
preparation, existing-value selection, missing-value draft creation, work-item
linking, receipt projection, configured failure, and no browser-side WGCF or
backend authority. Both exact heads received human review, passed their
required checks, merged to `main`, and closed through finalized Review Packets.

This remains source and contract evidence. It does not prove that the current
runtime has selected these exact revisions, projected distinct caller secrets,
reached current Workspace authority and WGCF, performed a real first-use
issuance, reconciled Catalog readback, survived restart, or cleaned up without
affecting unrelated state. Those are mandatory `#1231` proofs.

## Review Areas

### Identity And Authorization

The browser is not a WGCF, Workspace Governance, or Catalog-control caller.
The Console server may call only OOS under the existing Console application
identity; OOS uses separately admitted identities for WGCF and the bounded
Catalog backend. Caller identity, operator acceptance, repository name and
reference, Catalog value key, authority digest, readiness receipt, source
revision, mutation target, idempotency identity, backend result, and readback
must remain bound across the handoff.

The local operating-system account and configured Console operator remain the
human trust root for this lane. This review adds no shared, remote, multi-user,
stage, or production identity claim. Machine identities may not approve or
merge their own source work.

### Secrets And Data Minimization

Platform retains caller-secret custody and projects each secret only to its
declared server-side consumer. The browser receives the minimum validated
Repository and receipt projection; it does not receive internal endpoints,
caller credentials, raw Workspace Governance records, WGCF payloads, backend
tokens, private filesystem paths, or owner diagnostics.

Credentials and raw private payloads must remain absent from source, browser
state, logs, ART text, Review Packets, and durable receipts. The public
reference contains only bounded identity, scope, outcome, generation,
timestamp, URI, and digest values.

### Authority, Replay, And Evidence Integrity

Workspace Inventory reads the repository record and whole inventory digest at
one exact Workspace Governance revision. WGCF independently compares the
expected whole-file digest to current authority. Change between those reads
must return a stale or non-ready outcome with no usable reference.

WGCF evidence grants linking readiness only and explicitly carries no mutation
authority. OOS remains responsible for mutation-time revalidation, exact
operator acceptance, replay conflict rejection, bounded backend mutation, and
canonical readback. The Console must not infer success from a prepared
reference, an accepted request, navigation state, or a partial Delivery change
result.

### Runtime, Failure, Rollback, And Cleanup

Configured failure must stay unavailable. Missing configuration, inactive or
retired repository posture, changed authority, malformed response, wrong
subject, wrong receipt, unauthorized caller, dependency failure, backend
conflict, incomplete readback, interrupted execution, or replay conflict may
not fall back to fixture truth or local success.

Platform `#1231` must bind the exact revisions and architecture digest above;
use distinct server-only caller secrets; prove the positive first-use and
existing-reference paths; prove stale, unauthorized, malformed,
owner-unavailable, WGCF-unavailable, and backend-failure paths; and prove
restart, revocation, rollback, teardown, and preservation of canonical source
and evidence. Rollback disables the composition or reverts only the affected
owner Landing Unit. It must not delete Repository, Catalog, Git, ART, WGCF, or
audit history or disturb unrelated active profiles.

### AI

No model chooses repository identity, evaluates readiness, authorizes Catalog
mutation, supplies credentials, validates readback, approves source, or
establishes completion. AI output remains advisory and outside this authority
chain.

## Findings And Activation Conditions

1. **The exact composition is not yet operating-proven.** Platform `#1231`
   must select and prove the reviewed revisions and the complete positive and
   negative path before routine availability is claimed.
2. **Human identity remains local and single-operator.** Authenticated shared,
   remote, stage, or production use requires separate identity architecture,
   commissioning evidence, and Security review.
3. **Prepared readiness is not mutation success.** Only a current revalidated
   reference, bounded Catalog mutation, canonical readback, and the required
   Catalog and Delivery receipts can project completion.
4. **Configured live mode cannot fall back.** Any missing, stale, malformed,
   conflicting, unauthorized, partial, or unavailable owner truth remains a
   visible non-success state.
5. **Architecture and source successors are exact.** Platform must bind the
   packet digest plus the reviewed OOS and Console merges above. A different
   source successor, caller, authority, endpoint, or credential projection
   requires a fresh delta review.

These conditions are routed to existing Platform work item `#1231`; they do
not require a duplicate defect or remediation item.

## Decision

`approved-with-findings`

Approved:

- the exact OOS and Console reviewed heads, merged revisions, and finalized
  Review Packets above;
- current Workspace Governance repository authority and WGCF readiness as the
  only admitted upstream sources for this boundary;
- OOS-mediated first-use readiness issuance and mutation-time revalidation;
- the same-origin, server-only Console handoff with no browser credential or
  backend authority;
- bounded Platform commissioning and evidence collection under `#1231`; and
- `gate:repository-catalog-controlled-activation` for those exact inputs.

Not approved:

- routine operating readiness based on source tests or this review alone;
- direct browser access to WGCF, Workspace Governance, OpenProject, or Catalog
  control;
- Repository or Catalog mutation from readiness preparation;
- synthetic, stale, malformed, mismatched, or partial evidence as success;
- fixture fallback after live configuration is selected;
- shared, ambient, personal, long-lived, or browser-held credentials;
- machine self-approval or merge, direct-main source writes, or success before
  canonical readback; or
- stage, production, public, remote, or multi-user exposure.

## Related Artifacts

- [Refinement and Catalog dev-integration boundary review](2026-08-26-refinement-catalog-dev-integration-boundary.md)
- [Repository provisioning authority review](2026-08-29-repository-provisioning-authority.md)
- [Repository lifecycle authority review](2026-08-30-repository-lifecycle-authority.md)
- [Workspace Intake and Inventory controlled activation](2026-10-02-workspace-intake-inventory-controlled-activation.md)
- [Security delta review process](../security-delta-review-process.md)
- [Security review checklist](../security-review-checklist.md)
- [OOS pull request #278](https://github.com/mfshaf7/operator-orchestration-service/pull/278)
- [Console pull request #50](https://github.com/mfshaf7/governance-operations-console/pull/50)
