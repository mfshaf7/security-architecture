#!/usr/bin/env python3
"""Render a generated index of security-tagged owner change records."""

from __future__ import annotations

import argparse
from pathlib import Path
import re
import sys

import yaml


CHANGE_RECORD_NAME_RE = re.compile(r"^\d{4}-\d{2}-\d{2}-[a-z0-9-]+\.md$")
DATE_RE = re.compile(r"^- Date:\s*(.+)$", re.MULTILINE)
TITLE_RE = re.compile(r"^- Short title:\s*(.+)$", re.MULTILINE)


def parse_front_matter(path: Path) -> tuple[dict, str]:
    text = path.read_text()
    if not text.startswith("---\n"):
        return {}, text
    parts = text.split("\n---\n", 1)
    if len(parts) != 2:
        return {}, text
    return yaml.safe_load(parts[0][4:]) or {}, parts[1]


def scan_security_change_records(workspace_root: Path) -> dict:
    records: list[dict] = []
    for repo_root in sorted(path for path in workspace_root.iterdir() if path.is_dir() and (path / ".git").exists()):
        records_dir = repo_root / "docs" / "records" / "change-records"
        if not records_dir.exists():
            continue
        for path in sorted(records_dir.glob("*.md")):
            if path.name in {"README.md", "TEMPLATE.md"}:
                continue
            if not CHANGE_RECORD_NAME_RE.fullmatch(path.name):
                continue
            metadata, body = parse_front_matter(path)
            security_evidence = metadata.get("security_evidence") or {}
            if not security_evidence:
                continue
            date_match = DATE_RE.search(body)
            title_match = TITLE_RE.search(body)
            records.append(
                {
                    "repo": repo_root.name,
                    "path": str(path.relative_to(repo_root)),
                    "date": date_match.group(1).strip() if date_match else path.name[:10],
                    "short_title": title_match.group(1).strip() if title_match else path.stem,
                    "review_areas": security_evidence.get("review_areas") or [],
                    "findings": security_evidence.get("findings") or [],
                    "risks": security_evidence.get("risks") or [],
                    "workstreams": security_evidence.get("workstreams") or [],
                }
            )
    return {"schema_version": 1, "change_records": records}


def rendered_text(workspace_root: Path) -> str:
    return yaml.safe_dump(scan_security_change_records(workspace_root), sort_keys=False)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--workspace-root")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    workspace_root = (
        Path(args.workspace_root).resolve()
        if args.workspace_root
        else repo_root.parent
    )
    target = repo_root / "registers" / "security-change-record-index.yaml"
    expected = rendered_text(workspace_root)

    if args.check:
        if not target.exists():
            print(f"ERROR: missing generated change-record index: {target}")
            return 1
        if target.read_text() != expected:
            print(f"ERROR: generated change-record index out of date: {target}")
            return 1
        print("generated security change-record index is current")
        return 0

    target.write_text(expected)
    print(f"rendered {target}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
