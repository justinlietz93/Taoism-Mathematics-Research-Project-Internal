from __future__ import annotations

from dataclasses import dataclass

from .exact import AxisValue
from .field import ChannelAddress, ResidualChannel, two_lens_domain


@dataclass(frozen=True)
class LiftState:
    host_class: int
    u: int
    v: int
    phase_quarters: int
    active_axis: AxisValue
    latched_axes: tuple[AxisValue, ...]
    domain: tuple[ChannelAddress, ...]
    qbl_word: str


@dataclass(frozen=True)
class FloorField:
    term_n: int
    pre_l_seat_mod6: int
    orientation_bit: int
    post_l_seat_mod12: int


@dataclass(frozen=True)
class CuspCrossing:
    before: LiftState
    after_b: LiftState
    floor_field: tuple[FloorField, ...]
    after_l: LiftState
    channels_before: tuple[ResidualChannel, ...]
    qbl_word: str
    event_sequence: tuple[str, ...]


def open_cusp_state() -> LiftState:
    return LiftState(
        host_class=0,
        u=34,
        v=55,
        phase_quarters=5,
        active_axis=AxisValue(0, 1, 1870),
        latched_axes=(),
        domain=two_lens_domain(),
        qbl_word="",
    )


def apply_b(state: LiftState) -> LiftState:
    next_u, next_v = state.v, state.u + state.v
    next_den = next_u * next_v
    return LiftState(
        host_class=state.host_class,
        u=next_u,
        v=next_v,
        phase_quarters=state.phase_quarters,
        active_axis=state.active_axis.with_den(next_den),
        latched_axes=state.latched_axes,
        domain=state.domain,
        qbl_word=state.qbl_word + "B",
    )


def apply_floor(state: LiftState, channels: tuple[ResidualChannel, ...]) -> tuple[FloorField, ...]:
    return tuple(
        FloorField(
            term_n=channel.term_n,
            pre_l_seat_mod6=channel.address.pre_l_seat_mod6,
            orientation_bit=(channel.term_n % 12) // 6,
            post_l_seat_mod12=channel.address.pre_l_seat_mod6 + 6 * ((channel.term_n % 12) // 6),
        )
        for channel in channels
    )


def apply_l(state: LiftState) -> LiftState:
    return LiftState(
        host_class=state.host_class + 1,
        u=state.u,
        v=state.v,
        phase_quarters=state.phase_quarters + 1,
        active_axis=AxisValue(1, 0, 1),
        latched_axes=state.latched_axes + (state.active_axis.reduced(),),
        domain=state.domain,
        qbl_word=state.qbl_word + "L",
    )


def cross_cusp(state: LiftState, channels: tuple[ResidualChannel, ...]) -> CuspCrossing:
    after_b = apply_b(state)
    floor_field = apply_floor(after_b, channels)
    after_l = apply_l(after_b)
    return CuspCrossing(
        before=state,
        after_b=after_b,
        floor_field=floor_field,
        after_l=after_l,
        channels_before=channels,
        qbl_word=after_l.qbl_word,
        event_sequence=("B", "FLOOR", "L"),
    )
