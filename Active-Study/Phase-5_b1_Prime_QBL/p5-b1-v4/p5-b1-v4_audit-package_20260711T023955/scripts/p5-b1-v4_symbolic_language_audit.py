#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
import math
from decimal import Decimal, getcontext
from pathlib import Path
from typing import Dict, Iterable, Tuple

Interval = Tuple[Decimal, Decimal]

GAMMA_TEXT = "8.4702446042907841279349898711327462608"
STATES = ("7", "8", "9")
M = ((0, 1, 1), (1, 1, 1), (1, 1, 0))


def intersection(left: Interval, right: Interval) -> Interval | None:
    lo = max(left[0], right[0])
    hi = min(left[1], right[1])
    return (lo, hi) if hi > lo else None


def branch_image(interval: Interval, carry: str, gamma: Decimal) -> Interval:
    offset = gamma - Decimal(int(carry))
    return (Decimal(2) * interval[0] + offset, Decimal(2) * interval[1] + offset)


def partitions(a: Decimal) -> Dict[str, Interval]:
    return {
        "7": (Decimal(-1), -Decimal("0.5") - a),
        "8": (-Decimal("0.5") - a, -a),
        "9": (-a, Decimal(0)),
    }


def actual_cylinders(max_depth: int, gamma: Decimal) -> list[dict[str, Interval]]:
    a = (gamma - Decimal(8)) / Decimal(2)
    parts = partitions(a)
    levels: list[dict[str, Interval]] = [{state: parts[state] for state in STATES}]
    for _depth in range(2, max_depth + 1):
        previous = levels[-1]
        current: dict[str, Interval] = {}
        for word, interval in previous.items():
            image = branch_image(interval, word[-1], gamma)
            for state in STATES:
                clipped = intersection(image, parts[state])
                if clipped is not None:
                    current[word + state] = clipped
        levels.append(current)
    return levels


def edge_shift_words(depth: int) -> set[str]:
    words = set(STATES)
    if depth == 1:
        return words
    index = {state: i for i, state in enumerate(STATES)}
    for _ in range(2, depth + 1):
        words = {
            word + nxt
            for word in words
            for nxt in STATES
            if M[index[word[-1]]][index[nxt]]
        }
    return words


def edge_shift_count(depth: int) -> int:
    vector = [1, 1, 1]
    for _ in range(1, depth):
        vector = [sum(vector[i] * M[i][j] for i in range(3)) for j in range(3)]
    return sum(vector)


def interval_payload(interval: Interval | None) -> dict[str, str | bool]:
    if interval is None:
        return {"nonempty": False, "lo": "", "hi": ""}
    return {"nonempty": True, "lo": str(interval[0]), "hi": str(interval[1])}


def run(max_depth: int) -> dict:
    getcontext().prec = 100
    gamma = Decimal(GAMMA_TEXT)
    a = (gamma - Decimal(8)) / Decimal(2)
    levels = actual_cylinders(max_depth, gamma)

    actual3 = levels[2]
    envelope3 = edge_shift_words(3)
    all_words = sorted({a + b + c for a in STATES for b in STATES for c in STATES})
    length3_rows = []
    for word in all_words:
        actual_interval = actual3.get(word)
        length3_rows.append(
            {
                "word": word,
                "pairwise_envelope": word in envelope3,
                **interval_payload(actual_interval),
            }
        )

    complexity = []
    for depth, level in enumerate(levels, start=1):
        complexity.append(
            {
                "length": depth,
                "actual_nonempty_cylinders": len(level),
                "edge_shift_paths": edge_shift_count(depth),
                "difference": edge_shift_count(depth) - len(level),
            }
        )

    prefix_98 = levels[1]["98"]
    image_989 = branch_image(prefix_98, "8", gamma)
    i9 = partitions(a)["9"]
    forbidden_989 = intersection(image_989, i9) is None

    missing_envelope_words = sorted(envelope3 - set(actual3))
    expected_missing = ["787", "989"]
    entropy_envelope = math.log(1 + math.sqrt(2))
    entropy_degree2_bound = math.log(2)

    checks = {
        "length1_count_is_3": len(levels[0]) == 3,
        "length2_count_is_7": len(levels[1]) == 7,
        "length3_actual_count_is_15": len(levels[2]) == 15,
        "length3_envelope_count_is_17": edge_shift_count(3) == 17,
        "forbidden_989": forbidden_989,
        "actual_missing_envelope_words_match": missing_envelope_words == expected_missing,
        "edge_envelope_entropy_exceeds_degree2_bound": entropy_envelope > entropy_degree2_bound,
    }

    return {
        "status": "PASS" if all(checks.values()) else "FAIL",
        "parameter": {"gamma": str(gamma), "a": str(a)},
        "checks": checks,
        "forbidden_989": {
            "prefix_98_current_interval": interval_payload(prefix_98),
            "next_image_under_F8": interval_payload(image_989),
            "I9": interval_payload(i9),
            "intersection_nonempty": not forbidden_989,
            "symbolic_reason": "For a<1/4, -2+6a<-a, so the entire image lies left of I9.",
        },
        "length3_missing_from_actual_but_admitted_by_envelope": missing_envelope_words,
        "entropy": {
            "edge_shift_log_1_plus_sqrt2": entropy_envelope,
            "degree_two_upper_bound_log2": entropy_degree2_bound,
            "difference": entropy_envelope - entropy_degree2_bound,
        },
        "complexity": complexity,
        "length3_rows": length3_rows,
    }


def write_outputs(result: dict, out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "p5-b1-v4_symbolic-language-audit.json").write_text(
        json.dumps(result, indent=2) + "\n", encoding="utf-8"
    )

    with (out_dir / "p5-b1-v4_word-complexity.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=["length", "actual_nonempty_cylinders", "edge_shift_paths", "difference"],
        )
        writer.writeheader()
        writer.writerows(result["complexity"])

    with (out_dir / "p5-b1-v4_length3-language.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=["word", "pairwise_envelope", "nonempty", "lo", "hi"],
        )
        writer.writeheader()
        writer.writerows(result["length3_rows"])


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-depth", type=int, default=12)
    parser.add_argument("--out", type=Path, default=Path("outputs"))
    args = parser.parse_args()
    if not 3 <= args.max_depth <= 16:
        raise SystemExit("--max-depth must be between 3 and 16")
    result = run(args.max_depth)
    write_outputs(result, args.out)
    print(result["status"])
    print(json.dumps(result["checks"], indent=2))
    if result["status"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
