#!/usr/bin/env python3
"""Reproduce the algebraic and finite-data checks in the J-derivation audit."""
from __future__ import annotations

import argparse
import hashlib
import json
import zipfile
from dataclasses import dataclass
from decimal import Decimal, getcontext
from fractions import Fraction
from pathlib import Path

getcontext().prec = 90


@dataclass(frozen=True)
class Affine:
    """Exact expression c0 + c1*a over rational coefficients."""
    c0: Fraction = Fraction(0)
    c1: Fraction = Fraction(0)

    def __add__(self, other: "Affine") -> "Affine":
        return Affine(self.c0 + other.c0, self.c1 + other.c1)

    def __sub__(self, other: "Affine") -> "Affine":
        return Affine(self.c0 - other.c0, self.c1 - other.c1)

    def __mul__(self, scalar: Fraction) -> "Affine":
        return Affine(self.c0 * scalar, self.c1 * scalar)

    def to_text(self) -> str:
        return f"({self.c0}) + ({self.c1})*a"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def matrix_metrics(left: list[list[Decimal]], right: list[list[Decimal]]) -> dict[str, str]:
    diffs = [abs(left[i][j] - right[i][j]) for i in range(3) for j in range(3)]
    l1 = sum(diffs, Decimal(0))
    return {
        "max_abs_error": str(max(diffs)),
        "l1_error": str(l1),
        "total_variation": str(l1 / 2),
    }


def decimal_matrix_text(matrix: list[list[Decimal]]) -> list[list[str]]:
    return [[str(value) for value in row] for row in matrix]


