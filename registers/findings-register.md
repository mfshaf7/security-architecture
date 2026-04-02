# Findings Register

| Finding ID | Title | Severity | Likelihood | Affected Assets | Owner | Status | Target Date | Risk ID | Workstream |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| F-001 | Shared privileged credential blast radius | High | High | Vault, Argo CD, local admin, recovery handling | Security Architecture / Platform | Open | TBD | R-001 | Human identity modernization |
| F-002 | Recovery-material governance is incomplete | High | Medium | Vault recovery authority | Security Architecture / Platform | Open | TBD | R-002 | Recovery governance |
| F-003 | Argo CD repository trust drifted out of managed visibility | High | Medium | Argo CD, GitOps repo access | Platform | Mitigated | Completed | R-003 | Machine identity modernization |
| F-004 | Vault manual-unseal deployment was operationally fragile | Medium | Medium | Vault control plane | Platform | Mitigated | Completed | R-004 | Platform resilience |
| F-005 | Secret delivery was correct in design but brittle in recovery | Medium | Medium | Vault, ESO, runtime namespaces | Platform | Open | TBD | R-005 | Secret delivery resilience |
| F-006 | Host-control crosses a high-trust boundary | High | Medium | OpenClaw gateway, host bridge, WSL host | Security Architecture / Platform | Open | TBD | R-006 | Host-control security review |
| F-007 | AI and agentic governance is not yet formalized | Medium | Medium | AI-enabled and model-assisted workflows | Security Architecture | Open | TBD | R-007 | AI security and governance |

