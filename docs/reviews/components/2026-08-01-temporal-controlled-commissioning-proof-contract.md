# Temporal Controlled Commissioning Proof Contract

## Summary

- date: 2026-08-01
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
- ART contract work: `openproject://work_packages/789`
- future pre-run authorization: `openproject://work_packages/790`
- future post-run review: `openproject://work_packages/791`
- reviewed Workspace Governance PR: `workspace-governance` PR #134 at
  `b061533bbb04d320d06c657d0b8b466adc7c6cb9`
- reviewed Platform PR: `platform-engineering` PR #197 at
  `c773e5e302bfb60035b5ba8cef903cc0fbe5ccfe`
- decision: `approved-with-findings`

This review accepts the contract design for one permit-gated Temporal
commissioning proof while the profile remains `build-admitted`. It does not
issue the future permit, satisfy its `security_authorization_ref`, authorize an
executor, activate Temporal or either worker, approve workflow execution, or
replace the separate pre-run and post-run Security decisions.

## Scope Delta

### Design Intent

The build-admitted Temporal component needs a narrow path to collect operating
evidence without turning normal dev-integration launch on. Workspace Governance
defines an expiring `controlled-runtime-proof-authorization`; Platform routes
the proof through a `component-commissioning-proof` runtime-drill ledger.

The authority split remains:

- Platform issues one exact permit and owns the runtime-drill procedure,
  Temporal lifecycle, baseline capture, and restore.
- Security separately authorizes the exact future permit scope.
- the operator explicitly accepts the exact permit.
- OOS owns the single admitted aggregate definition and its worker.
- WGCF owns the bounded readiness activity and its worker.
- Temporal schedules and records execution but gains no business, approval,
  or canonical-backend authority.
- Governance Operations Console calls OOS only.

### Implemented Control

The reviewed source is contract-only:

- a strict authorization schema binds one component, profile lifecycle,
  definition version, source revisions, immutable artifacts, namespace,
  identities, task queues, scenarios, actions, approvals, validity window,
  evidence owner, baseline, restore, exceptions, and stop conditions
- validators fail closed on stale, widened, malformed, or unsupported permit
  fields
- the Platform drill profile scopes Temporal, the OOS worker, and the WGCF
  worker with eight required checks and exact-baseline restore
- ledger creation requires the exact authorization ref and digest
- activation recording remains denied until every scoped surface has a
  separate operator-reviewable baseline evidence ref
- ordinary Temporal launch, access, smoke, backup, restore, and workflow
  commands remain denied while the profile is `build-admitted`
- the operator surface states that no issuer, executor, permit, or runtime
  activation exists yet

The ledger records bounded owner actions. It does not perform runtime mutation
or become approval authority.

### Operating Evidence

Operating evidence is intentionally absent. No controlled permit has been
issued, no Security authorization for a run exists, and no Temporal runtime,
database, namespace, credential, worker poll, workflow, activity, backup,
restore, or post-run assessment is claimed.

Schema validation, profile tests, temporary local ledgers, and CI prove only
source behavior. They cannot satisfy the future pre-run authorization or
post-run Security review.

## Review Areas

### Identity

The contract correctly binds the Temporal runtime identity, OOS worker
identity, WGCF worker identity, namespace, and distinct task queues. The future
permit must resolve those refs to the exact operator-approved identities and
must expire before any mutation. Cross-owner queue consumption, anonymous
namespace access, shared long-lived worker credentials, and direct Console
credentials remain denied.

The future Security authorizer must compare the permit against current source,
artifact, identity, namespace, and queue truth. A syntactically valid reference
is not sufficient evidence that the identity exists or is correctly scoped.

### Secrets

The proof permits references, digests, bounded status, and receipt identifiers.
It does not permit secret values, raw context, unbounded logs, command output,
or full business records in Temporal history, the drill ledger, or promoted
evidence.

Before authorization, the exact runtime must prove namespace-scoped secret
delivery, storage and backup custody, diagnostic redaction, and least-privilege
worker credentials. Raw local ledgers remain local; only bounded summaries and
durable refs may be promoted to ART or Security evidence.

### Delivery

Merging the contract, ADR, drill profile, or operator procedure cannot activate
the component. The profile remains `build-admitted`, normal commands remain
fail-closed, and at most one `validation-readiness-run` may be named by a
future permit.

The future sequence remains separate:

1. #789 lands the contract and operator surface.
2. #790 reviews and authorizes one exact, unexpired permit.
3. the permit-bound executor may run only the declared proof.
4. exact-baseline restore completes before the run can close.
5. #791 reviews the operating evidence before any lifecycle decision.

No pre-run permit may be reused as activation or promotion evidence.

### Runtime

The baseline gate, verification pack, exception decisions, and exact restore
model are appropriate for a temporary runtime proof. The future executor must
stop on authorization expiry, source or artifact drift, unexpected scope,
identity or queue denial failure, payload-boundary failure, evidence-custody
failure, or restore failure.

One successful run proves only the permitted local commissioning scope. It
does not establish self-serve launch, a generally admitted workflow, stage
readiness, production readiness, or safe reuse for another source revision.

## Findings

1. The permit issuer and executor are not implemented. They must remain absent
   or fail closed until separately reviewed source exists. Owners: Platform and
   Workspace Governance. ART: #790 and the later executor work.
2. No per-run Security authorization exists. This contract review must not be
   used as `security_authorization_ref`; #790 must bind the exact permit and
   current runtime truth.
3. No operating evidence exists for identities, secrets, network isolation,
   persistence, restart, replay, idempotency, payload boundaries, backup,
   restore, or incident fencing. Owners: Platform, OOS, and WGCF. ART: #790,
   the controlled proof, and #791.
4. The local drill ledger can contain environment-sensitive references. Raw
   ledger files must stay local, while bounded summaries and durable refs are
   promoted through approved evidence custody.

These are fail-closed future gates, not accepted live defects.

## Decision

`approved-with-findings`

Approved:

- the controlled-proof authorization schema and fail-closed validation model
- the `component-commissioning-proof` runtime-drill taxonomy
- the Platform operator procedure and machine-readable drill/evidence profile
- baseline attestation before activation and exact-baseline restore
- continued `build-admitted`, non-self-serve Temporal posture

Not approved:

- issuance or acceptance of a controlled-proof permit
- use of this review as the permit's `security_authorization_ref`
- implementation or operation of a permit issuer or executor
- Temporal, OOS worker, or WGCF worker activation
- workflow or activity execution
- profile lifecycle `active`, stage, or production
- treating pre-run authorization as post-run acceptance

The contract may land. Runtime work remains denied until #790 records a fresh
Security decision for one exact permit and the operator explicitly approves it.
A successful proof still requires #791 before any later lifecycle change.

## Related Artifacts

- [Temporal build admission](2026-07-31-temporal-durable-orchestration-build-admission.md)
- [OOS durable-orchestration source admission](2026-08-01-operator-orchestration-service-durable-orchestration-source-admission.md)
- [Temporal security view](../../architecture/components/temporal/README.md)
- [Security delta review process](../security-delta-review-process.md)
- [Workspace Governance PR #134](https://github.com/mfshaf7/workspace-governance/pull/134)
- [Platform PR #197](https://github.com/mfshaf7/platform-engineering/pull/197)
