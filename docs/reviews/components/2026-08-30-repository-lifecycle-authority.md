# Repository Lifecycle Authority Review

## Summary

- date: 2026-08-30
- owner repo: `security-architecture`
- delivery ref: `openproject://work_packages/1052`
- parent feature: `openproject://work_packages/915`
- parent initiative: `openproject://work_packages/888`
- governing architecture:
  `wgcf://artifacts/delivery-art/sha256/d80a56d1c364c4b9c8d1cdd84934bb8f2419133a29dc3592e95b210a9f0c789a`
- reviewed source:
  - Workspace Governance merge:
    `workspace-governance@965b41961bb1d12e1380af57b1ac303a72e9ef67`
  - Platform Engineering merge:
    `platform-engineering@d03ac437af6902e6d10983d39ce81248d6a1d824`
- source evidence:
  - Workspace Governance Review Packet:
    `wgcf://artifacts/delivery-art/sha256/b36558b493af8b75395e9c75eb0dc7ef7c6a8023942b3d39b078f69b2abec3c2`
  - Platform Engineering Review Packet:
    `wgcf://artifacts/delivery-art/sha256/eefb028e74cfe42e23a8d911bbd8538534f15763a10491835761eec381bac073`
- decision: `approved-with-findings`

The reviewed revisions are acceptable as the inactive repository-lifecycle
policy and provider-identity foundation. Workspace Governance keeps provider
archive state, workspace-record retirement, and workspace custody as separate
axes. Platform supplies a third machine identity dedicated to provider archive
and unarchive, with one-repository token scope and independent revocation.

Normal repository-lifecycle activation is not approved by this review. ART
`#1059`, `#1051`, and `#1053` must implement and prove deterministic readiness,
workflow, recovery, receipt, and Console boundaries before the Feature can be
considered operating-ready.

## Scope Delta

### Design Intent

The change adds reversible repository lifecycle control after custody exists:

- transfer accountable workspace custody without physical provider transfer;
- archive or unarchive one provider repository;
- retire or restore one workspace record without changing provider state;
- assess downstream impact without rewriting consumers;
- preserve immutable action and reversal history; and
- expose a read-only audit projection that cannot repair or complete mutation.

Hard provider deletion, physical ownership transfer, personal credentials, and
automatic downstream mutation remain prohibited.

### Implemented Control

The reviewed source provides:

- independent custody, provider, and workspace-record state axes;
- typed request, decision, readback, receipt, and audit schemas;
- action-specific allowed states, confirmation requirements, impact
  dispositions, reversal references, and terminal outcomes;
- rejection of ambiguous transfer, hard deletion, provider ownership transfer,
  personal credentials, and downstream auto-mutation;
- a dedicated organization-owned GitHub App identity with exactly repository
  `Administration: write` and implicit `Metadata: read`;
- one requested repository per token, immutable numeric repository-id readback,
  one-hour maximum token lifetime, pinned provider destination, redirect denial,
  separate Vault custody, separate Kubernetes projection, and value-free
  receipts; and
- explicit normal-runtime denial and rollback that revokes permission without
  changing repository state.

### Operating Evidence

Workspace Governance passed its complete contract suite at the reviewed
revision. Platform passed its complete CI-equivalent suite and bounded sandbox
tests for identity commissioning, exact repository scope, immutable identity,
secret projection, revocation, redirect denial, and fail-closed mismatches.

This is source and sandbox evidence. No real lifecycle GitHub App installation,
provider mutation, WGCF decision, OOS workflow, Console composition, or
end-to-end archive/unarchive evidence exists yet.

## Review Areas

### Identity And Authorization

The provider identity must remain the dedicated organization-owned GitHub App.
Personal access tokens, OAuth user tokens, operator credentials, ambient `gh`
authentication, browser-held credentials, shared automation tokens, and the
custody or provisioning identities are not approved substitutes.

GitHub documents repository `Administration: write` as the required permission
for `PATCH /repos/{owner}/{repo}`, including the `archived` setting. No Contents,
issues, pull-request, workflow, package, organization-management, webhook, or
unrelated permission is justified.

Every runtime token must be narrowed to the exact repository and permission set
and must be checked against the positive decimal REST repository id. The real
installation should grant selected-repository access. An all-repositories
installation requires a fresh blast-radius decision even though runtime tokens
remain one-repository scoped.

### Secrets

Platform owns the App private key, installation identity, token minting,
projection, rotation, and revocation. OOS may consume only the short-lived
installation token. GitHub installation tokens expire after one hour; no code
may assume a fixed token length or durable token value.

Secret values must remain absent from source, requests, decisions, readbacks,
receipts, audit, logs, errors, fixtures, browser responses, and Review Packets.
Rollback removes the projection and revokes the token while preserving
value-free governance evidence.

### Delivery And Provider Trust

