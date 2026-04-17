#!/usr/bin/env python3
"""Validate security-architecture evidence inventories and remediation linkage."""

from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path
import re
import sys

import yaml

from render_register_views import generated_views


REVIEW_AREAS = {"identity", "secrets", "delivery", "runtime", "ai"}
CHANGE_REVIEW_STATUSES = {"baseline-current", "current"}
ASSESSMENT_STATUSES = {"published", "superseded"}
WORKSTREAM_STATUSES = {"active", "complete"}
FINDING_RISK_STATUSES = {"open", "mitigated", "accepted"}
CHANGE_RECORD_PATH_RE = re.compile(r"docs/records/change-records/\d{4}-\d{2}-\d{2}-[a-z0-9-]+\.md$")
FINDING_ID_RE = re.compile(r"^F-\d{3}$")
RISK_ID_RE = re.compile(r"^R-\d{3}$")
WORKSTREAM_ID_RE = re.compile(r"^WS-\d{3}$")
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


def parse_yaml_front_matter(path: Path) -> dict:
    text = path.read_text()
    if not text.startswith("---\n"):
        return {}
    parts = text.split("\n---\n", 1)
    if len(parts) != 2:
        return {}
    return yaml.safe_load(parts[0][4:]) or {}


def validate_generated_views(repo_root: Path, errors: list[str]) -> None:
    for path, expected in generated_views(repo_root).items():
        if not path.exists():
            errors.append(f"generated register view missing: {path.relative_to(repo_root)}")
            continue
        actual = path.read_text()
        if actual != expected:
            errors.append(f"generated register view out of date: {path.relative_to(repo_root)}")


def validate_change_record_linkage(
    *,
    repo_name: str,
    rel_path: str,
    item_id: str,
    workstream_id: str,
    collection_name: str,
    workspace_root: Path,
    errors: list[str],
) -> None:
    if not CHANGE_RECORD_PATH_RE.fullmatch(rel_path):
        return
    path = artifact_path(workspace_root, repo_name, rel_path)
    metadata = parse_yaml_front_matter(path)
    security_evidence = metadata.get("security_evidence") or {}
    if not security_evidence:
        errors.append(
            f"{repo_name}/{rel_path}: change record used as security remediation evidence must declare security_evidence front matter"
        )
        return
    findings = security_evidence.get("findings") or []
    risks = security_evidence.get("risks") or []
    workstreams = security_evidence.get("workstreams") or []
    review_areas = security_evidence.get("review_areas") or []
    if not isinstance(review_areas, list) or not review_areas or any(area not in REVIEW_AREAS for area in review_areas):
        errors.append(f"{repo_name}/{rel_path}: security_evidence.review_areas must be a non-empty list of valid review areas")
    if not isinstance(workstreams, list) or workstream_id not in workstreams:
        errors.append(
            f"{repo_name}/{rel_path}: security_evidence.workstreams must include {workstream_id}"
        )
    if collection_name == "findings":
        if not isinstance(findings, list) or item_id not in findings:
            errors.append(
                f"{repo_name}/{rel_path}: security_evidence.findings must include {item_id}"
            )
    elif collection_name == "risks":
        if not isinstance(risks, list) or item_id not in risks:
            errors.append(
                f"{repo_name}/{rel_path}: security_evidence.risks must include {item_id}"
            )


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
    validate_generated_views(repo_root, errors)
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
        for artifact in (workstream or {}).get("artifacts") or []:
            repo = artifact.get("repo")
            path = artifact.get("path")
            if isinstance(repo, str) and isinstance(path, str):
                if CHANGE_RECORD_PATH_RE.fullmatch(path):
                    validate_change_record_linkage(
                        repo_name=repo,
                        rel_path=path,
                        item_id="",
                        workstream_id=workstream_id,
                        collection_name="workstreams",
                        workspace_root=workspace_root,
                        errors=errors,
                    )

    for collection_name, entries in (("findings", findings), ("risks", risks)):
        for item_id, entry in entries.items():
            status = (entry or {}).get("status")
            if status not in FINDING_RISK_STATUSES:
                errors.append(
                    f"remediation-inventory {collection_name}.{item_id}: status must be one of {sorted(FINDING_RISK_STATUSES)}"
                )
            if collection_name == "findings":
                required_fields = ("title", "severity", "likelihood", "affected_assets", "owner", "risk_id")
            else:
                required_fields = ("title", "severity", "likelihood", "owner", "treatment", "residual_risk", "related_findings")
            for field_name in required_fields:
                if field_name not in (entry or {}):
                    errors.append(
                        f"remediation-inventory {collection_name}.{item_id}: missing field {field_name}"
                    )
            workstream = (entry or {}).get("workstream")
            if workstream not in workstreams:
                errors.append(
                    f"remediation-inventory {collection_name}.{item_id}: unknown workstream {workstream!r}"
                )
            if collection_name == "findings" and not FINDING_ID_RE.fullmatch(item_id):
                errors.append(f"remediation-inventory findings: invalid finding id {item_id!r}")
            if collection_name == "risks" and not RISK_ID_RE.fullmatch(item_id):
                errors.append(f"remediation-inventory risks: invalid risk id {item_id!r}")
            if workstream and not WORKSTREAM_ID_RE.fullmatch(workstream):
                errors.append(
                    f"remediation-inventory {collection_name}.{item_id}: invalid workstream id {workstream!r}"
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
                risk_id = (entry or {}).get("risk_id")
                if risk_id not in risks:
                    errors.append(
                        f"remediation-inventory findings.{item_id}: unknown linked risk {risk_id!r}"
                    )
            else:
                for finding_id in (entry or {}).get("related_findings") or []:
                    if finding_id not in findings:
                        errors.append(
                            f"remediation-inventory risks.{item_id}: unknown linked finding {finding_id!r}"
                        )
            validate_artifact_refs(
                (entry or {}).get("remediation_artifacts") or [],
                label=f"remediation-inventory {collection_name}.{item_id}",
                workspace_root=workspace_root,
                errors=errors,
            )
            for artifact in (entry or {}).get("remediation_artifacts") or []:
                repo = artifact.get("repo")
                path = artifact.get("path")
                if isinstance(repo, str) and isinstance(path, str):
                    validate_change_record_linkage(
                        repo_name=repo,
                        rel_path=path,
                        item_id=item_id,
                        workstream_id=workstream,
                        collection_name=collection_name,
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
