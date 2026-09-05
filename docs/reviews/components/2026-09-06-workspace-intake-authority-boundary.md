# Workspace Intake Authority Boundary Review

## Summary

- date: 2026-09-06
- owner repo: `security-architecture`
- delivery ref: `openproject://work_packages/1066`
- parent initiative: `openproject://work_packages/890`
- governing architecture:
  `wgcf://artifacts/delivery-art/sha256/0e0d7916e2e01e014ae682e47bf54e7632641b2e475c40a4a2ca9e869e4f061b`
- reviewed source:
  - Workspace Governance PR head:
    `workspace-governance@934c67587872c9df4693be4eef0477e339c09fb0`
  - Workspace Governance merge:
    `workspace-governance@6fd843eb43405f6bdcc439d23b18e556eca05b26`
  - Workspace Governance Control Fabric PR head:
    `workspace-governance-control-fabric@8c0c91784341c5fd5d66ff709e1a3ca121ade91e`
  - Workspace Governance Control Fabric merge:
    `workspace-governance-control-fabric@e8a96ecd01a1ea2481c436fd59fb339ab4fcb162`
  - Operator Orchestration Service workflow PR head:
    `operator-orchestration-service@c62ef3fc22d51ef5d8003c35fdbaa87720e7f463`
  - Operator Orchestration Service preparation correction PR head:
    `operator-orchestration-service@1dca8fdaedabc73bac58ce7f2d9749b1530a5ba2`
  - Operator Orchestration Service merge:
    `operator-orchestration-service@bcd077769f280c1f855a775cd84c412959b3538e`
  - Platform Engineering PR head:
    `platform-engineering@0d101cd5ffaca898983dd9b1294cf4d21abf6148`
  - Platform Engineering merge:
    `platform-engineering@859db25a4e6add832436c9655ac52a03e1a1638c`
  - Workspace Prototype Studio PR head:
    `workspace-prototype-studio@18ba5c49b70843c39ae538f891e7fc7a24607047`
  - Workspace Prototype Studio merge:
    `workspace-prototype-studio@41e3952dc62569612c3ecbfe5daa9c54b8a339b0`
  - Governance Operations Console PR head:
    `governance-operations-console@6193df873e547a51f5ddb992075f2f2e0f6d78a2`
  - Governance Operations Console merge:
    `governance-operations-console@3180754efc726ca0b830fc8940cce683378dd74e`
- decision: `approved-with-findings`

The exact source is acceptable as an inactive Workspace Intake foundation. It
keeps classification and canonical records in Workspace Governance,
non-mutating readiness in WGCF, durable source-review coordination in OOS,
machine identity and secret delivery in Platform Engineering, source-candidate
emission in the source owner, and operator projection in the Console.

Normal Workspace Intake availability is not approved. ART `#1082` may perform
bounded identity commissioning and provider-control proof. ART `#1069` must
close the source-candidate authenticity gap and prove the composed positive and
negative path before the Console can present Workspace Intake as operating.

## Scope Delta

### Design Intent

Workspace Intake classifies a repository, product, or component before active
inventory. The action must:

- bind one exact source candidate, target, current canonical state, requested
  record, operator decision, workflow execution, reviewed source change, merge,
  and canonical readback;
- keep intake classification, active-inventory posture, product maturity, and
  runtime activation as independent decisions;
- use one exact-repository, revocable application identity without personal or
  ambient operator credentials;
- mutate only `contracts/intake-register.yaml` on a non-default review branch;
- require exact-head owner validation, human review and merge, and merged
  canonical readback before success; and
- preserve denial, cancellation, replay, failure, review, and rollback evidence.

### Implemented Control

The reviewed source provides:

- Workspace Intake v2 schemas, canonical JSON digests, optimistic concurrency,
  immutable source identity on update, atomic owner mutation, and no hard delete;
- WGCF caller authentication, exact authority revision and file digests,
  immutable readiness receipts, replay-conflict denial, database-backed ledger
  evidence, and no canonical mutation;
- OOS caller binding, deterministic request identity, durable single-host
  coordination, kernel serialization, source preparation through the committed
  owner command, and retry/cancel/recovery semantics;
- an exact GitHub repository id and owner, `intake/<digest>` branch namespace,
  one-file/one-commit review checks, redirect denial, bounded provider responses,
  exact-head approval checks, trusted CI readback, and no merge endpoint;
