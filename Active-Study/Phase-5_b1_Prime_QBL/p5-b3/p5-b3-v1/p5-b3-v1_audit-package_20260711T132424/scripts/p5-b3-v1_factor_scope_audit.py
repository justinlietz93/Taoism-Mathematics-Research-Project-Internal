#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

import mpmath as mp
import sympy as sp


def capacity(j: int) -> int:
    if j == 1:
        return 2
    if j == 2:
        return 4
    return 2 ** (2 * j)


def threshold(A: int) -> int:
    mp.mp.dps = 200
    phi = (1 + mp.sqrt(5)) / 2
    y = (
        12 * (2 ** (A + 1) - 1) * mp.log(2) + mp.log(5)
    ) / (2 * mp.log(phi)) - mp.mpf(3) / 2
    return int(mp.ceil(y))


def simulate_domains(max_A: int) -> list[dict[str, object]]:
    A = 0
    u, v = 1, 1
    k = 0
    j = 1
    b_count = 0
    theta_quarters = 0
    word: list[str] = []
    rows: list[dict[str, object]] = []

    while A <= max_A:
        N = 6 * 2 ** A
        next_u, next_v = v, u + v
        if k < N - 1:
            can_b = next_u * next_v <= capacity(j)
        else:
            can_b = u * v < capacity(j)
        if can_b:
            u, v = next_u, next_v
            b_count += 1
            word.append("B")
            continue
        if k < N - 1:
            k += 1
            j += 1
            theta_quarters += 1
            word.append("Q")
            continue

        # pre-L boundary
        T = threshold(A)
        rows.append({
            "A": A,
            "j": j,
            "expected_J": 6 * (2 ** (A + 1) - 1),
            "b_count": b_count,
            "expected_T": T,
            "pair_u": str(u),
            "pair_v": str(v),
            "product_ge_capacity": u * v >= capacity(j),
            "prefix_length": len(word),
            "expected_prefix_length": b_count + j - 1,
            "theta_quarters": theta_quarters,
        })
        word.append("L")
        A += 1
        if A > max_A:
            break
        k = 0
        j += 1

    return rows


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    lam, beta, j, b, c = sp.symbols("lambda beta j b c", real=True)
    gamma = 6 * lam - beta
    pi = lam * j + beta - b
    pi_next = lam * (2 * j + 6) + beta - (2 * b + c)
    residual = sp.simplify(pi_next - (2 * pi + gamma - c))

    rows = simulate_domains(6)
    simulation_pass = all(
        row["j"] == row["expected_J"]
        and row["b_count"] == row["expected_T"]
        and row["product_ge_capacity"]
        and row["prefix_length"] == row["expected_prefix_length"]
        for row in rows
    )

    result = {
        "symbolic_factor_residual": str(residual),
        "symbolic_commutation_pass": residual == 0,
        "finite_custody_simulation": rows,
        "finite_custody_simulation_pass": simulation_pass,
        "proved_strength": {
            "canonical_boundary_state_internal_coordinate": True,
            "canonical_orbit_semiconjugacy": True,
            "carry_cocycle_from_successive_boundary_states": True,
            "full_affine_interval_factor": False,
            "full_affine_language_factor": False,
        },
        "factor_scope_reason": (
            "The packaged map is defined and proved on the canonical countable boundary orbit "
            "S_A^- and lands on the corresponding countable affine orbit E_A. It is not a "
            "surjective map onto the full interval coding system, and no equality between the "
            "canonical carry-word language and the full affine language is proved."
        ),
        "higher_order_L_audit": {
            "literal_carry_coordinate_appended_at_instantaneous_L": "FALSE",
            "boundary_return_arithmetic_cocycle": "PROVED",
            "higher_order_descriptive_L_identity": "NOT YET DERIVED",
            "agent_independent_extension_verdict": "UNSUPPORTED_FAIL",
            "reason": (
                "The carry needs two boundary states and is not appended at S_A^+. But algebraic "
                "derivability is not the same as absence of a new independent retained distinction. "
                "The open primary-pairing/chart/transfer recurrence is exactly where such a distinction "
                "would have to be tested."
            ),
        },
        "hierarchy_count_alignment": "J_A = 6 p(A) is exact; active-depth recurrence remains count alignment only.",
        "branch_status": "NOT YET CLOSED",
        "recommended_next_step": "p5-b3-v2",
    }
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if simulation_pass and residual == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
