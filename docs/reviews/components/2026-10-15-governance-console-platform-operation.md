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
  - `governance-operations-console@1d19fc2a0cc809a42905688296baf42793b7e066`
  - `operator-orchestration-service@4c74d35b09864c12b4a63beb4fa8a23416381e70`
  - `platform-engineering@52b71766dc4cf4eaa028aff45a4c57b5b569a51d`
  - `workspace-governance@ec499fcbdd7d62687d704b9f9e50c87a601c48ee`
  - `workspace-governance-control-fabric@7077ddf671e8697f1f09712023e3535556dfd2f1`
  - `workspace-prototype-studio@14dfcb5fad6272eabdc3edde55c1c26b017a4f3f`
- reviewed Platform tree:
  `platform-engineering-tree@43d24473dde30f0ec9a480c7ec731b6cb7e99b78`
- source reviews:
  - [Platform grouped readiness caller and issuer reconciliation PR #318](https://github.com/mfshaf7/platform-engineering/pull/318)
  - [Platform post-crash health PR #317](https://github.com/mfshaf7/platform-engineering/pull/317)
  - [OOS bounded dependency reads PR #349](https://github.com/mfshaf7/operator-orchestration-service/pull/349)
  - [Platform records and realization composition PR #316](https://github.com/mfshaf7/platform-engineering/pull/316)
  - [OOS canonical reads and realization bindings PR #348](https://github.com/mfshaf7/operator-orchestration-service/pull/348)
  - [Console fixed Preview freshness boundary PR #88](https://github.com/mfshaf7/governance-operations-console/pull/88)
  - [Console live registers and realization controls PR #87](https://github.com/mfshaf7/governance-operations-console/pull/87)
  - [WGCF current record snapshots PR #114](https://github.com/mfshaf7/workspace-governance-control-fabric/pull/114)
  - [Platform identity producer ownership correction PR #315](https://github.com/mfshaf7/platform-engineering/pull/315)
  - [Platform complete workflow credential lifecycle PR #314](https://github.com/mfshaf7/platform-engineering/pull/314)
  - [OOS partial provisioning baseline PR #346](https://github.com/mfshaf7/operator-orchestration-service/pull/346)
  - [Console retained correction and resume PR #86](https://github.com/mfshaf7/governance-operations-console/pull/86)
  - [WGCF bounded custody source activation PR #113](https://github.com/mfshaf7/workspace-governance-control-fabric/pull/113)
  - [Security WGCF source-activation approval PR #269](https://github.com/mfshaf7/security-architecture/pull/269)
  - [WGCF installed contract packaging PR #112](https://github.com/mfshaf7/workspace-governance-control-fabric/pull/112)
  - [Platform canonical resolution state PR #313](https://github.com/mfshaf7/platform-engineering/pull/313)
  - [OOS canonical Repository gate PR #345](https://github.com/mfshaf7/operator-orchestration-service/pull/345)
  - [Console live Repository gate PR #85](https://github.com/mfshaf7/governance-operations-console/pull/85)
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

#### Existing readiness caller and exact issuer reconciliation — 2026-10-16

The Summary's exact merged Platform source supersedes the earlier Platform
pin for this bounded maintenance delta. A real Proposal1305 Console Landing
request exposed stale credentials in the three dedicated Prototype consumer
Secrets. Full-process inspection covered every current OOS WGCF caller and
issuer expectation: shared credentials already match the current OOS registry
principal; Landing, Maturity and Closure copies do not. Their three expected
issuer revisions and Product Publication's expectation are historical, while
Workspace Intake already expects the current image. The caller is one
existing OOS registry principal; GitHub Apps and source permissions remain
separate. This does not create a new caller, role, source-writing purpose,
credential issuer, service, publication path, provider or exposure.

Platform now proves the active operator WGCF session, exact API credential
reference, owner activation, current Secret source, consumed credential and
actual image revision against the Security-accepted source set before
reconciliation. Only the three already-declared `wgcf-caller-secret` keys may
change. Original producer SSA ownership and resourceVersion CAS preserve
unrelated fields and concurrent-update denial. Caller-only correction does
not mint GitHub credentials. The existing grouped delivery marker additionally
uses Secret resource versions, so caller-only replacement and interrupted
consumption cause one required rollout, not a permanent stale process or an
unchanged-tick restart.

The same grouped operation binds all five existing consumer issuer
expectations to the current accepted WGCF revision, without changing their
enablement or privileges. Historical identity activation source remains
historical evidence. Pre-reconciliation admission permits the repairable stale
consumer expectation; issuer-source verification is still exact before any
write. Post-consumption checks reject stale active consumer expectations,
wrong caller values, unconsumed Secrets and failed authenticated readiness
reads. OOS's exact issuer, service-identity and receipt checks are unchanged.
No wildcard, automatic trust of an unreviewed image, credential value in argv
or output, browser token, fixture fallback or readiness bypass is accepted.

Engineering evidence: final Gary head
`64cf9f32d5093b7de5b6c8fa859b1917a8cdafb2` has the exact Summary tree and
merged as Platform PR318. Full committed local CI-equivalent `make validate`
passed with the canonical OOS source and fetched base
`6d7536e6f5f6815bb088214f16acbd5aabcbc00f`; CI38905153533 and Security
Posture38905153556 passed. All53 native/focused tests passed without skips,
including actual producer Secret/CAS recovery and real reviewed-issuer
positive/wrong-revision denial. The generated Node probe is executed for
staging, consumed caller, Prototype/publication issuer and HTTP denial cases.
These are source/engineering results, not a claim of applied operating proof.

Decision: `approved` for the exact local source set. Normal coordinated
activation, grouped caller/issuer consumption proof and continuation of the
SAME retained Landing request are required before maintenance completion.
Prototype source generation and Delivery-packet authoring remain unaccepted
operating capabilities; no real to-do product or Epic completion is asserted.

#### Post-crash health delta — 2026-10-16

The Summary source set supersedes the preceding maintenance pins. It accepts
all five existing local Ollama bindings at exactly `0.40.5`, retaining the
approved `qwen3:8b` digest
`500a1f067a9f782620b40bee6f7b0c89e17ae61f686b92c24933e4ca4b2b8b41`.
This is the operator-requested installed patch, not automatic acceptance of
future updates. Readiness now checks actual provider metadata with one-second
requests, no retry or inference, shared across identical bindings. Eligibility
and readiness remain distinct; version/digest mismatch and unavailable
providers deny readiness. Every invocation still repeats integrity checks.

Unchanged record refresh retains a still-valid checkpoint until atomic
replacement. Actual source changes invalidate both fixed owners before any
changed checkout; failed observation invalidates both owners, and a later
changed member cannot leave a refreshed peer without re-observation. The
existing five-minute expiry, source ancestry, allowed-path/mode boundaries,
read-only consumer mounts and credential-renewal independence remain intact.
Invalidation must not follow a clone or Git-directory symlink.

OOS reads dependency relations through its existing authenticated `involved`
API in batches of at most 100 IDs. Both endpoints, pagination, deduplication,
external dependency hydration and backend-error denial retain their existing
semantics. No cache, write route, readiness waiver or authority is added.

Engineering evidence: exact-head full Platform validation and CI passed;
metadata integrity includes a real local HTTP server; native Git/group
continuity and failure tests passed; both actual read-only consumer images
passed at a distinct UID. OOS passed 1,370 tests (two intentional skips),
CI-equivalent checks, native API/worker image builds and isolated smoke. Its
205-item fixture proves pagination and cross-batch dependency completeness.
These are engineering results, not post-activation operating claims. Current
provider, synthetic governed inference, refresh continuity and Console latency
must still be read back after exact-source activation.

Decision: `approved` for this exact local maintenance source set. No new
model/provider, source-writing purpose, repository installation, public
exposure, stage/prod authority or Prototype authoring path is granted. Epic
1275 and the real to-do exercise remain unfinished.

The preceding maintenance Landing Unit `maintenance-1275-console-journey-security` used
`child_isolated_landing_unit` for the existing exact-composition decision.
Recommendation posture is `extend`: retain Studio source ownership, OOS
workflow authority, WGCF read/evaluation authority, Platform runtime custody,
CGG context admission, Gary source authorship and human review/merge.
No new service, identity, provider, installation scope or generic command
authority is introduced.

Design intent: separate fixed reviewed control code from changing canonical
business records; restore the missing primary Prototype and Delivery reads;
commission the existing bounded Delivery source-realization mechanism and
fixed Studio Preview adapter. A fixture-free, all-route product qualification
remains a different obligation. This decision does not certify that a Prototype
can already be authored, that its Delivery packet can be created from the
Console, or that the real to-do app exists.

Implemented controls reviewed at the Summary's exact source set:

- Platform alone refreshes two private Git snapshots from the fixed canonical
  Workspace Governance and Studio providers. Only record/inventory paths and
  Studio incubation app source may advance from reviewed ancestry. Governing
  control code, schemas, skills, policy, executable modes, symlinks, unrelated
  paths, history rewrite and dirty local source are denied. It does not pull
  or rewrite primary execution checkouts. Candidate refs are not trusted until
  admission succeeds, and unique local work is preserved rather than reset.
- A five-minute atomic owner/ref/reviewed-revision/record-revision checkpoint
  authorizes read-only consumer snapshots. OOS and WGCF independently validate
  regular bounded files, exact Git identity and ancestry, source shape, timing
  and expiry. The existing credential timer checks every minute. Refresh
  failure invalidates record authority but does not skip the existing
  purpose-bound credential renewal. Neither a cached record nor a timer
  receipt is a canonical business approval.
- Console consumes only validated canonical envelopes for the actual nested
  ART register and Studio registry/captures. Empty live collections are valid;
  unavailable or conflicting authorities do not fall back to fixtures.
  Cold workflow reconstruction preserves actual owner receipts, and live
  Maturity projection no longer invokes fixture transition helpers or adds
  prototype-local evidence. Existing dialogs expose progress, review, failure,
  continuation and cancellation instead of silently discarding async failures.
- Delivery source realization uses only `source-realization-v1`, the existing
  pinned local Ollama `qwen3:8b` binding, single concurrency, zero automatic
  retries and bounded input/output/latency. Gateway caller workflow and
  Platform-owned structural schema now match the actual registered contract.
  OOS independently validates stricter change-set semantics and keeps contents
  private. The Console exposes objective, paths and digest approval through
  authenticated same-origin routes, never model tools or provider credentials.
  Only exact-digest acceptance reaches Gary's existing isolated executor;
  ordinary exact-head validation, human review and merge remain mandatory.
- An interrupted accepted generation may be cancelled with a substantive
  reason before source acceptance and retried with explicit predecessor
  binding. Applying/unknown application still requires same-action recovery;
  cancellation cannot conceal an uncertain source mutation.
- The fixed Studio Preview command executes reviewed owner code against its
  independently verified fresh record revision. Its private cache and state
  paths are deployment-owned, not browser-selected. The existing loopback,
  static-only, no-external-network source and profile checks remain in force.
- Normal complete-runtime activation and the finite provider start action
  reuse the existing admitted composition oneshot. Its product-owned drop-in
  retains helpers after controller exit and reapplies the whole reviewed
  composition rather than raw profile startup. Delegation happens before the
  lifecycle lock; inner activation does not recursively wait on its own lock.
  Uncached full proof requires retained supervision. The long-running web
  service restarts on unexpected successful exit as well as nonzero exit;
  explicit operator stop still remains stopped.
- Current clean Security `origin/main` and the complete decision/review
  contents are revalidated on every resolution. Provenance uses the last
  commit touching the four relevant acceptance files, so an unrelated generated
  index update does not force recommissioning. Changed/revoked decisions or
  relevant reviews do change the anchor and invalidate old bindings. Exact
  Platform tree and non-data owner source changes remain gated.
- Status proves actual read-only mounts, exact paths/owners, guard/profile
  values and consumed deployment generations, then the gateway profile and
  both live primary Console models. Homepage health alone is insufficient.
  Rollback restores primary owner mounts, disables the new guards and
  realization, removes only the product drop-in and preserves canonical
  history, cached unique work, Preview state and the generic profile unit.

Engineering evidence: OOS 1,369 passing tests with two intentional skips and
actual API/worker build/smoke; Console 559 passing semantic tests, guards,
types, safety/audit and exact-head CI production build; WGCF 519 passing tests
and actual non-root API/worker proof; Platform full local CI-equivalent
validation on committed Gary head `2c624ca935b725187077dc9385c901d953be019e`
after fetching base `31a12981a9f69f9c9f7006d3946f42ed5d611374`, including
Helm/Terraform, 45 complete-runtime cases (three native Kubernetes opt-in skips)
and 27 cross-domain cases. Eight native producer/actual-image cases prove fresh
acceptance and expired denial in actual built OOS/WGCF images, UID10001,
read-only mounts and no network. Platform CI `38885146994` and posture
`38885146870` passed; merged Platform tree equals that reviewed candidate tree.
These are source/engineering results, not substituted live product proof.

Decision: approve commissioning and bounded use of this exact single-operator,
loopback/cluster-local `dev-integration` composition. Source-only realization
approval is extended only by the corresponding operating-boundary delta and
this exact set. Primary checkouts must move together to the accepted set;
current operating readiness requires actual source-bound runtime readback.
Full lifecycle qualification and all three admitted ingress routes remain
required before Epic completion. Known missing Prototype authoring/handoff,
new-owner admission and product evidence are not silently waived, supplied by
hidden CLI mutation or replaced by successful screen health. Broader identities,
new repository scope, Prototype source-generation authority, publication,
remote access, stage and production are not granted by this maintenance review.

### Prior Workflow Credential Maintenance Acceptance

Maintenance Landing Unit `maintenance-1275-workflow-credential-lifecycle-security`
uses `child_isolated_landing_unit` for the existing exact-composition decision.
This accepts the bounded Platform renewal/readiness extension requested after
the real Console journey exposed expired downstream identity credentials.
Only Platform's revision/tree changes; the other Summary owner revisions,
architecture, operator approval, source gates and permission limits remain.

Design intent: maintain the five already-commissioned Proposal Target,
Prototype Landing, Prototype Maturity, Prototype Closure and Workspace Intake
credentials through the existing complete-runtime timer. Provisioning-only
renewal and a running pod did not prove those workflow prerequisites.

Implemented control: the closed App/installation set is source-bound, with
repository, permissions, Vault paths and credential-binding digests derived
from the existing owner identity contracts. Missing, disabled, differently
owned or wrong-profile bindings fail closed; renewal does not commission a
workflow, change provider scope or create source, product, ART or approval
authority. Existing App validation is reused and every replacement grant is
validated before the first Secret changes. Failed preparation revokes new,
unprojected grants. No human, ambient or other workflow token is substituted.

Replacement uses the original producer's server-side Apply operation and exact
field manager, with Kubernetes resource-version compare-and-swap. A native
pre-activation test caught PR314's replace operation transferring ownership and
breaking later producer recovery. This same maintenance scope corrects that
miss before live activation; using only the original manager name with replace
would not suffice. The corrected operation preserves all existing Secret
fields, including WGCF caller credentials. One non-secret batch
delivery-version update drives one OOS rollout; unchanged ticks do not force
restarts. Recovery first consumes a retained fresh delivery rather than
minting again. Readiness compares each actual mounted token with the delivered
Secret by digest, then uses it for a pinned, redirect-denied GitHub read that
must prove live acceptance and exactly the expected one repository. Expiry
annotations, missing projections, stale sessions, wrong repository scope and
HTTP denial cannot stand in for that proof. Prior tokens are revoked after
new consumption succeeds. Process loss or failed revocation may leave a
previous same-scope token usable only until its original maximum-one-hour
expiry; it cannot widen scope or authorize another workflow. Normal renewal
must complete revocation rather than report the failed attempt as success.

Vault remains private-key authority. The two absent declared bootstrap entries
were created without overwrite from existing operator keys. An invalid stored
Maturity PEM was replaced only after its existing valid key proved the exact
App/installation/permissions, using Vault version compare-and-swap with the
prior version retained. All five Vault keys and existing provider identities
were verified read-only. Ephemeral key files remain operator-private and are
removed on every exit; tokens and private keys never enter source, process
arguments, receipts, Console data or browser state.

The existing lifecycle lock and active exact-Security marker cover the group.
Rollback stops renewal before Console-owned credential revocation but does
not delete, disable or revoke the five pre-existing owner bindings. Their
bounded credentials may expire while renewal is stopped; later accepted
activation renews and proves consumption. This does not promise indefinite
availability or hide owner-state mutation behind Console cleanup. Proposal,
repository, Prototype and ART history remain outside this rollback boundary.

Source proof: 37 focused tests cover the complete identity set, expiry, denied
provider access, exact binding, compare-and-swap failure, private-key cleanup,
invalid later grant, unchanged ticks, forced renewal, interrupted consumption
without reminting, and preservation of other owner fields. Three native local
Kubernetes cases reproduce the legacy ownership conflict, exercise the actual
adapter's CAS/recovery for all five producers and use each existing producer's
actual Secret manifest (including stringData) for renewal/recovery. Unique
synthetic ConfigMaps and Secrets contain no provider credentials and are removed
on exit; no real owner binding or provider grant is changed by these cases.
Read-only actual
OOS checks proved all five configured mounts and correctly reported four
expired credentials rather than readiness. Candidate
`36eb6d8836104ee23e4364de7724d47e41c1a9f5` and merged Platform source have the
identical Summary tree. Full local `make validate` passed on that committed
candidate after fetching base `c1b65d945d95218f76c7e11bdf3c0a62b7f2bdec`,
including owner tests, Helm and Terraform validation. Exact-head CI
`38859925827` and Security Posture `38859925730` passed; all five Vault-key,
App and installation permission checks passed read-only. Accepted-source
activation, forced group renewal and the real to-do exercise remain separate
operating proof, not claims inferred from these source checks.

Decision: approved only for the Summary's exact source set in the existing
single-operator, loopback-only `dev-integration` composition. No new service,
identity, role, provider permission, stage/prod exposure, AI action or ART
child is admitted. Refresh the private policy from this merged decision and
prove current group readiness before resuming the same acceptance exercise.

### Prior Provisioning Maintenance Acceptance

Maintenance Landing Unit `maintenance-1275-provisioning-baseline-security` uses
`child_isolated_landing_unit` for this existing exact-composition review. The
Summary and YAML bind the two newly merged owner revisions. Platform head/tree,
Workspace Governance, WGCF, source activation and admission boundaries remain
unchanged. This is not a new ART child or approval mechanism.

Design intent: complete the unchanged approved provisioning baseline when a
real creation has been acknowledged but separate provider readback mismatches.
The Console must display a valid failed observation rather than reject it as
malformed success evidence, and must expose retained correction and interrupted
request recovery without adopting an unrelated repository or rewriting history.

Implemented control: OOS may finish only the approved mutable settings through
the same dedicated provisioning App after an acknowledged immutable ID and fresh
active owner/name readback. The bounded PATCH does not include rename, transfer,
archive, delete or initialization. A separate read must prove every exact
setting before successful custody. Unknown acknowledgement and coordinate
collisions grant no settings authority; observed wrong identity, coordinates or
archive state fail closed. Authorization failure is bounded and cannot borrow
the read-only App, human credentials or another provider destination.

A nonretryable failed creation is corrected only through a new, explicitly
reviewed request causally bound to its retained owner result. OOS validates
creation provenance, acknowledged ID, unchanged target/settings/custody/operator
and credential-binding identity, then obtains current WGCF readiness. It resumes
by that ID and never creates again. The original failed record and receipt remain
immutable. Applying checkpoints carry no fabricated terminal receipt and remain
readable after interruption. Retry rereads provider truth before any further
approved operation, including recovery after a lost settings acknowledgement.

Console keeps exact success settings, active-state, identity and receipt checks.
Only failed observations may carry the mismatch that explains their failure;
they never produce successful Repository custody or unlock the Proposal gate.
The existing dialog restores retained requests after reload, locks correction
target/settings and requires fresh baseline review and approval. Applying and
retryable requests resume through the same authenticated POST path: the server
rereads the canonical original request, verifies current operator/policy/binding
identity, and resubmits its exact original approval and digest. Browser fields
cannot reconstruct or replace that authority. No credential, policy or provider
call enters the browser, and no new endpoint, action, role or downstream effect
is admitted.

Source evidence: reviewed candidates OOS `4360777b2353c9494e359c92d2da56c8c0ae9d91`
and Console `d9a7ad374f6b8261967af31f975fffa9b83ca903` match their merged trees
`d6994a44e20934cb3e76a7de4f519b6e45ebc9bf` and
`b1178e438e184fdf92652f1261bddf5776b0670d`. OOS full serialized tests, 32 focused
client/service cases, deterministic bundles, all 178 documented API routes,
fetched-base controls, API/worker builds and health/default-denial smoke passed.
Console all guards, 544 tests, types, repository safety, production audit and
exact-base checks passed. Isolated browser conformance proved failed readback,
locked target, fresh correction review, preserved original failure, reload and
exact-request resume without live mutations. Both exact-head CI runs passed:
OOS `38850468538` and Console `38850386946`, including production build.

Local production builds also failed on the unchanged accepted baseline. The
operator directed continuation using successful GitHub CI for production-build
evidence while preserving other local checks and all review/runtime gates. This
is recorded validation provenance, not a durable weakening of the delivery
contract or a claim about the host's root cause. Runtime acceptance still requires
the actual Console correction and provider readback; synthetic UI proof and CI
alone cannot establish a successful real repository, app or operating lifecycle.

Decision: approved for the existing single-operator, loopback-only
`dev-integration` composition at the Summary's exact source set. Platform must
recommission that set and refresh dedicated credentials before the real journey
continues. Rollback preserves repositories and immutable results; it does not
delete a partially created repository, rewrite its receipt, substitute fixtures
or claim downstream admission. The original real failure remains historical
evidence even if a later reviewed correction succeeds.

### Prior WGCF Readiness Maintenance Acceptance

Maintenance Landing Unit `maintenance-1275-custody-readiness-composition-security` uses
`child_isolated_landing_unit` for this existing exact-source acceptance. The
current Summary and YAML decision supersede older source bindings below.

The real Console provisioning submission exposed a WGCF packaging failure:
the installed custody loader searched `/usr/local/contracts`, although the
image contained the pinned bundle under `/app/contracts`. Readiness failed
before the provider operation. This is not an approval or operator-identity
bypass, and no successful real-repository creation is claimed.

WGCF PR #112 binds the existing custody/lifecycle, repository readiness,
Agent Action, and Product Publication loaders to their packaged bundles. It
changes no policy, request schema, role, authorization, provider permission,
credential, or runtime activation gate. The default-denied boundaries remain
default-denied. Both targets inherit a build check that loads all twelve
operation bundles and the continuity schema through installed Python with
isolated imports, normal image bindings, and no test-supplied root override.
The check runs as UID10001; the base then restores its pre-existing root build
identity solely for subsequent package installation. Both final runtime users
remain UID10001. Existing CI and image publication require this shared build
to pass; no CI workflow or GitHub App permission change is included.

The later real Console submission correctly exposed a separate source-gate
mismatch: WGCF still required the upstream policy's global activation field,
which its canonical schema fixes at `false`. Security PR #269 explicitly
approved the bounded WGCF source change before implementation. WGCF PR #113
reuses the established manifest activation model, pins that merged review and
content digest, validates its metadata and exact link/provision capability
set, and additionally requires the existing profile and Platform enablement.
Upstream policy/schema bytes and the lifecycle builder remain unchanged.
Lifecycle remains denied even when its environment flag is explicitly set.
Missing or malformed source approval cannot become availability; caller,
credential, provider, admission and release boundaries are not widened.

The reviewed candidate `d46d5d9ce8e1810dd1d4f6f7369ba5eafe2eaa09` and merged
WGCF head in the Summary have the identical tree
`a51798fe1ecd5bf898a59c8694441aa8b7de5d32`. Source proof passed the isolated
owner validator and 514 tests, API/worker image builds, thirteen installed
contract/schema checks in each image, API health/readiness and exact revision
readback, worker status and controlled-proof status, runtime UID, immutable
revision marker and writable evidence roots. Both installed images constructed
the actual configured custody factory with normal bundles and real revision
markers, using an isolated database without provider or decision mutation.
Owner negatives cover missing/disabled source activation, malformed review,
widened capabilities, default/profile/configuration denial and lifecycle denial.
Both unapproved worker startup paths remain denied. Exact-base diff checks
used fetched `origin/main` at `bccd3742213bf5082da1c86b2265d19c20a48b8c`.

Decision: approved for the already-admitted single-operator, loopback-only
`dev-integration` composition at the Summary's exact source set. Console,
OOS, Workspace Governance, and Platform head/tree bindings are unchanged.
Platform must refresh its private accepted policy and deploy the new exact
WGCF image before resumed operation. Image smoke is not successful live
provisioning, final to-do acceptance, or a complete-runtime operating proof;
those proofs remain outstanding. Rollback uses the existing Platform path,
preserves canonical records, and does not substitute fixture success.

### Prior Repository Gate Maintenance Acceptance

Maintenance Landing Unit `maintenance-1275-repository-gate-security` uses
`child_isolated_landing_unit` for the existing cross-domain boundary review.
It extends this decision, not the ART tree or the authority architecture. The
exact revisions in the Summary and YAML decision are authoritative; historical
acceptances below are not current source bindings.

The Repository-to-Proposal delta is approved for the existing single-operator,
loopback-only `dev-integration` composition. The operator selects a retained
successful custody request and its exact provider receipt in Repository
Control. Console supplies verified session authorization, server-only caller
attribution and deterministic replay identity. OOS admits only the authenticated
Console caller, rejects development bypass and caller/operator mismatch, checks
the canonical accepted Proposal version and pending gate, and independently
reads and verifies the retained custody evidence before any canonical write.
Owner and source reference are derived from that evidence, never accepted as
browser authority. No provider mutation, new credential, role, installation
scope, repository admission or workspace promotion is added by resolution.

Canonical state retains one bounded typed current resolution with exact replay
inputs and original source/timestamp bindings. The Platform-owned optional
schema and OOS mirror preserve older records and do not create another ledger
or accumulate history in the state field. Immutable events remain OpenProject
journals. When a source write committed but journaling or the response failed,
canonical readback exposes pending acknowledgement and exact recovery inputs.
Console can retry those frozen inputs after reload without reapplying the
source update, rewriting Disposition or manufacturing a local receipt.
The server validates owner, record, event, resolution identity and custody
receipt agreement before reporting success. Pending history is not an actionable
handoff; offline or malformed owner truth never substitutes fixtures.

The empty Repository-register path now mounts its existing dialog stack, so
first-time provisioning is operable before a custody row exists. The UI keeps
the graduated Teras primitives and existing operator roles; no new control
plane or special one-off approval mechanism is introduced.

Reviewed source evidence comprises the Platform optional-state compatibility
and bounds tests, full Platform validation, OOS unit and recovery tests, API
contract synchronization, workflow bundles, exact-base governance gates,
API/worker image build and smoke, and Console semantic/type/architecture/build
validation. Isolated browser conformance covers first-use provisioning,
canonical pending request reload and offline denial without live mutation.
That mocked UI proof is not final operating evidence. The real to-do journey
and refreshed complete-runtime operating proof remain outstanding.

Local validation also encountered native build-process segmentation faults;
Git integrity and standalone type checks passed, and a preserved-cache/cold
build succeeded. This review neither identifies their root cause nor certifies
host hardware. Do not silently relabel those failures as an application defect
or a memory-pressure diagnosis.

Rollback uses the existing complete-runtime shutdown/revocation path and
preserves canonical records and journals. Do not downgrade to a decoder that
predates the optional resolution/event contract after it has been used, or
delete canonical outcomes to make old source appear compatible. Runtime
activation remains denied until this exact source acceptance is current.

Source review references: [Platform schema #313](https://github.com/mfshaf7/platform-engineering/pull/313),
[OOS canonical gate #345](https://github.com/mfshaf7/operator-orchestration-service/pull/345),
and [Console gate adapter #85](https://github.com/mfshaf7/governance-operations-console/pull/85).

### Prior Public-Probe Maintenance Acceptance

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

- a Repository-owned Proposal gate outcome whose source-version and successful
  custody evidence are verified before mutation; current typed canonical state
  survives recent-receipt rotation, while immutable journal history and frozen
  replay inputs allow browser recovery without another source mutation;

- an external Security decision contract whose gate, initiative, work item,
  Architecture Packet, six owner revisions, and Platform tree must all match;
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

This is an exact-source acceptance decision. All Summary revisions are merged;
the Current Maintenance Acceptance above states the current engineering proof
and remaining operating obligations. The component evidence below preserves
historical implementation and recovery provenance, not a claim that those
older source sets remain current or the whole journey has passed.

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

### Platform Command And Effect Boundary

OOS and Platform independently validate the same finite action, subject,
source version, capability, intent digest, and operator approval. Platform
constructs every owner command itself. A caller cannot supply a repository,
path, command, argument, destination, or credential. Terminal Platform
receipts and current Console readback—not OOS coordination state alone—are the
effect evidence.

### Repository Gate Authority And Recovery

The distinct Repository resolution operation accepts only a selected retained
custody request and exact receipt plus the reviewed Proposal source and notes.
It cannot perform a provider action or select Platform effects. OOS derives
the resolved owner/reference from its validated custody store. The current
typed resolution remains authoritative when the bounded recent-receipt list
rotates; pending history and exact retry inputs remain visible after reload.
The matching source write and history acknowledgement are distinct, and only
the latter permits a completed Console handoff projection. Source tests cover
negative caller, stale source, changed receipt, conflicting replay, source and
event interruption, cold recovery and receipt-list rotation cases. Console
tests reject inconsistent owner/record/event/receipt acknowledgement bindings.

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

Security emits `gate:platform-operation-security` only for the six exact owner
revisions and Platform tree listed in the Summary and machine-readable decision,
bound to the current Architecture Packet URI and digest. Historical source
bindings above do not replace that current set.

This approval permits activation, restart, and status readback of the exact
current composition and the later Console-only journey under `#1298`. It does
not permit a component-only,
stale, partial, dirty, synthetic-substitute, or differently composed source
set; fixture fallback; browser-held owner credentials; a generic Platform
command; Console-owned lifecycle state; stage or production use; or a claim
that operating readiness has already passed.

Except for the explicitly admitted record-only descendants, any change to the
accepted Platform tree, governing owner source, identity,
credential custody, action vocabulary, canonical-data authority, network
exposure, rollback boundary, or runtime profile requires a fresh Security
delta decision.
