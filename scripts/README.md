# Scripts

This directory contains lightweight validation helpers for repository structure
and minimum review-lane coverage.

## Available Scripts

- `render_register_views.py`
  - generates the findings and risk Markdown/CSV register views from
    `registers/remediation-inventory.yaml`
- `render_security_change_record_index.py`
  - generates the cross-repo index of owner change records that declare
    `security_evidence` front matter
- `validate_repo_structure.py`
  - verifies that the required hybrid security-architecture layout exists and
    that retired flat paths are gone
  - verifies that each review lane contains at least one dated review output
    beyond its directory `README.md`
  - verifies that the review inventory register exists
- `validate_security_evidence.py`
  - validates review-inventory change-review metadata, assessment freshness
    metadata, and remediation linkage against real owner-repo artifacts
