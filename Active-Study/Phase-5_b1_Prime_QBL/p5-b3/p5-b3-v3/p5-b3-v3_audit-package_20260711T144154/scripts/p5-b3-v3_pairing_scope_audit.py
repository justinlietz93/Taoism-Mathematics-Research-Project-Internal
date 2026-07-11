#!/usr/bin/env python3
from __future__ import annotations
import json
from fractions import Fraction

WORD = "BQQBBBQBQBBQBBL"

def local_trace():
    u = v = 1
    q_count = 0
    rows = []
    for index, op in enumerate(WORD, 1):
        if op == "B":
            u, v = v, u + v
        elif op == "Q":
            q_count += 1
        rows.append({"index": index, "op": op, "u": u, "v": v, "q_count": q_count})
    return rows

def main():
    rows = local_trace()
    pre_l = rows[-2]
    accepted = {
        "word": WORD,
        "pre_L_pair": [pre_l["u"], pre_l["v"]],
        "Q_count": pre_l["q_count"],
        "active_witness": "i/4895",
        "local_trace_pass": [pre_l["u"], pre_l["v"], pre_l["q_count"]] == [55, 89, 5],
        "B_local_ratio": "u/(u+v)",
        "Q_local_ratio": "i"
    }
    findings = {
        "verdict": "REVISE_SCOPE",
        "adopt": [
            "exact pairing type not yet derived",
            "exact seed not yet derived",
            "exact B/Q/L value recurrence not yet derived",
            "local B and Q active-axis recurrences",
            "first-domain active witness i/4895",
            "branch remains open"
        ],
        "revise": {
            "duality_morphism": "candidate realization, not necessity theorem",
            "earliest_missing_law": "PRIMARY_PAIRING_REALIZATION_AXIOM, not scalar variance alone",
            "seed_witness": "proves type ambiguity, not same-type seed nonuniqueness",
            "L_mixed_blocks": "both zero only under two-sided P-orthogonality or sufficient symmetry/adjoint assumptions",
            "lean_scope": "declarations and conditional lemmas, not derivation from authority"
        },
        "logical_dependencies": [
            "carrier/coefficient/codomain",
            "duality or adjoint operation",
            "linearity/additivity",
            "scalar variance",
            "symmetry/adjoint law",
            "rank and orthogonality",
            "seed",
            "B/Q/L value laws"
        ],
        "accepted_local_checks": accepted
    }
    print(json.dumps(findings, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
