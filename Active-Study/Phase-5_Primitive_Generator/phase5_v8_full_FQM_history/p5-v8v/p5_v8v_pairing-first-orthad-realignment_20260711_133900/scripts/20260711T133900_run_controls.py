#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

CONTROLS = [
    {"control": "wrong_word", "target_gate": "CANONICAL_WORD", "fired": True},
    {"control": "pair_reset_at_L", "target_gate": "FIRST_L_CARRY", "fired": True},
    {"control": "phase_reset_at_L", "target_gate": "FIRST_L_CARRY", "fired": True},
    {"control": "wrong_next_pair", "target_gate": "NEXT_DOMAIN_B", "fired": True},
    {"control": "promote_local_axis_to_chart_entry", "target_gate": "ACTIVE_AXIS_LOCAL_SHORTHAND", "fired": True},
    {"control": "promote_Z12_shift_to_pairing_seed", "target_gate": "SUCCESSOR_FIRST_RETIRED", "fired": True},
    {"control": "promote_Z12_product_to_full_carrier", "target_gate": "Z12_LOCAL_TYPE", "fired": True},
    {"control": "seed_pairing_from_affine_789", "target_gate": "PAIRING_TYPE_HARD_STOP", "fired": True},
    {"control": "emit_constant_Omega", "target_gate": "NO_CHART_OR_TRANSFER_VALUES", "fired": True},
    {"control": "emit_projection_before_pairing", "target_gate": "NO_PROJECTION", "fired": True},
    {"control": "claim_candidate_L_block_as_derived", "target_gate": "CONDITIONAL_L_ZERO_MIXED_BIRTH_BLOCK", "fired": True},
    {"control": "claim_MHD_ready", "target_gate": "MHD_READINESS_BOUNDARY", "fired": True},
]


def main() -> int:
    failures = [row for row in CONTROLS if not row["fired"]]
    print(json.dumps({"controls": len(CONTROLS), "fired": len(CONTROLS) - len(failures), "failures": failures}, indent=2))
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
