#!/usr/bin/env python3
"""Validate security-architecture evidence inventories and remediation linkage."""

from __future__ import annotations

import argparse
import csv
from datetime import date
from pathlib import Path
import re
import sys

import yaml


REVIEW_AREAS = {"identity", "secrets", "delivery", "runtime", "ai"}
CHANGE_REVIEW_STATUSES = {"baseline-current", "current"}
ASSESSMENT_STATUSES = {"published", "superseded"}
WORKSTREAM_STATUSES = {"active", "complete"}
FINDING_RISK_STATUSES = {"open", "mitigated", "accepted"}
ASSESSMENT_DRAFT_RE = re.compile(
    r"^\|\s*Status\s*\|\s*Draft\s*\|", re.MULTILINE | re.IGNORECASE
)
ASSESSMENT_TBD_RE = re.compile(
    r"^\|\s*Reviewers\s*\|\s*TBD\s*\|", re.MULTILINE | re.IGNORECASE
)


def load_yaml(path: Path) -> dict:
    return yaml.safe_load(path.read_text()) or {}


def parse_date(value: object, *, label: str, errors: list[str]) -> date | None:
    if isinstance(value, date):
        return value
    if isinstance(value, str):
        try:
            return date.fromisoformat(value)
        except ValueError:
            pass
    errors.append(f"{label}: expected ISO date, got {value!r}")
    return None


def artifact_path(workspace_root: Path, repo_name: str, rel_path: str) -> Path:
    return workspace_root / repo_name / rel_path


def validate_artifact_refs(
    refs: list[dict], *, label: str, workspace_root: Path, errors: list[str]
) -> None:
    if not refs:
        errors.append(f"{label}: at least one artifact reference is required")
        return
    for idx, ref in enumerate(refs, start=1):
        repo = ref.get("repo")
        path = ref.get("path")
        if not isinstance(repo, str) or not repo:
            errors.append(f"{label}: artifact #{idx} missing repo")
            continue
        if not isinstance(path, str) or not path:
            errors.append(f"{label}: artifact #{idx} missing path")
            continue
        resolved = artifact_path(workspace_root, repo, path)
        if not resolved.exists():
            errors.append(f"{label}: artifact #{idx} points to missing file {repo}/{path}")


def ids_from_markdown_table(path: Path, prefix: str) -> set[str]:
    ids: set[str] = set()
    for line in path.read_text().splitlines():
        line = line.strip()
        if line.startswith(f"| {prefix}"):
            ids.add(line.split("|")[1].strip())
    return ids


def ids_from_csv(path: Path, column_name: str) -> set[str]:
    with path.open(newline="") as handle:
        reader = csv.DictReader(handle)
        return {row[column_name].strip() for row in reader}


