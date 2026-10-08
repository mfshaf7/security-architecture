# Prototype Preview Runtime Execution-Boundary Security Delta

## Summary

- date: 2026-10-09
- owner repo: `security-architecture`
- delivery initiative: `openproject://work_packages/1203`
- parent feature: `openproject://work_packages/1213`
- security review item: `openproject://work_packages/1239`
- governing gate: `gate:preview-runtime-operating-acceptance`
- governing architecture packet:
  `wgcf://artifacts/delivery-art/sha256/3a4b5edb6bc54ff47a45f610b41f75bc57dd9d1ab56e9475518100d75ff72ab0`
- reviewed source:
  - Workspace Prototype Studio initial merge:
    `workspace-prototype-studio@5fb10dad78be88c65c3fe2a5deaaf0384bed844d`
  - Workspace Prototype Studio corrective reviewed head:
    `workspace-prototype-studio@b8b9064a28ad068e1daa99c1786e5d8d967013a8`
  - Workspace Prototype Studio corrective merge:
    `workspace-prototype-studio@2af8cfb95d40536ca8d50fbb5163e49df26c628e`
  - Governance Operations Console initial merge:
    `governance-operations-console@d5bb0ae792bf10f0014d3c8d6c5e3f44ab4876ca`
  - Governance Operations Console corrective reviewed head:
    `governance-operations-console@1349239a0294119cfd2f45736c90aed328dec2c7`
  - Governance Operations Console corrective merge:
    `governance-operations-console@d8bd3f1e7e528ea3bd8009db104f386e691cc2ad`
