# Governance Console Platform Operation Security Delta

## Summary

- date: 2026-10-15
- owner repo: `security-architecture`
- delivery initiative: `openproject://work_packages/1275`
- security acceptance item: `openproject://work_packages/1303`
- governed Platform item: `openproject://work_packages/1291`
- governing gate: `gate:platform-operation-security`
- architecture packet: `architecture-packet:delivery-1275-v1`
- architecture packet URI:
  `wgcf://artifacts/delivery-art/sha256/ea428f9ad9a14368aa9f789be278d3aac44def2cb2a4bc31caec7768f03335bb`
- architecture packet digest:
  `sha256:ea428f9ad9a14368aa9f789be278d3aac44def2cb2a4bc31caec7768f03335bb`
- reviewed exact revisions:
  - `governance-operations-console@9ae2edf5d5a4121ca198172225c65984494a3b72`
  - `operator-orchestration-service@c2bf368be17af127b344e236942049abf6d4ca3d`
  - `platform-engineering@b199a46e22b5e2d5f46b4f5f048018966b00dc5b`
  - `workspace-governance@9bf9d0485dd8292406464a73bc3b881503c52900`
  - `workspace-governance-control-fabric@18210752bc7450f7fed1fe62e8f41957c5031337`
- reviewed Platform tree:
  `platform-engineering-tree@c49a9c74abe4f16eef634e209aa528dd5df819e2`
