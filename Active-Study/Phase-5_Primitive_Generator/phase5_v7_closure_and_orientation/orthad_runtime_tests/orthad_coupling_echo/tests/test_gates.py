from pathlib import Path
from orthad_coupling_echo.experiment import run

def test_smoke_gates(tmp_path: Path):
    card = run(tmp_path)
    assert card["global_pass"] is True
    assert card["gates"]["legal_rewrite_invariance"] is True
    assert card["gates"]["same_projection_different_retained_history"] is True
    assert card["gates"]["illegal_cocycle_rejected"] is True
    assert card["gates"]["positive_coupling_echo_gain"] is True
