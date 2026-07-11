from orthad_v8v.primitive import exact_word, floor_reached, trace_first_crossing_and_next_b
from orthad_v8v.research import EXPECTED_WORD, EXPECTED_WORD_WITH_NEXT_B, snapshots, verify_baseline


def rows():
    return trace_first_crossing_and_next_b()


def test_word():
    trace = rows()
    assert exact_word(trace) == EXPECTED_WORD
    assert exact_word(trace, include_next_b=True) == EXPECTED_WORD_WITH_NEXT_B


def test_floor_is_predicate_not_symbol():
    trace = rows()
    lrow = next(row for row in trace if row["selected_primitive"] == "L")
    assert floor_reached(__import__("orthad_v8v.primitive", fromlist=["CustodyState"]).CustodyState(**{
        "A": lrow["before"]["A"],
        "u": lrow["before"]["u"],
        "v": lrow["before"]["v"],
        "phase_quarters": lrow["before"]["phase_quarters"],
        "k": lrow["before"]["k"],
        "j": lrow["before"]["j"],
        "word": lrow["before"]["word"],
    }))
    assert "FLOOR" not in exact_word(trace)


def test_boundary_snapshots():
    snap = snapshots(rows())
    assert snap["before_first_L"]["pair"] == [55, 89]
    assert snap["before_first_L"]["phase_quarters"] == 5
    assert snap["immediately_after_first_L"]["pair"] == [55, 89]
    assert snap["immediately_after_first_L"]["phase_quarters"] == 5
    assert snap["immediately_after_first_L"]["k"] == 0
    assert snap["immediately_after_first_L"]["j"] == 7
    assert snap["immediately_after_first_next_domain_B"]["pair"] == [89, 144]


def test_q_updates_j_and_k():
    for row in rows():
        if row["selected_primitive"] == "Q":
            assert row["after"]["k"] == row["before"]["k"] + 1
            assert row["after"]["j"] == row["before"]["j"] + 1


def test_local_axis_boundary():
    trace = rows()
    lrow = next(row for row in trace if row["selected_primitive"] == "L")
    assert lrow["active_axis_before"]["local_shorthand"] == "i/4895"


def test_baseline_full_gate():
    assert verify_baseline(rows())["pass"]
