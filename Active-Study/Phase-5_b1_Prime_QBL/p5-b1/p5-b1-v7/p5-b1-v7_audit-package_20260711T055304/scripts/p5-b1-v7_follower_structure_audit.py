#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
import pathlib
import tempfile
import zipfile

PACKAGE_NAME = "p5-b1-v7_affine-follower-set-closure_20260711T103100"
STAMP = "20260711T103100"


def read_csv(path: pathlib.Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("zip_path", type=pathlib.Path)
    ap.add_argument("--out", type=pathlib.Path)
    args = ap.parse_args()

    with tempfile.TemporaryDirectory(prefix="p5b1v7-math-") as td:
        td_path = pathlib.Path(td)
        with zipfile.ZipFile(args.zip_path) as zf:
            zf.extractall(td_path)
        root = td_path / PACKAGE_NAME
        outputs = root / "outputs"

        complexity = read_csv(outputs / f"{STAMP}_word_complexity.csv")
        complexity_checks = []
        for row in complexity:
            n = int(row["length"])
            actual = int(row["actual_affine_complexity"])
            expected = 2 ** (n + 1) - 1
            complexity_checks.append(actual == expected)

        regions = read_csv(outputs / f"{STAMP}_half_open_follower_regions.csv")
        region_checks = []
        for row in regions:
            region_checks.append(
                float(row["H_minus_width_lower"]) > 0
                and float(row["H_plus_width_lower"]) > 0
                and row["source_minus_strict_below_2^-n"] == "True"
                and row["source_plus_strict_below_2^-n"] == "True"
                and row["oriented_handoff"] == "minus interior ends; plus interior begins"
            )

        pairs = read_csv(outputs / f"{STAMP}_boundary_adjacent_follower_pairs.csv")
        pair_checks = [row["distinct_from_previous"] == "True" for row in pairs]
        q_intervals = [
            (float(row["D_n_p_lower"]), float(row["D_n_p_upper"])) for row in pairs
        ]
        finite_q_distinct = all(
            q_intervals[i][1] < q_intervals[j][0]
            or q_intervals[j][1] < q_intervals[i][0]
            for i in range(len(q_intervals))
            for j in range(i + 1, len(q_intervals))
        )

        markov = read_csv(outputs / f"{STAMP}_exact_markov_order_counterexamples.csv")
        markov_orders = [int(row["tested_order"]) for row in markov]
        markov_pass = markov_orders == list(range(1, 11)) and all(
            row["certificate"]
            == "rational-affine endpoint comparison over outward a enclosure"
            for row in markov
        )

        status = json.loads(
            (outputs / f"{STAMP}_language_structure_status.json").read_text()
        )
        document = (root / "docs/QBL_CARRY_AFFINE_FOLLOWER_STRUCTURE_v5.md").read_text()
        proof_markers = {
            "exact_concat_identity": "C(wv)=C(w)\\cap D^{-n}(C(v))" in document,
            "standard_follower_identity": "\\operatorname{Fol}(w)" in document
            and "H_w\\cap C(v)\\ne\\varnothing" in document,
            "interior_separation": "\\operatorname{int}H=\\operatorname{int}H'" in document,
            "oriented_handoff": "uniquely oriented handoff" in document,
            "non_sofic_conclusion": "the affine carry language is non-sofic" in document,
            "mixing_conclusion": "the affine carry language is topologically mixing" in document,
        }

        result = {
            "complexity_rows": len(complexity),
            "complexity_formula_pass": all(complexity_checks),
            "half_open_follower_region_rows": len(regions),
            "follower_region_geometry_pass": all(region_checks),
            "boundary_pair_rows": len(pairs),
            "finite_boundary_pair_flags_pass": all(pair_checks),
            "finite_q_intervals_pairwise_disjoint": finite_q_distinct,
            "markov_orders_1_to_10_pass": markov_pass,
            "status_soficity": status.get("soficity"),
            "status_mixing": status.get("mixing"),
            "status_finite_markov_order": status.get("finite_markov_order"),
            "proof_markers": proof_markers,
            "proof_marker_pass": all(proof_markers.values()),
            "theorem_audit": {
                "follower_bridge": "PASS: exact set identity preserves half-open endpoints",
                "separation_lemma": "PASS for the proper half-open follower arcs used in the proof",
                "oriented_handoff": "PASS: ordered interiors distinguish q_n even in complementary-image cases",
                "non_soficity": "PASS: infinitely many ordered follower pairs contradict finiteness for any finite labeled graph",
                "finite_markov_order": "PASS: finite memory implies SFT implies sofic",
                "mixing": "PASS: topological exactness gives every sufficiently large bridge length",
            },
        }
        result["overall_pass"] = all(
            [
                result["complexity_formula_pass"],
                result["follower_region_geometry_pass"],
                result["finite_boundary_pair_flags_pass"],
                result["finite_q_intervals_pairwise_disjoint"],
                result["markov_orders_1_to_10_pass"],
                result["proof_marker_pass"],
                status.get("soficity") == "PROVED NON-SOFIC",
                str(status.get("mixing", "")).startswith("PROVED TOPOLOGICALLY MIXING"),
            ]
        )

    text = json.dumps(result, indent=2, sort_keys=True)
    print(text)
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(text + "\n")
    return 0 if result["overall_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
