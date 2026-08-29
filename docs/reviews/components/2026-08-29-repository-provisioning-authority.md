# Repository Provisioning Authority Review

## Summary

- date: 2026-08-29
- owner repo: `security-architecture`
- delivery ref: `openproject://work_packages/1047`
- parent initiative: `openproject://work_packages/888`
- governing architecture:
  `wgcf://artifacts/delivery-art/sha256/7723dd72afd59e286c8b97933bd0c3fd4185f7a53159fcdf01cf67f6a987d673`
- reviewed source:
  - Workspace Governance merge:
    `workspace-governance@3dd225fba5a3d619bb99340e2d2d29e6ae833087`
  - Workspace Governance Control Fabric merge:
    `workspace-governance-control-fabric@7b6414019771ea9364c363aa8a19364f656a7446`
  - Operator Orchestration Service reviewed head:
    `operator-orchestration-service@ec1b72a52a645872ec63ccda3d7cb50835162aa4`
  - Operator Orchestration Service merge:
    `operator-orchestration-service@64d7b420fdc30fdafb4c48a0f728b120e5717f4b`
- source evidence:
  - Workspace Governance Review Packet:
    `wgcf://artifacts/delivery-art/sha256/6d5b77e749672cd202e6c4c6126c9a959ba3313d3299b74f91f268b08a7101fd`
  - WGCF Review Packet:
    `wgcf://artifacts/delivery-art/sha256/6ecf245c1ff165a61dbc9fb22a198a4f6d9ee16660ddf981c41f84a6ffd9e9b6`
  - OOS Review Packet:
    `wgcf://artifacts/delivery-art/sha256/4104c1b037870677638e4b7660db14a3e86afa685ce950272e2bcb8547eabc01`
- decision: `approved-with-findings`

The exact reviewed source is acceptable as the inactive repository-provisioning
foundation. It keeps policy authority in Workspace Governance, readiness
evaluation in WGCF, provider mutation and recovery in OOS, provider identity in
GitHub, machine-identity and secret delivery in Platform Engineering, and
operator projection in the Governance Operations Console.

Normal provisioning activation is not approved by this review. ART `#1048`
must commission and prove the dedicated GitHub App installation identity and
its secret, permission, destination, audit, recovery, and revocation controls.
ART `#1049` must then prove the Console composition and positive and negative
end-to-end path without browser or operator credentials.

## Scope Delta

### Design Intent

This change expands the earlier read-only existing-repository custody boundary
to one provider mutation: creating a GitHub repository inside an approved
organization. The action must:

- use a dedicated, revocable GitHub App installation identity;
- bind one exact organization, repository name, visibility, initialization,
  feature set, merge policy, operator approval, and idempotency identity;
- create at most once and recover uncertain outcomes through provider readback;
- prove immutable provider identity and applied settings before reporting
  success;
- retain value-free credential references in durable artifacts; and
- perform no automatic Workspace Intake, active-inventory, Delivery Catalog,
  product-admission, release, transfer, archive, or deletion action.

### Implemented Control

The reviewed source provides:

- a provider-neutral custody contract with a GitHub organization-only first
  provisioning scope and explicit baseline settings;
- a WGCF evaluator that rejects stale authority, missing exact approval,
  personal owner scope, unsupported providers, and secret-looking references;
- content-addressed decisions that bind the exact create target and settings;
- a caller-bound OOS command that persists `applying` before provider mutation;
- request-scoped serialization, deterministic request digest binding, and
  conflict rejection for changed content under the same request identity;
- a GitHub organization create call followed by separate immutable-ID,
  settings, and README readback;
- recovery by acknowledged provider ID or approved organization/name when the
  create outcome is uncertain, without a blind second create;
- bounded provider responses, fail-closed mismatches, durable terminal
  receipts, and audit attribution; and
- no provider delete or compensating-delete capability.

The source and contract keep normal activation disabled. OOS fails closed when
the provider identity is absent, and WGCF refuses runtime construction while
the authority contract remains inactive.

### Operating Evidence

The exact source revisions have passing contract, readiness, provenance,
provider-client, workflow, replay, recovery, HTTP, storage, OpenAPI, full-suite,
container-build, and smoke evidence. The reviewed WGCF source passed 363 tests;
the reviewed OOS source passed 891 tests and GitHub Actions run `33260269818`.

This is source and bounded sandbox evidence. No GitHub organization, GitHub App
installation, Platform secret projection, provider egress policy, revocation
exercise, or composed Console runtime was created or activated for this review.

## Review Areas

### Identity And Authorization

The routine identity must be a GitHub App installation token minted for the
approved organization installation. Personal access tokens, OAuth user tokens,
operator credentials, ambient `gh` authentication, shared automation tokens,
deploy keys, and browser-held credentials are not approved.

GitHub documents `Administration: write` as required for
`POST /orgs/{org}/repos`. The current proof also calls repository metadata and
README endpoints and inspects merge-policy fields. ART `#1048` must prove the
minimum effective GitHub App permission set for those exact calls. The accepted
upper bound is repository `Administration: write` plus only the minimum
`Contents` access demonstrated necessary for initialized-state and merge-policy
readback. No organization-management, issues, pull-request, workflow, webhook,
or unrelated repository permission is justified.

The installation must be bound to the target organization. GitHub grants an
app that creates a repository access to that newly created repository; no
personal-account fallback or operator membership authority may substitute for
the installation identity.

### Secrets

Platform Engineering owns the GitHub App private key, installation identity,
token minting, delivery, rotation, and revocation. OOS may consume only a
short-lived installation token. GitHub installation tokens expire after one
hour and may be further narrowed when minted; the runtime must not assume a
fixed token length or durable token value.

