# Governance Console Platform Operation Security Delta

## Summary

- date: 2026-10-16
- owner repo: `security-architecture`
- delivery initiative: `openproject://work_packages/1275`
- security acceptance item: `openproject://work_packages/1303`
- governed Platform item: `openproject://work_packages/1291`
- governing gate: `gate:platform-operation-security`
- architecture packet: `architecture-packet:delivery-1275-v1`
- architecture packet URI:
  `wgcf://artifacts/delivery-art/sha256/02840790fc36f5f8311d2d66cadec0d5e9ad98184aff3d88c6ff106a2d0afef4`
- architecture packet digest:
  `sha256:02840790fc36f5f8311d2d66cadec0d5e9ad98184aff3d88c6ff106a2d0afef4`
- reviewed exact revisions:
  - `governance-operations-console@8b7eac7066d05beae3234429e9e696e3feaa3e1c`
  - `operator-orchestration-service@5c75a8da879884bab924ac8d0a4476298c0ae7e1`
  - `platform-engineering@b5ff79ba09191dd141760fc2f4b0fa01ca14a2e2`
  - `workspace-governance@ec499fcbdd7d62687d704b9f9e50c87a601c48ee`
  - `workspace-governance-control-fabric@981aa6259b2dcc65d41dc739bddadbb395794973`
- reviewed Platform tree:
  `platform-engineering-tree@01542224d6948bd72183a084d70598da7860a317`
