from conftest import STAMP, load_json


def test_one_sided_orthogonality_counterexample():
    data = load_json(f"outputs/{STAMP}_first_L_mixed_block_cases.json")
    matrix = data["counterexample"]["matrix"]
    assert matrix[1][0] == 0
    assert matrix[0][1] == 1


def test_both_mixed_blocks_remain_open():
    claim = load_json(f"outputs/{STAMP}_claim_model.json")
    assert claim["first_L"]["right_mixed"] == "NOT_YET_DERIVED"
    assert claim["first_L"]["left_mixed"] == "NOT_YET_DERIVED"


def test_block_size_does_not_force_rank_increase():
    data = load_json(f"outputs/{STAMP}_rank_zero_birth_counterexample.json")
    assert data["old_block_size"] == 1
    assert data["new_block_size"] == 2
    assert data["old_algebraic_rank"] == data["new_algebraic_rank"] == 1


def test_gauge_full_aut_not_derived():
    data = load_json(f"outputs/{STAMP}_seed_gauge_quotient_boundary.json")
    assert data["full_Aut_H_quotient"] == "ADMISSIBLE_MODEL_NOT_DERIVED"


def test_downstream_closed_and_lifted_schema_only():
    claim = load_json(f"outputs/{STAMP}_claim_model.json")
    assert claim["lifted_state_schema"]["Xi_hat_t_emitted"] is False
    assert all(value is None for key, value in claim["lifted_state_schema"].items() if key in {"pairing", "omega_plus", "omega_minus", "transfer_plus_to_minus", "transfer_minus_to_plus"})
    assert claim["downstream"]["projection"] == "NOT_RUN"
