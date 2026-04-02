# Component Inventory

## Shared Control Plane

| Component | Role | Trust Relevance | Current Notes |
| --- | --- | --- | --- |
| Argo CD | GitOps control plane | deploys platform state and consumes repo credentials | repo access restored through Vault-backed secret management |
| Vault | secret source of truth | stores runtime secrets, operator credentials, and governed secret paths | manual-unseal deployment |
| External Secrets Operator | delivery plane | materializes Vault secrets into namespaces | environment stores now validated |
| Kubernetes API | orchestration plane | underpins service-account trust and controller authority | relied on by Vault Kubernetes auth |

## Runtime And Host Control

| Component | Role | Trust Relevance | Current Notes |
| --- | --- | --- | --- |
| openclaw-gateway prod | production runtime gateway | user and system interaction plane | chat and host-control boundary |
| openclaw-gateway stage | pre-production runtime gateway | validation boundary | mirrors production trust shape |
| Telegram extension | user interaction surface | receives commands and returns content | sensitive due to callback and file-delivery paths |
| host-control plugin | bridge client | connects runtime to host services | privileged boundary crossing |
| openclaw-host-bridge | host action executor | privileged local execution and staging | systemd-managed |
| openclaw-host-recovery | resilience service | recovery and supervision support | systemd-managed |

## AI And Agentic Surface

| Component | Role | Trust Relevance | Current Notes |
| --- | --- | --- | --- |
| LLM-integrated gateway behavior | model-assisted action path | can influence privileged workflows | needs explicit governance |
| future agents / copilots | agentic decision and action layer | increases prompt, tool, and policy risk | requires dedicated architecture controls |
