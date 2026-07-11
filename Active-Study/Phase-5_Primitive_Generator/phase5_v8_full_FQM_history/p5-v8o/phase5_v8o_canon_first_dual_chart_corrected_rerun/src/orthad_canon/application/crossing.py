from __future__ import annotations

from orthad_canon.domain.exact import phase_orientation
from orthad_canon.domain.models import FarChannel, InteriorChannel, LiftState


def emit_floor_field(state: LiftState, corrupt_floor_bit: bool = False) -> None:
    if state.lens is None or state.floor_bit is None:
        state.interior_field = ()
        state.event_log.append({"event": "FLOOR", "channel_count": 0})
        return
    state.floor_lens = state.lens
    floor_bit = state.floor_bit ^ (1 if corrupt_floor_bit else 0)
    rows: list[InteriorChannel] = []
    for slot in range(6):
        plus_row = slot
        minus_col = (-slot) % 12
        forward = state.lens.transfer_plus_to_minus[plus_row][minus_col]
        reverse = state.lens.transfer_minus_to_plus[plus_row][minus_col]
        orientation = phase_orientation(forward.phase_mod24) if forward.support and reverse.support else 0
        if slot % 2 != floor_bit:
            orientation = 0
        rows.append(InteriorChannel(
            channel_id=f"c{state.lens.event_count:02d}_{slot:02d}",
            basis_slot=slot,
            floor_bit=floor_bit,
            transfer_phase_forward=forward.phase_mod24,
            transfer_phase_reverse=reverse.phase_mod24,
            orientation_value=orientation,
        ))
    state.interior_field = tuple(rows)
    state.event_log.append({"event": "FLOOR", "channel_count": len(rows), "floor_bit_used": floor_bit})


def transport_after_l(state: LiftState) -> None:
    if state.lens is None or not state.interior_field or state.frozen_shift_mod6 is None:
        state.far_field = ()
        return
    out: list[FarChannel] = []
    shift = state.frozen_shift_mod6
    for source in state.interior_field:
        for hand in (0, 1):
            residue = (source.basis_slot + 6 * hand + shift) % 12
            lap_sign = 1 if hand == 0 else -1
            out.append(FarChannel(
                output_slot=residue,
                carrier_residue=residue,
                source_channel_id=source.channel_id,
                source_basis_slot=source.basis_slot,
                hand=hand,
                lap_sign=lap_sign,
                character_value=source.orientation_value * lap_sign,
            ))
    state.far_field = tuple(sorted(out, key=lambda row: row.output_slot))
