# Scripts

This directory contains lightweight validation helpers for repository structure
and minimum review-lane coverage.

## Available Scripts

- `validate_repo_structure.py`
  - verifies that the required hybrid security-architecture layout exists and
    that retired flat paths are gone
  - verifies that each review lane contains at least one dated review output
    beyond its directory `README.md`
