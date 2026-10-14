# Bounded Source Realization Security Delta

## Summary

- date: 2026-10-15
- owner repo: `security-architecture`
- delivery initiative: `openproject://work_packages/1275`
- security acceptance item: `openproject://work_packages/1286`
- reviewed owner repo: `operator-orchestration-service`
- reviewed pull request:
  [operator-orchestration-service #331](https://github.com/mfshaf7/operator-orchestration-service/pull/331)
- reviewed exact revision:
  `operator-orchestration-service@c2ed4aba7da8264623595ae7910aded4ba1c56a0`
- architecture packet: `architecture-packet:delivery-1275-v1`
- architecture packet digest:
  `sha256:ea428f9ad9a14368aa9f789be278d3aac44def2cb2a4bc31caec7768f03335bb`
- decision: `approved`

Security approves the exact reviewed OOS revision for merge as the bounded
source-realization implementation. This decision does not activate the runtime,
commission a model profile, approve a network exposure, replace human review,
or authorize merge by a model or Agent Gary.

The initial review found an audit-binding mismatch between the canonical
change-set digest accepted by the operator and the order-sensitive digest used
by the source executor's receipt and commit trailer. Revision `c2ed4ab` repairs
that mismatch and adds real-Git assertions that the accepted, committed,
receipted, and replayed change set carries one canonical digest. No open
finding remains from that review.

## Scope Delta

### Design Intent

The Console will submit a source objective for one active Delivery work
session. OOS captures bounded repository context, sends it through CGG, invokes
only the governed `source-realization-v1` model profile, validates the returned
change-set contract, and retains generated content in private workflow custody.
An operator accepts the exact staged digest before OOS asks the isolated source
executor to create one Agent Gary commit. The existing work-session lifecycle
then validates, publishes, reviews, and merges that exact head.

The trust split remains explicit:

- the model drafts data and has no shell, repository credential, approval,
  Security, ART, review, or merge authority;
- OOS owns orchestration, identity binding, durable replay, and state
  projection;
- CGG owns context admission, redaction, budget, and model-safe projection;
- Agent Gary alone authors source on the one recorded branch and repository;
- the human reviewer still approves and merges the exact pull-request head;
- Security accepts this trust boundary but does not implement or operate it;
- Platform may commission only the later exact reviewed composition.

### Implemented Control

The reviewed delta from OOS `main` at
`943a8b42e6e4d7a0848c200fafd57b0f424c6dcc` through `c2ed4ab` adds:

- authenticated, caller-bound read, start, continue, cancel, and recover APIs;
- a disabled-by-default runtime requiring both explicit enablement and a
  configured governed-AI gateway;
- strict start and change-set schemas with bounded objective, operation,
  content, path, and response sizes;
- exact work-session, operator, caller, Landing Unit, base commit, objective,
  context, profile, request, revision, and digest binding;
- CGG-only model-safe context projection with receipt and audit references;
- duplicate-path, path traversal, `.git`, symlink, credential-shaped filename,
  stale-content, dirty-worktree, and source-drift denial;
- private staged draft custody whose public projection exposes paths and
  digests but not generated source content;
- isolated real-Git apply with Agent Gary identity, a canonical digest commit
  trailer, exact changed-path verification, and pre-commit file restoration;
- durable request and action replay, unknown-apply reconciliation, cancellation,
  explicitly linked retry, and terminal receipts;
- current Architecture Packet enforcement for new work, compatible packet
  refresh for an unchanged active Landing Unit, and historical dependency
  validation that cannot authorize stale new work.

### Operating Evidence

This is a pre-merge source decision. Operating activation is intentionally not
claimed. Against exact OOS head `c2ed4ab`:

- the full serial owner suite passed 1,309 tests with two intentional skips and
  zero failures;
- focused real-Git source-realization and recovery tests passed;
- governance documentation validation passed;
- all 171 implemented and documented API routes matched;
- the source-backed change-record requirement passed;
- the OpenProject mutation contract validator reported no mutation-contract
  change; and
- `git diff --check origin/main...HEAD` passed.

Platform commissioning and live Console proof remain later, separately owned
steps. Their absence does not weaken this merge decision because this revision
keeps the new runtime disabled by default.

## Review Areas

### Identity And Authority

The authenticated Console caller and attributed operator must match the active
work session. The source executor receives the same bounded execution context.
Agent Gary is restricted to the exact admitted repository, branch, base, and
Landing Unit. Neither the model nor OOS may satisfy the human exact-head review
or protected merge requirement.

### Context And Disclosure

Repository content is captured only from a clean managed worktree, bounded by
file count and byte limits, and submitted through the existing CGG lifecycle
projection. OOS consumes only a model-safe packet with redaction, projection,
artifact, and audit bindings. Public realization status omits generated source
content and secret values. The later human review occurs against the ordinary
exact pull-request diff.

### Denial And Fail-Closed Behavior

Uncommissioned runtime, wrong identity, stale session revision, dirty or
changed source, wrong model profile, invalid result binding, unsafe path,
duplicate target, unexpected digest, oversized output, conflicting replay, and
unreconciled apply outcome all stop progress. None of those states grants merge
or silently falls back to a generic shell or raw model context.

### Replay, Recovery, And Rollback

Request and command identifiers bind immutable digests. Only the immediately
preceding terminal attempt may be retried. An unknown apply is reconciled
through the same accepted action. Before commit, failed application restores
the original files and index. After commit, source stays isolated on the
Landing Unit branch until validation, Security acceptance, exact-head human
review, and merge complete.

### Audit Integrity

The durable record retains the context packet, redaction receipt, projection
receipt, model profile selection, model audit reference, objective digest,
change-set digest, action state, failure, and source receipt. The exact same
canonical change-set digest now binds operator acceptance, executor receipt,
commit trailer, and replay reconciliation.

### Residual Risk And Activation Boundary

Model quality can still produce an unusable draft; the operator may cancel it
or explicitly retry after a terminal attempt. That is a contained product
outcome, not silent source authority. The reviewed source does not itself prove
the deployed gateway endpoint, model profile, restart recovery, Console UX, or
end-to-end product journey. Those operating boundaries remain gated by the
separately planned orchestration, Platform, Console, and final-journey work in
Epic 1275.

## Decision

`approved`

OOS revision `c2ed4aba7da8264623595ae7910aded4ba1c56a0` may proceed to
exact-head human review and protected merge. Approval is invalid for any later
OOS head unless a fresh Security delta explicitly accepts it. Runtime activation
must remain disabled until the separately owned exact Platform composition and
Security operating-boundary decisions are complete.
