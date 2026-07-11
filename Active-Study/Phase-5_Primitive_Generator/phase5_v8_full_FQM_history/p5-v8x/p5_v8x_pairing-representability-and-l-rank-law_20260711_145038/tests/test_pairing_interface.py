import csv
from conftest import ROOT, STAMP, load_json


def claim():
    return load_json(f"outputs/{STAMP}_claim_model.json")


def test_source_forced_two_slot_interface():
    data = claim()["source_forced_interface"]
    assert data["name"] == "two_slot_pullback_pairing_system"
    assert data["scalar_object_required"] is False
    assert data["duality_object_required"] is False


def test_source_ledger_has_four_pullbacks():
    path = ROOT / "outputs" / f"{STAMP}_pairing_representability_source_ledger.csv"
    rows = {row["source_id"]: row for row in csv.DictReader(path.open(encoding="utf-8"))}
    text = rows["S03_FOUR_PULLBACKS"]["literal_formula"]
    assert "iota_-^* P iota_+" in text
    assert "iota_+^* P iota_-" in text


def test_representability_stays_open():
    data = claim()
    assert data["statuses"]["DUALITY_MORPHISM_MODEL"] == "ADMISSIBLE_CANDIDATE"
    assert data["statuses"]["PAIRING_REPRESENTABILITY"] == "NOT_YET_DERIVED"
    assert "natural isomorphism" in data["duality_morphism_model"]["missing_axiom"]


def test_scalar_variance_is_downstream():
    data = claim()
    assert data["statuses"]["SCALAR_VARIANCE_STATUS"] == "DOWNSTREAM"
    assert "coefficient object K" in data["scalar_variance"]["dependencies"]
