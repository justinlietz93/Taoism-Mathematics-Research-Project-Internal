from conftest import load_json, STAMP


def sanity():
    return load_json(f"outputs/{STAMP}_primitive_sanity_check.json")


def test_exact_first_crossing_word():
    assert sanity()["word"] == "BQQBBBQBQBBQBBL"


def test_floor_boundary():
    data = sanity()
    assert data["floor_pair"] == [55, 89]
    assert data["floor_product"] == 4895
    assert data["Q_steps"] == 5
    assert data["phase_witness"] == "i"


def test_l_carry_and_next_b():
    data = sanity()
    after_l = data["after_L"]
    assert (after_l["A"], after_l["u"], after_l["v"], after_l["k"], after_l["j"]) == (1, 55, 89, 0, 7)
    after_b = data["after_next_B"]
    assert [after_b["u"], after_b["v"]] == [89, 144]
