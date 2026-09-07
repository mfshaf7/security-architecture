# Prototype Landing Normal-Availability Review

## Summary

- date: 2026-09-08
- owner repo: `security-architecture`
- delivery ref: `openproject://work_packages/1111`
- parent feature: `openproject://work_packages/1110`
- parent initiative: `openproject://work_packages/892`
- governing architecture:
  `wgcf://artifacts/delivery-art/sha256/4138e5dd1390a0c053d6d21c32177dbace85d85fdd57d79e9894ebff6a04f2b0`
- reviewed source:
  - Workspace Governance: `eb7fb3c182073d050e2cb95c4f3256be3c535eaa`
  - Workspace Prototype Studio: `2d18349ffab42bff052061e5adbc1d2c76d6210c`
  - Workspace Governance Control Fabric: `e19a18240a0ac1a5bbea8cceeaccbba4d544cd7b`
  - Operator Orchestration Service: `9735ec13b4d17be5199597df8c402b161bea50a8`
  - Platform Engineering: `c0cf02eec6eb61f4db31933862a70614717f643b`
  - Governance Operations Console: `213408df96714455f6bb46cd1b00f1e746bf5da4`
- prior review:
  `docs/reviews/components/2026-09-07-prototype-landing-trust-boundary.md`
- decision: `approved-with-findings`

Prototype Landing may become normally available in the local
`dev-integration` lane after the four findings in this review are satisfied in
order. The reviewed source already implements the required authority,
readiness, workflow, source-review, readback, receipt, identity, and Console
boundaries. This decision does not itself activate any runtime.

Stage or production availability, automatic merge, external exposure,
unadmitted import staging, and any Prototype maturity transition remain outside
this approval.

## Scope Delta

### Design Intent

The prior review approved an inactive implementation foundation. The current
delta is limited to making that same workflow available to operators in
`dev-integration` without changing its owner boundaries:

- Workspace Prototype Studio remains the Prototype registry and incubation
  source authority.
- WGCF remains readiness authority and cannot apply source changes.
- OOS remains durable coordination and receipt authority and cannot merge.
- Platform remains machine-identity, secret-delivery, runtime, suspension, and
  revocation authority.
- Security Architecture remains normal-availability decision authority.
- The Console remains a server-mediated operator client and cannot become a
  parallel workflow or source authority.

### Implemented Control

The reviewed source provides:

- immutable Entry Packet and stable Prototype identity binding;
- explicit source-custody postures and a bounded Prototype Studio changed-file
  set;
- content-addressed WGCF readiness with expiry, replay, and current-authority
  checks;
- durable OOS acknowledgement, idempotency, interruption reconciliation, and
  terminal receipts;
- non-default source branches, exact-head checks, human review and merge, and
  byte-identical canonical readback before success;
- a dedicated GitHub App installation restricted to
  `mfshaf7/workspace-prototype-studio`, with no bypass or merge authority;
- short-lived token delivery from Platform custody into a read-only runtime
  mount, plus persistent coordination state and explicit revocation; and
- same-origin Console routes that keep caller credentials server-side and
  refuse synthetic success when live mode is configured.

The WGCF and OOS manifests, Platform identity selection, and composed runtime
configuration remain explicitly inactive. Activation therefore remains
fail-closed until the downstream findings are completed.

### Operating Evidence

Owner-repo tests and the isolated composed conformance path cover direct,
proposal-routed, existing-source, and imported request shapes; readiness
denial; stale authority; replay conflict; interruption; changed review head;
merge denial; merged-source mismatch; terminal replay; and unchanged canonical
source during isolated proof.

The Platform identity proof validates the exact App, installation, account,
repository, permissions, provider rules, credential projection, rotation,
restart binding, suspension, revocation, and secret-free receipts. The Console
adapter tests validate server-side command construction and fail-closed live
mode. These are sufficient to authorize bounded activation work, but operating
availability is not established until `#1115` proves the composed operator
path against the activated `dev-integration` services.

## Review Areas

### Identity And Authorization

The dedicated installation identity is appropriate because it is selected for
one immutable repository and has only Metadata read, Contents write, Pull
requests write, and Checks read. Provider rules must continue to deny App
bypass, default-branch writes, force push, branch deletion, and machine merge.
OOS must reread the short-lived token and must bind the exact repository and
owner ids on every request.

The accountable operator approves the Landing command and later reviews the
exact source head. Neither the Console browser, WGCF, OOS, a support profile,
upstream proposal text, nor an AI advisor can authorize merge or completion.

