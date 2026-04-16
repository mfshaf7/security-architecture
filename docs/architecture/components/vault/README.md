# Vault Security View

## Purpose

Vault is the secret authority for managed platform and product runtime secrets.

## Security Role

- stores managed runtime secrets and controller credentials
- anchors secret-authority trust for the platform
- holds recovery-sensitive material and policies

## Trust Boundaries

- operator access to the control plane
- Kubernetes auth for controller-side secret delivery
- recovery authority and custody of break-glass material

## Principal Risks

- weak governance over recovery material
- brittle manual-unseal recovery paths
- static or over-shared operator credentials

## Required Controls

- recovery material must have explicit custody and review
- bootstrap and re-bootstrap paths must be documented and testable
- human access should move toward federated identity
- secret paths and policies should remain reviewable

## Evidence And Related Docs

- [`../../domains/secrets-and-recovery.md`](../../domains/secrets-and-recovery.md)
- [`../../domains/identity-and-access.md`](../../domains/identity-and-access.md)
- [`../../../assessments/platform/2026-04-detailed.md`](../../../assessments/platform/2026-04-detailed.md)
