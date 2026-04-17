# Host-Control Plugin Security View

## Purpose

The host-control plugin is the typed runtime-side tool surface that bridges
OpenClaw runtime requests toward the host-control enforcement boundary.

## Security Role

- exposes typed host-facing operations to the runtime
- defines permission and confirmation semantics before bridge execution
- shapes which host capabilities are even reachable from the product runtime

## Trust Boundaries

- product runtime to typed tool boundary
- typed tool contract to host bridge request boundary
- runtime-visible permission tiers to host-side enforcement

## Principal Risks

- widening tool exposure beyond intended permission tiers
- collapsing typed operations back into generic shell-like behavior
- allowing runtime or model logic to become the real enforcement point instead
  of the host bridge

## Required Controls

- host-facing actions must remain typed and policy-aligned
- permission tiers and admin/high-risk semantics must remain explicit
- downstream repos must consume published interface contracts instead of private
  source assumptions
- the bridge remains the enforcement boundary; the plugin must not become a
  hidden policy engine

## Evidence And Related Docs

- [`../../domains/host-control.md`](../../domains/host-control.md)
- [`../../products/openclaw/required-controls.md`](../../products/openclaw/required-controls.md)
- [`../../../reviews/security-review-checklist.md`](../../../reviews/security-review-checklist.md)