The provider API host remains server-owned and pinned to
`https://api.github.com`. Redirects must not forward credentials. A future
GitHub Enterprise host requires separate admission and review.

Archive or unarchive must apply only the approved `archived` value to the exact
repository. `Administration: write` must not become a generic repository
settings surface. A successful PATCH response is not completion; a fresh,
bounded provider readback must prove immutable identity, archive state, and
current provider version.

### Runtime, Impact, Audit, And Recovery

Every attempt must bind caller, operator, request and idempotency identities,
immutable repository identity, expected lifecycle axes and versions, requested
target, impact decision, confirmations, current WGCF decision, credential
binding, provider mutation readback when applicable, reversal reference, and
terminal receipt.

`defer` never permits mutation. `accept-risk` requires accountable authority,
justification, and evidence. No disposition may mutate downstream records.

Stale provider version, changed repository identity, denied policy, unavailable
provider, timeout, invalid readback, lost receipt, or conflicting replay must
not project success. An indeterminate provider mutation is reconciled through
fresh readback under the original request identity; it is never followed by a
blind second mutation or compensating deletion.

Historical receipts are append-only. Archive reverses through unarchive,
retirement through restore, and custody transfer through a new accepted
transfer. Audit remains read-only.

### AI And Agentic Influence

No model may authorize lifecycle work, select credentials, choose impact
disposition, perform provider mutation, validate readback, or project success.
An advisor may explain state or draft input, but deterministic contracts, human
confirmation, WGCF policy, OOS enforcement, provider truth, and receipt
validation remain authoritative.

## Findings And Activation Gates

1. **Readiness evaluation is not implemented.** ART `#1059` must bind the exact
   contract and this review, enforce state/version/impact/confirmation rules,
   and keep every prohibited or stale case fail-closed.
2. **Lifecycle orchestration is not implemented.** ART `#1051` must implement
   caller-bound APIs, idempotency, exact provider PATCH behavior, workspace-only
   transitions, readback, recovery, immutable receipts, and audit without hard
   deletion or downstream auto-mutation.
3. **The operator composition is absent.** ART `#1053` must prove that the
   Console cannot supply credentials or provider authority, cannot fabricate
   success, and preserves exact OOS decisions, recovery cues, receipts, and
   history without fixture fallback in configured live mode.
4. **Real provider authority is not commissioned or operating-proven.** Before
   activation, bounded evidence must prove the organization-owned App,
   selected-repository installation posture, exact token permissions and
   repository scope, destination containment, immutable-id readback, expiry,
   revocation, and removal of runtime projection.
5. **Normal activation remains denied.** Source work may proceed through the
   accepted ART sequence, but no provider mutation may be exposed until the
   exact remaining source and composed positive and negative evidence is
   accepted.

These findings are routed to existing Feature `#915` children and terminal
evidence requirements. No separate remediation record is required.

## Decision

`approved-with-findings`

Approved:

- the exact Workspace Governance lifecycle contract revision;
- the exact merged Platform lifecycle identity and inactive projection source;
- the bounded source and sandbox evidence finalized for ART `#1050` and
  `#1058`;
- the separation of custody transfer, provider archive state, workspace-record
  retirement, impact disposition, reversal, and audit; and
- bounded follow-on implementation under ART `#1059`, `#1051`, and `#1053`.

Not approved:

- normal repository-lifecycle runtime activation;
- live archive or unarchive during this review;
- hard deletion or physical provider ownership transfer;
- personal, operator, shared, ambient, browser-held, or long-lived provider
  credentials;
- permissions beyond repository `Administration: write` and implicit
  `Metadata: read`;
- arbitrary provider destinations or credential-forwarding redirects;
- mutation without current provider version, exact human gates, impact
  disposition, and fresh readback;
- blind retries, history rewrite, downstream auto-mutation, or fixture success
  in configured live mode; or
- stage, production, external, or multi-user operation.

Security Architecture retains final judgment on normal activation. This review
permits the exact follow-on source and bounded evidence work only.

## Related Artifacts

- [GitHub REST update-repository permissions](https://docs.github.com/en/rest/repos/repos#update-a-repository)
- [GitHub App installation-token scoping](https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/generating-an-installation-access-token-for-a-github-app)
- [GitHub App permission guidance](https://docs.github.com/en/apps/creating-github-apps/registering-a-github-app/choosing-permissions-for-a-github-app)
- [Repository custody provider identity review](2026-08-29-repository-custody-provider-identity-boundary.md)
- [Repository provisioning authority review](2026-08-29-repository-provisioning-authority.md)
- [Security delta review process](../security-delta-review-process.md)
- [Workspace Governance pull request #171](https://github.com/mfshaf7/workspace-governance/pull/171)
- [Platform Engineering pull request #228](https://github.com/mfshaf7/platform-engineering/pull/228)
