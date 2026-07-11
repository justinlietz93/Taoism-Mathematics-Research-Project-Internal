from __future__ import annotations

from orthad_canon.domain.models import FarChannel, InteriorChannel, LiftState


def before_rows(state: LiftState) -> list[dict]:
    rows: list[dict] = []
    for channel in state.interior_field:
        rows.append({
            "channel_id": channel.channel_id,
            "basis_slot": channel.basis_slot,
            "floor_bit": channel.floor_bit,
            "transfer_phase_forward": channel.transfer_phase_forward,
            "transfer_phase_reverse": channel.transfer_phase_reverse,
            "orientation_value": channel.orientation_value,
        })
    return rows


def after_rows(state: LiftState) -> list[dict]:
    rows: list[dict] = []
    for channel in state.far_field:
        n = 12 if channel.carrier_residue == 0 else channel.carrier_residue
        rows.append({
            "output_slot": channel.output_slot,
            "carrier_residue": channel.carrier_residue,
            "address_n": n,
            "source_channel_id": channel.source_channel_id,
            "source_basis_slot": channel.source_basis_slot,
            "hand": channel.hand,
            "lap_sign": channel.lap_sign,
            "character_value": channel.character_value,
        })
    return rows
