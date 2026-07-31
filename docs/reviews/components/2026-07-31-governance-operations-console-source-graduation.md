# Governance Operations Console Source Graduation Security Delta

## Summary

- date: 2026-07-31
- owner repo: `security-architecture`
- affected review subject:
  - `repos.governance-operations-console`
- security ART item: `openproject://work_packages/785`
- source landing ART item: `openproject://work_packages/784`
- source review:
  [governance-operations-console#3](https://github.com/mfshaf7/governance-operations-console/pull/3)
- reviewed source commit:
  [`9d8d2f0`](https://github.com/mfshaf7/governance-operations-console/commit/9d8d2f0e550cd14ee915ecdb0aadd5cceddcc38d)
- inherited reviews:
  - [baseline security delta](2026-07-30-governance-operations-console-baseline-security-delta.md)
  - [owner repository admission](2026-07-31-governance-operations-console-owner-repository-admission.md)
- review triggers:
  - `governance-console-source-graduation`
  - `governance-console-live-integration`
- decision: `approved-with-findings`

The exact reviewed source is approved to graduate from Workspace Prototype
Studio into the public Governance Operations Console owner repository. The
landing preserves the approved local-only boundary and does not activate a
shared runtime, live backend, authenticated identity, governed AI path,
deployment, release, stage, production, or public application endpoint.

## Scope Delta

### Design Intent

- Move the approved application baseline into its durable product-source
  owner without changing visual or workflow behavior.
- Preserve exact source provenance and keep Prototype Studio as historical
  prototype and graduation-record authority rather than a competing source
  owner.
- Make public-source safety, architecture guards, semantic tests, type checks,
  builds, and dependency audit part of owner-repository review.
- Keep later live integration separated by authority owner and fresh security
  review.

### Implemented Control

The reviewed owner-repository head provides:

- 1,106 application files transferred from the approved application tree, with
  the prototype-local README replaced by durable owner guidance
- 49 product records plus the approved design-baseline record and a
  machine-readable source-transfer manifest
- product source under `src/`, focused architecture guards, 330 semantic tests,
  and an isolated end-to-end foundation simulation
- a repository validator that rejects operator-local paths, the known private
  workspace endpoint, private-key material, unresolved placeholders,
  secret-bearing file types, environment files, dependency trees, build
  output, logs, and runtime state
- a loopback-only Next.js development command on `127.0.0.1:3317`
- the reviewed read-only local host telemetry route and manual,
  suggestion-only local Ollama path with synthetic context
- CI that runs repository validation, clean dependency installation, complete
  product checks, and production dependency audit
- a local container build definition with no registry push, deployment,
  ingress, secret, environment, or release activation

The Dockerfile and CI path match the live-integration trigger because those
paths can activate runtime or delivery in later changes. In this exact landing
they provide build proof only. No deployment consumer or externally reachable
runtime is added.

### Operating Evidence

- source PR head is
  `9d8d2f0e550cd14ee915ecdb0aadd5cceddcc38d`
- source manifest binds:
  - application commit
    `aa12fdbb9b4f7b16c8ac2d2229c4dd4f6c95ec98`
  - application tree
    `28647acecce1709f408f5b8b1f6e3f944cb46104`
  - product-record commit
    `32bbd95561a3ded8701cfa089bf6f1a68a879e2c`
  - product-record tree
    `50c049a6846b2f90a27f425b1d61b7daf1e22e1c`
  - approved baseline blob
    `e2b52ad598354364e82dd966c24e9fd6518018b2`
- the owner-repository validator passes across 1,167 tracked files
- all architecture guards pass
- all 330 semantic tests pass
- TypeScript and the optimized Next.js production build pass
- `npm audit --omit=dev` reports zero known vulnerabilities
- relative product and graduation document links resolve
- focused public-source scanning found no operator-local project path, private
  workspace endpoint, private-key marker, unresolved placeholder, environment
  file, secret-bearing file, or disposable runtime artifact
- runtime and test source differs from the approved application tree only for
  recorded owner-path references and nonfunctional root-file whitespace
  normalization

This is source and build evidence. It is not runtime operating evidence.

## Review Areas

### Identity

Source graduation does not add authentication, authorization, session, or
access-control behavior. The active identity fixture remains synthetic,
unauthenticated, and unable to grant operator authority. `GOC-SEC-02` remains
an expansion gate.

### Secrets

No credential, token, private key, environment file, or secret-delivery path is
present in the reviewed source. Public-source validation and review reduce
common leakage risk but do not replace future secret custody, secret scanning,
or data-loss prevention when live integrations are added.

### Delivery

The owner repository becomes durable product-source authority only. Workspace
Governance retains product classification, Workspace Delivery ART retains work
state, Platform Engineering retains runtime and release authority, and Security
Architecture retains security judgment.

The required landing order is:

1. merge this Security Architecture delta;
2. bind it from and merge the owner-repository source PR;
3. record Prototype Studio graduation and remove the competing active source
   copy;
4. promote the product through Workspace Governance; and
5. finalize one Review Packet over the complete ART landing unit.

### Runtime

The local development command remains loopback-only. The Dockerfile can build
the application but has no deployment, registry, ingress, environment, or
release consumer in this landing. The read-only host telemetry and local model
adapter retain the limits from the baseline review. `GOC-SEC-03` remains an
expansion gate.

### AI

The local assistant remains manual, suggestion-only, synthetic-context-only,
and without tools or mutation authority. Source graduation does not make it a
governed AI path. `GOC-SEC-01` and `GOC-SEC-04` remain expansion gates.

## Findings And Gates

No new blocker is introduced by the source transfer. The existing findings
remain open:

1. `GOC-SEC-01`: local Ollama bypasses the governed AI access plane.
2. `GOC-SEC-02`: the Console has no trusted identity or server-side
   authorization.
3. `GOC-SEC-03`: local runtime readiness includes host metadata that cannot be
   shared without access control and response minimization.
4. `GOC-SEC-04`: browser-memory agent evidence is not a durable audit trail.

These findings do not block the exact source graduation. They block expansion
into shared or governed runtime boundaries until separately reviewed controls
resolve or explicitly disposition them.

## Decision

`approved-with-findings`

Approval is limited to:

- source commit
  `9d8d2f0e550cd14ee915ecdb0aadd5cceddcc38d`
- the provenance and bounded adaptations in the source manifest
- public durable product-source custody
- loopback local preview
- fixture-backed or synthetic operational records
- read-only local host telemetry
- synthetic unauthenticated identity
- manual suggestion-only local Ollama use with synthetic context
- local build and CI validation

Approval excludes:

- live backend or canonical mutation
- durable workflow or receipt authority
- real identity, authorization, secrets, or client data
- shared model access or governed AI status
- deployment, ingress, runtime activation, stage, production, or release
- security acceptance beyond the exact reviewed local source boundary

## Related Artifacts

- [Security delta review process](../security-delta-review-process.md)
- [Security review checklist](../security-review-checklist.md)
- [Owner-repository source manifest](https://github.com/mfshaf7/governance-operations-console/blob/9d8d2f0e550cd14ee915ecdb0aadd5cceddcc38d/docs/graduation/source-manifest.json)
- [Owner-repository security boundary](https://github.com/mfshaf7/governance-operations-console/blob/9d8d2f0e550cd14ee915ecdb0aadd5cceddcc38d/docs/security-and-data-boundaries.md)
