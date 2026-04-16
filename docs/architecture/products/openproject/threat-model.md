# OpenProject Threat Model

## Principal Threats

| Threat | Why It Matters | Main Control Surface |
| --- | --- | --- |
| Over-broad admin access | weakens attribution and change governance | identity and access domain |
| Weak backup and restore governance | risks data loss or uncontrolled recovery paths | platform PostgreSQL component view |
| Mis-scoped secret delivery | can expose runtime secrets or cause insecure workarounds | secrets and recovery domain |
| Sensitive telemetry exposure | dashboards or logs may reveal application metadata | observability component view |
