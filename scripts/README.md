# Scripts

This directory contains lightweight validation helpers for repository structure
and minimum review-lane coverage.

## Available Scripts

- `render_register_views.py`
  - generates the findings/risk register views plus review/assessment inventory
    Markdown and CSV summaries from the YAML inventories under `registers/`
- `render_security_change_record_index.py`
  - generates the cross-repo index of owner change records that declare
    `security_evidence` front matter
- `validate_repo_structure.py`
  - verifies that the required hybrid security-architecture layout exists and
    that retired flat paths are gone
  - verifies that each review lane contains at least one dated review output
    beyond its directory `README.md`
  - verifies that the review inventory register exists
  - verifies that architecture docs keep design intent separate from evidence
    surfaces and that the platform component inventory covers admitted shared
    security-relevant components such as `operator-orchestration-service`
- `validate_security_evidence.py`
  - validates review-inventory change-review metadata, assessment freshness
    metadata, remediation linkage against real owner-repo artifacts, and that
    generated register views stay current