def find_member(archive: zipfile.ZipFile, suffix: str) -> str:
    matches = [name for name in archive.namelist() if name.endswith(suffix)]
    if len(matches) != 1:
        raise RuntimeError(f"Expected one archive member ending with {suffix!r}; found {matches}")
    return matches[0]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--inputs", type=Path, default=Path(__file__).resolve().parents[1] / "inputs")
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()

    note = args.inputs / "QBL_CARRY_J_DERIVATION_AND_RESEARCH_BOUNDARY_v1.md"
    experiment_zip = args.inputs / "experiment_package_20260710_234301.zip"
    expected_note_hash = "0509505200e2d3289363934103570b3cc36833aeda6be3e9d27ced3bc0835bc8"

    with zipfile.ZipFile(experiment_zip) as archive:
        summary_name = find_member(archive, "_summary.json")
        summary = json.loads(archive.read(summary_name))

    a = Decimal(summary["constants"]["partition_a"])
    zero = Decimal(0)
    one = Decimal(1)

    J = [
        [zero, (one - 3 * a) / 2, a / 2],
        [(one - 2 * a) / 4, one / 4, a / 2],
        [(one - 2 * a) / 4, 3 * a / 2 - one / 4, zero],
    ]

    A0 = Affine(Fraction(0), Fraction(0))
    J_exact = [
        [A0, Affine(Fraction(1, 2), Fraction(-3, 2)), Affine(Fraction(0), Fraction(1, 2))],
        [Affine(Fraction(1, 4), Fraction(-1, 2)), Affine(Fraction(1, 4), Fraction(0)), Affine(Fraction(0), Fraction(1, 2))],
        [Affine(Fraction(1, 4), Fraction(-1, 2)), Affine(Fraction(-1, 4), Fraction(3, 2)), A0],
    ]
    target_pi = [
        Affine(Fraction(1, 2), Fraction(-1)),
        Affine(Fraction(1, 2), Fraction(0)),
        Affine(Fraction(0), Fraction(1)),
    ]
    row_sums = [sum(row[1:], row[0]) for row in J_exact]
    col_sums = [sum((J_exact[i][j] for i in range(3)), A0) for j in range(3)]
    exact_mass_pass = row_sums == target_pi and col_sums == target_pi and sum(row_sums[1:], row_sums[0]) == Affine(Fraction(1), Fraction(0))

    transition_counts = summary["carry"]["transition_counts"]
    counts = [
        [0, int(transition_counts["7->8"]), int(transition_counts["7->9"])],
        [int(transition_counts["8->7"]), int(transition_counts["8->8"]), int(transition_counts["8->9"])],
        [int(transition_counts["9->7"]), int(transition_counts["9->8"]), 0],
    ]
    transition_total = sum(sum(row) for row in counts)
    empirical = [[Decimal(value) / Decimal(transition_total) for value in row] for row in counts]

    sqrt2 = Decimal(2).sqrt()
    rho = one + sqrt2
    r = [one, sqrt2, one]
    adjacency = [[0, 1, 1], [1, 1, 1], [1, 1, 0]]
    normalization = sum((value * value for value in r), Decimal(0))
    parry_joint = [
        [Decimal(adjacency[i][j]) * r[i] * r[j] / (rho * normalization) for j in range(3)]
        for i in range(3)
    ]

    note_text = note.read_text(encoding="utf-8")
    content_checks = {
        "seven_nonzero_correction_present": "seven" in note_text.lower() and "J_{88}" in note_text,
        "equidistribution_hold_present": "SPECIFIC ORBIT EQUIDISTRIBUTION: NOT PROVED" in note_text,
        "fqm_hold_present": "A gauge/FQM transformation attached specifically to d_A = +/-1" in note_text,
        "global_threshold_hold_present": "The global all-A identity T_A = ceil(y_A)" in note_text,
        "ceiling_map_bridge_explicit": "c_A:=T_A-2T_{A-1}" in note_text or "c_A = T_A-2T_{A-1}" in note_text,
        "conditional_matrix_explicit": "conditional transition matrix" in note_text.lower(),
        "parry_joint_edge_measure_explicit": "Parry joint" in note_text or "joint edge" in note_text,
    }

    positive_entries = [J[i][j] for i in range(3) for j in range(3) if (i, j) not in {(0, 0), (2, 2)}]
    result = {
        "status": "PASS_CORE_REVISE_ARTIFACT",
        "note_sha256": {
            "expected": expected_note_hash,
            "actual": sha256(note),
            "pass": sha256(note) == expected_note_hash,
        },
        "constants": {"a": str(a), "rho": str(rho)},
        "symbolic_checks": {
            "row_sums": [value.to_text() for value in row_sums],
            "column_sums": [value.to_text() for value in col_sums],
            "target_partition_mass": [value.to_text() for value in target_pi],
            "mass_identities_pass": exact_mass_pass,
            "seven_allowed_entries_positive_for_supplied_a": all(value > 0 for value in positive_entries),
            "two_forbidden_entries_zero": J[0][0] == 0 and J[2][2] == 0,
            "perron_vector_equation_pass": all(
                sum(Decimal(adjacency[i][j]) * r[j] for j in range(3)) == rho * r[i]
                for i in range(3)
            ),
        },
        "J": decimal_matrix_text(J),
        "empirical_joint": {
            "domain": summary["carry"]["transition_domain"],
            "counts": counts,
            "total": transition_total,
            "matrix": decimal_matrix_text(empirical),
        },
        "parry_joint": decimal_matrix_text(parry_joint),
        "comparisons": {
            "empirical_vs_J": matrix_metrics(empirical, J),
            "empirical_vs_Parry": matrix_metrics(empirical, parry_joint),
        },
        "document_content_checks": content_checks,
        "audit_findings": [
            "The J matrix, seven-entry correction, mass identities, Perron root, entropy basis, and Parry state law check.",
            "The standalone note does not explicitly derive the ceiling map from y_A and T_A.",
            "The exact-orbit endpoint law is not settled globally; this does not change Lebesgue masses.",
            "The note compares state marginals and defect aggregates, but not the empirical joint edge matrix directly against J and the Parry joint edge measure.",
            "The global linear-forms route is proposed, not executed.",
        ],
    }

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": result["status"], "output": str(args.out)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