Secret values must remain absent from source, environment templates, browser
responses, requests, decisions, readbacks, receipts, logs, errors, fixtures,
and Review Packets. Durable artifacts carry only the immutable value-free
credential binding reference and digest.

### Delivery And Provider Trust

The provider destination must be server-owned and pinned to
`https://api.github.com`, or to a separately admitted GitHub Enterprise API
host in a future review. Operator and browser input cannot select the API host.
ART `#1048` must prove that redirects or DNS and egress changes cannot forward
the installation credential outside the admitted provider boundary. The
current source's configurable base URL and default fetch redirect behavior are
not operating evidence for that control.

Organization repository-creation policy must explicitly allow the GitHub App
to create only the admitted visibility classes. A successful HTTP create
response is not completion; the immutable numeric REST repository ID and exact
settings readback remain required.

### Runtime, Audit, Recovery, And Revocation

Every attempt must bind caller, operator reference, request ID and digest,
workflow execution, current WGCF decision, target organization and name,
credential-binding reference, provider operation state, immutable provider ID,
readback digest, receipt digest, and outcome. Secret values and raw provider
responses must not appear in that audit chain.

Retry must reuse the original request identity. An uncertain create first
reconciles by acknowledged provider ID or approved coordinates. Name collision,
stale settings, missing README, unavailable provider, invalid response, stale
authority, or lost terminal evidence must not project success. Automatic
repository deletion is prohibited.

Rollback disables new provisioning, revokes or suspends the GitHub App
installation, and removes the runtime secret projection while retaining
requests, decisions, provider operation checkpoints, readbacks, receipts,
denials, failures, and source history. ART `#1048` must prove this behavior
without deleting the created repository as compensation.

### AI And Agentic Influence

No model participates in authorization, provider identity, permission
selection, create execution, readback validation, recovery, or completion.
An advisor may explain state or draft operator input, but deterministic
contracts, exact operator approval, WGCF policy, OOS enforcement, and provider
truth remain authoritative.

## Findings And Activation Gates

1. **The provider identity is not commissioned.** ART `#1048` must create the
   dedicated organization GitHub App installation and prove installation-token
   issuance, value-free binding, Platform-owned secret delivery, rotation,
   revocation, and denial of personal or ambient credentials.
2. **The minimum effective permission set needs operating proof.** ART `#1048`
   must prove the exact create and readback calls against GitHub App
   installation credentials. Any permission beyond `Administration: write`
   and the minimum Contents access required by the reviewed readback is denied.
3. **Provider destination containment is not operating-proven.** ART `#1048`
   must prove API-host pinning, redirect containment, and egress behavior. If
   the current OOS client cannot satisfy the negative case, the owner source
   must be corrected and freshly reviewed before activation.
4. **The composed operator path is absent.** ART `#1049` must prove that the
   Console cannot provide credentials or provider authority and that success,
   denial, recovery, and receipt projections preserve exact OOS and provider
   truth without fixture fallback.
5. **Normal activation remains denied.** No provider mutation may be exposed
   outside the bounded `#1048` and `#1049` evidence work until Security accepts
   the exact operating evidence and source revisions.

These findings are routed to existing accepted ART children. No separate
remediation record is required.

## Decision

`approved-with-findings`

Approved:

- the exact Workspace Governance provisioning contract revision;
- the exact WGCF provisioning-readiness evaluator revision;
- the exact merged OOS idempotent create, recovery, readback, receipt, and
  inactive runtime source;
- the bounded source and sandbox evidence finalized for ART `#1054`, `#1055`,
  and `#1046`; and
- bounded Platform and Console work under ART `#1048` and `#1049` needed to
  satisfy the activation gates.

Not approved:

- normal repository-provisioning runtime activation;
- live repository creation during this review;
- personal, operator, shared, ambient, browser-held, or long-lived provider
  credentials;
- a personal-account repository or an organization not bound to the approved
  installation;
- permissions beyond the proven minimum required by the exact API calls;
- arbitrary provider destinations or credential-forwarding redirects;
- blind create retries, success without separate provider readback, or
  compensating repository deletion;
- automatic downstream admission, inventory, Catalog, product, or release
  mutation; or
- stage, production, external, or multi-user operation.

Security Architecture retains normal-activation judgment. This review permits
the exact source foundation and the bounded work needed to produce operating
evidence; it does not commission the provider identity or activate mutation.

## Related Artifacts

- [GitHub REST create-organization-repository permissions](https://docs.github.com/en/rest/repos/repos#create-an-organization-repository)
- [GitHub App endpoint permission reference](https://docs.github.com/en/rest/authentication/permissions-required-for-github-apps)
- [GitHub REST README permissions](https://docs.github.com/en/rest/repos/contents#get-a-repository-readme)
- [GitHub App permission guidance](https://docs.github.com/en/apps/creating-github-apps/registering-a-github-app/choosing-permissions-for-a-github-app)
- [GitHub App installation-token scoping](https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/generating-an-installation-access-token-for-a-github-app)
- [GitHub organization repository-creation policy](https://docs.github.com/en/organizations/managing-organization-settings/restricting-repository-creation-in-your-organization)
- [Existing-repository custody security review](2026-08-29-repository-custody-provider-identity-boundary.md)
- [Security delta review process](../security-delta-review-process.md)
- [Workspace Governance pull request #170](https://github.com/mfshaf7/workspace-governance/pull/170)
- [WGCF pull request #58](https://github.com/mfshaf7/workspace-governance-control-fabric/pull/58)
- [OOS pull request #182](https://github.com/mfshaf7/operator-orchestration-service/pull/182)
