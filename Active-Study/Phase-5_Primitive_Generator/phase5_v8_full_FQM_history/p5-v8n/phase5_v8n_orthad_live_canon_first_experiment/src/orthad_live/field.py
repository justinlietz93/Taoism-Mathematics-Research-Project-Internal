from __future__ import annotations

from dataclasses import dataclass
from math import gcd


@dataclass(frozen=True)
class ChannelAddress:
    pre_l_seat_mod6: int
    orientation_bit: int

    @property
    def post_l_seat_mod12(self) -> int:
        return self.pre_l_seat_mod6 + 6 * self.orientation_bit

    @property
    def canonical_n(self) -> int:
        seat = self.post_l_seat_mod12
        return 12 if seat == 0 else seat


@dataclass(frozen=True)
class ResidualChannel:
    address: ChannelAddress
    term_n: int
    support: bool
    character: int
    magnitude_n: int
    exponent_num: int
    exponent_den: int


def chi12(n: int) -> int:
    if gcd(n, 6) != 1:
        return 0
    residue = n % 12
    return 1 if residue in (1, 11) else -1


def two_lens_domain() -> tuple[ChannelAddress, ...]:
    return tuple(
        ChannelAddress(pre_l_seat_mod6=seat, orientation_bit=orientation)
        for orientation in (0, 1)
        for seat in range(6)
    )


def bind_residual_field(domain: tuple[ChannelAddress, ...]) -> tuple[ResidualChannel, ...]:
    rows = []
    for address in domain:
        n = address.canonical_n
        character = chi12(n)
        rows.append(
            ResidualChannel(
                address=address,
                term_n=n,
                support=character != 0,
                character=character,
                magnitude_n=n,
                exponent_num=n * n,
                exponent_den=24,
            )
        )
    return tuple(rows)
