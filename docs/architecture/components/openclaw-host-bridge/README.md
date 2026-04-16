# OpenClaw Host Bridge Security View

## Purpose

The OpenClaw host bridge is the host-side enforcement boundary for privileged
actions triggered from the OpenClaw runtime.

## Security Role

- enforces allowed roots and permission tiers
- stages exports and screenshots
- records host-facing audit evidence
- exposes health and attestation for the live host runtime

## Trust Boundaries

- product runtime to bridge request boundary
- bridge policy to host execution boundary
- audit and staging paths on the host
- stage versus prod environment alignment when both exist

## Principal Risks

- privileged host behavior influenced by user-facing or model-driven inputs
- policy drift between the running bridge and governed intent
- audit or staging paths crossing environment boundaries

## Required Controls

- typed operations instead of raw shell exposure
- explicit permission tiers and admin gating
- policy and audit outside the model surface
- runtime attestation for the live service
- environment-specific validation when stage and prod coexist

## Evidence And Related Docs

- [`../../domains/host-control.md`](../../domains/host-control.md)
- [`../../products/openclaw/README.md`](../../products/openclaw/README.md)
- [`../../../assessments/platform/2026-04-detailed.md`](../../../assessments/platform/2026-04-detailed.md)
