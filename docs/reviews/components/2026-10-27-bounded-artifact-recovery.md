# Bounded local artifact recovery security delta

## Summary

Approve the bounded dev-integration recovery design and exact Gary Platform
candidate `bb7da2e7c10aab4dcb5450011d50da953509cf1c`, tree
`a95a67d0916ec3be8b147acbbb378afabb9bbfe5`. Required hosted source checks and
delegated review must pass before merge; the paired finite decision must select
the identical merged tree before installation/commissioning. This is source
acceptance, not proof that automatic recovery has already operated.

## Scope Delta

Extend existing Platform lifecycle with a root-installed stdlib image checker
and finite check/repair/confirm actions. The product admission restricts the
existing local Console namespaces and public image repositories. Invocation uses
the existing Windows/WSL administrative boundary, isolated Python, fixed paths
and arguments, and independently bounded root execution. No service, model or
browser receives containerd sockets, root shell text, arbitrary filesystem paths,
image references or registry credentials. No new daemon or identity is introduced.
NoNewPrivileges remains on the existing user services; Windows/WSL administration
is an explicitly admitted host boundary, not something that flag contains.

The invocation factory cross-checks its declared `Platform-Core` distribution
against the existing Platform host configuration. Native user-systemd proof
exercised that actual factory under NoNewPrivileges/PrivateTmp and confirmed the
intended root context. A mismatched distribution is rejected before invocation;
generic administrator availability is not sufficient host-binding proof.

The idle preflight explicitly uses the owner k3s kubeconfig. Artifact discovery
includes admitted cached images from retained workload/Job templates after Pods
retire. Immutable tag-plus-digest references retain the exact digest; ambiguous
cached tags refuse. Dormant unadmitted controllers are not activated or granted
repair authority. Native declaration proof still selects the same17 images.

During a pre-merge validation, a URI-query dry-run with a DeleteOptions body
retired one already-completed storage-provisioning Pod. The completed Job and
Bound database/object-storage volumes remain; no provisioning work was replayed.
The existing accepted recovery candidate records this agent validation miss.
Disposable-only reproduction confirms that URI dry-run was ineffective for
that body on this cluster, while explicit body dryRunAll retains the same object
and wrong UID rejects deletion. The disposable objects were removed. Production
cleanup uses explicit exact UID preconditions and retains completed-Pod identities
in its attempt journal; it does not claim a dry-run or erase Job/business history.

Independently verify image manifests/config/layers by digest, reconstruct OCI
file inventories without archive extraction, and compare a read-only unpacked
root rather than writable containers or mounted data. Protected checksummed
baselines optimize startup; any mismatch rebuilds the baseline and rereads the
actual filesystem. Missing local compressed layers may be fetched only from the
same exact public registry digest over HTTPS with scoped anonymous pull tokens;
do not import ambient Docker/GitHub/provider credentials or forward registry
tokens to redirected blob storage. Unadmitted redirects, unsupported OCI parent
links, unavailable artifacts and failed digests stop before cache repair.

Every diagnostic mount is unmounted with native snapshot-view removal, including
verification failures. A pre-merge native check identified the missing removal
flag in the initial draft. The same unmerged source now includes the regression
case; native repeated-mismatch proof leaves zero views for its exact scratch
root. Only the21 identified unmounted draft diagnostic views were retired;
all1,681 other snapshot records were retained. No broad cache prune is authorized.

Shared/exclusive owner-operation and existing lifecycle locks prevent repair
from overlapping admitted Platform owner work. Pending Helm compensation defers
it. Plan all consumers before effects, reject unmanaged/unsupported users,
preserve controller UID/replica evidence, quiesce affected controllers and wait.
The root helper separately requires no CRI image users; it may remove only exited
containers in admitted namespaces whose pods are absent, then refreshes exact
aliases through native image operations and verifies replacement bytes. It never
deletes PVCs, DB state, source work, provider accounts or credentials. A retained
shared snapshot or ambiguous identity is a refusal, not a force-delete path.

Attempts are durably recorded before destructive effects. Failed/uncertain
attempts are not replayed. Safe interrupted quiescence or a freshly proven
completed replacement may resume without repeating removal. Root state and user
journals survive restart. Fatal artifact faults exit78, and the retained
supervisor prevents automatic restart for that status. Deferred busy-owner work
remains retryable. The existing timer detects cheap runtime faults before hashing
and does not repeatedly scan/restart an unexplained ongoing fault. Resumption
uses the retained supervisor rather than a short-lived timer cgroup.

