# Agent Gary Source Identity Boundary Review

## Summary

- date: 2026-09-11
- owner repo: `security-architecture`
- delivery ref: `openproject://work_packages/1135`
- parent feature: `openproject://work_packages/920`
- parent initiative: `openproject://work_packages/892`
- governing architecture:
  `wgcf://artifacts/delivery-art/sha256/71411b67037b7c64a05f6bd93d1a5a882169a724e2c3a4dd66bc7fd78708c934`
- reviewed source:
  - Workspace Governance pull-request head:
    `workspace-governance@3b2c7502f01f5bc5262fe8269dc677dd7d688ae7`
  - Workspace Governance merge:
    `workspace-governance@8c5c0889708d67d57602a13b80395d7ca510cd67`
- source evidence:
  - Workspace Governance Review Packet:
    `wgcf://artifacts/delivery-art/sha256/d9b21cd097c012fd5e2d7c7455b38f582c137b760727058d8a42f11ecc4247b9`
  - Workspace Governance pull request:
    `https://github.com/mfshaf7/workspace-governance/pull/185`
- decision: `approved-with-findings`

The Agent Gary source-implementation contract is acceptable as an inactive
identity and authorization foundation. It separates logical agent attribution,
provider transport, workflow coordination, credential custody, and accountable
human review instead of collapsing them into one identity.

This decision permits the bounded Platform and OOS implementation work in ART
`#1136` and `#1137`. It does not approve normal Agent Gary availability, the
current bootstrap credential as durable custody, broad installation-token use,
default-branch mutation, self-review, automatic approval, or automatic merge.

## Scope Delta

### Design Intent

Agent Gary is the first named AI source implementor. The role may author and
push one exact non-default branch and open or update its pull request for an
admitted Landing Unit. It does not inherit the accountable operator's identity
or authority.

The authority split is:

| Principal | Security responsibility |
| --- | --- |
| `agent-gary` | Logical attribution for the source implementation session |
| `mfshaf7-agent-gary[bot]` | GitHub App transport for bounded branch and pull-request operations |
| OOS | Admitted workflow coordination, exact session binding, and receipts |
| Platform Engineering | Private-key custody and short-lived token issuance |
| `mfshaf7` | Accountable human review, approval, and merge |

Possession of an installation token does not confer approval or merge
authority. Agent authorship does not satisfy human review. Human review does
not permit source activity to be attributed to the human when Agent Gary
performed it.

### Implemented Control

The merged Workspace Governance contract provides:

- product-neutral `Agent <Name>` and `agent-<name>` identity grammar;
- exact Agent Gary provider principal and Git author attribution;
- selected-repository GitHub App transport with Metadata read, Contents write,
  Pull requests write, and Checks read;
- exact Landing Unit, repository, repository id, non-default branch, fetched
  base, provider installation, token expiry, pusher, reviewed head, reviewer,
  and merged-head bindings;
- explicit denial of approval, merge, default-branch push, repository
  administration, ruleset changes, deletion, installation-scope broadening,
  and human-credential fallback;
- secret-value exclusion from durable evidence; and
- a bounded bootstrap limited to ART `#1134` through `#1137`, with normal
  activation disabled.

The contract is authority definition only. Platform credential custody and OOS
runtime consumption are not implemented by the reviewed source.

### Operating Evidence

The bootstrap provider evidence establishes:

- GitHub App id `4907049`, installation id `160815600`, and provider principal
  `mfshaf7-agent-gary[bot]`;
- `selected` installation scope over exactly the five repositories required by
  the approved bootstrap and immediate dependent correction:
  `platform-engineering`, `security-architecture`, `workspace-governance`,
  `operator-orchestration-service`, and `workspace-prototype-studio`;
- the exact reviewed permission set: Metadata read, Contents write, Pull
  requests write, and Checks read;
- successful minting of a short-lived token restricted to only repository id
  `1212447211`, `mfshaf7/workspace-governance`;
- App-authored PR `#185` at exact head
  `3b2c7502f01f5bc5262fe8269dc677dd7d688ae7`;
- required `validate` success and exact-head human approval by `mfshaf7`; and
- merge by `mfshaf7` to merged commit
  `8c5c0889708d67d57602a13b80395d7ca510cd67`.

