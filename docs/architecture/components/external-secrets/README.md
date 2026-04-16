# External Secrets Security View

## Purpose

External Secrets Operator materializes governed secret values from Vault into
runtime namespaces.

## Security Role

- bridges cluster workloads to Vault-backed secret authority
- converts controller trust into runtime secret delivery

## Trust Boundaries

- Kubernetes service-account identity to Vault auth
- namespace scoping and SecretStore ownership
- secret materialization into runtime namespaces

## Principal Risks

- overly broad controller authorization
- namespace secret delivery drift during recovery
- runtime teams bypassing governed secret paths with manual secrets

## Required Controls

- Vault auth and role mapping must be explicit and reviewable
- SecretStores should be namespace-scoped where practical
- recovery should validate controller trust and expected store health
- runtime teams should not carry unmanaged substitute secrets

## Evidence And Related Docs

- [`../../domains/secrets-and-recovery.md`](../../domains/secrets-and-recovery.md)
- [`../../../assessments/platform/2026-04-detailed.md`](../../../assessments/platform/2026-04-detailed.md)
