from __future__ import annotations

from primitive_custody.application.engine import StepRecord


EXPECTED_CROSSING_WORD = "BQQBBBQBQBBQBBL"
EXPECTED_FLOOR_PAIR = (55, 89)
EXPECTED_NEXT_PAIR = (89, 144)


def crossing_index(records: list[StepRecord]) -> int:
    for index, record in enumerate(records):
        if record.primitive == "L":
            return index
    raise ValueError("trace has no L")


def summarize(records: list[StepRecord]) -> dict[str, object]:
    idx = crossing_index(records)
    l_record = records[idx]
    next_record = records[idx + 1]
    before_l = l_record.before
    after_l = l_record.after
    after_next = next_record.after
    crossing_word = str(after_l["word"])
    q_steps = crossing_word.count("Q")
    return {
        "crossing_word": crossing_word,
        "floor_pair": before_l["pair"],
        "floor_product": before_l["pair_product"],
        "q_steps": q_steps,
        "phase_at_boundary": before_l["phase_label"],
        "phase_quarters_at_boundary": before_l["phase_quarters"],
        "floor_reached_before_l": l_record.floor_reached_before,
        "post_l_A": after_l["A"],
        "post_l_pair": after_l["pair"],
        "post_l_phase_quarters": after_l["phase_quarters"],
        "post_l_phase_label": after_l["phase_label"],
        "post_l_k": after_l["k"],
        "post_l_j": after_l["j"],
        "first_next_domain_primitive": next_record.primitive,
        "first_next_domain_pair": after_next["pair"],
        "first_next_domain_word": after_next["word"],
    }
