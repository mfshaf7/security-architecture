# Workspace Prototype Studio

## Role

`workspace-prototype-studio` is the fast product-incubation source lane for
internal tools, future client apps, UI prototypes, and UI-plus-backend
experiments before they graduate into governed delivery, an existing product
repo, or a new dedicated product repo.

It does not own production releases, platform deployment authority, Workspace
Delivery ART state, security acceptance, real client-data custody, or long-lived
product source after graduation.

## Trust Boundary

Prototype Studio sits before governed product delivery. Its main security risk
is letting fast exploration quietly become a real system without the review,
identity, data, runtime, and delivery controls that governed delivery requires.

The approved default boundary is:

- mock or synthetic data only
- private internal visibility by default
- no production deployment
- no repository secrets or real client data
- no mutable writes to real systems
- no AI-assisted decision or action path without explicit review
- no client-visible review surface until a client-safe evidence path exists

## Current Admitted Shape

- owner repo: `workspace-prototype-studio`
- workspace authority owner: `workspace-governance`
- platform runtime owner: `platform-engineering`
- security owner: `security-architecture`
- current runtime lane: source-only prototype lane with local validation
- governed stage/prod status: not admitted
- default prototype data mode: `synthetic`
- default visibility tier: `private-internal`
- default mutation boundary: `none`

## Security Model

### Identity

Prototype Studio does not approve identity, authentication, authorization, or
session behavior for production use. Any prototype that introduces identity or
client-facing access must trigger security review and usually graduation.

### Secrets

Secrets, tokens, credentials, webhooks, private operational logs, and production
exports must not be committed to this repo. Prototypes must use mock or
synthetic data unless `real-readonly` has explicit security-review evidence.

### Delivery

This repo is not a release authority. Prototype source may be reviewed here,
but durable delivery must graduate into the appropriate governed ART, owner
repo, platform lane, or client portfolio before release evidence is accepted.

### Runtime

Local previews and disposable prototype-local backends are acceptable while
state is mock, synthetic, local, or sandboxed. External hosting, inbound network
exposure, durable backend state, client-facing access, or mutable real-system
integration is not approved here.

### AI

Prototype Studio may shape AI-assisted UX concepts, but it does not approve
model invocation, governed AI access, autonomous action, tool-calling, or raw
context projection. AI-assisted action paths must route through the governed AI
and context admission controls before implementation.

## Review Triggers

Open or refresh a security review when a prototype introduces:

- identity, authentication, authorization, or sessions
- secrets, webhooks, API keys, tokens, or credentials
- real client data, operational exports, or regulated data
- client-visible or public-demo exposure
- external hosting or inbound network exposure
- mutable writes outside prototype-local state
- payment, billing, healthcare, legal, finance, or regulated workflows
- AI-assisted decisions, model invocation, tool use, or action paths

## Required Companion Artifacts

- Product-incubation security baseline:
  [../../../reviews/components/2026-05-06-workspace-prototype-studio-product-incubation-baseline.md](../../../reviews/components/2026-05-06-workspace-prototype-studio-product-incubation-baseline.md)
- Prototype Studio owner docs:
  `workspace-prototype-studio/README.md`
- Prototype Studio data boundary checklist:
  `workspace-prototype-studio/docs/security-and-data-boundaries.md`
- Workspace repo rule:
  `workspace-governance/contracts/repo-rules/workspace-prototype-studio.yaml`
