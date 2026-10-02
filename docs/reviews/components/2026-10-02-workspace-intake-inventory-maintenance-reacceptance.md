# Workspace Intake And Inventory Maintenance Re-Acceptance

## Summary

- date: 2026-10-02
- owner repo: `security-architecture`
- affected review subjects:
  - `repos.platform-engineering`
  - `repos.workspace-governance`
  - `repos.workspace-governance-control-fabric`
  - `repos.operator-orchestration-service`
  - `repos.governance-operations-console`
- predecessor review:
  [`2026-10-02-workspace-intake-inventory-controlled-activation.md`](2026-10-02-workspace-intake-inventory-controlled-activation.md)
- maintenance tracking:
  `improvement-candidate:2026-10-02-intake-inventory-runtime-false-completion`
- decision: `approved-with-findings`

The predecessor review accepted source that was later commissioned with the
wrong evidence surface. Platform's recorded Console activity checks proved the
Console-to-OOS/WGCF read boundary only; they did not configure or call the
Workspace Intake and Inventory runtime paths. This review does not preserve
that completion claim.

This review accepts only the exact repaired revisions below for controlled,
single-operator, loopback `dev-integration` activation. It does not approve a
replacement ART defect chain and does not claim operating readiness. Platform
must pin this review, deliver the bounded identity, and produce direct runtime
proof before any new commissioning claim is valid.

### Exact Source Binding

