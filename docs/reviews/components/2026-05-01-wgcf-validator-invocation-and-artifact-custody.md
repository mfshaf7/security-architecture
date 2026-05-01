# WGCF Validator Invocation And Artifact Custody Security Delta

## Summary

- date: 2026-05-01
- owner repo: `security-architecture`
- affected review subjects:
  - `repos.platform-engineering`
  - `repos.workspace-governance`
  - `repos.workspace-governance-control-fabric`
  - `components.workspace-governance-control-fabric`
- ART item: `openproject://work_packages/532`
- related ART children:
  - `openproject://work_packages/533`
  - `openproject://work_packages/534`
  - `openproject://work_packages/535`
- decision: `approved-with-findings`

This delta review evaluates the security boundary for using WGCF to invoke
workspace governance validators, emit compact receipts, and participate in
shadow parity before any direct validator path is retired.

The review approves a gated shadow and limited cutover model. It does not
approve raw artifact custody, stage/prod deployment, direct ART mutation,
security acceptance, or workspace contract mutation by WGCF.

## Scope Delta

### Design Intent

- `platform-engineering` defines the runtime profile gates for WGCF validator
  invocation.
- `workspace-governance` defines the validator catalog and shadow-parity
  cutover contract.
- `workspace-governance-control-fabric` implements planning, invocation,
  receipt, ledger, and compact projection behavior.
- WGCF may make validation faster and more observable, but direct validator
  rollback remains available until the cutover contract marks a scope
  retirement-eligible.

### Implemented Control

The reviewed slice is a control-plane contract and documentation slice:

- platform profile gates for `devint-shadow`, `stage-readiness`,
  `prod-readiness`, and `break-glass`
- workspace shadow-parity requirements for representative workspace, ART,
  platform, and security scopes
- receipt-only evidence posture for normal cutover
- explicit denial of direct authority mutation by WGCF
- retained direct-validator rollback while parity is being proven

No new raw artifact store, external ingress, service credential, model path, or
stage/prod runtime is approved by this review.

### Operating Evidence

Operating evidence for broad cutover is still pending. Before cutover is safe,
the owner repos must produce:

- platform profile-gate evidence
- a current security delta review reference
- shadow-parity evidence comparing direct validators with WGCF receipts
- compact receipt evidence that omits raw sensitive output
- rollback evidence proving direct validators remain executable

## Review Areas

### Identity

WGCF validator invocation creates a caller-attribution boundary. The security
position is:

- local/source and `devint-shadow` use may rely on operator-controlled local
  execution and local-k3s profile identity
- governed runtime use needs service identity and caller authorization by
  operation and profile before activation
- `break-glass` must record operator, reason, target scope, expiry, and
  receipt reference
- WGCF must not borrow OOS, platform, or security authority identities to
  mutate upstream systems

### Secrets

Validator output may include secret-like material, environment variables,
internal hostnames, private addresses, tokens, or operational context. The safe
default is:

- compact receipts may cite redaction counts, suppressed windows, digests, and
  artifact references
- raw validator output must not be projected into operator or model-safe
  packets by default
- raw artifacts remain local or denied unless a governed custody store,
  retention policy, access control, and deletion path are approved
- stage/prod secret delivery for WGCF remains out of scope

### Delivery

The authority split is acceptable only if it remains enforced:

- OOS remains the only Delivery ART mutation authority.
- `platform-engineering` remains the release and deployment authority.
- `security-architecture` remains the security acceptance authority.
- `workspace-governance` remains the contract and validator-catalog authority.
- WGCF receipt output is evidence, not approval.

Any implementation that turns WGCF into a mutation path for those authority
stores is a security-significant regression.

### Runtime

Approved runtime posture for this delta:

- source-local and `devint-shadow` validator planning, invocation, and receipt
  comparison
- compact receipt and ledger emission
- profile-gated remote or live reads only after the platform gate admits that
  safety class

Not approved by this delta:

- stage/prod WGCF runtime deployment
- API-side broad validation execution as a governed service
- raw artifact custody outside local files
- unbounded recursive validation plans
- network, Kubernetes, GitHub, or broker mutation by WGCF
- direct replacement of direct validators before shadow parity and rollback
  evidence exist

### AI

This change does not approve model invocation. If WGCF receipts, excerpts, or
artifact references are later consumed by an AI workflow, the context must pass
through the approved context-admission and governed model-access paths.

Raw operational context must remain denied by default for model projection.

## Decision

`approved-with-findings`

Approved because the proposed model keeps WGCF as a governed validation
control plane and evidence producer, not an authority replacement. The
approval is limited to gated shadow parity, compact receipts, and controlled
cutover planning.

Findings and residual risk:

1. Identity for governed runtime invocation is not approved yet. Stage/prod or
   service-side validation execution still needs caller identity,
   authorization, and audit correlation.
2. Raw artifact custody remains blocked. Full raw or redacted artifact storage
   requires approved object-store custody, retention, encryption, access, and
   deletion controls.
3. Receipt leakage risk remains. Receipts must stay compact, budgeted,
   redacted, and reference-based instead of copying raw command output.
4. Direct validator rollback must remain available until workspace shadow
   parity marks a scope retirement-eligible.
5. WGCF must remain evidence-only for ART, platform release, security
   acceptance, and workspace contract decisions.

## Acceptance Gates Before Broad Cutover

Broad normal operator or CI cutover to WGCF validator invocation requires:

- platform profile gate satisfied for the intended lane
- current security delta review remains `approved` or `approved-with-findings`
- workspace shadow-parity contract passes for representative workspace, ART,
  platform, and security scopes
- receipt parity proves equivalent pass/fail posture and meaningful findings
- rollback keeps direct validators callable
- raw artifact custody remains denied unless separately approved
- denied, suppressed, stale, and waived checks are visible in the receipt

## Related Artifacts

- `platform-engineering/docs/components/workspace-governance-control-fabric/validator-invocation-gates.md`
- `platform-engineering/docs/components/workspace-governance-control-fabric/release-governance.md`
- `workspace-governance/contracts/governance-engine-shadow-parity.yaml`
- `workspace-governance/scripts/validate_governance_engine_shadow_parity.py`
- `workspace-governance/docs/governance-engine-foundation.md`
- `workspace-governance/docs/governance-validator-catalog.md`
- [`2026-04-30-workspace-governance-control-fabric-devint-runtime.md`](2026-04-30-workspace-governance-control-fabric-devint-runtime.md)
- [`2026-04-30-workspace-governance-control-fabric-operator-surface.md`](2026-04-30-workspace-governance-control-fabric-operator-surface.md)
