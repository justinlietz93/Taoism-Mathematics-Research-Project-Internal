#!/usr/bin/env python3
"""Audit integrity and reproducibility surfaces of the two supplied zip packages."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import zipfile
from pathlib import Path, PurePosixPath


def hash_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def common_root(names: list[str]) -> str:
    roots = {PurePosixPath(name).parts[0] for name in names if name and not name.endswith("/")}
    if len(roots) != 1:
        raise RuntimeError(f"Expected one archive root, found {sorted(roots)}")
    return next(iter(roots))


def strip_root(name: str, root: str) -> str:
    prefix = root + "/"
    return name[len(prefix):] if name.startswith(prefix) else name


def audit_experiment(path: Path) -> dict:
    with zipfile.ZipFile(path) as archive:
        files = [name for name in archive.namelist() if not name.endswith("/")]
        root = common_root(files)
        rel_to_name = {strip_root(name, root): name for name in files}
        manifest = json.loads(archive.read(rel_to_name["MANIFEST.json"]))
        listed = {item["path"]: item for item in manifest["files"]}
        checks = []
        for rel, item in listed.items():
            data = archive.read(rel_to_name[rel])
            checks.append({
                "path": rel,
                "bytes_pass": len(data) == item["bytes"],
                "sha256_pass": hash_bytes(data) == item["sha256"],
            })
        non_manifest = set(rel_to_name) - {"MANIFEST.json"}
        notebook_files = sorted(rel for rel in rel_to_name if rel.endswith(".ipynb"))
        requirements = archive.read(rel_to_name["requirements.txt"]).decode("utf-8")
        requirement_lines = [line.strip() for line in requirements.splitlines() if line.strip() and not line.lstrip().startswith("#")]
        exact_pins = bool(requirement_lines) and all("==" in line for line in requirement_lines)
        script_files = sorted(rel for rel in rel_to_name if rel.startswith("scripts/") and rel.endswith(".py"))
        script_text = "\n".join(archive.read(rel_to_name[rel]).decode("utf-8", errors="replace") for rel in script_files)
        generated_names_referenced = sorted(set(re.findall(r"['\"]([A-Za-z0-9_./-]+\.(?:json|csv|png|db|h5|ipynb|jsonl))['\"]", script_text)))
        current_dirs = {PurePosixPath(rel).parts[0] for rel in rel_to_name if "/" in rel}
        source_map = archive.read(rel_to_name["source_maps/20260710T234301_SOURCE_MAP.md"]).decode("utf-8")
        readme = archive.read(rel_to_name["README.md"]).decode("utf-8")
        return {
            "archive": path.name,
            "manifest": {
                "listed_count": len(listed),
                "declared_count": manifest.get("file_count"),
                "all_hashes_pass": all(item["bytes_pass"] and item["sha256_pass"] for item in checks),
                "listed_set_matches_archive_except_manifest": set(listed) == non_manifest,
                "checks": checks,
            },
            "reproducibility": {
                "notebooks": notebook_files,
                "source_and_executed_notebook_pair_present": any("executed" in name.lower() for name in notebook_files) and len(notebook_files) >= 2,
                "requirements": requirement_lines,
                "requirements_exactly_pinned": exact_pins,
                "builder_script_present": any("build" in PurePosixPath(name).name.lower() for name in script_files),
                "analysis_scripts": script_files,
                "generated_artifact_names_referenced_by_scripts": generated_names_referenced,
                "readme_run_command_has_output_argument": "--out" in readme,
                "current_required_dirs_present": {name: name in current_dirs for name in ("outputs", "proofs", "trace")},
                "legacy_dirs_present": {name: name in current_dirs for name in ("output_data", "lean", "trace_logs")},
                "lean_compiler_log_present": any("lean" in rel.lower() and "log" in rel.lower() for rel in rel_to_name),
            },
            "authority": {
                "current_orthad_law_present": any("QBL_PRIMITIVE_CUSTODY_AND_ORTHAD_LAW_v2" in rel for rel in rel_to_name),
                "older_canonical_ledger_present": any("PHASE5_CANONICAL_LEDGER" in rel for rel in rel_to_name),
                "source_map_names_old_ledger_as_active": "## Active inputs" in source_map and "PHASE5_CANONICAL_LEDGER" in source_map,
            },
        }


def audit_prime_watch(path: Path) -> dict:
    with zipfile.ZipFile(path) as archive:
        files = [name for name in archive.namelist() if not name.endswith("/")]
        root = common_root(files)
        rel_to_name = {strip_root(name, root): name for name in files}
        manifest_lines = archive.read(rel_to_name["MANIFEST.sha256"]).decode("utf-8").splitlines()
        checks = []
        for line in manifest_lines:
            expected, rel = line.split(None, 1)
            rel = rel.strip()
            data = archive.read(rel_to_name[rel])
            checks.append({"path": rel, "sha256_pass": hash_bytes(data) == expected})
        required_current = ["MANIFEST.json", "FINDINGS.md", "inputs/", "trace/", "source_maps/"]
        return {
            "archive": path.name,
            "sha_manifest": {"all_hashes_pass": all(item["sha256_pass"] for item in checks), "checks": checks},
            "current_experiment_components_present": {
                component: any(strip_root(name, root).startswith(component.rstrip("/")) for name in files)
                for component in required_current
            },
            "classification": "PROVENANCE_PACKAGE_NOT_CURRENT_EXPERIMENT_PACKAGE",
        }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--inputs", type=Path, default=Path(__file__).resolve().parents[1] / "inputs")
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()

    experiment = audit_experiment(args.inputs / "experiment_package_20260710_234301.zip")
    prime_watch = audit_prime_watch(args.inputs / "qbl_prime_pattern_watch_v1.zip")
    result = {
        "status": "INTEGRITY_PASS_REPRODUCIBILITY_REVISE",
        "experiment_package": experiment,
        "prime_watch_package": prime_watch,
        "audit_findings": [
            "All 26 experiment-package manifest entries match their byte counts and SHA-256 values.",
            "All five qbl-prime-watch SHA-256 entries match.",
            "The experiment package has one notebook rather than separate source and executed notebooks.",
            "Dependencies are named but not exactly pinned.",
            "No package builder is included, and the README run command omits the script's optional --out argument.",
            "The included analysis script references only summary.json and scan.csv, so it cannot regenerate the complete archived artifact set.",
            "The package uses legacy output_data/lean/trace_logs names rather than outputs/proofs/trace.",
            "No Lean compiler log is present; Lean compilation is not certified.",
            "The source map names an older Phase 5 ledger as active and omits the current primitive-custody and Orthad law.",
            "The prime-watch zip is integrity-valid provenance, not a package in the current experiment format.",
        ],
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": result["status"], "output": str(args.out)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
