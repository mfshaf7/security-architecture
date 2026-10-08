# Proposal Target Application Trust-Boundary Security Delta

## Summary

- date: 2026-10-08
- owner repo: `security-architecture`
- delivery initiative: `openproject://work_packages/1203`
- parent feature: `openproject://work_packages/1212`
- security review item: `openproject://work_packages/1235`
- governing architecture packet:
  `wgcf://artifacts/delivery-art/sha256/3a4b5edb6bc54ff47a45f610b41f75bc57dd9d1ab56e9475518100d75ff72ab0`
- reviewed source:
  - Workspace Prototype Studio reviewed head:
    `workspace-prototype-studio@873b5cc12362846f9bcfd7d4e414853cf90ed59b`
  - Workspace Prototype Studio merge:
    `workspace-prototype-studio@eab7af0c44de2e76eb381bf06447105ce3a28863`
  - Workspace Prototype Studio handoff-reference contract repair merge:
    `workspace-prototype-studio@4066ea5ba5a68ab7ab12acc7fc395897e1ae6c3f`
  - Operator Orchestration Service reviewed head:
    `operator-orchestration-service@d1431e8ff5152abd8bc11be33fec39aa1318eeb3`
  - Operator Orchestration Service merge:
    `operator-orchestration-service@875696096adae15cf2e068054a5fa8d6e28d8524`
  - Operator Orchestration Service handoff-reference contract repair merge:
    `operator-orchestration-service@7263aae5b4eac17376a84b96f8f533b39a7e1500`
  - Operator Orchestration Service zero-mutation restart repair merge:
    `operator-orchestration-service@0e935029327c3195f7ad1026c6f450f4b32c52dd`
  - Platform commissioning receipt-source binding repair merge:
    `platform-engineering@85d7287ddccf021637d36131a5b661e75f1fdf4c`
  - Governance Operations Console reviewed head:
    `governance-operations-console@f71f1a240901bf93c6e65b3b2666791fa6e0fcd3`
  - Governance Operations Console merge:
    `governance-operations-console@e993e9a55b80a24dcab4b96b8291ece822c8dd0f`
  - Governance Operations Console caller-attribution repair merge:
    `governance-operations-console@f1564dcd6ef46db9cceff09a598d64265074896b`
  - Governance Operations Console preparation-contract repair merge:
    `governance-operations-console@1c106066118c32d8db38cf34850a6560d821da66`
  - Governance Operations Console submission-contract repair merge:
    `governance-operations-console@b7dda700e1a6f12f445a42391737e20d5310b09e`
  - Governance Operations Console live-handoff conformance merge:
    `governance-operations-console@d66411f128c3fd2f21ac274f620352977966fecd`
- prior ART source evidence:
  - Studio Review Packet:
    `wgcf://artifacts/delivery-art/sha256/e35fe9362734acdef717ff35de764e1333e92adcef2f2c9806afd7c6eef1696c`
  - OOS Review Packet:
    `wgcf://artifacts/delivery-art/sha256/9494b0a4cd423b9d8c2c5b01a20a2ec4e39fdf7dd0cde49792aa4e4109bbd025`
  - Console Review Packet:
    `wgcf://artifacts/delivery-art/sha256/6c1eba3948fe352841ed21428747bb7d20fdffb4df268373c08f16e8846a89e2`
- corrective owner-review evidence:
  - Workspace Prototype Studio pull request:
    `https://github.com/mfshaf7/workspace-prototype-studio/pull/23`
  - Operator Orchestration Service pull request:
    `https://github.com/mfshaf7/operator-orchestration-service/pull/285`
  - Governance Operations Console caller-attribution repair pull request:
    `https://github.com/mfshaf7/governance-operations-console/pull/53`
  - Governance Operations Console preparation-contract repair pull request:
    `https://github.com/mfshaf7/governance-operations-console/pull/54`
  - Governance Operations Console submission-contract repair pull request:
    `https://github.com/mfshaf7/governance-operations-console/pull/56`
  - Workspace Prototype Studio handoff-reference repair pull request:
    `https://github.com/mfshaf7/workspace-prototype-studio/pull/24`
  - Operator Orchestration Service handoff-reference repair pull request:
    `https://github.com/mfshaf7/operator-orchestration-service/pull/288`
  - Operator Orchestration Service zero-mutation restart repair pull request:
    `https://github.com/mfshaf7/operator-orchestration-service/pull/289`
  - Governance Operations Console live-handoff conformance pull request:
    `https://github.com/mfshaf7/governance-operations-console/pull/57`
  - Platform commissioning receipt-source binding repair pull request:
    `https://github.com/mfshaf7/platform-engineering/pull/274`
