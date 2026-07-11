from conftest import STAMP, load_json


def test_inference_uses_source_rows_and_rules():
    claim = load_json(f"outputs/{STAMP}_claim_model.json")
    rules = load_json(f"outputs/{STAMP}_inference_rules.json")
    assert claim["verifier_evidence_mode"] == "SOURCE_ROWS_PLUS_EXPLICIT_INFERENCE_RULES"
    assert all(rule["evidence_class"] == "SOURCE_DERIVED" for rule in rules)


def test_rank_law_not_typed():
    claim = load_json(f"outputs/{STAMP}_claim_model.json")
    assert claim["statuses"]["FIRST_L_PAIRING_RANK_LAW"] == "NOT_YET_TYPED"
    assert claim["rank_semantics"]["architectural_axis_count"] == "DERIVED"
    assert claim["rank_semantics"]["pairing_morphism_rank"] == "NOT_YET_TYPED"
