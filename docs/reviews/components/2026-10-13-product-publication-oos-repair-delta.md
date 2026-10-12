# Product Publication OOS Repair Security Delta

## Summary

- date: 2026-10-13
- owner repo: `security-architecture`
- delivery initiative: `openproject://work_packages/894`
- active commissioning item: `openproject://work_packages/1273`
- baseline decision:
  `security-architecture://product-publication/decisions/lifecycle-maintenance-v1`
- baseline review:
  `docs/reviews/components/2026-10-12-product-publication-lifecycle-maintenance-boundary.md`
- baseline OOS activation revision:
  `operator-orchestration-service@2bb51556202a9f3819ca99bad3cad06256480db9`
- reviewed repair revision:
  `operator-orchestration-service@94534d621aa9300b51035cd05554f27b6b4e3180`
- reviewed repair commits:
  - `2be983711e4794cddbaeeb4f9551a258f9cabb1c`
  - `94534d621aa9300b51035cd05554f27b6b4e3180`
- decision: `approved`

Security approves advancing the Platform commissioning policy's exact OOS
source pin from `2bb5155` to `94534d6`. The two descendant commits repair
workflow evidence integrity; they do not add an action, target, identity,
credential, authority, endpoint, or trust boundary.

This delta does not replace or broaden the baseline lifecycle-maintenance
decision. The runtime security decision URI, digest, and revision remain bound
to the original reviewed decision. This artifact supplies the later source
repair judgment without creating a circular dependency in which an OOS source
commit would have to bind a Security commit that reviews that same OOS commit.

## Scope Delta

### Design Intent

The exact-source gate correctly stopped commissioning after two OOS repair
commits landed. The durable correction is to review those commits and advance
the exact pin. Replacing the pin with an open-ended descendant rule is denied
because it would admit future OOS changes without an explicit source decision.

### Implemented Control

The reviewed delta from `2bb5155` through `94534d6` is limited to:

- a shared monotonic workflow-progress helper and adoption by the existing
  proposal, prototype, intake, and inventory workflows;
- tests proving a recorded same-sequence failure advances the externally
  visible workflow projection instead of reusing stale revision identity;
- corrected Workspace Inventory history readback that compares the lifecycle
  event's nested target record identifier to the requested record; and
- real-Git and service tests proving the latest immutable lifecycle event is
  returned after merge.

The Product Publication action set, approved postures, caller authentication,
owner boundaries, journal semantics, Workspace Registry mutation path, WGCF
readiness authority, and browser denial remain unchanged.

### Operating Evidence

OOS pull requests `#320` and `#321` were authored by the bounded Agent source
identity, approved by the human reviewer, passed exact-head CI, merged to
protected `main`, and completed strict branch-lifecycle cleanup. The local OOS
suite passed 1,281 tests with two documented skips, and the real-Git Workspace
Inventory conformance suite passed 12 checks.

The repaired source was rolled into the existing `refinement-catalog`
dev-integration composition by the Platform-owned Workspace Intake credential
rotation path. A new OOS pod started at `2026-10-12T19:54:51Z`, runtime status
passed, and live source readback contained the corrected nested target-record
comparison. These facts demonstrate the repair is operable; final lifecycle
sequence acceptance remains owned by work item `#1273`.

## Review Areas

### Identity And Secrets

No identity, permission, secret, custody path, caller, or token scope changes.
The rollout reused the existing short-lived Workspace Intake identity and its
bounded one-repository installation token.

### Delivery And Source Integrity

Both repair commits descend from the baseline OOS activation revision. The
Platform policy must continue to require one exact OOS revision and may advance
that value only to `94534d621aa9300b51035cd05554f27b6b4e3180` under this
review. The original lifecycle-maintenance Security decision stays immutable.

### Runtime And Evidence Integrity

The monotonic projection repair prevents a journaled failure from being hidden
behind a reused external revision. The history readback repair prevents a
valid merged lifecycle event from being projected as absent. Both changes
strengthen fail-closed recovery and auditability without granting a new
mutation path.

### Residual Risk

The repairs have operating proof, but the complete publication and Registry
round trip is not yet accepted. Existing work item `#1273` must still prove the
ordered sequence, negative cases, process-loss recovery, restart, rollback,
and final owner reconciliation. This is the existing commissioning condition,
not a new finding or work item.

## Decision

`approved`

Platform may advance the exact OOS source revision in the existing Product
Publication commissioning policy to
`94534d621aa9300b51035cd05554f27b6b4e3180`. It must preserve the original
Security decision URI, digest, revision, approved targets, denied targets, and
owner boundaries. Any broader source authority rule, new action, new target,
new identity, or changed trust boundary requires a fresh decision.