- source reviews:
  - [Platform public Console probe contract PR #312](https://github.com/mfshaf7/platform-engineering/pull/312)
  - [OOS retained request readback PR #344](https://github.com/mfshaf7/operator-orchestration-service/pull/344)
  - [Console canonical Repository register PR #84](https://github.com/mfshaf7/governance-operations-console/pull/84)
  - [Security bounded readback PR #264](https://github.com/mfshaf7/security-architecture/pull/264)
  - [Platform provisioning composition PR #311](https://github.com/mfshaf7/platform-engineering/pull/311)
  - [WGCF continuity projection PR #109](https://github.com/mfshaf7/workspace-governance-control-fabric/pull/109)
  - [Console canonical continuity PR #81](https://github.com/mfshaf7/governance-operations-console/pull/81)
  - [OOS Platform-operation adapter PR #336](https://github.com/mfshaf7/operator-orchestration-service/pull/336)
  - [Platform complete-runtime PR #303](https://github.com/mfshaf7/platform-engineering/pull/303)
  - [OOS evidence failure projection PR #337](https://github.com/mfshaf7/operator-orchestration-service/pull/337)
  - [OOS trusted-ancestor profile repair PR #338](https://github.com/mfshaf7/operator-orchestration-service/pull/338)
  - [Platform evidence-profile repair PR #304](https://github.com/mfshaf7/platform-engineering/pull/304)
  - [Platform private-state and rollback-order repair PR #305](https://github.com/mfshaf7/platform-engineering/pull/305)
  - [Platform governed recovery-successor record PR #306](https://github.com/mfshaf7/platform-engineering/pull/306)
  - [Platform reviewed-worktree source repair PR #307](https://github.com/mfshaf7/platform-engineering/pull/307)
  - [Platform final operating-proof successor PR #308](https://github.com/mfshaf7/platform-engineering/pull/308)
  - [OOS live-evidence process-boundary repair PR #339](https://github.com/mfshaf7/operator-orchestration-service/pull/339)
  - [OOS interrupted-acquisition recovery repair PR #340](https://github.com/mfshaf7/operator-orchestration-service/pull/340)
  - [Platform operating-proof receipt-replay successor PR #309](https://github.com/mfshaf7/platform-engineering/pull/309)
  - [WGCF historical architecture-lineage repair PR #110](https://github.com/mfshaf7/workspace-governance-control-fabric/pull/110)
  - [OOS Epic retirement field-shape repair PR #341](https://github.com/mfshaf7/operator-orchestration-service/pull/341)
  - [Workspace Governance Console operating-truth correction PR #281](https://github.com/mfshaf7/workspace-governance/pull/281)
  - [WGCF continuity-schema packaging repair PR #111](https://github.com/mfshaf7/workspace-governance-control-fabric/pull/111)
  - [Security repository-custody controlled-activation PR #261](https://github.com/mfshaf7/security-architecture/pull/261)
  - [OOS repository-custody activation PR #342](https://github.com/mfshaf7/operator-orchestration-service/pull/342)
  - [Console fixture-isolation PR #82](https://github.com/mfshaf7/governance-operations-console/pull/82)
  - [Console fail-closed resume PR #83](https://github.com/mfshaf7/governance-operations-console/pull/83)
  - [OOS gated-handoff compatibility PR #343](https://github.com/mfshaf7/operator-orchestration-service/pull/343)
  - [Platform current-composition candidate PR #310](https://github.com/mfshaf7/platform-engineering/pull/310)
- decision: `approved`

### Current Maintenance Acceptance

Verification-only maintenance Landing Unit
`maintenance-1275-runtime-probe-security` uses `child_isolated_landing_unit`
for this exact-tree decision refresh. The Platform candidate corrects the
commissioning probe to the observed public Console error contract. The Console
returns HTTP 404, code `repository_custody_oos_rejected`, and the exact
missing-request message; the old probe incorrectly required OOS's internal
error code. The candidate checks live mode, that exact public response, and
the missing-request identity. Wrong-route lookalikes, unauthorized results,
preview responses, and unexpected success still fail closed. It permits at
most thirty seconds of transport/502/503 recovery after the already approved
OOS rollout, without relaxing identity, canonical integrity, source acceptance,
or readiness requirements.

Focused tests cover the observed response, restart recovery, and false
readiness rejection. A read-only invocation of the corrected probe passed
against the actual accepted Console runtime before source publication. Full
Platform validation also passed at the committed candidate. No API, action,
credential, effect, provider, permission, or rollback authority changes; this
refresh accepts only the corrected read-only checker at the Summary's exact
head and tree. The earlier runtime-composition implementation is now merged
as Platform PR #311. Its source and activation state are not claimed to be a
passed commissioning proof; the corrected complete operating proof remains
required before final journey acceptance.

Maintenance Landing Unit `maintenance-1275-runtime-provisioning-security`
uses `child_isolated_landing_unit`: the exact-composition Security decision
has its own review and rollback boundary, independent from the Platform
implementation. It creates no new ART child or authority plane.

The current source dependencies are merged OOS PR #344 and Console PR #84,
whose bounded canonical request-enumeration boundary was accepted in Security
PR #264. The verification-only Platform successor is the pending candidate
and must remain unmerged until this exact decision lands. The Summary and YAML
decision above supersede all historical source identities below.

The Platform candidate restores the already accepted dedicated provisioning
App and organization installation through the existing Vault and identity
delivery path. It activates WGCF custody readiness, binds OOS to the dedicated
runtime Secret and a fixed operator-private persistent custody directory,
and projects only policy and credential-binding references to Console.
It does not borrow the existing-repository read identity, deliver a private
key to OOS, or grant automatic intake, inventory, Catalog, product, or release
authority. The separate read-only existing-repository identity is not claimed
operating by this provisioning composition.

Purpose-bound credential maintenance extends the existing user-systemd runtime
lifecycle. A fixed five-minute timer renews only the accepted App's token when
fewer than twenty minutes remain. Each run revalidates the exact current
Security decision, owner sources, materialized policy, and active marker before
using Vault or changing runtime. It holds the same lifecycle lock without
waiting; normal activation, proof, restart, and rollback hold that lock too.
Rollback disables renewal before revoking and removing the projection.
The timer has no caller-selected credential, repository, command, host, or
destination, and service arguments contain no credential values.

OOS receives its token at process startup. A stable non-secret token-expiry
annotation makes delivery consumption idempotent and recoverable if a host
crash occurs after Secret replacement but before the required OOS rollout.
Unchanged versions do not restart OOS. A new token performs one bounded rollout
and rechecks readiness while preserving persistent workflow state. Failed
Vault access, stale authority, or rollout failure produces non-success; neither
the timer nor its receipt can substitute an ambient identity or operating proof.

Generated provider, composition, and credential-maintenance services use the
surviving workspace main checkout only when clean main, remote main, and the
reviewed candidate have identical committed trees. Otherwise the candidate
path remains explicit and cannot be retired as if restart-ready. This closes
the proven missing-worktree startup regression without weakening source checks.

Implemented-source evidence covers private-key stdin handling and temporary
file custody; exact Secret/env/state bindings; canonical cold-browser readback;
early renewal, unchanged-version reconciliation, expired-token recovery,
stale-marker denial, lifecycle-lock contention, and bounded rollback.
Full owner validation and exact-head CI are required for the pending candidate.
The operating verifier rejects earlier partial receipts and must now prove
renewal, credential revocation, restart, teardown, restoration, the active
timer, and executable Console provisioning. Current live success remains
unproven by this source decision. Final journey work #1298 retains the real
fixture-free to-do exercise and browser-reload proof.

Security accepts only this exact reviewed composition for bounded local
commissioning. The exact Platform tree is part of the decision so later source
changes cannot silently alter the accepted runtime.

This decision does not itself assert current commissioning or complete-system
operating verification. Earlier work under Platform item `#1291` remains
historical component evidence and recovery history, not current completion.
The earlier `#1291` component proof did not compose repository provisioning.
Its completion is not current complete-system proof. This maintenance repair
requires exact-composition commissioning and status readback before work item
`#1298` may use the runtime for fixture-free journey evidence.

The prior-composition refresh accepted the later reviewed source identities
without widening the approved boundary. Architecture Packet v6 corrects the
gate sequence: Platform candidate PR #310 exists first at exact head
`305862655d2df3185ac74cdebc72cad9919e24e8` and tree
`f7888387a6dead537550b3f105b4c9b8295d807d`, Security accepts that candidate
here, and Platform remains unmerged until this exact decision lands. Workspace
Governance PR #281 corrects the declared Console operating truth; WGCF PR #111
packages the canonical continuity schema used by its existing projection;
Security PR #261 accepts bounded repository-custody activation; and OOS PR
#342 activates only that already reviewed custody manifest. Console PRs #82
and #83 isolate live records from fixtures and fail closed when resume context
is stale or unknown. OOS PR #343 preserves a compatible consumer session when
only the gated Security producer Landing Unit attempt changes while the same
gate, authority owner, work item, evidence contract, and accepted architecture
remain fixed. Those repairs narrow failure behavior and current source
identity; they add no Platform action, caller, credential, network exposure,
canonical-data authority, or rollback scope.

The replacement is a `child_isolated_landing_unit` Security delta because this
review and rollback boundary is independent from the Platform source repairs
and their documentation-only recovery successors.
It changes no identity, credential, action vocabulary, network exposure,
canonical-data authority, runtime profile, or rollback scope. It accepts the
existing OOS profile and recovery controls plus two bounded repairs: live
evidence executes outside the supervising executor process group, and an
interrupted merged acquisition may enter the existing evidence-preserving
replacement path without claiming readiness. Platform serializes the proof
with one operator-private lock and reuses only a digest-valid receipt bound to
this exact Security decision, reviewed revision set, complete proof shape, and
restored normal availability. Candidate commands remain untrusted, and
post-merge evidence remains bound to the accepted head without fallback.

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
- a fixed mode-`0700`, UID-1000-owned Platform state directory mounted only at
  `/var/lib/oos/platform-operation`, with no browser projection, caller-chosen
  host path, or credential storage in that directory;
- canonical WGCF continuity validation, projection-digest verification, exact
  WGCF/OOS Registry reconciliation, and no fixture fallback while configured
  owner truth is loading or unavailable;
- repository-custody activation only through the separately accepted bounded
  manifest, provider identities, and server-side credential path;
- live primary-record isolation from fixture records and fail-closed resume
  handling when no exact lifecycle record can be selected;
- runtime-only activation of
  `WGCF_WORKSPACE_CONTINUITY_PROJECTION_ENABLED=true` using the existing
  server-side Console WGCF credential, with literal-value verification and
  removal during rollback;
- explicit unavailable, stale, denied, failed, cancelled, and blocked states
  rather than inferred success; and
- bounded rollback, cleanup, and teardown that remove only the dedicated
  provider, OOS binding, Console/WGCF runtime bindings, generated credentials,
  and optional composition activation while preserving canonical owner and
  evidence state; and
- a host-local exclusive proof lock plus exact-decision receipt validation so
  executor replacement cannot repeat teardown or accept stale, malformed,
  partial, or different-revision operating evidence.

### Operating Evidence

This is an exact-source acceptance decision. All dependency revisions are
merged. The exact Platform candidate is open and intentionally unmerged until
this decision lands; complete Platform commissioning and fixture-free journey
evidence remain separate operating proofs.

- Workspace Governance PR #281 is merged and records the corrected current
  capability posture. WGCF PR #111 is merged and packages the corresponding
  continuity schema into the runtime artifact without changing WGCF mutation
  authority. Live work item `#1295` then returned HTTP 200 from both Console
  Registry and Portfolio continuity endpoints, with the same Workspace
  Governance authority revision and no canonical mutation. That readback is
  current operating evidence for the continuity projection only; it is not
  Platform commissioning or the final idea-to-product journey.

- WGCF PR #109 is merged, approved, and passed both exact-head validation
  checks; its projection was also exercised against the current committed
  Workspace Governance authority. WGCF PR #110 is merged, passed repository
  validation, and has a separate approved Security delta in PR #259. It changes
  only historical Architecture Packet supersession resolution and retains full
  active-subject validation.
- Console PR #81 is merged, approved, and passed exact-head CI. Its owner check
  passed all architecture guards, 534 semantic tests, TypeScript validation,
  and the production build. Positive and negative cases cover cross-view
  identity, duplicate or contradictory lifecycle state, stale actionability,
  OOS drift, tampered projection digest, browser credential exclusion, and
  live-mode fixture-dashboard exclusion.
- Console PRs #82 and #83 are merged, approved, and passed exact-head CI. PR
  #82 prevents live primary records from being populated by fixture data. PR
  #83 refuses stale or unknown resume context instead of silently selecting a
  different lifecycle record. Neither repair grants Console owner credentials,
  canonical mutation authority, or a broader action vocabulary.
- OOS PRs #336, #337, #338, #339, #340, and #341 are merged, approved, and passed
  exact-head CI.
  Security work item #1302 separately accepted the Platform-operation adapter's
  finite command, denial, disclosure, replay, recovery, and audit boundary;
  the OOS repair PRs narrow evidence-profile failure, process survival, and
  evidence-preserving recovery behavior without changing that command
  boundary. The Platform repairs correct the
  profile timeout, mount one fixed operator-private state directory into the
  non-root OOS container, remove the OOS binding before rollback waits for
  readiness, and keep composed source selection on the reviewed Platform
  worktree. They do not add an action, caller, credential, network exposure,
  or owner authority.
  OOS PR #341 changes only the existing OpenProject retirement adapter: an Epic
  may omit the Iteration field that its live form does not expose, while
  non-Epic retirement stays fail closed. It adds no Platform command, caller,
  credential, source-executor action, or Console authority.
- OOS PR #342 is merged, approved, and passed exact-head CI. It activates only
  the bounded repository-custody manifest accepted by Security PR #261 and
  pins the corrected Workspace Governance authority. It does not add a custody
  action, provider, permission, destination, or credential path.
- OOS PR #343 is merged, approved, and passed exact-head CI. It treats only a
  gated producer Landing Unit attempt-identity refresh as compatible when the
  same human gate, producer owner, producer work item, evidence contract, and
  accepted architecture remain fixed. Any gate or handoff semantic change
  still supersedes the consumer session. It changes no Platform command,
  caller, credential, network exposure, or owner authority.
- The generated Security change-record index includes OOS's merged
  `2026-10-15-repository-custody-source-activation` record, preserving the
  owner-to-Security evidence link at the reviewed OOS revision.
- Security PR #261 is merged, approved, and passed exact-head CI. It preserves
  fresh Platform credential delivery and downstream live journey proof as
  operating conditions rather than treating source activation as readiness.
- Platform PRs #304 and #305 are merged, approved, and passed exact-head CI.
  The complete repository validation also passed locally with the documented
  explicit OOS source root. Focused tests cover the finite
  catalog, stale Security denial, exact approval, conflicting replay,
  truthful terminal receipts, closed runner mapping, recovery, credential
  custody, private writable OOS state projection, failure-first rollback,
  incomplete rollback, and workspace-continuity activation and removal.
- Platform PR #306 is merged, approved, and passed exact-head CI. Its only
  changed surface is the commissioning record that binds PR #305, Security PR
  #254, the `r2` successor session, and the corrected PR #304 evidence lineage.
  The runtime implementation and evidence profile are byte-identical to the
  tree accepted by Security PR #254.
  Security binds the PR's exact reviewed head
  `11465f6b50a218e4282e1394c9cb2d307c6c34ae`, which is the source revision
  used by the governed post-merge evidence acquisition. Squash merge
  `df6844ded120c2325bb09d0b41dacc10fe33a44e` has the same accepted tree but
  is retained as merge evidence rather than substituted for the acquisition's
  source identity.
- Platform PR #307 is merged, approved, and passed exact-head CI. It makes the
  complete-runtime verifier forward its current Platform checkout to the
  shared composition and cross-domain controls, while preserving an explicit
  operator `--repo-path` override. Focused tests cover both selection paths;
  the change does not widen the source set or execution authority.
- Platform PR #308 is the documentation-only `r3` successor. Full local
  repository validation passed, protected review and merge completed, and its
  live proof exposed the executor process-group conflict before a result could
  be retained. The attempt was archived with its exact merge-ready packet and
  is not represented as operating-ready.
- Platform PR #309 is the `r4` receipt-replay successor. Full local repository
  validation passed against base
  `1549e86aff70d341fdb8d76219aebe84814d08d5`. Focused tests prove exact cached
  receipt reuse and rejection of stale or malformed receipts. Security binds
  its merged revision `068c6078755ec8a3df73e65f67131eb3e4cf07fa`
  and tree `0ce3a6aeedc81227f2e55ac06a7f93eb271065b2` before the governed post-merge
  operating-evidence acquisition. That tree is byte-identical to the reviewed
  PR head `328af66193a1f6e5a9118a2107106d2dba65aad2`.
- Platform PR #310 is the current-composition candidate. Its exact open head
  `305862655d2df3185ac74cdebc72cad9919e24e8` and tree
  `f7888387a6dead537550b3f105b4c9b8295d807d` bind the complete-runtime policy
  to Architecture Packet v6. Exact-head CI and the focused complete-runtime,
  provider, coordinator, and dev-integration tests pass. The PR remains
  intentionally unmerged until this Security decision is merged.

No source test or this decision is represented as current live commissioning
evidence. Earlier `#1291` attempts remain historical component evidence while
the item stays open for current exact-composition commissioning. Work item
`#1298` must then demonstrate that composition through the real Console journey
after activation and status readback.

The negative decision is equally binding: the prior Architecture Packet
digest or any prior Console, OOS, Workspace Governance, or WGCF revision set is
stale evidence and cannot authorize the composed Platform merge. Component-only
proof, a partial source set, or the `#1295` continuity readback by itself also
cannot satisfy `gate:platform-operation-security`.

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

The OOS binding is removed before cross-domain rollback waits for OOS
readiness. If environment or state-volume removal fails, cross-domain cleanup
is not represented as successful and the operator receives an incomplete
rollback result for bounded retry.

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

The dedicated OOS operation-state directory persists across pod restart and is
preserved when its mount is removed. It is restricted to the local operator
account and contains workflow state rather than the provider caller secret.
Host compromise remains inside the already accepted single-operator local
trust boundary.

The final fixture-free idea-to-product journey, including creation of a real
to-do application, remains owned by work item `#1298`. This decision does not
substitute component fixtures or source tests for that later proof.

## Decision

`approved`

Security emits `gate:platform-operation-security` for Platform candidate
revision `b5ff79ba09191dd141760fc2f4b0fa01ca14a2e2` with tree
`01542224d6948bd72183a084d70598da7860a317`, composed only with the four other
exact revisions listed in the Summary and the current Architecture Packet URI
and digest.

This approval permits activation, restart, and status readback of the exact
current composition and the later Console-only journey under `#1298`. It does
not permit a component-only,
stale, partial, dirty, synthetic-substitute, or differently composed source
set; fixture fallback; browser-held owner credentials; a generic Platform
command; Console-owned lifecycle state; stage or production use; or a claim
that operating readiness has already passed.

Any change to the accepted Platform tree, owner revision set, identity,
credential custody, action vocabulary, canonical-data authority, network
exposure, rollback boundary, or runtime profile requires a fresh Security
delta decision.
