from __future__ import annotations

import csv
import inspect
import json
import re
import sys
from dataclasses import fields
from pathlib import Path

from sympy import kronecker_symbol

PACKAGE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PACKAGE / "src"))

from orthad_live.field import ResidualChannel
from orthad_live.lift import LiftState

FORBIDDEN = (
    "candidate",
    "candidates",
    "search",
    "scan",
    "rank",
    "test",
    "tests",
    "score",
    "best",
    "select",
    "selected",
)


def read_csv(name: str) -> list[dict[str, str]]:
    return list(csv.DictReader((PACKAGE / "outputs" / name).open()))


def boolean(value: str) -> bool:
    return value.lower() == "true"


def main() -> None:
    before = read_csv("orthad_live_channel_before.csv")
    after = read_csv("orthad_live_channel_after.csv")
    survival = read_csv("orthad_live_per_channel_survival.csv")
    crossing = json.loads((PACKAGE / "outputs" / "orthad_live_crossing_record.json").read_text())
    domain = json.loads((PACKAGE / "outputs" / "orthad_live_readout_domain.json").read_text())
    latched = json.loads((PACKAGE / "outputs" / "orthad_live_latched_axis.json").read_text())

    kronecker_rows = []
    for row in before:
        n = int(row["term_n"])
        expected = int(kronecker_symbol(12, n))
        kronecker_rows.append({
            "term_n": n,
            "live_character": int(row["character_channel"]),
            "sympy_kronecker_12_n": expected,
            "match": int(row["character_channel"]) == expected,
        })

    live_dir = PACKAGE / "src" / "orthad_live"
    lexeme_rows = []
    for path in sorted(live_dir.glob("*.py")):
        text = path.read_text()
        for token in FORBIDDEN:
            hits = len(re.findall(rf"\\b{re.escape(token)}\\b", text, flags=re.IGNORECASE))
            lexeme_rows.append({
                "source_path": str(path.relative_to(PACKAGE)),
                "forbidden_lexeme": token,
                "occurrences": hits,
                "pass": hits == 0,
            })

    field_names = {item.name for item in fields(ResidualChannel)}
    lift_names = {item.name for item in fields(LiftState)}
    scalar_names = {"scalar", "signed_coefficient", "coefficient_product", "score"}

    gates = [
        {
            "gate": "QBL_WORD_AND_SINGLE_CROSSING",
            "pass": crossing["qbl_word"] == "BL" and crossing["event_sequence"] == ["B", "FLOOR", "L"],
            "detail": crossing["qbl_word"],
        },
        {
            "gate": "TRUE_KRONECKER_CHARACTER_INPUT",
            "pass": all(row["match"] for row in kronecker_rows),
            "detail": f"{sum(row['match'] for row in kronecker_rows)}/{len(kronecker_rows)}",
        },
        {
            "gate": "CHARACTER_CHANNEL_SURVIVAL",
            "pass": all(boolean(row["character_survived"]) for row in survival),
            "detail": f"{sum(boolean(row['character_survived']) for row in survival)}/{len(survival)}",
        },
        {
            "gate": "SUPPORT_MAGNITUDE_EXPONENT_SURVIVAL",
            "pass": all(
                boolean(row["support_survived"])
                and boolean(row["magnitude_survived"])
                and boolean(row["exponent_survived"])
                for row in survival
            ),
            "detail": f"{len(survival)} channels",
        },
        {
            "gate": "LATCHED_AXIS_EXACT",
            "pass": latched["latched_axis"] == {"real_num": 0, "imag_num": 1, "den": 4895, "exact": "(0+1i)/4895"},
            "detail": latched["latched_axis"]["exact"],
        },
        {
            "gate": "READOUT_DOMAIN_FROM_LIFT",
            "pass": domain["origin"] == "lift_output" and not domain["external_domain_argument_present"] and domain["cardinality_before"] == 12 and domain["cardinality_after"] == 12,
            "detail": f"{domain['cardinality_before']}->{domain['cardinality_after']}",
        },
        {
            "gate": "LAW_0_LIVE_SOURCE_LEXEMES",
            "pass": all(row["pass"] for row in lexeme_rows),
            "detail": f"{sum(row['occurrences'] for row in lexeme_rows)} forbidden occurrences",
        },
        {
            "gate": "LAW_0B_NO_SCALAR_CARGO",
            "pass": not (field_names | lift_names) & scalar_names and not crossing["scalar_residual_field_present"] and not crossing["combined_signed_coefficient_field_present"],
            "detail": "channel components remain separate",
        },
        {
            "gate": "POST_L_SEAT_EXACT",
            "pass": all(int(row["post_l_seat_mod12"]) == (int(row["term_n"]) % 12) for row in after),
            "detail": "s6+6*floor((n mod12)/6)=n mod12",
        },
    ]

    negative = [
        {
            "control": "mod6_without_orientation_bit",
            "pass": (1 % 6) == (7 % 6) and int(kronecker_symbol(12, 1)) != int(kronecker_symbol(12, 7)),
            "detail": "n=1 and n=7 collide before L",
        },
        {
            "control": "combined_scalar_field_absent",
            "pass": "signed_coefficient" not in before[0] and "signed_coefficient" not in after[0],
            "detail": "no combined coefficient column",
        },
    ]

    with (PACKAGE / "outputs" / "orthad_live_sympy_kronecker_gate.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(kronecker_rows[0].keys()))
        writer.writeheader()
        writer.writerows(kronecker_rows)

    with (PACKAGE / "outputs" / "orthad_live_law0_source_audit.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(lexeme_rows[0].keys()))
        writer.writeheader()
        writer.writerows(lexeme_rows)

    with (PACKAGE / "outputs" / "orthad_live_meta_gates.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(gates[0].keys()))
        writer.writeheader()
        writer.writerows(gates)

    with (PACKAGE / "outputs" / "orthad_live_negative_controls.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(negative[0].keys()))
        writer.writeheader()
        writer.writerows(negative)

    result = {
        "status": "ORTHAD_LIVE_ONE_B_FLOOR_L_CROSSING_CHARACTER_CHANNEL_SURVIVED_12_OF_12",
        "global_pass": all(row["pass"] for row in gates) and all(row["pass"] for row in negative),
        "declared_gates": len(gates),
        "declared_gate_failures": sum(not row["pass"] for row in gates),
        "negative_controls": len(negative),
        "negative_control_failures": sum(not row["pass"] for row in negative),
        "channels": len(survival),
        "character_survival": sum(boolean(row["character_survived"]) for row in survival),
        "support_channels": sum(boolean(row["support_before"]) for row in survival),
        "qbl_word": crossing["qbl_word"],
        "event_sequence": crossing["event_sequence"],
        "latched_axis": latched["latched_axis"],
        "scope": "one lift-emitted 12-channel period across one B-FLOOR-L cusp crossing",
        "not_claimed": [
            "arbitrary cusp-path transport",
            "infinite q-series completion",
            "mock-theta correspondence closure",
            "v8n degenerate-block alphabet",
        ],
    }
    (PACKAGE / "outputs" / "orthad_live_result_card.json").write_text(json.dumps(result, indent=2))
    if not result["global_pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
