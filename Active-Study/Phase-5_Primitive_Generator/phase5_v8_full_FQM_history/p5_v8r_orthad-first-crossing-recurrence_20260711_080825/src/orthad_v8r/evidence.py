from __future__ import annotations

from .engine import StepRecord

EXPECTED_WORD = "BQQBBBQBQBBQBBL"
EXPECTED_NEXT_WORD = EXPECTED_WORD + "B"


def first_l_index(records: list[StepRecord]) -> int:
    for idx, record in enumerate(records):
        if record.primitive == "L":
            return idx
    raise ValueError("trace has no L")


def snapshots(records: list[StepRecord]) -> dict[str, dict[str, object]]:
    idx = first_l_index(records)
    return {
        "before_first_L": records[idx].before,
        "immediately_after_first_L": records[idx].after,
        "immediately_after_first_next_domain_B": records[idx + 1].after,
    }


def boundary_summary(records: list[StepRecord]) -> dict[str, object]:
    idx = first_l_index(records)
    before = records[idx].before
    after = records[idx].after
    next_after = records[idx + 1].after
    return {
        "word": after["word"],
        "floor_pair": before["pair"],
        "floor_product": before["pair_product"],
        "q_steps": str(after["word"]).count("Q"),
        "phase_at_boundary": before["phase_label"],
        "phase_quarters_at_boundary": before["phase_quarters"],
        "floor_reached": records[idx].floor_reached_before,
        "after_L": after,
        "first_next_domain_primitive": records[idx + 1].primitive,
        "after_first_next_domain_B": next_after,
    }