The repository ruleset denies direct updates to `main`, deletion, and
non-fast-forward mutation; requires the trusted `validate` check, one current
approval, stale-review dismissal, latest-push approval separation, and review
conversation resolution; and grants no Agent Gary bypass.

This is bounded bootstrap and provider evidence. The local bootstrap key is
not accepted as normal Platform custody, no shared OOS credential-consumption
path is active, and no stage or production operating claim is made.

## Review Areas

### Identity And Authorization

The five identities and roles are correctly separated. `agent-gary` is an
attribution identity, not an authorization grant. The GitHub App installation
authenticates source transport but cannot supply operator approval. OOS may
coordinate only an admitted Landing Unit and cannot review or merge its own
source output. The human operator remains accountable for exact-head review and
merge.

The App installation may select the finite repository set needed by the
approved bootstrap, but every issued token and work session must narrow that
set to one exact owner repository and repository id. A token exposing all
selected repositories to one Landing Unit is not approved. Repository scope
cannot be inferred from branch name, remote URL, current directory, or ambient
Git configuration.

Human credentials, ambient `gh` authentication, OAuth user tokens, personal
access tokens, deploy keys, and another workflow's GitHub App are prohibited
fallbacks for Agent Gary source authorship. The accountable human may use the
provider's human-only merge path after exact-head approval; that action must
remain attributed to the human, not Agent Gary.

### Secrets And Credential Delivery

Platform Engineering must own the App private key, token minting, projection,
rotation, suspension, revocation, and recovery. OOS may receive only a
short-lived installation token scoped to one exact repository. The private
key, client secret, webhook secret, and token value must remain outside source,
requests, workflow state, pull-request text, logs, browser responses, receipts,
Review Packets, and model context.

The current bootstrap material is temporary operator-local custody. File-mode
restriction is useful containment but is not the approved normal custody
model. ART `#1136` must create or rotate the operational private key into the
Platform-owned boundary, prove the selected App and installation ids, and
retire bootstrap material that is not needed after commissioning. Unused
client or webhook secrets must not be projected into OOS.

Tokens must be minted just in time, expire without renewal by possession, and
be re-read after restart or rotation. OOS must not persist an installation
token in durable work-session or evidence state. A missing, expired, revoked,
wrong-repository, or over-scoped token fails closed.

### Source, Review, And Provider Trust

Source work must descend from the recorded fetched base and remain on the
recorded non-default branch. OOS and provider evidence must agree on logical
agent id, App installation, provider principal, Git author, repository id,
branch, pushed head, human reviewer, reviewed head, and merged head.

The reviewed head must equal the final pushed head. A later push invalidates
the earlier approval. Success requires provider-confirmed merge, ancestry from
the recorded base, and merged-head readback from authoritative `main`. A pull
request, successful CI check, approval, local commit, or branch push alone is
not completion.

The App's Contents and Pull requests permissions are necessary for branch and
PR operation but are broader than the intended business action. Provider
rules, exact-repository token scoping, OOS path and branch checks, human review,
and merged readback must operate together. No application check is accepted as
a substitute for provider-enforced default-branch and merge denial.

### Audit, Restart, Revocation, And Rollback

Every source session must retain value-safe evidence for the logical agent,
provider installation and principal, repository and repository id, Landing
Unit, branch, fetched base, token expiry, pushed head, human reviewer, reviewed
head, merged head, workflow correlation, and terminal outcome. Secret values
must never appear in that evidence.

Restart must recover the durable session without recovering a stored provider
token. The resumed worker must obtain a fresh exact-repository token and
reconcile current branch, PR, review, merge, and source state before any write.
Replay against changed repository, base, head, reviewer, or Landing Unit must
fail closed.

Suspension or revocation must stop new token issuance and new source writes,
invalidate or allow expiry of outstanding short-lived tokens, and leave
provider and OOS evidence available for review. Rollback disables activation,
revokes credential delivery, removes runtime projection, and preserves merged
contracts, provider history, work-session receipts, and human decisions.

### AI And Agentic Influence

