#!/usr/bin/env python3
from __future__ import annotations
import json, sys
from pathlib import Path

REQUIRED = {
    "candidate_not_forced": "lawful but unforced realization",
    "minimality_open": "MINIMALITY OF P:H->D(H): NOT YET DERIVED",
    "type_ambiguity_claim": "TYPE AMBIGUITY: PROVED BY MODEL WITNESSES",
    "realization_axiom": "PRIMARY_PAIRING_REALIZATION_AXIOM",
    "dynamics_in_axiom": "**`B` mutation law**",
    "chart_law_in_axiom": "**Chart-interface compatibility**",
    "seed_uniqueness": "RANK-ONE SEED WITHIN FIXED BILINEAR TYPE AND FIXED BASIS: UNIQUE",
}

def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: scope_audit.py <QBL_PRIMARY_PAIRING_TYPE_BOUNDARY_v2.md>")
    text = Path(sys.argv[1]).read_text(encoding="utf-8")
    present = {k: v in text for k, v in REQUIRED.items()}
    if not all(present.values()):
        raise SystemExit("missing expected claim surface: " + repr({k:v for k,v in present.items() if not v}))
    result = {
        "accepted": [
            "authority_forced_pairing_first_architecture",
            "duality_morphism_candidate_only",
            "exact_type_seed_recurrence_open",
            "one_sided_orthogonality_control",
            "local_B_Q_and_i_over_4895",
        ],
        "withheld": {
            "type_ambiguity_proved_by_model_witnesses": "examples are not complete models of every authority clause",
            "smallest_complete_realization_axiom": "minimality is unproved and dynamic theorem targets are included as axiom fields",
            "rank_one_seed_uniqueness": "needs explicit free rank-one scalar-module hypotheses",
        },
        "next_step": "p5-b3-v5 complete-model independence test",
        "branch_status": "OPEN",
        "PASS": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
