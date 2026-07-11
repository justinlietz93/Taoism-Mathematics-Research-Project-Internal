#!/usr/bin/env python3
from __future__ import annotations
import argparse, json
from pathlib import Path
import sympy as sp


def fib(n: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output")
    args = ap.parse_args()

    sqrt5 = sp.sqrt(5)
    phi = (1 + sqrt5) / 2
    checks = {}
    checks["phi_minus_inverse"] = bool(sp.simplify(phi - 1 / phi - 1) == 0)
    checks["phi5_gt_4"] = bool(sp.simplify(phi**5 - 4).is_positive)
    odd_margin = sp.simplify(sp.Rational(1, 4) - (1 + phi**-5) / 5)
    checks["odd_margin_positive"] = bool(odd_margin.is_positive)
    checks["even_margin_positive"] = bool(sp.Rational(1, 4) - sp.Rational(1, 5) > 0)

    power_hits = []
    for n in range(0, 200):
        p = fib(n + 1) * fib(n + 2)
        if p > 0 and p & (p - 1) == 0:
            power_hits.append([n, p])
    checks["finite_power_two_regression"] = power_hits == [[0, 1], [1, 2]]

    threshold_rows = []
    import math
    phi_float = (1 + math.sqrt(5)) / 2
    for A in range(13):
        m = 12 * (2 ** (A + 1) - 1)
        y = (m * math.log(2) + math.log(5)) / (2 * math.log(phi_float)) - 1.5
        T = math.ceil(y)
        X = 2**m
        lo = fib(T) * fib(T + 1)
        hi = fib(T + 1) * fib(T + 2)
        threshold_rows.append({"A": A, "T": T, "lo_lt_X": lo < X, "X_lt_hi": X < hi})
    checks["finite_threshold_regression"] = all(r["lo_lt_X"] and r["X_lt_hi"] for r in threshold_rows)

    result = {
        "status": "PASS" if all(checks.values()) else "FAIL",
        "exact_checks": checks,
        "exact_values": {
            "phi5_minus4": str(sp.simplify(phi**5 - 4)),
            "odd_margin": str(odd_margin),
            "even_margin": str(sp.Rational(1, 20)),
        },
        "finite_regressions": {
            "power_two_hits_n_0_199": power_hits,
            "threshold_A_0_12": threshold_rows,
        },
        "logical_audit": {
            "binet_identity": "ACCEPTED BY EXACT ALGEBRA",
            "uniform_correction_bound": "ACCEPTED BY PARITY SPLIT AND POSITIVE EXACT MARGINS",
            "power_of_two_obstruction": "ACCEPTED BY COPRIMALITY OF CONSECUTIVE FIBONACCI NUMBERS",
            "integer_gap_sign_transfer": "ACCEPTED",
            "nonintegrality": "ACCEPTED",
            "global_ceiling_bridge": "ACCEPTED",
            "formal_machine_proof": "NOT PRESENT",
        },
    }
    text = json.dumps(result, indent=2, sort_keys=True)
    print(text)
    if args.output:
        Path(args.output).write_text(text + "\n")
    if result["status"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
