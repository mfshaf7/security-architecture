#!/usr/bin/env python3
"""Validate the security-architecture repository structure."""

from __future__ import annotations

import argparse
from pathlib import Path
import re
import sys


REQUIRED_PATHS = [
    "README.md",
    "AGENTS.md",
    "docs/README.md",
    "docs/charter.md",
    "docs/architecture/README.md",
    "docs/architecture/platform/README.md",
    "docs/architecture/platform/overview.md",
    "docs/architecture/platform/component-inventory.md",
    "docs/architecture/platform/trust-boundaries.md",
    "docs/architecture/domains/README.md",
    "docs/architecture/domains/identity-and-access.md",
    "docs/architecture/domains/secrets-and-recovery.md",
    "docs/architecture/domains/gitops-and-machine-trust.md",
    "docs/architecture/domains/host-control.md",
    "docs/architecture/domains/ai-and-agentic.md",
    "docs/architecture/components/README.md",
    "docs/architecture/components/argo-cd/README.md",
    "docs/architecture/components/vault/README.md",
    "docs/architecture/components/external-secrets/README.md",
    "docs/architecture/components/observability/README.md",
    "docs/architecture/components/platform-postgresql/README.md",
    "docs/architecture/components/openclaw-host-bridge/README.md",
    "docs/architecture/products/README.md",
    "docs/architecture/products/openclaw/README.md",
    "docs/architecture/products/openclaw/security-overview.md",
    "docs/architecture/products/openclaw/data-flow-and-boundaries.md",
    "docs/architecture/products/openclaw/threat-model.md",
    "docs/architecture/products/openclaw/required-controls.md",
    "docs/architecture/products/openproject/README.md",
    "docs/architecture/products/openproject/security-overview.md",
    "docs/architecture/products/openproject/threat-model.md",
    "docs/architecture/products/openproject/required-controls.md",
    "docs/standards/README.md",
    "docs/reviews/README.md",
    "docs/assessments/README.md",
    "docs/methodology/README.md",
    "docs/strategy/README.md",
    "docs/templates/README.md",
    "registers/README.md",
    "scripts/README.md",
    "skills-src/README.md",
    "skills-src/security-governance-review/SKILL.md",
]

FORBIDDEN_PATHS = [
    "docs/architecture/platform-overview.md",
    "docs/architecture/component-inventory.md",
    "docs/architecture/trust-boundaries.md",
    "docs/assessments/platform-security-assessment-2026-04.md",
    "docs/assessments/platform-security-executive-report-2026-04.md",
]

REVIEW_OUTPUT_DIRECTORIES = [
    "docs/reviews/platform",
    "docs/reviews/components",
    "docs/reviews/products",
]
DATED_REVIEW_OUTPUT_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2}-.+\.md$")


def validate(repo_root: Path) -> list[str]:
    errors: list[str] = []

    for rel in REQUIRED_PATHS:
        path = repo_root / rel
        if not path.exists():
            errors.append(f"missing required path: {rel}")

    for rel in FORBIDDEN_PATHS:
        path = repo_root / rel
        if path.exists():
            errors.append(f"retired path still exists: {rel}")

    for rel in REVIEW_OUTPUT_DIRECTORIES:
        directory = repo_root / rel
        if not directory.exists():
            continue
        dated_outputs = [
            path.name
            for path in sorted(directory.glob("*.md"))
            if path.name != "README.md" and DATED_REVIEW_OUTPUT_PATTERN.match(path.name)
        ]
        if not dated_outputs:
            errors.append(
                f"review output lane must contain at least one dated review artifact: {rel}"
            )

    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", default=".")
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    errors = validate(repo_root)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print("security-architecture repo structure is valid")
    return 0


if __name__ == "__main__":
    sys.exit(main())
