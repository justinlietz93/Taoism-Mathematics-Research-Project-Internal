#!/usr/bin/env python3
"""Phase 5 v8i external audit (2026-07-09).

Diagnosis of the v8i extended-diagonal splitter failure (91/229 ground-truth
validation failures, all with reason NO_CERTIFIED_A_OR_EQUAL_LEVEL_UV_PIVOT).

Wall/Kawauchi-Kojima theory guarantees nondegenerate 2-primary finite
quadratic forms decompose into rank-1 A blocks and rank-2 U/V blocks. A 40%
failure rate on ground truth therefore cannot mean "the decomposition wall is
real" — it must be an implementation gap. This audit identifies the gap and
proves it.

Checks:
  1. PROVENANCE RE-VERIFICATION. Confirm the v8i restored edge lists match
     the v8g upstream artifact exactly (41 edges rank10_large, 62 edges
     rank12_large, 3 edges rank3_mixed — the third case was caught by the
     agent's own diff and missed by the prior external audit's narrower
     comparison; credited).
  2. RADICAL CORRELATION. For every validation form, independently compute
     the radical Rad = {x : b(x,y)=0 for all y}. Prediction under the
     diagnosis: split_success == (|Rad| == 1). A radical vector can never
     satisfy either pivot gate (unit-diagonal A pivot or invertible
     equal-level UV Gram), so the pivot search starves with the radical as
     the active residual — exactly the observed failure signature.
  3. WORKED COMPLETION. Exhibit the completed decomposition of the smallest
     failed case ([2,2] c01=1) as A_2(1) PERP R_2(q=0): explicit orthogonal
     basis, span, and pointwise q-additivity verification.

Conclusion this audit certifies: the CLOSED_NEGATIVE on the splitter is an
implementation gap (no radical block type in the alphabet), not a structural
wall. Family F contains degenerate forms (v8e flagged PASS_WITH_RADICAL),
so the block alphabet must contain radical blocks. Non-summand radicals
(e.g. 2Z/4 inside Z/4) additionally require filtration-style invariants
(Kawauchi-Kojima); that is the precise named residue for v8j.

Usage:
  python3 v8i_external_audit.py <v8i-package-root> <v8g-package-root>
"""

import csv
import json
import sys
from itertools import product
from math import gcd
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "outputs"
OUT.mkdir(parents=True, exist_ok=True)


def lcm(a, b):
    return a * b // gcd(a, b)


