from primitive_custody.application.engine import run_to_first_l_and_next_b
from primitive_custody.application.evidence import summarize
from primitive_custody.orthad.boundary import (
    ORTHAD_CHART_RECURRENCE_NOT_YET_DERIVED,
    OrthadNotDerivedError,
    terminal_projection,
)


def test_exact_first_crossing_word() -> None:
    _, records = run_to_first_l_and_next_b()
    assert summarize(records)["crossing_word"] == "BQQBBBQBQBBQBBL"


def test_floor_boundary_and_q_phase() -> None:
    _, records = run_to_first_l_and_next_b()
    result = summarize(records)
    assert result["floor_pair"] == [55, 89]
    assert result["floor_product"] == 4895
    assert result["q_steps"] == 5
    assert result["phase_at_boundary"] == "i"
    assert result["floor_reached_before_l"] is True


def test_l_carries_pair_and_phase_and_resets_only_local_position() -> None:
    _, records = run_to_first_l_and_next_b()
    result = summarize(records)
    assert result["post_l_A"] == 1
    assert result["post_l_pair"] == [55, 89]
    assert result["post_l_phase_quarters"] == 5
    assert result["post_l_k"] == 0
    assert result["post_l_j"] == 7


def test_first_next_domain_step() -> None:
    _, records = run_to_first_l_and_next_b()
    result = summarize(records)
    assert result["first_next_domain_primitive"] == "B"
    assert result["first_next_domain_pair"] == [89, 144]


def test_floor_is_not_a_primitive() -> None:
    _, records = run_to_first_l_and_next_b()
    assert all(record.primitive in ("B", "Q", "L") for record in records)
    assert "FLOOR" not in "".join(record.primitive for record in records)


def test_projection_refuses_underived_chart_recurrence() -> None:
    lifted, _ = run_to_first_l_and_next_b()
    assert lifted.orthad_boundary.status == ORTHAD_CHART_RECURRENCE_NOT_YET_DERIVED
    try:
        terminal_projection(lifted.orthad_boundary)
    except OrthadNotDerivedError:
        return
    raise AssertionError("projection must refuse an underived Orthad")
