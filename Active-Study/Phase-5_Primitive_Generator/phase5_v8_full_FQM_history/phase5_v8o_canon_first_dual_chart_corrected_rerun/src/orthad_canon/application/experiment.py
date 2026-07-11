from __future__ import annotations

from orthad_canon.application.compiler import apply_b, apply_l
from orthad_canon.application.crossing import emit_floor_field, transport_after_l
from orthad_canon.domain.models import AxisState, LiftState, RunOptions


def run_once(options: RunOptions = RunOptions()) -> LiftState:
    pair = options.pair_override if options.pair_override is not None else (34, 55)
    state = LiftState(axes=[AxisState(pair[0], pair[1])])
    if not options.delete_b:
        apply_b(state, sever_transfer=options.sever_cross_transfer)
    emit_floor_field(state, corrupt_floor_bit=options.corrupt_floor_bit)
    if not options.delete_l:
        apply_l(state, sever_transfer=options.sever_cross_transfer, corrupt_axis=options.corrupt_latched_axis)
        transport_after_l(state)
    return state