- decision: `approved`

The exact repaired source separates the Console, OOS, GitHub review, and
Prototype Studio authorities and now fails closed before public publication.
Prototype Studio contract v2 accepts only generated identifiers and labels,
opaque canonical refs, digests, timestamps, and enumerated posture. OOS keeps
operator identity and free-form Proposal content inside its private workflow
state and cannot serialize those fields into the public target request.

The Console caller-attribution repair at
`governance-operations-console@f1564dcd6ef46db9cceff09a598d64265074896b`
restores the reviewed boundary in the executable adapter: the OOS command
operator is the authenticated `governance-operations-console` machine caller,
while `operator:workspace-owner` remains only the verified same-origin session
principal. It does not add an identity, permission, secret, repository, route,
or exposure boundary. The included Next.js patch update changes no Proposal
Target authority and removes the dependency advisories present at review time.

The follow-up preparation-contract repair at
`governance-operations-console@1c106066118c32d8db38cf34850a6560d821da66`
removes the caller-supplied `prototype_id` from the OOS preparation request.
OOS remains the only authority that derives the Proposal-bound Prototype
identity. The repair narrows the request to the already reviewed contract and
adds an exact-body assertion; it adds no authority or data field.

The submission-contract repair at
`governance-operations-console@b7dda700e1a6f12f445a42391737e20d5310b09e`
removes the unapproved `suggested_name` and `suggested_objective` fields from
the Prototype binding sent to OOS. The Console now submits only the
OOS-derived Prototype identity already admitted by this review. The exact-body
test prevents the public-source payload from regaining free-form Proposal
content; no identity, permission, secret, repository, route, or exposure
boundary changes.

The handoff-reference repair binds the target application to the same bounded
identifier already accepted by the canonical Proposal workflow. Studio and OOS
now accept the live deterministic form
`proposal-handoff:idea-<id>:version-<version>` while retaining the prior
`proposal-packet:<id>` form for existing durable records. Studio still proves
that the Proposal id, OpenProject record id, Prototype id, and handoff Proposal
id agree. OOS pins the exact Studio schemas and digests, and the Console
conformance fixture now exercises the form it actually emits. The change adds
no free-form public field, new caller, repository, permission, secret, target,
or exposure boundary.

The zero-mutation restart repair closes only the recovery gap created when
Prototype Studio authority changes after OOS accepts a command but before it
prepares any target files. A replacement target-authority binding requires an
explicit cancellation, a cancelled record with no preparation, review, target
result, Proposal acknowledgement, or canonical mutation, and an identical
caller, Proposal, Prototype, approval, session, execution, correlation, and
idempotency identity. The service and durable store enforce those conditions
independently, preserve history, and retain fail-closed conflicts for every
prepared, reviewed, completed, or otherwise changed command. This does not add
a caller, permission, repository, secret, merge authority, or direct mutation
path.

The Platform receipt-source binding repair at
`platform-engineering@85d7287ddccf021637d36131a5b661e75f1fdf4c`
separates the immutable activation baseline from the current target authority.
Lifecycle receipts retain the policy-approved Prototype Studio activation
revision; the canonical target proof independently requires the reviewed merge
to be an ancestor of current clean Studio `main` and both bounded capture files
to exist there. This removes a false post-success rejection without accepting
stale target state, weakening merge evidence, or expanding identity, secret,
repository, route, or runtime authority.

The separate Delivery ART v6 control adds the missing OOS-owned source
activation Landing Unit between this Security decision and Platform
commissioning. This review emits `gate:proposal-target-controlled-activation`
for that bounded OOS activation step. It does not authorize Platform
commissioning until the activation revision is merged and proven through the
v6 sequence.

## Scope Delta

### Design Intent

- apply one accepted Proposal routed to Prototype Studio without giving the
  browser direct source-provider or OpenProject authority;
- let OOS coordinate one deterministic, human-reviewed target-source change;
- let Prototype Studio own the capture record and receipt while stopping before
  Prototype Landing, registry admission, runtime activation, or implementation
  claims;
- acknowledge the Proposal only after exact merged-source readback and the
  target-owned receipt; and
- keep runtime activation separate from source implementation and Security
  acceptance.

### Implemented Control

