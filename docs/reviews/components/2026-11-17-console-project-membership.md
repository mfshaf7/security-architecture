# Console Delivery project membership

## Summary

Review the operator-approved, bounded project-membership extension in the
current maintenance preview batch. Main-agent Security judgment and final
landing judgment remain under standing delegated operator authority; this is
not independent assurance. Landing Unit Decision: `feature_single_landing_unit`,
`maintenance-project-membership-review-20261117`, separate from implementation
owner Landing Units because Security retains its review boundary.

This is an additive review. Prior Console/OOS context, advisor and runtime
reviews retain their scopes. It does not qualify the whole pending batch or
replace its final composed-source acceptance.

## Scope Delta

Console adds a Project Members table and reviewed add/change/remove forms from
Catalog's Assignee / Responsible category. OOS authenticates a caller-specific
credential, requires Delivery mutation authority and binds the configured
operator for both reads and writes. The Console server independently verifies
the existing session role/authority and requires same-origin JSON mutation.
Browser input has no project, caller or operator authority fields.

Platform extends the existing bounded OpenProject Catalog adapter with two
closed membership routes. Native Members services run under the existing
non-admin broker identity and enforce current OpenProject role grantability
and group propagation/cleanup. The separate local profile provisioning adds
only `view_members` and `manage_members` to that identity in the Delivery
project. Project-specific role overrides prevent applying that grant to the
Proposal project. Platform-integrated production is unchanged.

The existing transactional setting/receipt store binds the accepted decision,
native effect, readback and receipt in one commit. Exact replay returns the
original outcome even after a newer decision; conflicting request reuse and
stale target versions fail. Runtime read failure never substitutes fixtures.
The Catalog lookup now follows the native assignment-eligibility scope, rather
than mislabelling every active project user as assignable. Native qualification
checks both addition to the assignment/Catalog choices and removal after a
Reader role change. Placeholder records remain inspectable with their actual
kind, while mutation stays limited to the approved existing users/groups.
Unknown browser outcomes freeze the request, survive form close in the mounted
workspace, and block replacements while exact recovery is pending. Canonical
recent outcomes remain available after browser restart. A later list failure
retains an applied receipt while preventing further mutations.

## Review Areas

- Identity: exact configured Delivery project; native visible existing users
  and groups; existing non-built-in project roles only. Global and internal
  service roles are excluded. Administrator/service memberships and groups
  containing those identities are protected. Individually inherited roles
  remain managed through their group. No user creation, invitations, directory
  enumeration privilege, new identity provider or generic admin proxy.
- Secrets: reuse existing server-held OOS caller and Catalog adapter secrets.
  Browser state and public source contain no backend credentials. Membership
  details and receipts remain in the installation database/private evidence.
- Delivery: explicit reviewed request; current membership version; receipt and
  native readback checks; no fabricated success, replacement retry or rollback
  of a later decision. Historical assignments are not rewritten on removal.
- Runtime: bounded response pages and account search, existing local profile,
  exact source activation still required. Source rollback removes only the
  added broker role and paired adapter, retaining memberships and receipts.
- AI: no advisor tool or autonomous identity/membership authority is added.

## Evidence

Native permission preflight first returned 403. Under the project-scoped role,
the actual OpenProject membership form and role/principal routes returned 200.
The native rollback-only integration support checks HTTP authentication and
dispatch, add, role change, removal, exact historical replay, conflicting retry,
stale review, service protection, global-role denial, group inheritance/cleanup,
bounded search/pagination and complete fixture/receipt rollback.

OOS checks cover request authority injection, exact actor attribution, receipt
digests/readback, native denial mapping, caller-specific authentication,
operator binding and duplicate transport keys. Browser checks cover explicit
disconnected add/change/remove, protected access, failed-read retry with no
fixture substitution, and exact request recovery after form close. Filled
layout and form overflow are checked at 1700×1050 and 1280×720. These are native
rollback and isolated transport proofs, not published operating acceptance.

## Decision

`approved` for the bounded source design and local qualification described
above. This decision grants no production activation or broader identity
administration. Final composed-source acceptance and commissioning of the
coordinated preview batch remain required before claiming live capability.
No Security risk acceptance or exception is introduced by this review.

## Owner artifacts

- [OOS membership service](https://github.com/mfshaf7/operator-orchestration-service/blob/main/src/catalog/membership-service.js)
- [OOS operator procedure](https://github.com/mfshaf7/operator-orchestration-service/blob/main/docs/operations/delivery-project-members.md)
- [Platform native adapter](https://github.com/mfshaf7/platform-engineering/blob/main/products/openproject/catalog-control/openproject_delivery_catalog_control.rb)
- [Native rollback qualification](https://github.com/mfshaf7/platform-engineering/blob/main/products/openproject/catalog-control/test_memberships_native.rb)
- [Console procedure](https://github.com/mfshaf7/governance-operations-console/blob/main/docs/product/refinement-catalog-live-integration.md)

The owner sources are now merged. The subsequent [complete-batch exact-source
review](2026-11-18-console-advisor-execution-catalog.md) records their PRs, merged
revisions and final activation boundary. This original scoped review does not
substitute for that composed acceptance or live commissioning.