- source reviews:
  - [WGCF continuity projection PR #109](https://github.com/mfshaf7/workspace-governance-control-fabric/pull/109)
  - [Console canonical continuity PR #81](https://github.com/mfshaf7/governance-operations-console/pull/81)
  - [OOS Platform-operation adapter PR #336](https://github.com/mfshaf7/operator-orchestration-service/pull/336)
  - [Platform complete-runtime PR #303](https://github.com/mfshaf7/platform-engineering/pull/303)
- decision: `approved`

Security accepts only this exact composed candidate for Platform source
publication, human exact-head review, protected merge, and subsequent bounded
local commissioning. The Platform commit is a clean local descendant of the
open PR head because the governing pre-merge gate correctly prevents OOS from
publishing it until this decision lands. Its exact tree is part of the decision
so the later merge commit cannot silently change the accepted composition.

This decision does not assert that commissioning or operating verification has
already passed. Platform work item `#1291` must still publish the accepted
candidate, rerun exact-head source evidence and CI, obtain human approval,
merge, and prove activation, restart, rollback, teardown, and restored normal
availability.

## Scope Delta

### Design Intent

The local Governance Operations Console reuses the existing
`refinement-catalog` composition. The browser calls only Console same-origin
routes. Console uses server-held OOS and WGCF credentials. OOS admits a finite,
operator-approved Platform command vocabulary and coordinates durable replay,
retry, cancellation, and readback. Platform alone performs the declared
dev-integration effects. Workspace Governance remains the canonical inventory
and product-lifecycle authority, while WGCF exposes one read-only continuity
projection for Console Registry and Portfolio views.

The trust split remains explicit:

- Console presents canonical reads and operator intent but owns no Platform,
  inventory, lifecycle, publication, release, or Security authority;
- OOS owns workflow admission, caller/operator binding, durable coordination,
  safe projection, and audit, but not Platform effects;
- Platform owns the finite operation catalog, effect execution, local runtime
  composition, credentials, recovery, and cleanup;
- WGCF validates and projects canonical continuity without mutation authority;
- Workspace Governance remains the source of inventory and product truth;
- Security accepts this exact boundary but does not perform its operations;
- the human reviewer remains the only source approver and merger.

### Implemented Control

The exact reviewed composition provides:

- an external Security decision contract whose gate, initiative, work item,
  Architecture Packet, five owner revisions, and Platform tree must all match;
- selection of that decision only from clean current Security `origin/main`,
  followed by mode-`0600` private materialization rather than a circular
  post-review source-pin commit;
- a finite Platform action set for start, status, access, smoke, stop, and
  promotion check, with no caller-selected URL, method, header, executable,
  secret, shell, or arbitrary input;
- exact command source version, canonical intent digest, operator approval,
  caller identity, idempotency identity, retry, cancellation, and terminal
  receipt bindings;
- an authenticated cluster-local OOS-to-Platform route with one generated
  composition credential kept out of source, browser payloads, receipts, and
  process arguments;
- persisted operation state before worker dispatch, exact PID plus kernel boot
  and process-start identity, lost-worker blocking, bounded retry, and
  cancellation only of the same live process group;
- canonical WGCF continuity validation, projection-digest verification, exact
  WGCF/OOS Registry reconciliation, and no fixture fallback while configured
  owner truth is loading or unavailable;
- runtime-only activation of
  `WGCF_WORKSPACE_CONTINUITY_PROJECTION_ENABLED=true` using the existing
  server-side Console WGCF credential, with literal-value verification and
  removal during rollback;
- explicit unavailable, stale, denied, failed, cancelled, and blocked states
  rather than inferred success; and
- bounded rollback, cleanup, and teardown that remove only the dedicated
  provider, OOS binding, Console/WGCF runtime bindings, generated credentials,
  and optional composition activation while preserving canonical owner and
  evidence state.

### Operating Evidence

This is a pre-merge composed-source decision. Operating readiness is
intentionally pending.

- WGCF PR #109 is merged, approved, and passed both exact-head validation
  checks; its projection was also exercised against the current committed
  Workspace Governance authority.
- Console PR #81 is merged, approved, and passed exact-head CI. Its owner check
  passed all architecture guards, 534 semantic tests, TypeScript validation,
  and the production build. Positive and negative cases cover cross-view
  identity, duplicate or contradictory lifecycle state, stale actionability,
  OOS drift, tampered projection digest, browser credential exclusion, and
  live-mode fixture-dashboard exclusion.
- OOS PR #336 is merged, approved, and passed exact-head CI. Security work item
  #1302 separately accepted its finite command, denial, disclosure, replay,
  recovery, and audit boundary.
- The clean Platform candidate passed the complete repository validation with
  the documented explicit OOS source root. Focused tests cover the finite
  catalog, stale Security denial, exact approval, conflicting replay,
  truthful terminal receipts, closed runner mapping, recovery, credential
  custody, incomplete rollback, and workspace-continuity activation and
  removal.
- The earlier Platform PR head passed both source CI and repository-posture
  CI. The accepted follow-up commit must still be published and pass those
  checks at its new exact head before merge.

No source test or this decision is represented as live commissioning evidence.
The `verify-operating` command and OOS operating-ready acquisition remain
mandatory after protected Platform merge.

## Review Areas

### Identity, Approval, And Secrets

The browser, Console machine caller, OOS caller/operator binding, Platform
provider caller, Security reviewer, Agent Gary author, and human reviewer are
distinct roles. Platform accepts only the configured OOS caller secret and the
exact `operator:workspace-owner` approval binding. The Console-to-OOS,
Console-to-WGCF, and OOS-to-Platform credentials remain server-side and are
stored only in private runtime files or Kubernetes Secrets. No machine identity
may approve or merge its own source.

This shared-secret arrangement is accepted only for the single-operator,
loopback and cluster-local `dev-integration` lane. It is not approval for
remote, shared, stage, production, or public access.

### Command And Effect Boundary

OOS and Platform independently validate the same finite action, subject,
source version, capability, intent digest, and operator approval. Platform
constructs every owner command itself. A caller cannot supply a repository,
path, command, argument, destination, or credential. Terminal Platform
receipts and current Console readback—not OOS coordination state alone—are the
effect evidence.

### Canonical Continuity And Disclosure

The WGCF endpoint is read-only and default-denied. Console recomputes the
projection digest and rejects unknown fields, duplicate identities,
cross-product readiness, changed authority revision, inconsistent lifecycle,
or disagreement with the OOS Registry projection. Registry mutation remains an
OOS workflow. Portfolio product identity and lifecycle remain canonical
Workspace Governance data. Live failure never selects fixture data, and the
browser receives neither a WGCF credential nor direct canonical-source access.

### Denial, Replay, Recovery, And Revocation

Missing or non-current Security evidence, a different Platform tree, changed
owner revision, dirty checkout, invalid credential, stale capability source,
wrong operator, malformed or conflicting intent, lost worker identity,
incomplete rollback, or unavailable owner dependency prevents normal
availability. Persisted command and control identities make exact replay
idempotent and conflicting replay invalid. A lost process becomes a visible
retryable blocker; PID reuse cannot authorize a signal.

Rollback removes the dedicated Platform provider and OOS binding and invokes
the existing Console cross-domain rollback, which also removes the continuity
enablement and its dedicated WGCF caller binding. Cleanup removes generated
private material. Teardown additionally suspends the reused composition. A
later Security decision with `status` other than `accepted`, a changed source
tree, or removal of the decision blocks fresh provider startup.

### Audit And Visibility

Receipts bind the Architecture Packet, Security decision digest and URI,
reviewed revisions, source version, bounded outcome, and non-secret proof.
Operation projections expose safe state, blockers, failures, event sequence,
receipt reference, and a safe log reference. The primary runbook identifies
the exact activation, status, restart, operating-proof, rollback, cleanup, and
teardown commands and distinguishes source proof from operating proof.

### Residual Risk And Commissioning Boundary

The local operating-system account and local Kubernetes administrator remain
inside the trusted dev-integration boundary. Partial activation can leave
visible runtime resources that require the documented rollback; it cannot
produce a success receipt when cleanup is incomplete. Availability and
performance on this single host remain operational concerns, not expanded
authorization.

The final fixture-free idea-to-product journey, including creation of a real
to-do application, remains owned by work item `#1298`. This decision does not
substitute component fixtures or source tests for that later proof.

## Decision

`approved`

Security emits `gate:platform-operation-security` for Platform candidate
`b199a46e22b5e2d5f46b4f5f048018966b00dc5b` with tree
`c49a9c74abe4f16eef634e209aa528dd5df819e2`, composed only with the four other
exact revisions listed in the Summary and the current Architecture Packet URI
and digest.

This approval permits publication of that candidate, fresh exact-head source
evidence, human review, protected merge, and bounded local commissioning. It
does not permit a component-only, stale, partial, dirty, synthetic-substitute,
or differently composed source set; fixture fallback; browser-held owner
credentials; a generic Platform command; Console-owned lifecycle state; stage
or production use; or a claim that operating readiness has already passed.

Any change to the accepted Platform tree, owner revision set, identity,
credential custody, action vocabulary, canonical-data authority, network
exposure, rollback boundary, or runtime profile requires a fresh Security
delta decision.
