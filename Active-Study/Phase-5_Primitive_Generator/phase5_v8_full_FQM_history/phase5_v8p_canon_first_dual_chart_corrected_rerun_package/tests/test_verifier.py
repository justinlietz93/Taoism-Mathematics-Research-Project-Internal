from pathlib import Path

from orthad_canon import run_once
from orthad_canon.meta.verify import evidence_control, source_control


def test_evidence_control_fires() -> None:
    assert evidence_control(run_once())


def test_lexeme_control_fires() -> None:
    assert source_control()