| Owner | Accepted revision | Landing evidence | Security-relevant scope |
| --- | --- | --- | --- |
| Workspace Governance | [`b7dbe6655b68845bc55d783e54b8f1bd4afdb7b0`](https://github.com/mfshaf7/workspace-governance/commit/b7dbe6655b68845bc55d783e54b8f1bd4afdb7b0) | [PR #219](https://github.com/mfshaf7/workspace-governance/pull/219) | Restores the existing review transition contract and extends the existing `refinement-catalog` composition with explicit Intake and Inventory runtime bindings. |
| Workspace Governance Control Fabric | [`e31688369a3f59c76762b8f9359bd2acc478dcb4`](https://github.com/mfshaf7/workspace-governance-control-fabric/commit/e31688369a3f59c76762b8f9359bd2acc478dcb4) | [PR #94](https://github.com/mfshaf7/workspace-governance-control-fabric/pull/94) | Activates the three workspace-operation readiness runtimes with dedicated caller binding, source mounts, storage identity, and status evidence. |
| Operator Orchestration Service | [`4b0c3f9891e38c53412548bcbb355c7c8162fa18`](https://github.com/mfshaf7/operator-orchestration-service/commit/4b0c3f9891e38c53412548bcbb355c7c8162fa18) | [PR #258](https://github.com/mfshaf7/operator-orchestration-service/pull/258) | Configures the existing Intake and Inventory runtimes, exact WGCF bindings and source/state mounts, adds direct Inventory smoke, and requires exact-head human review before merge. |
| Governance Operations Console | [`d17912691a6dd99335c327637eda98c4105d98eb`](https://github.com/mfshaf7/governance-operations-console/commit/d17912691a6dd99335c327637eda98c4105d98eb) | [PR #48](https://github.com/mfshaf7/governance-operations-console/pull/48) | Retains the server-only Console request boundary and does not become commissioning authority. |
| Platform Engineering | [`b7c9151d83cbe5f51b396eff72b84f3abdd16a43`](https://github.com/mfshaf7/platform-engineering/commit/b7c9151d83cbe5f51b396eff72b84f3abdd16a43) | [PR #257](https://github.com/mfshaf7/platform-engineering/pull/257) | Expands the existing exact-repository identity to the Inventory authority files, blocks activation pending this review, adds credential-bound direct Intake/Inventory status proof, and invalidates Console-only commissioning evidence. |

All listed pull requests were authored by the admitted Agent Gary GitHub App,
approved by `mfshaf7`, merged to `main`, and passed their required checks. A
different owner revision requires another delta review or an explicit review
update; compatible intent is not a substitute for exact binding.

## Scope Delta

### Design Intent

- Keep Workspace Governance as the only canonical Intake and Inventory source.
- Use the existing `refinement-catalog` composition and existing OOS, WGCF,
  Console, and Platform identities; do not introduce another service or control
  plane.
- Let the existing Workspace Governance GitHub App prepare review branches for
  the exact Intake and Inventory authority files, while preserving human-only
  approval and merge.
- Require Platform commissioning to call the capability-specific authenticated
  Intake and Inventory routes and to prove invalid-caller denial.
- Keep Console cross-domain activity evidence explicitly separate from
  Workspace operations commissioning evidence.

### Implemented Control

The Workspace Governance App remains selected to one immutable repository with
Metadata read, Contents write, Pull requests write, and Checks read. The source
boundary now permits only these branches:

- `intake/<64-hex-digest>`
- `inventory/<64-hex-digest>`
- `inventory-lifecycle/<64-hex-digest>`

OOS limits writes to the intake register, `repos.yaml`, `products.yaml`,
`components.yaml`, and the append-only inventory history. The provider token
does not have per-file permissions, so application enforcement and protected
`main` remain required compensating controls. The App is denied approval,
merge, bypass, force-push, direct-main write, repository administration,
secret access, and unrelated-repository access.

The repaired composition supplies explicit Intake and Inventory enable flags,
separate state roots, the canonical Workspace Governance authority mount,
dedicated OOS-to-WGCF caller configuration, exact implementation and service
identity references, and persistent local state. WGCF retains non-mutating
readiness authority; OOS retains request, source-review, recovery, and receipt
authority.

Platform `status` now verifies the exact projected credential binding and the
approved profile/session before executing a bounded in-pod probe. The probe
calls authenticated Intake preparation and Inventory registry routes, requires
the same 40-character canonical authority revision, verifies
`canonical_mutation: false`, checks required runtime bindings and mounts, and
requires an invalid caller to receive `401 caller_auth_invalid`. Its receipt is
secret-free and must reference this exact Security acceptance.

### Operating Evidence

The exact source revisions and their CI checks are present. Direct live
Workspace operations evidence is not yet present. The earlier Platform record
is explicitly invalidated because it exercised only the Console activity
surface.

Operating evidence must be produced after the Platform contract pins the
merged revision containing this review. It must cover identity commission and
delivery, direct `status`, restart and repeated `status`, revocation, bounded
rollback, teardown, and final activation. The review cannot approve its own
future merge or that later runtime evidence.

## Review Areas

### Identity And Authorization

No new machine or human identity is introduced. The existing Workspace
Governance App gains narrowly defined application-level Inventory source
scope. The repository-level Contents permission is broader than those paths,
so the activation remains conditional on exact branch/path enforcement,
protected `main`, no App bypass, and exact-head human review by `mfshaf7`.

The Console caller, OOS-to-WGCF caller, Workspace Governance App, Agent Gary,
and human reviewer remain distinct. The Platform probe may use the configured
Console caller secret inside the OOS pod to prove the OOS authorization
boundary; that does not prove browser-to-Console operation and must not be
reported as Console end-to-end evidence.

### Secrets And Custody

The GitHub App private key remains in Platform Vault custody. OOS receives only
a short-lived installation token through a read-only Secret volume and rereads
the projected file. Caller credentials remain server-side. Source, browser
responses, logs, ART text, review artifacts, and receipts may contain only
bounded identities, revisions, digests, outcomes, and timestamps—not secret
values or authorization headers.

### Delivery And Machine Trust

Agent Gary authors and publishes source; `mfshaf7` reviews and merges. The
Workspace Governance runtime App may prepare bounded review source but may not
approve or merge it. Exact source revisions, exact current PR head, trusted
owner checks, canonical merged readback, and branch protection remain required
before a source mutation can be considered complete.

### Runtime, Visibility, Rollback, And Cleanup

Activation is limited to the existing local `accepted-idea-delivery` profile
inside the `refinement-catalog` composition. Platform must expose a secret-free
receipt that binds the profile, session, exact source revisions, credential
binding, Security review reference, authority revision, direct route results,
and denial result.

Rollback must revoke the projected token, remove its Secret and deployment
mounts, suspend or remove only the affected composition state, and retain Git,
review, denied-path, and receipt history. Restart proof must show that the same
bounded configuration and identity survive reconciliation without fixture or
Console-activity fallback.

### AI

No model call, model-selected action, prompt boundary, AI approval, or tool
authority is introduced. AI output cannot supply identity, widen source scope,
approve, merge, or establish runtime readiness.

## Findings And Activation Conditions

1. **Repository Contents permission is not a file-level control.** OOS path and
   branch enforcement plus protected `main` are mandatory compensating
   controls. Any provider bypass or broader application path fails activation.
2. **The direct in-pod probe is capability commissioning evidence, not Console
   end-to-end evidence.** It must not be used to claim browser, session, or
   Console workflow readiness.
3. **Source acceptance is not operating proof.** Platform must pin the merged
   Security revision and successfully run the direct proof sequence before
   recording commissioning.
4. **The local operating-system account remains the human trust root.** This is
   accepted only for single-operator loopback `dev-integration`. Shared,
   remote, multi-user, stage, production, ingress, and public exposure remain
   outside this decision.
5. **No replacement ART decomposition is authorized by this review.** The
   repair and Security acceptance are owner-repo maintenance. Any existing ART
   item may consume the eventual proof, but it is not the implementation home.

The owner for conditions 1 through 3 is `platform-engineering`, with OOS and
Workspace Governance as the implementation owners for their existing
enforcement surfaces. Conditions 4 and 5 are explicit scope limits. Failure of
any condition blocks activation rather than creating a partial-success claim.

## Decision

`approved-with-findings`

Approved:

- the exact five source revisions bound above;
- extension of the existing Workspace Governance App to the exact Inventory
  branch and file set under the compensating controls in this review;
- the existing `refinement-catalog` composition as the only local runtime
  composition for this capability;
- secret-free, credential-bound direct Intake preparation, Inventory registry,
  shared-authority-revision, and invalid-caller proof; and
- controlled single-operator loopback `dev-integration` activation after
  Platform pins this review's merged revision.

Not approved:

- the invalidated Console-activity receipts as Workspace operations evidence;
- runtime readiness based on source or this review alone;
- any unbound source revision, broader GitHub App scope, branch, or file path;
- machine approval, merge, protected-branch bypass, direct-main write, or
  success before canonical merged readback;
- fixture fallback after live configuration is selected;
- shared, remote, multi-user, stage, production, ingress, or public use; or
- deletion of canonical source, review, denial, or receipt history during
  rollback and cleanup.

## Related Artifacts

- [Predecessor Intake and Inventory review](2026-10-02-workspace-intake-inventory-controlled-activation.md)
- [Workspace Intake authority-boundary review](2026-09-06-workspace-intake-authority-boundary.md)
- [Governance Console identity activation review](2026-09-27-governance-operations-console-identity-activation.md)
- [Identity and access architecture](../../architecture/domains/identity-and-access.md)
- [Secrets and recovery architecture](../../architecture/domains/secrets-and-recovery.md)
- [GitOps and machine trust architecture](../../architecture/domains/gitops-and-machine-trust.md)
- [Security delta review process](../security-delta-review-process.md)
- [Security review checklist](../security-review-checklist.md)