The Console re-reads canonical Proposal truth before submission, requires an
accepted Prototype route, resolved repository custody, the exact prepared
handoff, and current record version, and constructs caller, session, execution,
and replay bindings server-side. The browser never receives the OOS caller
secret or source-provider credential.

OOS rejects inactive runtime, wrong callers, unresolved custody, stale target
state, broad provider identity, personal tokens, alternate provider
destinations, conflicting replay, unexpected branch content, missing checks,
missing human review, non-canonical merge ancestry, and merged readback drift.
The installation token must resolve to exactly the Prototype Studio repository.

Prototype Studio accepts only a clean digest-derived review branch and a v2
public-safe request. It requires Proposal-bound generated application and
Prototype identities, rejects every additional field, writes one capture record
plus one immutable application-history record, preserves deterministic replay,
and rejects dirty, detached, stale, malformed, conflicting, or duplicate source
state. The capture stays `exploring` and `captured`; it does not update
`prototypes.yaml` or claim Prototype Landing.

### Operating Evidence

The original three source Landing Units passed their owner validations, human
review, protected-repository checks, merged readback, and finalized Review
Packets. The corrective Studio and OOS maintenance Landing Units then passed
their complete owner suites and CI at the exact revisions above. Studio proved
a safe generated capture and rejection of operator, suggestion, rationale, and
custody-reference fields. OOS proved the exact v2 owner pin, a request free of
caller-written content, Proposal-bound identities, disposable real-Git source
preparation, and its full 1,228-test suite.

The corrective Console maintenance Landing Unit passed its clean install,
repository architecture checks, 469 semantic tests, type checking, production
build, zero-vulnerability production dependency audit, exact-head CI, human
review, and protected merge. This is source conformance evidence only; live
Proposal Target commissioning remains Platform-owned operating evidence.

The activated runtime has now produced intermediate operating evidence for the
human-reviewed target merge, canonical Proposal acknowledgement, required
denials, restart recovery, rollback, cleanup, and clean redelivery. Final
commissioning evidence is not yet accepted: the Platform verifier repair and
this exact-revision reacceptance must land first, then Platform must rerun the
non-mutating commissioning check against fresh lifecycle receipts. Source and
review evidence do not substitute for that final operating proof.

## Review Areas

### Identity And Authorization

The separation between the Console machine caller, OOS workflow authority,
repository-scoped GitHub App identity, and human source reviewer is sound for a
single-operator local lane. Machine identities cannot approve or merge their
own source work, and the Console cannot select the provider repository or
credential.

The fixed Console adapter now preserves machine attribution by serializing the
authenticated `governance-operations-console` caller as the OOS command
operator rather than serializing the local human session principal. Trusted
human identity is still absent. Existing Console finding `GOC-SEC-02`
therefore continues to block shared or multi-user exposure.

### Secrets

The Console caller secret and Proposal target installation token remain
server-side file or environment bindings. They must not enter browser payloads,
source, logs, Review Packets, receipts, or public target records. Platform must
deliver the provider credential only to the OOS target-application runtime and
keep it restricted to the exact Prototype Studio repository.

### Public Source And Data Handling

`workspace-prototype-studio` is a public repository whose owner rules prohibit
real client data, secrets, production exports, and unreviewed client-visible
content. Contract v2 now makes the public-source boundary structural rather
than review-dependent. Its closed schema has no operator, suggestion,
rationale, custody owner/source, correlation, or idempotency fields. Proposal
number generates the application identity, Prototype identity, and display
label; the objective is null; route and custody values are enums; canonical
refs and digests are bounded patterns.

OOS accepts private workflow bindings internally but constructs the Studio
request by explicit projection, not by copying the Proposal route or caller
object. Negative tests reject added free-form fields and mismatched generated
identities. GitHub review remains a source-integrity control, while the v2
schema and adapter are the pre-publication data-admission controls.

### Delivery, Replay, And Evidence Integrity

The exact-base, one-commit, bounded-path, required-check, human-review,
canonical-merge, and byte-for-byte readback controls are sufficient once the
payload itself is safe for public source. Deterministic application and
idempotency identities preserve replay; conflicting reuse must remain denied.

Prepared or reviewed source is not application success. Only merged target
readback, a valid Studio receipt, and canonical Proposal acknowledgement may
project success. Cancellation after a merge must reconcile to the durable
target instead of claiming false cancellation or deleting evidence.

### Runtime And Activation Ownership

