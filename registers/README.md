# Security Registers

Registers track live security facts that need regular maintenance.

## Current Registers

- [`findings-register.md`](findings-register.md)
- [`risk-register.md`](risk-register.md)
- [`credential-inventory.md`](credential-inventory.md)
- [`ai-system-inventory.md`](ai-system-inventory.md)
- [`review-inventory.yaml`](review-inventory.yaml)
- [`assessment-inventory.yaml`](assessment-inventory.yaml)
- [`remediation-inventory.yaml`](remediation-inventory.yaml)

CSV exports live under `csv/` when a tabular export is useful.

The YAML inventories are the machine-readable source of truth for review
coverage, assessment freshness, and remediation linkage. The Markdown and CSV
tables are human-readable summaries and should stay aligned with the inventory
metadata.
