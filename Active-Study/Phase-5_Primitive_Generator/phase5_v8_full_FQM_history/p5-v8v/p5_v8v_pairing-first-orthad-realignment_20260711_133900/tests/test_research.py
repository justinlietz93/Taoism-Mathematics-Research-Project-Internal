from orthad_v8v.research import (
    STATUSES,
    affine_boundary,
    causal_trace,
    mhd_readiness,
    mutation_assessments,
    pairing_seed_assessment,
    pairing_type_assessment,
    trace_first_crossing_and_next_b,
    z12_assessment,
)


def test_pairing_gap_is_first():
    assert STATUSES["FIRST_TRUE_GAP"] == "PRIMARY_PAIRING_TYPE_SEED_AND_MUTATION"
    assert pairing_type_assessment()["status"] == "NOT_YET_DERIVED"
    assert pairing_seed_assessment()["status"] == "NOT_YET_DERIVED"


def test_successor_is_downstream():
    assert STATUSES["NATIVE_SUCCESSOR_ON_Z12"] == "DOWNSTREAM_COORDINATE_QUESTION"
    assert z12_assessment()["successor_status"] == "DOWNSTREAM_COORDINATE_QUESTION"


def test_no_pairing_chart_or_transfer_values():
    trace = causal_trace(trace_first_crossing_and_next_b())
    fields = [
        "P_t", "P_t_plus_1", "Omega_t_plus", "Omega_t_plus_1_plus",
        "Omega_t_minus", "Omega_t_plus_1_minus", "T_t_plus_to_minus",
        "T_t_plus_1_plus_to_minus", "T_t_minus_to_plus", "T_t_plus_1_minus_to_plus",
    ]
    for row in trace:
        for field in fields:
            assert row[field]["value"] is None


def test_no_projection():
    assert all(not row["projection_performed"] for row in causal_trace(trace_first_crossing_and_next_b()))
    assert STATUSES["TERMINAL_PROJECTION"] == "NOT_RUN"


def test_mutations_remain_open():
    assessments = mutation_assessments()
    assert all(assessments[p]["status"] == "NOT_YET_DERIVED" for p in ("B", "Q", "L"))


def test_affine_boundary():
    data = affine_boundary()
    assert data["QBL_TO_AFFINE_FACTOR_MAP"] == "NOT_YET_DERIVED"
    assert data["INTERNAL_ORTHAD_SEED_FROM_AFFINE_MAP"] == "NOT_LICENSED"


def test_mhd_not_ready():
    data = mhd_readiness()
    assert data["MHD_ORTHAD_READINESS"] == "NOT_READY"
    assert len(data["missing"]) == 9