The reviewed OOS manifest still sets `runtime_activation: false`, and
`createProposalTargetRuntime` throws unless that source-owned flag is true and
the profile is `dev-integration`. No Platform overlay can legitimately replace
that embedded OOS decision.

Delivery ART architecture v6 now requires an OOS-owned source activation
Landing Unit after this Security approval and before Platform commissioning.
That unit must bind this decision and the repaired owner revisions, change only
the bounded OOS activation surface, and leave deployment, credentials, and live
proof to Platform. The staged v6 contract and both consumers reject missing,
out-of-order, or source-snapshot-mismatched activation evidence.

### AI

No model selects the Proposal, approves public-source content, chooses a
repository, authorizes source mutation, reviews or merges the target change, or
establishes completion. The reviewed path adds no AI authority.

## Closed Findings And Residual Constraints

1. **Public-source admission: closed.** Studio v2 and OOS PR #285 enforce the
   public-safe projection before branch publication and prove both positive and
   negative cases.
2. **Source activation ownership: closed at the planning-control layer.** The
   staged v6 contract and its OOS/WGCF consumers require the OOS-owned activation
   Landing Unit and exact source-snapshot evidence.
3. **Platform commissioning remains sequenced, not pre-approved.** Work item
   `#1236` may start only after v6 activation, the OOS activation revision, and
   its required evidence are current.
4. **Existing expansion gates remain.** Trusted human identity, governed shared
   secret delivery, repeatable exact-image operating proof, stage, production,
   public Console exposure, and AI-driven application remain outside scope.

## Decision

`approved`

Approved only for the bounded OOS-owned `dev-integration` source activation
step represented by `gate:proposal-target-controlled-activation` and for
Platform commissioning against the exact corrective Console revision
`d66411f128c3fd2f21ac274f620352977966fecd`, OOS revision
`0e935029327c3195f7ad1026c6f450f4b32c52dd`, and Prototype Studio revision
`4066ea5ba5a68ab7ab12acc7fc395897e1ae6c3f`, using the repaired Platform
verifier revision `85d7287ddccf021637d36131a5b661e75f1fdf4c`.

Not approved:

- Platform commissioning while the exact OOS source remains runtime-inactive;
- direct browser access to OOS, GitHub, OpenProject, or Prototype Studio source;
- synthetic, stale, malformed, mismatched, partial, or unreviewed evidence as
  success; or
- shared, stage, production, remote, multi-user, or AI-driven operation.

Platform must separately prove the activated source revision, dedicated
credential delivery, composed loopback runtime, and live acceptance before
claiming commissioning. Any change to the v2 public projection, target repo,
identity model, exposure, or environment requires another delta review.

## Related Artifacts

- [Proposal live-integration review](2026-08-16-governance-operations-console-proposal-live-integration.md)
- [Proposal-to-Delivery application review](2026-08-21-proposal-to-delivery-application.md)
- [Security delta review process](../security-delta-review-process.md)
- [Security review checklist](../security-review-checklist.md)
- [Studio pull request #22](https://github.com/mfshaf7/workspace-prototype-studio/pull/22)
- [Studio public-safe correction #23](https://github.com/mfshaf7/workspace-prototype-studio/pull/23)
- [OOS pull request #283](https://github.com/mfshaf7/operator-orchestration-service/pull/283)
- [OOS public-safe correction #285](https://github.com/mfshaf7/operator-orchestration-service/pull/285)
- [Console pull request #52](https://github.com/mfshaf7/governance-operations-console/pull/52)
- [Console caller-attribution repair pull request #53](https://github.com/mfshaf7/governance-operations-console/pull/53)
- [Console preparation-contract repair pull request #54](https://github.com/mfshaf7/governance-operations-console/pull/54)
- [Console submission-contract repair pull request #56](https://github.com/mfshaf7/governance-operations-console/pull/56)
- [Studio handoff-reference repair pull request #24](https://github.com/mfshaf7/workspace-prototype-studio/pull/24)
- [OOS handoff-reference repair pull request #288](https://github.com/mfshaf7/operator-orchestration-service/pull/288)
- [OOS zero-mutation restart repair pull request #289](https://github.com/mfshaf7/operator-orchestration-service/pull/289)
- [Console live-handoff conformance pull request #57](https://github.com/mfshaf7/governance-operations-console/pull/57)
- [Platform receipt-source binding repair pull request #274](https://github.com/mfshaf7/platform-engineering/pull/274)
- [Delivery ART v6 activation-ownership review](2026-10-08-delivery-art-architecture-v6-activation-ownership.md)
