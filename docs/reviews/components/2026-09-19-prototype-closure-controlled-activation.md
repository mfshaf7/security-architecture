# Prototype Closure Controlled-Activation Review

## Summary

- date: 2026-09-19
- owner repo: `security-architecture`
- delivery ref: `openproject://work_packages/1140`
- parent feature: `openproject://work_packages/921`
- parent initiative: `openproject://work_packages/892`
- governing architecture: `wgcf://artifacts/delivery-art/sha256/cb0773fca32a66e78909ec697cae49d134137c216f555b0fd0262ea7463d83bb`
- reviewed source: the seven exact `origin/main` revisions in that architecture packet
- prior reviews: `2026-09-12-prototype-closure-implementation-admission.md` and `2026-09-12-prototype-closure-causality-correction.md`
- decision: `approved-with-findings`

This decision permits the bounded owner-backed activation work in local
`dev-integration` under #1149, #1150, #1107, and #1151. It does not make
Prototype Closure normally available. Normal availability requires the
configured Console operating proof in #1151 after WGCF, OOS, and Platform
have supplied their own exact receipts.

## Scope Delta

### Design Intent

Prototype Closure has four distinct actions: apply accepted Delivery, graduate
source to an accepted durable custodian, retire incubation, and reopen retained
incubation. Delivery phase and Studio source custody are independent. Neither
a submitted request nor a selected target is accepted target authority.
Closure must not delete durable source, infer Portfolio publication, or reuse
Landing or Maturity credentials.

### Implemented Control

The merged Workspace Governance contract fixes event-before-receipt causality.
Studio owns reviewed source mutation and append-only history. WGCF has Closure
readiness schemas, policy, ledger, and an inactive manifest. OOS has the
four-action durable coordinator and bounded operator routes, but its configured
runtime remains inactive. The Console has a same-origin preparation surface;
Platform defines a dedicated selected-repository GitHub App identity with
bounded branch and write paths, but its app, installation, key projection, and
runtime are not commissioned.

Current owner code fails closed rather than supplying live Closure authority:
WGCF's `build_prototype_closure_readiness_runtime` rejects configuration after
the inactive manifest check, and OOS's Closure runtime rejects configuration
after its inactive manifest check. Changing only a manifest flag is therefore
not an activation plan. The Platform identity definition still says
`defined-inactive` and `runtime_enabled: false`.

### Operating Evidence

#1109 completed sixteen isolated scenarios across all four actions. Its
conformance record declares `synthetic-owner-fixture` evidence with
`sandbox-runtime` and `real-git` fidelity; it includes stale source, missing
Delivery target, review separation, cancellation, caller isolation, replay,
restart, changed review head, exact merge, owner proof, recovery, and Studio
history checks. The OOS source and this isolated proof are valuable
implementation evidence, not configured WGCF/OOS/Platform/Console operating
evidence. No commissioned Closure credential or live owner-backed terminal
receipt is established by this review.

## Review Areas

### Identity, Review, And Secrets

The Closure identity is separate from Landing, Maturity, and Agent Gary source
authorship. It is selected to `mfshaf7/workspace-prototype-studio`, has at most
one repository, short-lived installation tokens, and no merge, direct-main,
administration, or bypass authority. Platform must prove the actual App and
installation IDs, selected repository ID, permission and branch restrictions,
provider-enforced exact-head review, trusted owner validation, Vault custody,
read-only runtime projection, suspension, and revocation. The definition alone
proves none of those operating facts.

Agent Gary's attributed source authorship and delegated operator actions do
not constitute independent human review of a future Closure source mutation.
The provider must enforce that separation at the exact reviewed head. No
personal or ambient credential may substitute for the dedicated Closure
identity, and no key or token value may enter source, logs, ART, or receipts.

### Source, Target, And Receipt Authority

Studio alone mutates Prototype lifecycle and history. WGCF decides readiness
from current owner evidence; OOS coordinates and issues terminal receipts only
after exact reviewed merge and canonical Studio readback. Accepted Delivery or
durable-custodian evidence must come from its target owner. One active source
custodian, exact pre-merge state, prior history digest, and action-specific
target receipt must be bound before the Studio event. The Studio event cannot
cite the later terminal OOS receipt.

An identical replay may return the retained result. Changed authority under
the same idempotency key, stale source, missing or revoked target acceptance,
review-head change, merge uncertainty, readback mismatch, or receipt failure
must remain denied or pending reconciliation without a second source event or
false completed projection.

### Runtime, Recovery, And Visibility

Retirement requires exact active-resource cleanup or absence proof before its
terminal receipt. Graduation needs an explicit incubation-resource disposition.
Reopen retains retirement history and does not restore prior runtime secrets.
Suspension must stop new Closure work and revoke only Closure credentials and
resources, preserving Landing, Maturity, accepted target source, Git history,
and audit evidence.

The Console is a server-mediated operator client, not a second authority.
It must show request, block, review, merge, recovery, and terminal states from
the configured OOS path. A fixture, advisor, browser response, or disconnected
readout cannot project successful Closure. Neither this review nor local
commissioning grants stage or production authority.

## Findings And Activation Gates

1. **WGCF owner-backed readiness is absent.** #1149 must replace the
   configuration dead end with current Studio and target-authority evidence,
   exact caller and source binding, durable decision receipts, and negative
   tests for missing, stale, tampered, replayed, or fixture-only evidence.
2. **OOS owner-backed composition is absent.** #1150 must consume the admitted
   WGCF decision and real Studio/target adapters, preserve the reviewed
   source-event and terminal-receipt order, and prove cancellation, restart,
   review denial, readback, recovery, and receipt behavior without synthetic
   success fallback.
3. **Platform commissioning is absent.** #1107 must follow #1150, activate
   only the exact Closure identity and local profile, prove provider review
   rules, token custody, restart, suspension, revocation, resource cleanup,
   and rollback, and retain secret-free owner receipts. Its
   `normal_availability_gate` label must not be interpreted as availability
   before #1151.
4. **Configured Console proof is absent.** #1151 must exercise all four
   actions through the commissioned Console and owner path, including denied,
   stale, replayed, interrupted, review-rejected, readback-mismatched,
   suspended, and revoked cases. Only after that proof may local normal
   operator availability be considered.

These are ordered conditions, not accepted risk. A failed condition returns
to its owner work item and keeps Closure inactive.

## Decision

`approved-with-findings`

Approved: the bounded local activation sequence in Architecture Packet v25,
the dedicated inactive identity design, exact owner and receipt boundaries,
and source implementation work under #1149, #1150, #1107, and #1151.

Not approved: normal availability now; manifest-only activation; fixture-only
readiness; uncommissioned or ambient credentials; agent self-review or merge;
direct default-branch writes; source graduation without accepted durable
custody; completion without merged Studio readback and an OOS terminal receipt;
unbounded cleanup; Portfolio publication; or stage and production use.
