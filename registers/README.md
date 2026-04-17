# Security Registers

Registers track live security facts that need regular maintenance.

## Current Registers

- [`findings-register.md`](findings-register.md)
- [`risk-register.md`](risk-register.md)
- [`review-inventory.md`](review-inventory.md)
- [`assessment-inventory.md`](assessment-inventory.md)
- [`credential-inventory.md`](credential-inventory.md)
- [`ai-system-inventory.md`](ai-system-inventory.md)
- [`review-inventory.yaml`](review-inventory.yaml)
- [`assessment-inventory.yaml`](assessment-inventory.yaml)
- [`remediation-inventory.yaml`](remediation-inventory.yaml)
- [`security-change-record-index.yaml`](security-change-record-index.yaml)

CSV exports live under `csv/` when a tabular export is useful:

- findings and risks
- review inventory
- assessment inventory

The YAML inventories are the machine-readable source of truth for review
coverage, assessment freshness, and remediation linkage. The Markdown and CSV
tables are human-readable summaries and should stay aligned with the inventory
metadata.

`security-change-record-index.yaml` is a generated cross-repo view of owner
change records that declare `security_evidence` metadata.

Render or verify the generated views with:

```bash
python3 scripts/render_register_views.py --repo-root .
python3 scripts/render_register_views.py --repo-root . --check
```
