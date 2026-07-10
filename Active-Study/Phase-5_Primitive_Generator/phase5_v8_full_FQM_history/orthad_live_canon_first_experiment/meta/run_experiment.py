from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

PACKAGE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PACKAGE / "src"))

from orthad_live import after_rows, before_rows, bind_residual_field, cross_cusp, open_cusp_state


def write_csv(path: Path, rows: tuple[dict, ...] | list[dict]) -> None:
    rows = list(rows)
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    state = open_cusp_state()
    field = bind_residual_field(state.domain)
    crossing = cross_cusp(state, field)
    before = before_rows(crossing)
    after = after_rows(crossing)

    write_csv(PACKAGE / "outputs" / "orthad_live_channel_before.csv", before)
    write_csv(PACKAGE / "outputs" / "orthad_live_channel_after.csv", after)

    survival = []
    for left, right in zip(before, after, strict=True):
        survival.append({
            "channel_id": left["channel_id"],
            "term_n": left["term_n"],
            "character_before": left["character_channel"],
            "character_after": right["character_channel"],
            "character_survived": left["character_channel"] == right["character_channel"],
            "support_before": left["support"],
            "support_after": right["support"],
            "support_survived": left["support"] == right["support"],
            "magnitude_before": left["magnitude_channel_n"],
            "magnitude_after": right["magnitude_channel_n"],
            "magnitude_survived": left["magnitude_channel_n"] == right["magnitude_channel_n"],
            "exponent_num_before": left["exponent_num"],
            "exponent_num_after": right["exponent_num"],
            "exponent_survived": left["exponent_num"] == right["exponent_num"] and left["exponent_den"] == right["exponent_den"],
            "post_l_seat_mod12": right["post_l_seat_mod12"],
        })
    write_csv(PACKAGE / "outputs" / "orthad_live_per_channel_survival.csv", survival)

    crossing_record = {
        "qbl_word": crossing.qbl_word,
        "event_sequence": list(crossing.event_sequence),
        "before": {
            "host_class": crossing.before.host_class,
            "pair": [crossing.before.u, crossing.before.v],
            "phase_quarters": crossing.before.phase_quarters,
            "active_axis": crossing.before.active_axis.as_record(),
            "domain_cardinality": len(crossing.before.domain),
        },
        "after_B": {
            "host_class": crossing.after_b.host_class,
            "pair": [crossing.after_b.u, crossing.after_b.v],
            "phase_quarters": crossing.after_b.phase_quarters,
            "active_axis": crossing.after_b.active_axis.as_record(),
        },
        "floor": {
            "rule": "orientation_bit=(n mod 12)//6; post_l_seat=pre_l_seat+6*orientation_bit",
            "rows": [row.__dict__ for row in crossing.floor_field],
        },
        "after_L": {
            "host_class": crossing.after_l.host_class,
            "pair": [crossing.after_l.u, crossing.after_l.v],
            "phase_quarters": crossing.after_l.phase_quarters,
            "latched_axes": [axis.as_record() for axis in crossing.after_l.latched_axes],
            "new_active_axis": crossing.after_l.active_axis.as_record(),
            "domain_cardinality": len(crossing.after_l.domain),
        },
        "scalar_residual_field_present": False,
        "combined_signed_coefficient_field_present": False,
    }
    (PACKAGE / "outputs" / "orthad_live_crossing_record.json").write_text(json.dumps(crossing_record, indent=2))

    domain_record = {
        "origin": "lift_output",
        "before_two_lens_domain": [
            {
                "pre_l_seat_mod6": item.pre_l_seat_mod6,
                "orientation_slot": item.orientation_bit,
                "canonical_n": item.canonical_n,
            }
            for item in crossing.before.domain
        ],
        "after_post_l_domain": [row["post_l_seat_mod12"] for row in after],
        "cardinality_before": len(before),
        "cardinality_after": len(after),
        "external_domain_argument_present": False,
    }
    (PACKAGE / "outputs" / "orthad_live_readout_domain.json").write_text(json.dumps(domain_record, indent=2))

    latched = crossing.after_l.latched_axes[-1]
    (PACKAGE / "outputs" / "orthad_live_latched_axis.json").write_text(json.dumps({
        "crossing_local_qbl_word": crossing.qbl_word,
        "pair_after_B": [crossing.after_b.u, crossing.after_b.v],
        "floor_denominator": crossing.after_b.u * crossing.after_b.v,
        "phase_quarters_before_L": crossing.after_b.phase_quarters,
        "latched_axis": latched.as_record(),
    }, indent=2))


if __name__ == "__main__":
    main()
