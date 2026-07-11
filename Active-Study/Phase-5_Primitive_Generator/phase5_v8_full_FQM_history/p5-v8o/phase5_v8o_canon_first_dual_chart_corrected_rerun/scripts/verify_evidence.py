#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from pathlib import Path

from sympy import kronecker_symbol


FORBIDDEN = re.compile(r"\b(search|scan|rank|test|candidate)\b", re.IGNORECASE)


def read_csv(path: Path) -> list[dict]:
    with path.open(newline="") as handle:
        return list(csv.DictReader(handle))


def truth(value: str) -> bool:
    return value.lower() in {"1", "true", "yes"}


def verify(root: Path, mutate_character: bool = False, inject_lexeme: bool = False) -> dict:
    before = {row["channel_id"]: row for row in read_csv(root / "outputs/channel_readout_before.csv")}
    after = read_csv(root / "outputs/channel_readout_after.csv")
    if mutate_character:
        after[0]["character_value"] = str(-int(after[0]["character_value"]) or 1)
    failures = []
    for row in after:
        prior = before[row["source_channel_id"]]
        transported = int(prior["orientation_value"]) * int(row["lap_sign"])
        actual = int(row["character_value"])
        expected = int(kronecker_symbol(12, int(row["address_n"])))
        if not (transported == actual == expected):
            failures.append({"output_slot": int(row["output_slot"]), "transported": transported, "actual": actual, "expected": expected})

    live_paths = [
        root / "src/orthad_canon/domain/models.py",
        root / "src/orthad_canon/domain/exact.py",
        root / "src/orthad_canon/application/compiler.py",
        root / "src/orthad_canon/application/crossing.py",
        root / "src/orthad_canon/application/readout.py",
        root / "src/orthad_canon/application/experiment.py",
    ]
    lexeme_hits = []
    for path in live_paths:
        text = path.read_text()
        if inject_lexeme and path.name == "compiler.py":
            text += "\nsearch\n"
        for match in FORBIDDEN.finditer(text):
            lexeme_hits.append({"path": str(path), "word": match.group(0), "offset": match.start()})

    ablations = read_csv(root / "outputs/ablation_results.csv")
    ablation_failures = [row for row in ablations if truth(row["survival_gate"])]
    gates = read_csv(root / "outputs/declared_gates.csv")
    controls = read_csv(root / "outputs/gate_negative_controls.csv")
    global_pass = (
        len(after) == 12
        and not failures
        and not lexeme_hits
        and not ablation_failures
        and all(truth(row["pass"]) for row in gates)
        and all(truth(row["control_fired"]) for row in controls)
    )
    return {
        "global_pass": global_pass,
        "evidence_failures": failures,
        "lexeme_hits": lexeme_hits,
        "ablation_gate_failures": ablation_failures,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", type=Path)
    parser.add_argument("--mutate-character", action="store_true")
    parser.add_argument("--inject-lexeme", action="store_true")
    args = parser.parse_args()
    result = verify(args.root, args.mutate_character, args.inject_lexeme)
    print(json.dumps(result, indent=2))
    return 0 if result["global_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
