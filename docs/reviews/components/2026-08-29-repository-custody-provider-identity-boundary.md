# Repository Custody Provider Identity Boundary Review

## Summary

- date: 2026-08-29
- owner repo: `security-architecture`
- delivery ref: `openproject://work_packages/1043`
- parent initiative: `openproject://work_packages/888`
- governing architecture:
  `wgcf://artifacts/delivery-art/sha256/7cf6776956727ed04aa2a6fd10086d614cb635d7acae163d2a473b080c8e0cb2`
- reviewed source:
  - Workspace Governance:
    `workspace-governance@eb59c5141ec00d460c929888b93b46ac88bd7e42`
  - Workspace Governance Control Fabric:
    `workspace-governance-control-fabric@5cd7efb6c793358ba6d1f2e9dd25ef40acd65f17`
  - Operator Orchestration Service pull request:
    `operator-orchestration-service@860257facfb015d44d8355a873ab3f7b5363fc6d`
- decision: `approved-with-findings`

The existing-repository custody source is acceptable to merge at the exact OOS
revision above. The workflow keeps policy evaluation in WGCF, provider
readback and terminal workflow evidence in OOS, and repository ownership or
downstream admission outside this action.

Normal runtime activation is not approved by this review. It remains blocked
until Platform Engineering provisions and proves a dedicated GitHub App
installation identity under ART `#1044`, and the Console composition and
positive and negative end-to-end evidence land under ART `#1045`.

## Scope Delta

### Design Intent

- establish immutable repository identity before workspace custody is linked;
- use one dedicated machine identity instead of an operator credential or
  personal access token;
- permit only the provider metadata read needed to prove repository identity;
- preserve exact request, decision, readback, correlation, idempotency, and
  terminal receipt evidence; and
- perform no repository creation, transfer, archive, deletion, workspace
  admission, active-inventory mutation, Delivery catalog mutation, or product
  admission through the existing-link action.

### Implemented Control

The reviewed contract and source provide:

- an authority bundle pinned by digest and exact Workspace Governance commit;
- WGCF evaluation and reread of one content-addressed custody decision;
- a caller-bound OOS API with deterministic request and idempotency identity;
- bounded GitHub REST readback through `GET /repositories/{repository_id}`;
- positive decimal GitHub REST repository `id` validation across request,
  decision, readback, receipt, examples, and tests;
- rejection of GraphQL `node_id` substitution, unsupported providers,
  mismatched immutable identity, oversized responses, stale or tampered
  artifacts, and absent provider credentials;
- durable terminal readback and receipt evidence with retry-safe replay; and
- default runtime denial while activation evidence is absent.

The initial fixture used a GitHub GraphQL `node_id` where the REST endpoint
requires the numeric repository `id`. Workspace Governance, WGCF, and OOS were
corrected before this approval. The OOS OpenAPI examples are now validated
against the canonical custody contract so the contradiction cannot silently
return through generated operator documentation.

### Operating Evidence

The reviewed source has passing contract, API, provider-client, workflow,
replay, failure, authorization, provenance, and container-sandbox evidence.
The OOS full suite passed 879 tests at the exact reviewed revision.

This is source and bounded sandbox evidence. No admitted GitHub App
installation identity, Platform-owned secret projection, or composed Console
runtime evidence exists yet, so normal mutable operation remains unavailable.

## Review Areas

### Identity And Authorization

The routine provider identity must be a dedicated GitHub App installation
identity. A personal access token, operator token, shared automation token,
OAuth user token, deploy key, or ambient Git credential is not approved.

The app installation and each issued installation token must be scoped to the
exact repository or explicitly approved bounded repository set. The provider
action requires only `Metadata` repository permission at read level. GitHub's
`Get a repository` endpoint documents that permission as sufficient, and the
workflow does not justify `Contents`, administration, organization, issue,
pull-request, webhook, or write permission.

The Console supplies accountable operator intent but never receives or selects
the provider credential. OOS authenticates its caller and binds the accepted
request, while WGCF remains policy authority. Platform owns machine-identity
commissioning and credential delivery.

### Secrets

The GitHub App private key and installation-token minting material must remain
under the approved Platform secret authority and projection path. Runtime
consumes a short-lived installation token; it does not become secret authority.

Secret values must remain absent from source, browser responses, request and
decision artifacts, readback, receipts, logs, errors, test fixtures, and Review
Packets. The credential binding is represented only by a non-secret immutable
reference and digest. Rotation, revocation, installation suspension, repository
removal, and expiry must fail closed and remain observable without exposing
secret material.