- a selected but inactive GitHub App definition with Metadata read, Contents
  write, Pull requests write, and Checks read, plus Platform-owned secret custody
  and explicit revocation requirements;
- a Prototype source adapter that validates committed registry and approved
  baseline evidence before emitting a candidate; and
- same-origin Console routes that keep OOS credentials server-side, re-read
  canonical preparation immediately before submission, reject malformed OOS
  projections, and never fall back to fixture mutation.

### Operating Evidence

All reviewed pull-request heads passed their repository checks. The owner
Review Packets and tests cover schema and digest failure, stale authority,
replay conflict, exact Git source changes, process interruption, provider
readback, malformed Console responses, and inactive runtime behavior.

This remains source and bounded sandbox evidence. No Workspace Intake GitHub
App, installation token, provider ruleset proof, Platform secret projection,
active WGCF/OOS composition, or real end-to-end entrant classification has been
commissioned by this review.

## Review Areas

### Identity And Authorization

The routine source identity must be the dedicated GitHub App installation
defined by Platform Engineering and selected only for
`mfshaf7/workspace-governance`, repository id `1212447211`. Personal tokens,
OAuth user tokens, operator credentials, ambient `gh` login, shared automation
tokens, deploy keys, and the repository-provisioning or repository-lifecycle
Apps are not approved substitutes.

The App's Contents write permission is broader than the normal one-file source
operation and can reach provider merge or branch-write APIs. ART `#1082` must
therefore prove provider-enforced main-update and merge denial, exact-repository
selection, no App bypass, required current-head human review, stale-approval
dismissal, trusted owner validation, and force-push/deletion denial. OOS
application checks supplement these provider controls; they do not replace them.

The current Console-to-OOS boundary authenticates a service caller, not an end
user. Synthetic local operator attribution is acceptable only for bounded
`dev-integration` evidence. Wider or multi-user operation requires a separately
reviewed authenticated operator delegation path.

### Secrets

Platform Engineering owns the App private key, installation identity, token
minting, delivery, rotation, suspension, and revocation. OOS may receive only a
short-lived installation token from a read-only mounted directory and must
re-read it for rotation. The private key must never enter OOS.

Secret values must remain absent from source, browser responses, requests,
decisions, workflow state, provider review text, receipts, logs, fixtures, and
Review Packets. The Console caller credential and WGCF caller credential must
remain server-side and separately scoped to their exact consumers.

### Delivery, Source And Provider Trust

Workspace Governance merged Git is the only classification authority. WGCF
readiness, OOS acknowledgement, a prepared branch, an open review, and a source
preparation receipt are evidence only. OOS must observe an exact reviewed merge,
successful owner checks, canonical-main ancestry, and digest-matching merged
readback before reporting success.

The provider destination is `https://api.github.com`; redirects are denied.
Operator and browser input cannot select provider host, repository, branch, or
write path. ART `#1082` must pin the actual runtime endpoint and prove that the
installation credential cannot be forwarded outside the admitted boundary.

The source-candidate boundary is not complete. The Prototype emitter itself
validates committed source, but the current Console submission accepts candidate
source and requested-record fields returned by the browser. OOS and WGCF verify
their schema and decision binding but do not resolve the candidate reference and
digest against the Delivery or Prototype source owner. Operator acceptance and
human source review still prevent silent admission, but they do not make a
browser-supplied provenance claim authoritative. ART `#1069` must reconstruct or
resolve the candidate server-side against its owner and prove altered source
reference, digest, evidence, target metadata, or requested record is rejected
before normal availability.

### Runtime, Audit, Recovery And Rollback

Every attempt must bind caller, operator reference, request and idempotency
identities, source candidate, current authority revision, request and decision
digests, session and execution, readiness receipt, source branch and head,
provider review, merge, readback, terminal receipt, and outcome.

The OOS store is an explicitly single-host durable coordination mechanism. Its
atomic writes, fsync, integrity digest, and kernel lock are acceptable for the
admitted local `dev-integration` profile; they are not multi-replica or governed
stage/production evidence. Corrupt or unavailable state must stop writes rather
than recreate completion.

