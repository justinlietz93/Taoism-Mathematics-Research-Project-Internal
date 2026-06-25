from orthad_voidwalker_overset.harness import run_scenario
from orthad_voidwalker_overset.scenarios import base_scenarios, random_legal_scenario, random_illegal_scenario
import random


def test_base_gates():
    results = [run_scenario(sc, ticks=180, walkers=18, seed=11) for sc in base_scenarios()]
    h1, h2, h3, h4 = results
    assert h1.visible_projection == h2.visible_projection
    assert h1.true_coupling_signature == h2.true_coupling_signature
    assert h1.matrix_match and h2.matrix_match
    assert h1.visible_projection == h3.visible_projection
    assert h1.true_coupling_signature != h3.true_coupling_signature
    assert h3.matrix_match
    assert not h4.admitted
    assert h4.topology_spikes > 0


def test_random_legal_and_illegal_smoke():
    rng = random.Random(2026)
    for idx in range(8):
        legal = run_scenario(random_legal_scenario(idx, 4, 7, rng), ticks=220, walkers=20, seed=idx)
        assert legal.pass_case
        illegal = run_scenario(random_illegal_scenario(idx + 100, 4, 7, rng), ticks=220, walkers=20, seed=idx + 80)
        assert illegal.pass_case
