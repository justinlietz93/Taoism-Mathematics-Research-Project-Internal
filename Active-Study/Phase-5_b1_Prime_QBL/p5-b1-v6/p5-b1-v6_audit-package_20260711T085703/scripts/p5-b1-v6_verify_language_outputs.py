#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
from collections import Counter
from pathlib import Path

STAMP = "20260711T083401"


def one(root: Path, suffix: str) -> Path:
    matches = list(root.rglob(f"*{suffix}"))
    if len(matches) != 1:
        raise RuntimeError(f"expected one *{suffix}, found {len(matches)}")
    return matches[0]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("root")
    ap.add_argument("--json-out")
    args = ap.parse_args()
    root = Path(args.root)

    complexity = list(csv.DictReader(one(root, "_word_complexity.csv").open()))
    complexity_checks = []
    for row in complexity:
        n = int(row["length"])
        actual = int(row["actual_affine_complexity"])
        complexity_checks.append(actual == 2 ** (n + 1) - 1)

    counts = Counter()
    with one(root, "_exact_cylinders_depth12.csv").open() as f:
        for row in csv.DictReader(f):
            counts[int(row["length"])] += 1
    direct_expected = {n: 2 ** (n + 1) - 1 for n in range(1, 13)}

    witnesses = list(csv.DictReader(one(root, "_exact_markov_order_counterexamples.csv").open()))
    witness_checks = []
    for row in witnesses:
        k = int(row["tested_order"])
        witness_checks.append(
            row["word_1"][-k:] == row["shared_suffix"] == row["word_2"][-k:]
            and row["extensions_1"] != row["extensions_2"]
            and row["certificate"] == "rational-affine endpoint comparison over outward a enclosure"
        )

    follower = list(csv.DictReader(one(root, "_boundary_adjacent_follower_pairs.csv").open()))
    follower_checks = [row["distinct_from_previous"] == "True" for row in follower]

    boundary = json.loads(one(root, "_finite_boundary_certificate.json").read_text())
    gap = float(boundary["minimum_boundary_distance_lower_bound"]["distance_lower_bound"])

    report = {
        "complexity_rows": len(complexity),
        "complexity_formula_checks": complexity_checks,
        "complexity_formula_pass": len(complexity) == 20 and all(complexity_checks),
        "direct_cylinder_counts": dict(sorted(counts.items())),
        "direct_cylinder_counts_pass": dict(counts) == direct_expected,
        "finite_markov_witnesses": len(witnesses),
        "finite_markov_witnesses_pass": len(witnesses) == 10 and all(witness_checks),
        "follower_boundary_rows": len(follower),
        "finite_follower_orbit_distinct_pass": len(follower) == 20 and all(follower_checks),
        "boundary_steps": boundary["certified_carry_steps"],
        "boundary_disjoint": boundary["all_E_A_boundary_disjoint_for_A_0_10000"],
        "minimum_boundary_gap": gap,
        "finite_boundary_pass": boundary["all_imported_carries_certified"] and boundary["certified_carry_steps"] == 10000 and boundary["all_E_A_boundary_disjoint_for_A_0_10000"] and gap > 0,
        "scope_note": "These checks reproduce finite outputs. They do not prove the missing all-n follower-set endpoint bridge.",
    }
    report["overall_pass"] = all([
        report["complexity_formula_pass"],
        report["direct_cylinder_counts_pass"],
        report["finite_markov_witnesses_pass"],
        report["finite_follower_orbit_distinct_pass"],
        report["finite_boundary_pass"],
    ])
    payload = json.dumps(report, indent=2, sort_keys=True) + "\n"
    print(payload, end="")
    if args.json_out:
        Path(args.json_out).write_text(payload)
    return 0 if report["overall_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