Frontend restoration is confined to its exact source/toolchain-derived cache:
stop the managed consumer after a proven mismatch, quarantine owned output,
rebuild clean committed source without live credentials, verify inventory and
native process/custody/memory settings, and only then retire superseded derived
quarantine. Repeated/interrupted failed rebuilds latch. Existing serving budgets
and separation from hot reload remain intact.

## Review Areas

Runtime/host: this explicitly admits bounded image-cache administration, not
general host repair or a change to stage/prod authority. Root-owned helper and
policy custody, accepted-source hashes, no caller mutation parameters and finite
actions constrain the path. Existing Platform capability availability/reasons
and blocked owner-operation receipts surface recovery restrictions without a
new public action schema.

Direct artifact and dependent-consumer readiness is confirmed before exposing
active Platform capabilities; a deliberately blocked capability is not its own
repair-completion prerequisite. Full Console acceptance remains a later separate
proof. The regression exercises actual capability projection before/after the
incident closes. Original alias mappings are restored idempotently: aliases
already recreated by CRI pull are verified and retained, never retagged or
force-overwritten. Native tests confirm this on both affected images. Preserve
mismatch/controller/Pod evidence in closed incidents and success receipts.

Unit receipt roots are isolated in temporary directories. Fourteen exact
synthetic artifact receipts from the initial tests were quarantined outside
operator runtime state; all genuine native receipts were preserved. No synthetic
receipt is accepted as native operating evidence.

Identity/secrets: no new credentials or principal. Dedicated provider/model
accounts, purpose binding, source-author identity, repository custody and all
other execution-owner pins/gates remain inherited. Security remains separate
from runtime health and the main agent retains Security closure/final landing
judgment under the standing delegated operator authority.

Delivery: Platform ADR031, owner change record and primary operating procedure
define installation, diagnosis, bounded failure and rollback. Register the
owner evidence index in this same dependent Security landing. Do not advance the
watched Platform checkout or install root code until both source and acceptance
land. A record-only governance update does not require a new executable pin.

Evidence: full local Platform make validate passed at the exact committed head
with absolute canonical OOS validation source; base-aware whitespace and normal
governance-document proof passed against fetched e43abde. Focused tests cover
faithful one-bit filesystem corruption, OCI whiteouts/links/path escape, content
digest failure, shared users, no repeated uncertain repair, real owner flock
exclusion, idle timer behavior, retained-supervisor resume and unknown-fault
refusal. Read-only native inspection covered17 images/203,874 entries;15 images
matched and two cached executables differed. A missing local GHCR layer was
independently fetched and verified successfully. No automatic repair or DB
integrity claim follows from those read-only/source tests.

## Decision

**approved** for this exact candidate/tree and the bounded local scope. Require
hosted checks, exact Gary author/head review and identical merged-tree readback;
then select that merged revision in the existing composed decision and land this
Security acceptance before root installation/live activation. Preserve all other
decision, architecture, model, workflow and owner bindings.

Native operating acceptance must exercise the actual two damaged cached tools,
show exact-image restoration and trusted replacement hashes, normal full Console
startup/credential renewal, authenticated owner/current/history/model readback
and retained original records. Keep that evidence in the existing recovery
candidate/PR314; do not create another ART item or source-pin loop. The operator
accepts imperfect RAM; software cannot guarantee a correct verifier, repair of
mutable data or availability of a dead host. Unknown host/data faults require
their owner procedure. Rollback preserves data and evidence and disables only
the admitted automatic repair or restores previous reviewed source.

## Source landing evidence

Platform [PR345](https://github.com/mfshaf7/platform-engineering/pull/345)
merged as `1e687aac02ec04b504c925fcf1e8f05820a2fde7` after the exact Gary head
received delegated human approval. Its tree is
`a95a67d0916ec3be8b147acbbb378afabb9bbfe5`, identical to the reviewed candidate.
Hosted validation [attempt2](https://github.com/mfshaf7/platform-engineering/actions/runs/40389951534/attempts/2)
passed in5m30s; repository posture also passed. The first hosted attempt stalled
in Ubuntu mirror metadata download and was cancelled without changing source.
The finite composed decision selects this merged revision and unchanged tree;
all other owner revisions and architecture bindings remain unchanged. The
watched Platform checkout and privileged helper remain unchanged until this
Security acceptance lands. Native automatic operating proof is still required.
