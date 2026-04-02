# Risk Register

| ID | Title | Severity | Status | Summary | Target Workstream |
| --- | --- | --- | --- | --- | --- |
| R-001 | Shared privileged credential blast radius | High | Open | A single secret has been reused across multiple privileged workflows. | Identity modernization |
| R-002 | Recovery-material governance weakness | High | Open | Vault recovery material was recoverable but not under a clearly governed storage model. | Recovery governance |
| R-003 | Controller Git credential drift | High | Mitigated | Argo Git credentials drifted out of managed visibility and were restored through Vault-backed management. | Machine identity |
| R-004 | Manual-unseal probe fragility | Medium | Mitigated | Vault probes were incompatible with manual-unseal startup and caused control-plane instability. | Platform resilience |
