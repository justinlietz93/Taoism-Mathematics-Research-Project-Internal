from orthad_v8r.axis import compile_active_axis
from orthad_v8r.engine import run_first_crossing_and_next_b
from orthad_v8r.evidence import boundary_summary, snapshots
from orthad_v8r.oracle import independent_oracle


def test_exact_word_and_floor() -> None:
    _, records = run_first_crossing_and_next_b()
    result = boundary_summary(records)
    assert result["word"] == "BQQBBBQBQBBQBBL"
    assert result["floor_pair"] == [55, 89]
    assert result["floor_product"] == 4895
    assert result["q_steps"] == 5
    assert result["phase_at_boundary"] == "i"


def test_three_snapshots() -> None:
    _, records = run_first_crossing_and_next_b()
    s = snapshots(records)
    assert s["before_first_L"]["word"] == "BQQBBBQBQBBQBB"
    assert s["immediately_after_first_L"]["word"] == "BQQBBBQBQBBQBBL"
    assert s["immediately_after_first_next_domain_B"]["word"] == "BQQBBBQBQBBQBBLB"


def test_first_l_carry() -> None:
    _, records = run_first_crossing_and_next_b()
    s = snapshots(records)
    before = s["before_first_L"]
    after = s["immediately_after_first_L"]
    assert before["pair"] == after["pair"] == [55, 89]
    assert before["phase_quarters"] == after["phase_quarters"] == 5
    assert after["A"] == 1 and after["k"] == 0 and after["j"] == 7


def test_first_next_domain_b() -> None:
    _, records = run_first_crossing_and_next_b()
    s = snapshots(records)
    assert s["immediately_after_first_next_domain_B"]["pair"] == [89, 144]


def test_axis_trace() -> None:
    _, records = run_first_crossing_and_next_b()
    rows = compile_active_axis(records)
    assert rows[13].active_axis == "i/4895"
    assert rows[14].latched_axis == "i/4895"
    assert rows[14].active_axis == "1"
    assert rows[15].active_axis == "1/12816"


def test_independent_oracle() -> None:
    _, records = run_first_crossing_and_next_b()
    oracle = independent_oracle()
    assert [r.primitive for r in records] == [r["primitive"] for r in oracle]
    assert [r.word_prefix for r in records] == [r["word_prefix"] for r in oracle]
