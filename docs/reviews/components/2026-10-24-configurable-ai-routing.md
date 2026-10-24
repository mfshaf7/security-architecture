# Configurable AI routing security review

## Summary

Approve the exact Epic 1313 local dev-integration composition for source landing
and subsequent commissioning. This decision extends the existing Console/OOS/
governed gateway boundary with operator-configured backend/model/native effort
and explicit fallback. It does not create a second control plane or give a model
source, account, approval, merge, deployment or canonical mutation authority.

The accepted architecture is
`wgcf://artifacts/delivery-art/sha256/7715729bdb3420a790ff816d204c4c9c96a94745265444c517b2d02cb3e316b6`,
digest `sha256:7715729bdb3420a790ff816d204c4c9c96a94745265444c517b2d02cb3e316b6`.
The schema-six content retains logical artifact `architecture-packet:delivery-1313-v1`.
The paired YAML is the finite activation decision; runtime must read it from
current clean Security main and verify the exact source/tree bindings.

## Scope Delta

Reviewed exact sources:

- `context-governance-gateway@46ae520359bbce1b2bf0e06cd8a3f638c2684169`
- `governance-operations-console@6c9d407d85a0344509024a0f01c6b616366f3015`
- `operator-orchestration-service@fe3396df56576a439897866b4b844a03491a77fe`
- `platform-engineering@4501e9ab2b674ca0a06a46a2b25d28cdaa316a53`
- `workspace-governance@ebb2693615c58448d904cbd6f0772073820fecf1`
- `workspace-governance-control-fabric@1fc25783c59d1a6b0eb9935f42b0ee1fd81cf144`
- `workspace-prototype-studio@e04dfd2dd8ac6aa5b7049ccb8bde7f2452c0f5e1`
- `platform-engineering-tree@cf99a8eb54f84ca0d3073e6da6736562a5e249af`