Retry reuses the original identity. Conflicting reuse, stale authority, changed
review head, dependency failure, cancellation race, missing checks, or readback
mismatch must remain visibly non-successful. Rollback disables new requests,
revokes token delivery, and removes runtime projection while retaining Git,
workflow, review, denial, failure, readback, and receipt history.

### AI And Agentic Influence

The reviewed workflow uses an operator-authored decision. AI suggestions remain
optional, separately governed, and non-authoritative. A model must not supply
caller identity, accept its own suggestion, select credentials, authorize source
mutation, merge a review, or establish completion. Deterministic owner, WGCF,
OOS, provider, and canonical-readback checks remain authoritative.

## Findings And Activation Gates

1. **The provider identity is selected but not commissioned.** ART `#1082` must
   prove exact App and installation ids, exact repository selection and owner,
   minimum permissions, token issue/rotation, secret projection, audit,
   suspension, revocation, and rollback without exposing credential values.
2. **Provider-enforced merge and main-write denial is not proven.** ART `#1082`
   must prove the App cannot merge, update `main`, bypass current-head human
   review, force-push, delete refs, or reach another repository. Failure blocks
   activation rather than widening permissions or using a personal credential.
3. **Source-candidate authenticity is incomplete.** ART `#1069` must bind the
   submitted candidate to authoritative Delivery or Prototype owner readback and
   reject browser-altered provenance or requested-record fields. Shape and digest
   syntax alone are insufficient.
4. **The composed operating path is absent.** ART `#1069` must prove preparation,
   submission, readiness, branch publication, exact-head review, human merge,
   canonical readback, cancellation, replay, stale authority, altered candidate,
   provider denial, dependency failure, and rollback through the Console/OOS
   composition.
5. **Normal availability remains denied.** Bounded commissioning may proceed only
   to produce `#1082` and `#1069` evidence. Stage, production, external, multi-user,
   inventory-promotion, lifecycle, repository-provisioning, and runtime-activation
   claims remain outside this decision.

These findings are routed to existing ART children `#1082` and `#1069`. No
separate remediation item is required.

## Decision

`approved-with-findings`

Approved:

- the exact inactive Workspace Governance v2 intake contract and owner command;
- the exact inactive WGCF readiness evaluator and immutable receipt boundary;
- the exact inactive OOS workflow, source-review, recovery, and merged-readback
  implementation;
- the exact selected-not-active Platform identity definition;
- the exact Prototype candidate emitter and Console same-origin adapter as
  source implementations;
- bounded `#1082` identity commissioning needed to produce provider evidence;
  and
- bounded `#1069` correction and composed conformance needed to close the
  candidate and operating-evidence gates.

Not approved:

- normal Workspace Intake operator availability;
- treating browser-supplied source candidate fields as authoritative provenance;
- live source mutation before the exact App identity and provider controls pass;
- personal, ambient, shared, browser-held, or long-lived credentials;
- direct-main writes, automatic merge, App bypass, force-push, hard delete, or
  unrelated repository access;
- Console or WGCF mutation of canonical Workspace Governance files;
- success before exact reviewed merge and digest-matching canonical readback;
- intake classification as active inventory, product maturity, or runtime
  activation; or
- stage, production, external, or multi-user operation.

Security Architecture retains normal-availability judgment. This decision
allows only the bounded work needed to satisfy the existing activation and
conformance gates.

## Related Artifacts

- [Security delta review process](../security-delta-review-process.md)
- [Workspace Governance pull request #172](https://github.com/mfshaf7/workspace-governance/pull/172)
- [WGCF pull request #60](https://github.com/mfshaf7/workspace-governance-control-fabric/pull/60)
- [OOS Workspace Intake pull request #186](https://github.com/mfshaf7/operator-orchestration-service/pull/186)
- [OOS preparation correction pull request #187](https://github.com/mfshaf7/operator-orchestration-service/pull/187)
- [Platform identity definition pull request #229](https://github.com/mfshaf7/platform-engineering/pull/229)
- [Prototype candidate pull request #5](https://github.com/mfshaf7/workspace-prototype-studio/pull/5)
- [Console adapter pull request #19](https://github.com/mfshaf7/governance-operations-console/pull/19)
- [GitHub App permission reference](https://docs.github.com/en/rest/authentication/permissions-required-for-github-apps)
- [GitHub repository rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets)