Agent Gary may use AI reasoning to create source, but neither model output nor
the logical agent identity supplies authority. Deterministic contract,
readiness, source, provider, review, and readback checks remain outside the
model. Untrusted repository content, ART text, review comments, and tool output
must not broaden repository scope, credential access, write paths, or merge
authority.

The model must never receive private-key or token values. Context admission may
carry bounded, redacted metadata needed for implementation, but context packets
remain evidence inputs rather than authorization.

## Findings And Activation Gates

1. **Normal Platform custody is absent.** ART `#1136` must commission the exact
   App and installation, replace or rotate temporary bootstrap key material
   into Platform-owned custody, issue only short-lived exact-repository tokens,
   exclude unused secrets, and prove rotation, suspension, revocation, restart,
   and rollback without exposing secret values.
2. **Normal OOS credential consumption is absent.** ART `#1137` must bind the
   exact Agent Gary identity and token metadata to the admitted Landing Unit,
   re-read credentials after restart or rotation, enforce branch and repository
   scope, preserve human review separation, and emit secret-safe terminal
   receipts.
3. **Composed denial evidence remains required.** The dependent work must prove
   wrong repository, broad token, wrong principal, human fallback, default
   branch, stale base, changed pushed head, self-review, merge denial, expired
   token, restart, revocation, and rollback paths. Failure blocks activation;
   it does not permit credential or provider-policy weakening.
4. **Bootstrap must end.** The bounded bootstrap may support only ART `#1134`
   through `#1137`. It must not become an undocumented permanent operator path
   or authorize later Agent Gary work without the normal activated OOS and
   Platform boundaries.

These findings are routed to existing ART `#1136` and `#1137`. They are
activation conditions, not accepted risk, and no additional remediation item
is required.

## Decision

`approved-with-findings`

Approved:

- the exact merged Agent Gary source-implementation identity contract;
- distinct logical-agent, provider, orchestrator, platform-custodian, and human
  identities;
- the exact five-repository selected installation for the bounded bootstrap;
- one-repository-per-token and one-repository-per-session enforcement;
- attributed non-default branch authorship and pull-request creation;
- exact-head CI, human review, human merge, and merged-source readback;
- bounded source implementation for ART `#1136` and `#1137`; and
- retained, secret-safe audit and rollback evidence.

Not approved:

- normal Agent Gary availability before `#1136` and `#1137` are merged and
  their exact operating evidence is accepted;
- the current bootstrap key as normal or durable Platform custody;
- one session receiving access to every repository selected on the App;
- personal, ambient, shared, browser-held, long-lived, or human-fallback
  credentials;
- private keys, client secrets, webhook secrets, or installation-token values
  entering OOS state, source, logs, evidence, Review Packets, or model context;
- direct default-branch writes, force push, ref deletion, repository
  administration, ruleset changes, automatic approval, automatic merge,
  self-review, or App bypass;
- success without exact provider, human-review, merge, and canonical-readback
  agreement; or
- stage, production, product-runtime, release, or broader agent authority.

Security Architecture retains normal-activation judgment. Any implementation
that cannot preserve these boundaries must stop and return for a fresh delta
review rather than widening identity, token, repository, or human-review scope.

## Related Artifacts

- [Security delta review process](../security-delta-review-process.md)
- [AI security and governance standard](../../standards/ai-security-and-governance.md)
- [Identity and access standard](../../standards/identity-and-access.md)
- [Secrets and recovery standard](../../standards/secrets-and-recovery.md)
- [Governed agent action boundary](2026-08-24-governed-agent-action-boundary.md)
- [Repository custody provider identity boundary](2026-08-29-repository-custody-provider-identity-boundary.md)
- [Workspace Governance Agent Gary contract](https://github.com/mfshaf7/workspace-governance/blob/8c5c0889708d67d57602a13b80395d7ca510cd67/contracts/agent-source-implementation.yaml)
- [Workspace Governance pull request #185](https://github.com/mfshaf7/workspace-governance/pull/185)
- [GitHub App permission guidance](https://docs.github.com/en/apps/creating-github-apps/registering-a-github-app/choosing-permissions-for-a-github-app)
- [GitHub App installation token scoping](https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/generating-an-installation-access-token-for-a-github-app)