- source review:
  - [Studio owner implementation PR #26](https://github.com/mfshaf7/workspace-prototype-studio/pull/26)
  - [Studio source-binding correction PR #27](https://github.com/mfshaf7/workspace-prototype-studio/pull/27)
  - [Console owner adapter PR #58](https://github.com/mfshaf7/governance-operations-console/pull/58)
  - [Console atomic-binding correction PR #59](https://github.com/mfshaf7/governance-operations-console/pull/59)
- decision: `approved`

The corrected source is approved for loopback-only, single-operator
`dev-integration` preview operation and for exact-revision operating proof. It
does not approve shared hosting, public or client exposure, real data, external
network access, mutable product behavior, stage, production, or release use.

The initial implementation correctly bounded the server and Console adapter,
but exact-head review found two incomplete claims: Studio could report `HEAD`
from a dirty checkout, and Console checked expected runtime state before a
separate Studio command rather than under the Studio mutation lock. PRs #27 and
#59 close both gaps. Security approval applies only to the corrective merge
revisions above.

## Scope Delta

### Design Intent

- operate one static Prototype preview from Workspace Prototype Studio;
- bind only to `127.0.0.1` with no public ingress or external network;
- serve only synthetic or mock, read-only prototype source;
- let the Governance Operations Console request only `start`, `restart`, and
  `stop` through a server-only fixed owner adapter;
- preserve exact source, profile, runtime-instance, command, replay, receipt,
  and proof identity; and
- keep Security acceptance separate from source implementation and operating
  evidence.

### Implemented Control

Studio validates a closed profile schema, Prototype registry identity, source
location, loopback bind, data mode, mutation boundary, persistence posture,
runtime activation flag, and external state location. It rejects dirty tracked
source, untracked served files, ignored served files, symlinked served files,
directory traversal, dotfiles, mutation methods, stale process identity, and
invalid request identities before claiming reviewed source.

Every mutation now receives the exact operator-reviewed instance id, runtime
state, profile digest, source digest, and source revision. Studio normalizes and
checks that binding while holding the same file lock used for mutation. The
binding is retained inside the digest-bound receipt, so conflicting replay or a
changed state cannot be accepted as the reviewed action.

The Console invokes only the fixed Studio Python entrypoint with argument
arrays, a bounded non-secret environment, the configured owner checkout, an
external state root, and an exact 40-character Studio revision. The browser
cannot choose an executable, path, repository, state root, source revision, or
environment value. Mutation routes require the existing Console same-origin
session authorization. Configured owner failures and partial configuration
fail closed without prototype-local success.

Console validates the complete Studio projection, loopback endpoint, boundary,
source revision, digests, receipt, expected-state binding, before/after state,
readback, and proof. Private paths, process ids, raw diagnostics, and server
configuration are not projected to the browser.

### Operating Evidence

Studio PR #27 passed 74 tests and all repository validators. Its suite proves
clean-checkout and served-file custody, owner-locked stale-state denial,
conflicting replay denial, receipt tamper rejection, profile-boundary denial,
loopback lifecycle, traversal and dotfile denial, proof readback, and cleanup.

Console PR #59 passed architecture guards, 478 tests, type checking, production
build, and exact-head CI. Its adapter suite proves fixed command construction,
complete expected-state transport, stale preflight denial, owner-receipt binding,
malformed owner-output denial, proof binding, bounded failures, and explicit
disconnected behavior.

This is source and review evidence, not live operating proof. OOS must still
start the exact merged Studio revision, bind the exact Console revision, collect
current positive and negative proof, stop the process, and prove cleanup before
the parent Feature can be operating-ready.

## Review Areas

### Identity And Authorization

No new remote or shared identity is introduced. Local process and state access
remain under the operator account. The Console mutation route uses its existing
same-origin session authorization; the browser has no direct Studio command or
filesystem authority. This posture is acceptable only for the current
loopback, single-operator lane. Trusted multi-user identity remains an expansion
gate.

### Secrets And Data

The path requires no new secret. The subprocess environment is explicit and
contains no OOS, GitHub, OpenProject, or client credential. Runtime state and
receipts are operator-private outside source. The profile permits synthetic
data only, and the server has no external network path. Real or client data is
not approved.

### Delivery And Source Integrity

The runtime now requires a clean reviewed checkout and exact tracked custody
for every served file. Console independently pins the Studio revision, and both
profile and served-source digests flow through projection, expected state,
receipt, health, and proof. The corrective PR sequence preserves human review,
protected merge, rollback, and exact-source auditability.

### Runtime, Replay, And Failure Integrity

The owner lock is the mutation serialization point. Expected-state validation,
process identity, mutation, and receipt publication occur within that boundary.
Requests are replay-safe only when action and expected state are identical.
Stale state, conflicting replay, malformed output, digest mismatch, false
receipt, source drift, and incomplete readback fail without a success projection.

The static server binds only to loopback, emits defensive browser headers,
serves regular reviewed files, disables request logging, and denies every
mutation method. Stop refuses to signal a process unless exact health and
instance identity are current.

### Maturity And Evidence

The runtime and health response claim only `prototype-preview-only`. Proof
binds current profile, source, instance, health, and latest command receipt. The
proof's Security gate marker is an input to OOS sequencing; it is not itself a
Security decision or Platform readiness claim.

## Decision

`approved`

Security emits `gate:preview-runtime-operating-acceptance` for operating proof
against exactly:

- `workspace-prototype-studio@2af8cfb95d40536ca8d50fbb5163e49df26c628e`;
- `governance-operations-console@d8bd3f1e7e528ea3bd8009db104f386e691cc2ad`;
- the active `client-review-portal` profile;
- an operator-private state root outside both repositories; and
- the loopback-only boundary described above.

Not approved:

- dirty, detached, stale, mismatched, partial, synthetic-substitute, or
  unreviewed source evidence;
- direct browser selection of owner commands, paths, revisions, or environment;
- shared, remote, public, client-visible, stage, production, or release runtime;
- real data, external network access, mutable external systems, or persistent
  product state; or
- treating Preview proof as Platform, production, graduation, or security
  readiness beyond this exact gate.

Any change to identity, source custody, executable selection, served-file
policy, network reachability, data mode, mutation boundary, persistence,
exposure, or environment requires another delta review.

## Related Artifacts

- [Security delta review process](../security-delta-review-process.md)
- [Security review checklist](../security-review-checklist.md)
- [Governance Operations Console source-owned local-preview baseline](../products/2026-07-31-governance-operations-console-source-owned-local-preview.md)
- [Workspace Prototype Studio incubation baseline](2026-05-06-workspace-prototype-studio-product-incubation-baseline.md)
