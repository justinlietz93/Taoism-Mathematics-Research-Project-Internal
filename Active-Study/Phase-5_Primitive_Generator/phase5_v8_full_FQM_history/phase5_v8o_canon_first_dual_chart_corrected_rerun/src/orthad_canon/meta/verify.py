from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

from orthad_canon.application.readout import after_rows, before_rows
from orthad_canon.domain.exact import matrix_changed_cells, matrix_digest_rows
from orthad_canon.domain.models import LiftState
from orthad_canon.meta.reference import shadow_reference


FORBIDDEN = re.compile(r"\b(search|scan|rank|test|candidate)\b", re.IGNORECASE)


def compare_evidence(state: LiftState) -> list[dict]:
    before = {row["channel_id"]: row for row in before_rows(state)}
    rows: list[dict] = []
    for after in after_rows(state):
        reference = shadow_reference(after["address_n"])
        prior = before[after["source_channel_id"]]
        transported = prior["orientation_value"] * after["lap_sign"]
        rows.append({
            **after,
            **reference,
            "transport_recomputed": transported,
            "transport_survived": transported == after["character_value"],
            "character_matched": after["character_value"] == reference["character_reference"],
            "survival": transported == after["character_value"] == reference["character_reference"],
        })
    return rows


def evidence_gate(state: LiftState) -> bool:
    rows = compare_evidence(state)
    return len(rows) == 12 and all(row["survival"] for row in rows)


def source_gate(paths: list[Path]) -> tuple[bool, list[dict]]:
    hits: list[dict] = []
    for path in paths:
        text = path.read_text(encoding="utf-8")
        for match in FORBIDDEN.finditer(text):
            hits.append({"path": str(path), "word": match.group(0), "offset": match.start()})
    return len(hits) == 0, hits


def scalar_gate(state: LiftState) -> bool:
    payload = json.dumps({"before": before_rows(state), "after": after_rows(state)}, sort_keys=True)
    return "combined_scalar" not in payload and "signed_coefficient" not in payload


def dual_chart_gate(state: LiftState) -> bool:
    return state.lens is not None and bool(state.lens.omega_plus) and bool(state.lens.omega_minus)


def transfer_gate(state: LiftState) -> bool:
    if state.lens is None:
        return False
    return any(entry.support for row in state.lens.transfer_plus_to_minus for entry in row)


def word_domain_gate(open_state: LiftState, state: LiftState) -> bool:
    return open_state.lens is None and not open_state.interior_field and len(state.interior_field) == 6


def evidence_control(state: LiftState) -> bool:
    rows = after_rows(state)
    if not rows:
        return False
    target = next(row for row in rows if row["character_value"] != 0)
    target["character_value"] *= -1
    before = {row["channel_id"]: row for row in before_rows(state)}
    recomputed = []
    for after in rows:
        ref = shadow_reference(after["address_n"])
        transported = before[after["source_channel_id"]]["orientation_value"] * after["lap_sign"]
        recomputed.append(transported == after["character_value"] == ref["character_reference"])
    return not all(recomputed)


def source_control() -> bool:
    return FORBIDDEN.search("the lens must not search the field") is not None


def scalar_control() -> bool:
    payload = {"combined_scalar": 1}
    return not ("combined_scalar" not in payload and "signed_coefficient" not in payload)


def dual_chart_control(state: LiftState) -> bool:
    if state.lens is None:
        return False
    altered = state.lens.__class__(
        pairing=state.lens.pairing,
        omega_plus=state.lens.omega_plus,
        omega_minus=(),
        transfer_plus_to_minus=state.lens.transfer_plus_to_minus,
        transfer_minus_to_plus=state.lens.transfer_minus_to_plus,
        carrier_size=state.lens.carrier_size,
        event_count=state.lens.event_count,
    )
    copy = LiftState(axes=list(state.axes), active_axis=state.active_axis, word=state.word, lens=altered)
    return not dual_chart_gate(copy)


def transfer_control(state: LiftState) -> bool:
    if state.lens is None:
        return False
    zero = tuple(tuple(entry.__class__(0, 0) for entry in row) for row in state.lens.transfer_plus_to_minus)
    altered = state.lens.__class__(
        pairing=state.lens.pairing,
        omega_plus=state.lens.omega_plus,
        omega_minus=state.lens.omega_minus,
        transfer_plus_to_minus=zero,
        transfer_minus_to_plus=zero,
        carrier_size=state.lens.carrier_size,
        event_count=state.lens.event_count,
    )
    copy = LiftState(axes=list(state.axes), active_axis=state.active_axis, word=state.word, lens=altered)
    return not transfer_gate(copy)


def matrix_hash(matrix) -> str:
    data = json.dumps(matrix_digest_rows(matrix), separators=(",", ":")).encode()
    return hashlib.sha256(data).hexdigest()


def omega_diff(baseline: LiftState, altered: LiftState) -> dict:
    if baseline.lens is None:
        raise ValueError("baseline lens missing")
    if altered.lens is None:
        return {"omega_plus_changed": 144, "omega_minus_changed": 144, "transfer_changed": 144}
    return {
        "omega_plus_changed": matrix_changed_cells(baseline.lens.omega_plus, altered.lens.omega_plus),
        "omega_minus_changed": matrix_changed_cells(baseline.lens.omega_minus, altered.lens.omega_minus),
        "transfer_changed": matrix_changed_cells(baseline.lens.transfer_plus_to_minus, altered.lens.transfer_plus_to_minus),
    }