### Delivery And Provider Trust

The trusted provider API base is server-owned configuration. Platform must pin
`https://api.github.com` or an explicitly admitted GitHub Enterprise API host;
operator or browser input must not choose an arbitrary destination. Redirects
must not widen the destination or forward credentials to another host.

Provider coordinates such as owner, name, URL, default branch, visibility, and
lifecycle state are mutable readback facts. Only the positive decimal REST
repository `id` is the immutable provider identity for this contract. Source
contracts, generated API examples, and runtime comparisons must stay aligned on
that meaning.

### Runtime, Audit, And Recovery

Provider responses remain size-bounded and schema-validated before custody is
recorded. A mismatch, denial, timeout, invalid response, expired token, missing
terminal receipt, or receipt-write failure must never project success.

Retry must reuse the original request and idempotency identity. A terminal
success must be replayed without another provider side effect; a retryable
failure may reread under the same immutable request. Audit evidence must bind
caller, operator reference, workflow execution, request digest, policy
decision, provider identity, readback digest, receipt digest, and outcome.

Rollback disables new custody requests and revokes the installation identity
while retaining governance artifacts, denial evidence, readbacks, receipts,
and source history.

### AI And Agentic Influence

No model is part of the authorization, identity resolution, provider readback,
or custody decision path. An advisor may explain state or draft operator input,
but deterministic contracts, caller authentication, WGCF policy, provider
identity comparison, and receipt validation remain outside the model.

## Findings And Activation Gates

1. **The provider identity is not commissioned.** ART `#1044` must provision a
   repository-scoped GitHub App installation identity with read-only Metadata
   permission, approved secret custody, short-lived token issuance, revocation,
   destination pinning, and positive and negative operating evidence.
2. **The Console composition is not proven.** ART `#1045` must prove that the
   browser cannot supply provider credentials or provider authority, and that
   the Console-to-OOS path preserves operator, request, revision, correlation,
   result, and receipt truth without fixture fallback.
3. **Normal activation remains denied.** The OOS source may merge, but its
   repository-custody runtime gate must remain false until the exact `#1044`
   and `#1045` evidence is accepted. Any broader provider action, permission,
   destination, secret path, or identity model requires fresh review.

These findings are already routed to the accepted ART children that exist to
close them. No separate remediation record is required.

## Decision

`approved-with-findings`

Approved:

- the exact Workspace Governance repository-custody authority contract;
- the exact WGCF readiness projection and terminal-receipt contract;
- merge of the exact OOS existing-repository custody source revision reviewed
  here;
- the bounded source, real-Git provenance, and sandbox evidence already
  produced for ART `#1042`; and
- Platform and Console work under ART `#1044` and `#1045` needed to satisfy the
  remaining activation gates.

Not approved:

- normal repository-custody runtime activation before `#1044` and `#1045`;
- personal, operator, shared, ambient, or browser-held provider credentials;
- permissions beyond read-only repository Metadata for this action;
- arbitrary provider destinations or credential-forwarding redirects;
- GraphQL node IDs, owner/name pairs, or URLs as immutable repository identity;
- fallback to fixtures or unauthenticated public reads in configured live mode;
- repository mutation or downstream admission through the existing-link
  workflow; or
- stage, production, external, or multi-user operation.

Security Architecture retains final judgment on normal activation. This review
permits source landing and the bounded follow-on commissioning work only.

## Related Artifacts

- [GitHub REST `Get a repository` permissions](https://docs.github.com/en/rest/repos/repos#get-a-repository)
- [GitHub App permission guidance](https://docs.github.com/en/apps/creating-github-apps/registering-a-github-app/choosing-permissions-for-a-github-app)
- [GitHub App installation token scoping](https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/generating-an-installation-access-token-for-a-github-app)
- [Security delta review process](../security-delta-review-process.md)
- [OOS pull request #181](https://github.com/mfshaf7/operator-orchestration-service/pull/181)
- [Workspace Governance repository-custody contract](https://github.com/mfshaf7/workspace-governance/blob/eb59c5141ec00d460c929888b93b46ac88bd7e42/contracts/repository-custody.yaml)
- [WGCF repository-custody manifest](https://github.com/mfshaf7/workspace-governance-control-fabric/blob/5cd7efb6c793358ba6d1f2e9dd25ef40acd65f17/contracts/repository-custody/manifest.json)