### Secrets And Data

The GitHub App private key remains in Platform Vault. OOS receives only a
short-lived installation token and its dedicated WGCF caller credential.
Secrets must remain absent from source, browser responses, Entry Packets,
plans, readiness artifacts, logs, errors, receipts, and ART evidence.

External and imported content remains untrusted. Reference-only source is not
mutated. Import execution remains denied unless Platform separately admits an
exact staging root and the existing path, digest, traversal, size, unsafe-link,
and secret-finding controls all pass.

### Delivery And Runtime

Normal availability is limited to the accepted `dev-integration` OOS profile.
Activation requires the new Security review reference in WGCF and OOS, current
source identities, current implementation digests, and one Platform-owned
runtime configuration that enables both source-owned gates together. A partial
activation must remain unavailable.

Success still requires a human-reviewed provider merge and canonical Studio
readback. Landing cannot activate a Prototype preview runtime, promote maturity,
create Delivery work, create or transfer repository custody, publish Portfolio
visibility, or claim stage or production readiness.

### Visibility, Audit, And Recovery

Operator projection must distinguish durable acknowledgement, blocked
readiness, source review required, merged readback, cancellation, failure, and
terminal success. It must expose the exact next action and value-safe evidence
without returning source bytes or credentials.

Suspension disables new requests. Rollback disables the OOS and WGCF gates,
revokes and removes runtime credential projection, and retains coordination,
review, source, denial, and receipt history. An interrupted workflow is
reconciled from current readiness, provider, and canonical source truth rather
than inferred from process state.

### AI And Agentic Influence

An advisor may explain choices or draft operator input. It is not identity,
readiness, security, merge, source, custody, or completion authority. Untrusted
source content must not reach a model outside an admitted context-governance
path, and model output must pass the same deterministic request validation as
human-authored input.

## Findings And Activation Gates

1. **WGCF activation is pending.** ART `#1112` must pin this merged review,
   enable only the existing Prototype Landing readiness capability, preserve
   caller authentication and content-addressed current-authority checks, and
   prove stale, unauthorized, expired, and replay-conflict denial.
2. **OOS activation is pending.** ART `#1113` must pin this merged review and
   current WGCF implementation, enable only the existing Prototype Landing
   workflow, preserve dedicated caller and source identities, and prove
   durable restart, cancellation, idempotency, exact-head review, merged
   readback, and value-safe receipts.
3. **Platform commissioning is pending.** ART `#1114` must run only after
   `#1112` and `#1113`, activate the exact selected App installation and both
   source-owned gates in one bounded runtime composition, and record restart,
   rotation, suspension, revocation, and rollback evidence without secret
   values.
4. **Normal operator proof is pending.** ART `#1115` must complete one
   authorized Landing through the Console and prove blocked, stale,
   unauthorized, replayed, interrupted, review-denied, readback-mismatched,
   suspended, and revoked paths remain visibly non-successful. No fixture or
   disconnected local receipt may satisfy this gate.

These findings are already routed to Feature `#1110`. They are activation
conditions, not accepted risk. Feature `#920` remains blocked until all four
are complete and `#1110` closes.

## Decision

`approved-with-findings`

Approved:

- the reviewed Prototype Landing authority and trust-boundary model;
- bounded normal operator availability in local `dev-integration` after ART
  `#1112`, `#1113`, `#1114`, and `#1115` complete in order;
- the dedicated one-repository GitHub App identity and short-lived credential
  projection;
- human-review-only merge with exact-head checks and canonical readback;
- content-addressed readiness, durable coordination, idempotent recovery,
  value-safe receipts, suspension, revocation, and rollback; and
- the Console as a same-origin server-mediated operator adapter.

Not approved:

- claiming normal availability before all four findings close;
- partial WGCF, OOS, identity, or Console activation;
- stage or production operation, external exposure, or broad runtime authority;
- automatic or machine-authorized merge, default-branch write, or provider
  bypass;
- mutation of referenced external source or implicit custody transfer;
- unadmitted import staging or execution of untrusted imported content;
- browser-held, personal, ambient, shared, broad, or long-lived credentials;
- Prototype runtime activation, Candidate or Baseline Promotion, Delivery
  creation, repository provisioning, or Portfolio publication by Landing; or
- model authorization, security acceptance, merge, or success projection.

Security Architecture retains authority over any later trust-boundary change.
If activation cannot preserve this exact boundary, the affected unit must stop
and return for a fresh delta review rather than weakening a gate locally.
