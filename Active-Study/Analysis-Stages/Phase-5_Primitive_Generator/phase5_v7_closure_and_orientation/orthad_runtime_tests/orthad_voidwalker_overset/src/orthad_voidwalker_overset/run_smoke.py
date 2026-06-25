from __future__ import annotations

import csv
import json
import random
from pathlib import Path
from typing import List

from .harness import run_scenario
from .scenarios import base_scenarios, random_illegal_scenario, random_legal_scenario


def main() -> int:
    root = Path(__file__).resolve().parents[2]
    outdir = root / "outputs"
    outdir.mkdir(parents=True, exist_ok=True)
    modulus = 7
    base = base_scenarios(modulus)
    results = [run_scenario(sc, ticks=180, walkers=18, seed=11) for sc in base]

    rng = random.Random(1234)
    random_results = []
    for idx in range(40):
        n = 4 if idx < 24 else 5
        sc = random_legal_scenario(idx, n, modulus, rng)
        random_results.append(run_scenario(sc, ticks=220 if n == 4 else 300, walkers=20 if n == 4 else 24, seed=idx + 20))
    for idx in range(20):
        n = 4 if idx < 12 else 5
        sc = random_illegal_scenario(idx + 100, n, modulus, rng)
        random_results.append(run_scenario(sc, ticks=220 if n == 4 else 300, walkers=20 if n == 4 else 24, seed=idx + 90))

    all_results = results + random_results
    fields = list(all_results[0].to_dict().keys())
    with (outdir / "scenario_results.csv").open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for r in all_results:
            writer.writerow(r.to_dict())

    h1, h2, h3, h4 = results
    legal_rewrite_invariance = (
        h1.visible_projection == h2.visible_projection
        and h1.true_coupling_signature == h2.true_coupling_signature
        and h1.matrix_match and h2.matrix_match
    )
    same_projection_separation = (
        h1.visible_projection == h3.visible_projection
        and h1.true_coupling_signature != h3.true_coupling_signature
        and h3.matrix_match
    )
    illegal_rejected = (not h4.admitted) and h4.topology_spikes > 0
    random_legal = [r for r in random_results if r.expected_admissible]
    random_illegal = [r for r in random_results if not r.expected_admissible]
    random_legal_pass_rate = sum(r.pass_case for r in random_legal) / len(random_legal)
    random_illegal_pass_rate = sum(r.pass_case for r in random_illegal) / len(random_illegal)
    legal_gains = [r.coupling_echo_gain for r in all_results if r.expected_admissible]
    bad_spikes = [r.topology_spikes for r in all_results if not r.expected_admissible]
    good_spikes = [r.topology_spikes for r in all_results if r.expected_admissible]
    card = {
        "package": "orthad_voidwalker_overset",
        "claim_class": "bounded smoke/adversarial harness, not theorem",
        "base_gates": {
            "legal_rewrite_invariance": legal_rewrite_invariance,
            "same_projection_different_retained_separation": same_projection_separation,
            "illegal_cocycle_rejected_by_walkers": illegal_rejected,
        },
        "random_stress": {
            "legal_cases": len(random_legal),
            "illegal_cases": len(random_illegal),
            "legal_pass_rate": random_legal_pass_rate,
            "illegal_pass_rate": random_illegal_pass_rate,
            "min_legal_coupling_echo_gain": min(legal_gains),
            "median_legal_coupling_echo_gain": sorted(legal_gains)[len(legal_gains)//2],
            "max_good_topology_spikes": max(good_spikes) if good_spikes else 0,
            "min_bad_topology_spikes": min(bad_spikes) if bad_spikes else 0,
        },
        "global_pass": bool(
            legal_rewrite_invariance
            and same_projection_separation
            and illegal_rejected
            and random_legal_pass_rate >= 0.95
            and random_illegal_pass_rate >= 0.95
            and min(legal_gains) >= 0.99
            and (max(good_spikes) if good_spikes else 0) == 0
            and (min(bad_spikes) if bad_spikes else 0) > 0
        ),
    }
    with (outdir / "result_card.json").open("w") as f:
        json.dump(card, f, indent=2)

    # compact telemetry table
    with (outdir / "gate_summary.txt").open("w") as f:
        f.write(json.dumps(card, indent=2))
        f.write("\n")
    print(json.dumps(card, indent=2))
    return 0 if card["global_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