The Platform revision is the actual Gary-authored [PR336 candidate](https://github.com/mfshaf7/platform-engineering/pull/336),
not an invented future merge. Its source tree must be identical after merge.
Foundation PR334 and custody correction PR335 are already in its base. OOS
PR374 and Console PR118 are merged. The other execution owners retain their
previous implementation. Studio's intervening changes are bounded Prototype
lifecycle/design records, with no change to its execution controls.

The reviewed [Platform composition](https://github.com/mfshaf7/platform-engineering/blob/4501e9ab2b674ca0a06a46a2b25d28cdaa316a53/products/governance-operations-console/scripts/console_model_management.py)
is part of the existing complete-runtime operator path. Its parent consumes
this decision before image import, credential issuance or workload effects.
This review also retains the inherited finite Platform-operation, repository
provisioning, source-authoring, publication and owner-record boundaries from
the [preceding complete-runtime acceptance](2026-10-15-governance-console-platform-operation.md).
Their independent owner gates and exact bindings remain enforced.

## Review Areas

### Identity and source separation

Only the admitted Console operator submits bounded management intent. Console
derives the authenticated actor server-side; OOS requires its exact caller and
operator binding. Browser bodies cannot supply another identity, endpoint,
permission, binary, Vault path or provider secret. OOS binds original request,
expected revision, immutable owner command and receipt digests. Another caller's
request cannot be listed, read, cancelled or adopted.

Agent Gary continues to author and publish source. The delegated accountable
human identity reviews and merges through the existing ART source workflow.
Model output remains a proposal: deterministic schemas, CGG admission, native
source policy, exact-digest acceptance and the existing Gary executor remain
outside model authority. No model receives a repository or installation token.

### Provider account and management credentials

The dedicated native account is held only at
`kv/data/components/governed-ai-gateway/dev-integration/codex-account`.
The gateway's renewable Vault token permits create/read/update of that one data
path, plus ordinary self-lease operations. It cannot list or read other provider
or source identities. The intended token ID is persisted privately before issue;
an uncertain response reuses that identity. Root Vault authority remains in the
Platform operator path and never reaches gateway, OOS, Console or a model.

The new OOS management token is separate from both Vault and native provider
credentials. OOS receives only that token. Gateway init projects its credentials
as UID1000 mode0600 files; native Codex gets an isolated account home and scratch
directory, not the management/Vault environment. Native sign-in is explicit and
retains its original journal. Interactive CLI/Desktop credentials are not imported.
Account refresh uses Vault compare-and-swap and remains gateway-owned.

The existing credential timer maintains the scoped lease. Rollback stops that
timer first, removes both management bindings, revokes the lease and removes
its projections and added egress. Configuration/history and the Vault account
remain available for reviewed recovery. No raw token is placed in process
arguments, source, Console state, receipts, ordinary logs or model context.

### Runtime and network

The executable is Codex 0.163.0 with raw SHA256
`399ff69c431c066e40de318fba45c2b07f45a76b19939d247ee4828fc70c4215`.
Its image uses Python base
`sha256:46cb7cc2877e60fbd5e21a9ae6115c30ace7a077b9f8772da879e4590c18c2e3`.
Construction and invocation check the actual executable digest. The gateway
runs nonroot with a read-only root filesystem, dropped capabilities, no service
account token or host/project mounts, one CPU, 1GiB memory and bounded temporary
storage. Codex metadata/sign-in/inference share one native process slot; managed
Ollama calls share one local slot and unload after use.

Only the gateway gains public IPv4 TCP443 and exact Vault-service TCP8200 egress.
The public rule excludes local/private ranges; existing declared Ollama and DNS
rules remain. This is a dedicated trusted adapter's TLS route, not an arbitrary
browser-supplied destination or a direct consumer provider client. OOS and other
consumer bypass denial remain unchanged. This is not FQDN enforcement, private
client qualification, general host access, stage or production exposure.

Native threads are ephemeral and sandboxed read-only with network tools off.
Ambient configuration, plugins and project roots are absent. The adapter rejects
tool/action items, mismatched thread/turn identity, changed model/effort and
invalid structured output. Native output-token control is not offered by this
installed protocol; elapsed time, queues/messages, final bytes and container
resources remain enforced. Private reasoning is not returned to consumers.

### Model choices, context and fallback

The existing six profiles retain purpose, caller, CGG model-safe data, task,
output and operator-acceptance contracts. Registration and runtime routing use
the exact reviewed management policy for those existing scopes. The legacy
source-selected local binding remains available. This acceptance explicitly
admits the dedicated Codex and managed Ollama alternatives; it does not activate
the pending direct OpenAI API billing route or expand private-client data scope.
Secrets and raw unadmitted context remain excluded.

Registration performs bounded synthetic verification rather than treating a
catalogue entry as readiness. Native effort values preserve string/boolean/null
types and are revalidated. Defaults, explicit task overrides and an inherited
default are distinct. Finite ordered fallback is opt-in; no intelligence rank
or fixed provider priority is imposed. Source-selected profile permissions and
actual runtime selection have separate, preserved evidence.

Only known pre-submission unavailability/busy permits fallback. Submitted or
ambiguous completion, policy/integrity/output failure and post-completion
credential-custody failure stop without a second inference. Invocation and
configuration revisions are retained; stale edits need a newly reviewed intent.
Lost acknowledgements replay the original request/owner command. Cancellation
reports only an owner-confirmed terminal outcome. Historical readback binds the
accepted receipt revision even when another edit has advanced the current tip.

### Visibility and compatibility

The existing Teras Model Operations surface exposes registration, native sign-in,
task/default routing, effort, fallback, conflicts, history and original-request
recovery. It needs no previous profile-lifecycle completion receipt. Provider
loss remains unavailable, with no fixture substitution. Current management API
availability and historical verified registration do not claim model entitlement
or current inference health.

Optional task-bound selection evidence is preserved by existing consumers;
historical records remain readable and business output schemas are unchanged.
The Agent, Delivery and Prototype source views can show actual model/effort.
Full provider/consumer operating evidence remains a later requirement.

## Evidence and limits

Source evidence includes the Platform foundation's real transport/filesystem
tests and custody regression, OOS's 1618 passing owner tests and actual API/worker
image smoke, and Console's 704 passing semantics plus architecture/type/build/
public-source/dependency checks. Isolated browser proof covers cold registration,
native effort/fallback, dirty guards, response loss and original-ID reload,
stale revisions, native cancellation and unavailable-owner denial.

The actual commissioning manifest passed Kubernetes server dry-run without a
deployment. A local image passed executable digest/version checks. Its runtime
image inputs are unchanged by the final test-only correction. The exact corrected
candidate passed 87 tests in the existing admitted runner environment. Its
composition wrapper ran 11 composition tests and 69 complete-runtime tests; four optional native
cluster ownership tests remain explicit skips. Those tests isolate source and
synthetic protocol behavior, not provider account entitlement or real workflow
completion. Source-local checks and provider CI are retained with the PR; native
ART evidence must cover the final exact head before source merge.

That final native acquisition passed at
`4501e9ab2b674ca0a06a46a2b25d28cdaa316a53`; OOS reports current merge-ready
evidence and blocks the candidate specifically on this planned Security gate.
The exact-head [Platform CI run](https://github.com/mfshaf7/platform-engineering/actions/runs/40099191216)
and repository-posture check passed. No commissioning merge or activation is
claimed by those results.

The correction makes the existing tests bind their fixture operator instead of
inheriting terminal identity. Runtime identity policy, evidence isolation and
authority remain unchanged. This is not a new workflow mechanism.

## Decision

Approved for the exact local dev-integration source/tree set and the existing
commissioning path. This artifact satisfies the composed Security judgment and
commissioning-candidate source review after its own normal reviewed source
landing; it does not itself merge or deploy Platform source.

Platform must verify the accepted candidate tree after merge and read this
unrevoked decision before commissioning. Actual dedicated account sign-in,
model verification, Console configuration, Codex/Ollama calls, fallback and
recovery across current consumers belong to #1320/#1321 operating evidence.
Retain source/receipt correlation, revocation, rollback and owned-resource cleanup.
Do not infer private client custody, autonomous code quality or stage/prod from
this acceptance. Existing baseline findings and separate authority gates remain
in their own inventories; none is silently closed by this delta.
