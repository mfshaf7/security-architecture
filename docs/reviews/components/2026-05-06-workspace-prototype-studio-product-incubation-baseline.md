# Workspace Prototype Studio Product-Incubation Security Baseline

## Summary

- date: 2026-05-06
- owner repo: `security-architecture`
- affected review subjects:
  - `repos.workspace-prototype-studio`
- ART item: `openproject://work_packages/681`
- related implementation evidence:
  - `workspace-prototype-studio`
  - `workspace-governance/contracts/repo-rules/workspace-prototype-studio.yaml`
  - `workspace-prototype-studio/docs/security-and-data-boundaries.md`
- decision: `approved-with-findings`

This baseline reviews Workspace Prototype Studio as a fast
product-incubation source lane. The approval is limited to source control,
local validation, mock or synthetic data, private internal visibility, and
explicit lifecycle records before graduation.

It does not approve production deployment, governed stage/prod release,
identity, secrets, real client data, client-visible exposure, durable backend
runtime, external hosting, mutable real-system integration, or AI-assisted
action paths.

## Scope Delta

### Design Intent

- Provide a low-bureaucracy place to shape internal tools, client app ideas,
  UI prototypes, and UI-plus-backend experiments.
- Preserve lifecycle, visibility, data-mode, mutation-boundary, decision-log,
  and graduation controls while avoiding ART overhead for early design churn.
- Graduate prototypes before they become durable products, client-visible
  systems, or governed runtime components.

### Implemented Control

The reviewed foundation provides:

- repo-local `AGENTS.md`, README, and operating model
- `prototypes.yaml` registry with lifecycle, visibility tier, data mode,
  mutation boundary, runtime-lane target, delivery refs, and evidence refs
- JSON schemas for prototype registry, design baselines, graduations, and
  retirements
- repo-local validator and CI workflow
- security and data-boundary checklist
- GitHub CODEOWNERS and PR template sections for prototype governance,
  security triggers, validation, and graduation impact
- initial Governance Operations Console prototype candidate with mock/synthetic
  data posture

### Operating Evidence

Current evidence is source and local validation only:

- `make validate` passes in `workspace-prototype-studio`
- workspace governance declares the repo as active `product-incubation`
- no dev-integration preview lane is active yet
- no client-visible, real-data, external-hosted, or production runtime is
  approved by this review

## Review Areas

### Identity

No identity, authentication, authorization, or session implementation is
approved in this slice. Any prototype requiring login, role mapping, client
access, or operator identity binding must trigger a security review and
graduation decision.

### Secrets

Repository content must not include secrets, tokens, credentials, webhooks,
production exports, private operational logs, or real client data. The default
data modes are mock or synthetic. `real-readonly` requires explicit
security-review evidence, and `real-mutable` requires both security review and
a governed delivery or graduation plan.

### Delivery

Prototype Studio is not a release authority. It can prove product shape and
design direction, but durable source ownership, governed stage/prod, client
delivery, and platform deployment must move to the correct owner path before
release evidence is accepted.

### Runtime

Local previews and disposable prototype-local backends are acceptable while
state is mock, synthetic, local, or sandboxed. External hosting, inbound network
exposure, durable backend state, client-facing access, or mutable real-system
integration is not approved here.

### AI

AI-assisted UX concepts may be explored, but this review does not approve model
invocation, governed AI access, autonomous action, tool-calling, or raw context
projection. AI-related prototypes must route through context admission and
governed AI controls before implementation.

## Decision

`approved-with-findings`

Approved because the foundation keeps fast prototype delivery separate from
governed release authority and records lifecycle, visibility, data, mutation,
security-trigger, and graduation controls.

Findings and residual risk:

1. Prototype speed can still cause scope creep. Graduation triggers must be
   enforced before real runtime or client-visible behavior lands.
2. Synthetic data can become too realistic. Prototypes must avoid copied
   operational exports or client-identifying traces.
3. Local previews can drift toward unreviewed services. A dev-integration
   profile and fresh review are required before shared preview infrastructure
   or persistent backend state is activated.
4. AI-assisted concepts can blur into action paths. Model invocation and tool
   use remain blocked until governed AI and context admission controls are in
   place.

## Acceptance Gates Before Expansion

Before Prototype Studio can host mature runtime or client-visible review:

- security review must be refreshed for the concrete exposure
- client/data classification must be explicit
- identity and access model must be defined
- secret custody must be approved
- runtime lane must be registered or waived
- graduation target must be recorded
- Workspace Delivery ART, client portfolio, or owner repo handoff must exist
- context admission must packetize large or sensitive runtime/CI output before
  model projection

## Related Artifacts

- [../../architecture/components/workspace-prototype-studio/README.md](../../architecture/components/workspace-prototype-studio/README.md)
- `workspace-prototype-studio/README.md`
- `workspace-prototype-studio/docs/security-and-data-boundaries.md`
- `workspace-governance/contracts/repo-rules/workspace-prototype-studio.yaml`
