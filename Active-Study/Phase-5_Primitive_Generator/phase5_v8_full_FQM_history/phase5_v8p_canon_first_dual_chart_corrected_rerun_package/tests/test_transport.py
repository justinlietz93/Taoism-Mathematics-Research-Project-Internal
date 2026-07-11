from pathlib import Path

from orthad_canon import RunOptions, run_once
from orthad_canon.application.readout import after_rows
from orthad_canon.meta.verify import evidence_gate, source_gate, transfer_gate


def test_baseline_evidence_passes() -> None:
    state = run_once()
    assert state.word == "BL"
    assert state.axes[0].lens_axis == "i/4895"
    assert len(after_rows(state)) == 12
    assert evidence_gate(state)


def test_required_ablations_fail() -> None:
    options = [
        RunOptions(delete_b=True),
        RunOptions(delete_l=True),
        RunOptions(pair_override=(1, 1)),
        RunOptions(pair_override=(100, 101)),
        RunOptions(corrupt_floor_bit=True),
        RunOptions(corrupt_latched_axis=True),
        RunOptions(sever_cross_transfer=True),
    ]
    assert all(not evidence_gate(run_once(option)) for option in options)


def test_dual_chart_and_transfer_exist() -> None:
    state = run_once()
    assert state.lens is not None
    assert state.lens.omega_plus
    assert state.lens.omega_minus
    assert transfer_gate(state)


def test_live_path_contains_no_external_term_label() -> None:
    root = Path(__file__).resolve().parents[1]
    paths = [
        root / "src/orthad_canon/application/compiler.py",
        root / "src/orthad_canon/application/crossing.py",
        root / "src/orthad_canon/application/readout.py",
    ]
    text = "\n".join(path.read_text() for path in paths)
    assert "term_n" not in text
    clean, hits = source_gate(paths)
    assert clean
    assert hits == []
