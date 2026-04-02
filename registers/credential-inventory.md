# Credential Inventory

| Credential Class | Scope | Owner | Storage | Rotation Model | Notes |
| --- | --- | --- | --- | --- | --- |
| Vault human operator access | Human | Platform owner | Transitional local/Vault | Pending redesign | Move to OIDC |
| Argo human operator access | Human | Platform owner | Transitional local/Argo | Pending redesign | Move to OIDC |
| Argo repo access | Machine | Platform | Vault-backed ExternalSecret | Replace | Target GitHub App |
| External Secrets Vault auth | Machine | Platform | Kubernetes service account + Vault role | Periodic review | Correct model, keep |
| Vault recovery material | Break-glass | Security/Platform | Approved secure storage + encrypted backup | Governed review | Needs formal policy |
