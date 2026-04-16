# Argo CD Security View

## Purpose

Argo CD is the GitOps control plane that turns approved Git state into live
cluster state.

## Security Role

- consumes repository trust
- applies approved platform and product manifests
- acts as a high-impact control plane for deployment and rollback

## Trust Boundaries

- GitHub source to controller trust
- controller identity inside Kubernetes
- operator access to sync, refresh, and override behavior

## Principal Risks

- repository credentials drifting out of managed visibility
- manual controller actions bypassing governed intent
- over-privileged controller access inside the cluster

## Required Controls

- repository access must be explicit, reviewable, and recoverable
- promotions must preserve digest and source attestation
- manual actions must not become a substitute for governed source changes
- operator access should move toward federated identity

## Evidence And Related Docs

- [`../../domains/gitops-and-machine-trust.md`](../../domains/gitops-and-machine-trust.md)
- [`../../platform/overview.md`](../../platform/overview.md)
- [`../../../assessments/platform/2026-04-detailed.md`](../../../assessments/platform/2026-04-detailed.md)