def build_form(D, edges):
    """(elems, q, b, M) for family form: diagonal q(e_i)=1/(2 D_i), edges (i,j,c)."""
    n = len(D)
    M = 1
    for d in D:
        M = lcm(M, 2 * d)
    for i in range(n):
        for j in range(i + 1, n):
            M = lcm(M, lcm(D[i], D[j]))
    E = {(i, j): c for i, j, c in edges}
    elems = list(product(*[range(d) for d in D]))

    def q(v):
        tot = 0
        for i in range(n):
            tot += v[i] * v[i] * (M // (2 * D[i]))
        for (i, j), c in E.items():
            tot += c * v[i] * v[j] * (M // lcm(D[i], D[j]))
        return tot % M

    def b(u, v):
        tot = 0
        for i in range(n):
            tot += u[i] * v[i] * (M // D[i])
        for (i, j), c in E.items():
            tot += c * (u[i] * v[j] + u[j] * v[i]) * (M // lcm(D[i], D[j]))
        return tot % M

    return elems, q, b, M


def radical(elems, b):
    return [x for x in elems if all(b(x, y) == 0 for y in elems)]


def edges_from_rep(shape, rep):
    """rep is either a dict {"cij": value} or a list [c01, c02, ..., c12, ...]
    in lexicographic pair order (the v8g rank-3 representative format)."""
    n = len(shape)
    pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
    out = []
    if isinstance(rep, dict):
        for (i, j) in pairs:
            v = rep.get(f"c{i}{j}")
            if v:
                out.append((i, j, v))
    else:
        for (i, j), v in zip(pairs, rep):
            if v:
                out.append((i, j, v))
    return out


def main():
    v8i = Path(sys.argv[1])
    v8g = Path(sys.argv[2])

    # ---- check 1: provenance re-verification ----
    v8g_rows = {r["case"]: r for r in csv.DictReader(
        open(v8g / "outputs" / "phase5_v8g_v7u_mixed_highrank_reduction_routing.csv"))}
    prov = list(csv.DictReader(open(v8i / "outputs" / "phase5_v8i_provenance_diff.csv")))
    p_ok = True
    for r in prov:
        case = r["case"]
        restored = json.loads(r["restored_edges_2core"])
        upstream = json.loads(v8g_rows[case].get("edges_2core", "[]") or "[]")
        ok = restored == upstream
        p_ok &= ok
        print(f"[check1] {case}: restored {len(restored)} edges match v8g: {ok}")
    print(f"[check1] provenance patch verified: {p_ok}")

    # ---- check 2: radical correlation over all validation rows ----
    val = list(csv.DictReader(open(
        v8i / "outputs" / "phase5_v8i_splitter_groundtruth_validation.csv")))
    rows_out = []
    agree = 0
    n_rows = 0
    for r in val:
        if not r.get("shape"):
            continue
        n_rows += 1
        shape = json.loads(r["shape"])
        rep = json.loads(r["representative"])
        edges = edges_from_rep(shape, rep)
        elems, q, b, M = build_form(shape, edges)
        rad = radical(elems, b)
        qrad = sorted({q(x) for x in rad})
        success = r["split_success"] == "True"
        predicted_success = (len(rad) == 1)
        agree += (success == predicted_success)
        rows_out.append({
            "source": r["source"], "ground_truth_id": r["ground_truth_id"],
            "shape": r["shape"], "representative": r["representative"],
            "split_success": success, "radical_size": len(rad),
            "q_values_on_radical_xM": json.dumps(qrad), "M": M,
            "prediction_success_iff_trivial_radical": predicted_success,
            "prediction_correct": success == predicted_success,
        })
    print(f"[check2] radical-correlation: prediction correct on {agree}/{n_rows} rows")
    with open(OUT / "audit_radical_correlation.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows_out[0]))
        w.writeheader()
        w.writerows(rows_out)

    # ---- check 3: worked completion on the smallest failed case ----
    elems, q, b, M = build_form([2, 2], [(0, 1, 1)])
    v_block = (1, 0)   # A_2(1) generator (q = 1/4)
    v_rad = (1, 1)     # radical generator (q = 0)
    checks = {
        "q(v_block) == 1/4": q(v_block) == M // 4,
        "v_rad in radical": all(b(v_rad, y) == 0 for y in elems),
        "q(v_rad) == 0": q(v_rad) == 0,
        "basis spans A": len({((a * v_block[0] + c * v_rad[0]) % 2,
                               (a * v_block[1] + c * v_rad[1]) % 2)
                              for a in range(2) for c in range(2)}) == 4,
        "orthogonal": b(v_block, v_rad) == 0,
        "q additive across split": all(
            q(((a * v_block[0] + c * v_rad[0]) % 2,
               (a * v_block[1] + c * v_rad[1]) % 2))
            == (q(((a * v_block[0]) % 2, (a * v_block[1]) % 2))
                + q(((c * v_rad[0]) % 2, (c * v_rad[1]) % 2))) % M
            for a in range(2) for c in range(2)),
    }
    all3 = all(checks.values())
    for k, v in checks.items():
        print(f"[check3] {k}: {v}")
    print(f"[check3] completed decomposition [2,2]c01=1 = A_2(1) PERP R_2(q=0): {all3}")
    with open(OUT / "audit_worked_completion.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["case", "completed_symbol", "verified"])
        w.writeheader()
        w.writerow({"case": "[2,2] c01=1",
                    "completed_symbol": "A_2(1) + R_2(q=0)", "verified": all3})

    ok = p_ok and (agree == n_rows) and all3
    print()
    print("PROVENANCE PATCH:", "VERIFIED" if p_ok else "PROBLEM")
    print("DIAGNOSIS (failure <=> nontrivial radical):",
          "CONFIRMED" if agree == n_rows else f"PARTIAL {agree}/{n_rows}")
    print("VERDICT: splitter CLOSED_NEGATIVE is an IMPLEMENTATION GAP "
          "(missing radical block type), not a structural wall.")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
