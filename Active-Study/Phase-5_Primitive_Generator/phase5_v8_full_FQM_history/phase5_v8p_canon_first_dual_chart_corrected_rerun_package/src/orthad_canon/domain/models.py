from __future__ import annotations

from dataclasses import dataclass, field
from fractions import Fraction
from typing import Tuple


@dataclass(frozen=True)
class AxisState:
    u: int
    v: int
    phase_mod4: int = 0
    clock: int = 0
    frozen: bool = False

    @property
    def uv(self) -> int:
        return self.u * self.v

    @property
    def lens_axis(self) -> str:
        return f"i/{self.uv}"


@dataclass(frozen=True)
class ExactEntry:
    support: int
    phase_mod24: int


ExactMatrix = Tuple[Tuple[ExactEntry, ...], ...]


@dataclass(frozen=True)
class DualChartLens:
    pairing: ExactMatrix
    omega_plus: ExactMatrix
    omega_minus: ExactMatrix
    transfer_plus_to_minus: ExactMatrix
    transfer_minus_to_plus: ExactMatrix
    carrier_size: int
    event_count: int


@dataclass(frozen=True)
class InteriorChannel:
    channel_id: str
    basis_slot: int
    floor_bit: int
    transfer_phase_forward: int
    transfer_phase_reverse: int
    orientation_value: int


@dataclass(frozen=True)
class FarChannel:
    output_slot: int
    carrier_residue: int
    source_channel_id: str
    source_basis_slot: int
    hand: int
    lap_sign: int
    character_value: int


@dataclass
class LiftState:
    axes: list[AxisState]
    active_axis: int = 0
    word: str = ""
    lens: DualChartLens | None = None
    floor_lens: DualChartLens | None = None
    interior_field: tuple[InteriorChannel, ...] = ()
    far_field: tuple[FarChannel, ...] = ()
    floor_bit: int | None = None
    frozen_shift_mod6: int | None = None
    event_log: list[dict] = field(default_factory=list)

    @property
    def active(self) -> AxisState:
        return self.axes[self.active_axis]


@dataclass(frozen=True)
class RunOptions:
    delete_b: bool = False
    delete_l: bool = False
    pair_override: tuple[int, int] | None = None
    corrupt_floor_bit: bool = False
    corrupt_latched_axis: bool = False
    sever_cross_transfer: bool = False