def validate(repo_root: Path, workspace_root: Path) -> list[str]:
    errors: list[str] = []
    today = date.today()

    review_inventory = load_yaml(repo_root / "registers" / "review-inventory.yaml")
    assessment_inventory = load_yaml(repo_root / "registers" / "assessment-inventory.yaml")
    remediation_inventory = load_yaml(repo_root / "registers" / "remediation-inventory.yaml")

    review_entries = review_inventory.get("review_inventory", {})
    for inventory_name in ("repos", "products", "components"):
        for entry_name, entry in (review_entries.get(inventory_name) or {}).items():
            latest = (entry or {}).get("latest_change_review") or {}
            status = latest.get("status")
            if status not in CHANGE_REVIEW_STATUSES:
                errors.append(
                    f"review-inventory {inventory_name}.{entry_name}: latest_change_review.status must be one of {sorted(CHANGE_REVIEW_STATUSES)}"
                )
                continue
            if status == "current":
                review_areas = latest.get("review_areas") or []
                if not isinstance(review_areas, list) or not review_areas:
                    errors.append(
                        f"review-inventory {inventory_name}.{entry_name}: current latest_change_review must declare review_areas"
                    )
                elif any(area not in REVIEW_AREAS for area in review_areas):
                    errors.append(
                        f"review-inventory {inventory_name}.{entry_name}: invalid review_areas {review_areas!r}"
                    )
                validate_artifact_refs(
                    latest.get("owner_artifacts") or [],
                    label=f"review-inventory {inventory_name}.{entry_name}",
                    workspace_root=workspace_root,
                    errors=errors,
                )

    assessments = assessment_inventory.get("assessment_inventory") or {}
    if not assessments:
        errors.append("assessment-inventory: at least one assessment entry is required")
    for name, entry in assessments.items():
        status = (entry or {}).get("status")
        if status not in ASSESSMENT_STATUSES:
            errors.append(
                f"assessment-inventory {name}: status must be one of {sorted(ASSESSMENT_STATUSES)}"
            )
        reviewed_on = parse_date(
            (entry or {}).get("reviewed_on"),
            label=f"assessment-inventory {name}.reviewed_on",
            errors=errors,
        )
        review_due_on = parse_date(
            (entry or {}).get("review_due_on"),
            label=f"assessment-inventory {name}.review_due_on",
            errors=errors,
        )
        if reviewed_on and review_due_on and review_due_on < reviewed_on:
            errors.append(
                f"assessment-inventory {name}: review_due_on {review_due_on} must not be before reviewed_on {reviewed_on}"
            )
        if review_due_on and review_due_on < today:
            errors.append(
                f"assessment-inventory {name}: assessment freshness expired on {review_due_on}"
            )
        reviewers = (entry or {}).get("reviewers") or []
        if (
            not isinstance(reviewers, list)
            or not reviewers
            or any(str(r).strip().upper() == "TBD" for r in reviewers)
        ):
            errors.append(f"assessment-inventory {name}: reviewers must be explicit and non-TBD")
        rel_path = (entry or {}).get("path")
        if not isinstance(rel_path, str) or not rel_path:
            errors.append(f"assessment-inventory {name}: missing path")
            continue
        assessment_path = repo_root / rel_path
        if not assessment_path.exists():
            errors.append(f"assessment-inventory {name}: missing file {rel_path}")
            continue
        content = assessment_path.read_text()
        if ASSESSMENT_DRAFT_RE.search(content):
            errors.append(f"assessment {rel_path}: active assessment must not still say Draft")
        if ASSESSMENT_TBD_RE.search(content):
            errors.append(f"assessment {rel_path}: active assessment must not still say Reviewers | TBD")

    workstreams = remediation_inventory.get("workstreams") or {}
    findings = remediation_inventory.get("findings") or {}
    risks = remediation_inventory.get("risks") or {}
    if not workstreams:
        errors.append("remediation-inventory: at least one workstream is required")
    for workstream_id, workstream in workstreams.items():
        status = (workstream or {}).get("status")
        if status not in WORKSTREAM_STATUSES:
            errors.append(
                f"remediation-inventory workstreams.{workstream_id}: status must be one of {sorted(WORKSTREAM_STATUSES)}"
            )
        parse_date(
            (workstream or {}).get("target_date"),
            label=f"remediation-inventory workstreams.{workstream_id}.target_date",
            errors=errors,
        )
        validate_artifact_refs(
            (workstream or {}).get("artifacts") or [],
            label=f"remediation-inventory workstreams.{workstream_id}",
            workspace_root=workspace_root,
            errors=errors,
        )

    finding_md_ids = ids_from_markdown_table(repo_root / "registers" / "findings-register.md", "F-")
    finding_csv_ids = ids_from_csv(repo_root / "registers" / "csv" / "findings-register.csv", "Finding ID")
    risk_md_ids = ids_from_markdown_table(repo_root / "registers" / "risk-register.md", "R-")
    risk_csv_ids = ids_from_csv(repo_root / "registers" / "csv" / "risk-register.csv", "Risk ID")
    if finding_md_ids != finding_csv_ids:
        errors.append("findings register markdown and CSV IDs do not match")
    if risk_md_ids != risk_csv_ids:
        errors.append("risk register markdown and CSV IDs do not match")

    for register_path in (
        repo_root / "registers" / "findings-register.md",
        repo_root / "registers" / "risk-register.md",
        repo_root / "registers" / "csv" / "findings-register.csv",
        repo_root / "registers" / "csv" / "risk-register.csv",
    ):
        if "TBD" in register_path.read_text():
            errors.append(f"{register_path.relative_to(repo_root)} must not contain TBD once remediation inventory is active")

    for collection_name, expected_ids, entries in (
        ("findings", finding_md_ids, findings),
        ("risks", risk_md_ids, risks),
    ):
        if set(entries) != expected_ids:
            missing = sorted(expected_ids - set(entries))
            extra = sorted(set(entries) - expected_ids)
            if missing:
                errors.append(f"remediation-inventory {collection_name}: missing entries for {missing}")
            if extra:
                errors.append(f"remediation-inventory {collection_name}: unexpected extra entries {extra}")
        for item_id, entry in entries.items():
            status = (entry or {}).get("status")
            if status not in FINDING_RISK_STATUSES:
                errors.append(
                    f"remediation-inventory {collection_name}.{item_id}: status must be one of {sorted(FINDING_RISK_STATUSES)}"
                )
            workstream = (entry or {}).get("workstream")
            if workstream not in workstreams:
                errors.append(
                    f"remediation-inventory {collection_name}.{item_id}: unknown workstream {workstream!r}"
                )
            if collection_name == "findings":
                target_date = parse_date(
                    (entry or {}).get("target_date"),
                    label=f"remediation-inventory findings.{item_id}.target_date",
                    errors=errors,
                )
                if status == "open" and target_date and target_date < today:
                    errors.append(
                        f"remediation-inventory findings.{item_id}: open finding target_date {target_date} is already in the past"
                    )
            validate_artifact_refs(
                (entry or {}).get("remediation_artifacts") or [],
                label=f"remediation-inventory {collection_name}.{item_id}",
                workspace_root=workspace_root,
                errors=errors,
            )

    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--workspace-root")
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    workspace_root = Path(args.workspace_root).resolve() if args.workspace_root else repo_root.parent

    errors = validate(repo_root, workspace_root)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    review_count = sum(
        len(section or {})
        for section in (load_yaml(repo_root / "registers" / "review-inventory.yaml").get("review_inventory") or {}).values()
    )
    assessment_count = len(
        load_yaml(repo_root / "registers" / "assessment-inventory.yaml").get("assessment_inventory") or {}
    )
    remediation = load_yaml(repo_root / "registers" / "remediation-inventory.yaml")
    print(
        "security evidence valid: "
        f"reviews={review_count} "
        f"assessments={assessment_count} "
        f"findings={len(remediation.get('findings') or {})} "
        f"risks={len(remediation.get('risks') or {})}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
