from __future__ import annotations

from .field import ResidualChannel
from .lift import CuspCrossing


def seat_character(seat: int) -> int:
    if seat in (1, 11):
        return 1
    if seat in (5, 7):
        return -1
    return 0


def before_rows(crossing: CuspCrossing) -> tuple[dict[str, int | bool | str], ...]:
    axis = crossing.before.active_axis.as_record()
    return tuple(
        {
            "channel_id": index,
            "term_n": channel.term_n,
            "pre_l_seat_mod6": channel.address.pre_l_seat_mod6,
            "support": channel.support,
            "character_channel": channel.character,
            "magnitude_channel_n": channel.magnitude_n,
            "exponent_num": channel.exponent_num,
            "exponent_den": channel.exponent_den,
            "axis_real_num": axis["real_num"],
            "axis_imag_num": axis["imag_num"],
            "axis_den": axis["den"],
            "axis_exact": axis["exact"],
        }
        for index, channel in enumerate(crossing.channels_before)
    )


def after_rows(crossing: CuspCrossing) -> tuple[dict[str, int | bool | str], ...]:
    latched = crossing.after_l.latched_axes[-1].as_record()
    floor_by_n = {row.term_n: row for row in crossing.floor_field}
    return tuple(
        {
            "channel_id": index,
            "term_n": channel.term_n,
            "pre_l_seat_mod6": floor_by_n[channel.term_n].pre_l_seat_mod6,
            "orientation_bit": floor_by_n[channel.term_n].orientation_bit,
            "post_l_seat_mod12": floor_by_n[channel.term_n].post_l_seat_mod12,
            "support": seat_character(floor_by_n[channel.term_n].post_l_seat_mod12) != 0,
            "character_channel": seat_character(floor_by_n[channel.term_n].post_l_seat_mod12),
            "magnitude_channel_n": channel.magnitude_n,
            "exponent_num": channel.exponent_num,
            "exponent_den": channel.exponent_den,
            "latched_axis_real_num": latched["real_num"],
            "latched_axis_imag_num": latched["imag_num"],
            "latched_axis_den": latched["den"],
            "latched_axis_exact": latched["exact"],
        }
        for index, channel in enumerate(crossing.channels_before)
    )
