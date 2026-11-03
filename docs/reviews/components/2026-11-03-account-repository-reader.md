# Account metadata reader maintenance

## Summary

Review the operator-approved maintenance that makes one GitHub metadata reader
connection cover future repositories and renew through the existing Console
runtime. This extends the existing identity producer, credential timer and OOS
adapter; it introduces no new service, host privilege or workflow engine.

The main agent retains Security and landing judgment under the operator's
standing delegation. This is not independent third-party attestation. The
review inherits the unchanged controls and exact-source requirements in
[repository verification maturity](2026-11-03-repository-verification-maturity.md)
and [the existing composition review](2026-10-24-configurable-ai-routing.md).

## Scope Delta

### Design intent

An operator explicitly chooses either selected-repository isolation or one
personal account/organization's metadata, including repositories created later.
The latter must not require another installation selection for every project.
GitHub's All repositories grant is deliberate and limited to Metadata read;
source-content and all write permissions remain separate.

### Implemented control

- Platform's existing `repository-provider-identity` command accepts mutually
  exclusive `--repository` and `--account` scopes. Existing selected mode stays
  unchanged. Denial never silently chooses account scope.
- The account producer verifies signed native App and installation identity,
  the intended User or Organization account, no suspension, no events, exact
  Metadata read permissions and the explicit All repositories grant. It omits
  repository filters when issuing that token, so future repositories are not
  excluded by a token snapshot. The returned token must also attest All
  repositories; a changed or missing token scope is revoked before projection.
  Token lifetime remains at most one hour.
- The protected prepared/delivered receipt binds App, installation, account,
  contract, credential scope, expiry and token fingerprint. No secret value
  enters evidence. The same Platform-owned Kubernetes Secret carries the
  reader token and account. No minting key reaches OOS or the browser.
- OOS rejects another account before coordinate lookup, and rejects a foreign
  account in immutable-ID readback. Provider destination, redirect denial,
  payload bounds, immutable identity validation and authenticated callers
  remain enforced. Provisioning uses its separate credential.
- The Console uses its existing authenticated read-only OOS route without
  demanding unused link/create authority references. Mutation commands retain
  their own policy and binding checks. Native machine error codes remain
  distinct from human messages, so account/setup failures are not presented as
  transient retry opportunities. History separates recorded receipts from
  provider observations and preserves original references.
- The existing complete-runtime timer maintains only an explicitly generated
  private selection. Absence enables nothing. Owner/mode/size, profile, local
  cluster, contract, native credential binding and Secret ownership are checked.
  Rotation reuses the existing producer and Vault custody; it does not add a
  caller-selected destination, new namespace or minting API.
- Fewer than twenty remaining minutes triggers renewal. Matching prepared
  deliveries resume after interruption without another token. A missing
  projection is restored only from the valid existing selection; malformed or
  foreign state withholds the reader rather than widening the grant.
- The existing group rollout consumes only the two optional reader Secret
  references. Locked selection comparison prevents stale renewal from
  overwriting disconnect or account replacement; revocation clears the two
  reader consumer fields through the existing rollout.
- The same rollout records a delivery version. An unchanged healthy tick causes no new
  reader issuance or pod-template change. Revocation does not block core
  startup, and an unavailable reader cannot prevent maintenance of the five
  existing workflow identities. Previous credentials retire only after actual
  consumer fingerprint and account checks pass.

### Operating evidence boundary

Source tests exercise account types, scope/permission denial, token expiry,
protected selection, interrupted delivery, missing projection, renewal,
consumption-before-retirement and optional failure isolation. OOS exercises a
repository appearing after connection setup using the same client, token and
configuration, plus foreign-account denial. These are isolated engineering
proofs, not a live repository-creation claim.

Native account-wide commissioning now verifies the exact Metadata read grant
and returned All repositories token scope, with no repository filter in the
issuance request. That token read an existing private repository outside the
previous single-repository selection; the proof token was revoked. No new live
repository was created, and this does not prove deployed OOS scope enforcement
or unattended runtime renewal.

Exact reviewed source activation, actual Console
readback, renewal and restart readback remain required before that mode is
reported operational. Customer-facing setup and fresh customer installation
qualification remain open product-readiness work.

## Review Areas

- **Identity:** an account grant is broader than selected-repository access and
  must be explicitly authorized. Its boundary is one connected account, not an
  arbitrary repository set or access to another account's private data.
- **Secrets:** use the existing dedicated metadata App/Vault path, short-lived
  installation token and protected projection. No operator/PAT, provisioning
  credential fallback, browser secret or minting key in OOS.
- **Delivery/runtime:** maintain the existing exact-source composition gate.
  Account connection does not enable custody decisions, lifecycle writes,
  Catalog updates or production release authority. Optional connection failure
  preserves core operation and other credential maintenance.
- **Privacy:** account metadata access includes names and metadata of future
  private repositories. The operator must understand that scope. Selected mode
  remains available when account-wide metadata access is inappropriate.

## Decision

Approved for source landing within these boundaries. This decision permits
bounded native commissioning of the explicitly authorized metadata-only account
identity; it does not itself activate a new runtime source set. Before normal
activation, bind the final merged OOS/Console source and Platform tree in the
existing composed Security decision and follow its normal activation procedure.
Do not infer account-mode operating acceptance from selected-token containment
or simulated future repositories.

Revoke through the same producer with the exact account/App/installation and
preserve the revoked selection outcome. Runtime references remain optional so
the core can restart without that Secret. Reconnection uses normal explicit
delivery. Roll back the coordinated Platform/OOS scope extension while retaining
existing workflow credentials, repository data, original receipts and selected
mode. This is local dev-integration acceptance, not stage/production or complete
customer-installation qualification.

## Native Readiness And History Compatibility

Native activation exposed a response-contract mismatch in Platform's existing
negative-read probe. The authenticated Console route correctly preserved OOS's
`repository_custody_request_not_found` code and returned its original live 404;
the probe still expected the former generic adapter code. The correction uses
the canonical machine code while preserving the HTTP status, message and
live-mode checks. A generic or unrelated 404 remains denied. The corrected
probe passed against the actual Console response before source landing.

Native History inspection also found a setup response incorrectly classified
as transient: OOS's disabled lifecycle runtime returns a configuration 503.
The Console adapter now marks the known runtime/provider setup codes as
nonretryable while preserving Retry for genuine provider unavailability. The
actual-backend preview keeps the recorded creation receipt visible, identifies
the disabled lifecycle source and offers no misleading Retry. This changes
failure presentation; it enables no lifecycle command or provider privilege.

The accepted account connection passed real public and private repository
metadata reads through Console and deployed OOS, and rejected a foreign account.
A bounded reader-only rotation used the existing accepted maintainer and grouped
consumer rollout under its lifecycle lock. Actual consumer account/fingerprint
checks passed before the previous token retired; a new maintainer instance
then reused the current credential without issuing another one. This is native
rotation/reuse evidence, not a claim that timed expiry or a new live repository
creation was observed. Final source acceptance, the supported runtime restart
and complete status checks remain required for composition closure.
