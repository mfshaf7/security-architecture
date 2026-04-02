# Roadmap

## Phase 0: Stabilize

- recover Vault and Argo trust paths
- restore managed secret delivery
- inventory exposed and shared credentials
- classify current break-glass materials

## Phase 1: Establish Control Baselines

- create security standards for identity, secrets, recovery, and machine credentials
- document current-state architecture and trust relationships
- build a credential inventory with owners and rotation cadence
- define a break-glass policy

## Phase 2: Human Identity Modernization

- design OIDC integration for Vault
- design OIDC integration for Argo CD
- define group-to-role mapping
- retire routine use of local operator passwords

## Phase 3: Machine Identity Modernization

- replace Argo Git PAT access with GitHub App credentials
- reduce or remove long-lived static automation tokens
- define repository access governance for controllers and CI/CD

## Phase 4: Recovery and Resilience

- formalize storage and restore process for recovery material
- test Vault recovery quarterly
- validate secret bootstrap and restore paths
- validate platform rebuild from declared state

## Phase 5: Continuous Security Review

- add security review checkpoints to major platform changes
- maintain architecture decision records for sensitive changes
- track remediation closure against risk register entries
