from __future__ import annotations

import random
from dataclasses import dataclass
from typing import List, Sequence, Tuple

from .events import HistoryEvent
from .history import (
    CompiledHistory,
    compile_history,
    explicit_latches_from,
    legal_adjacent_swap,
    make_potential_history,
)


@dataclass
class Scenario:
    name: str
    compiled: CompiledHistory
    expected_admissible: bool
    notes: str


def complete_edges(n: int) -> Tuple[Tuple[int, int], ...]:
    return tuple((i, j) for i in range(n) for j in range(i + 1, n))


def ring_plus_chord_edges(n: int) -> Tuple[Tuple[int, int], ...]:
    edges = {(i, (i + 1) % n) for i in range(n)}
    edges = {tuple(sorted(e)) for e in edges}
    if n >= 4:
        edges.add((0, 2))
        edges.add((1, 3))
    return tuple(sorted(edges))


def base_scenarios(modulus: int = 7) -> List[Scenario]:
    n = 4
    edges = complete_edges(n)
    h1_events = make_potential_history(n, [0, 1, 2, 3], edges, modulus)
    h1 = compile_history(n, h1_events, modulus)
    h2 = compile_history(n, legal_adjacent_swap(h1_events), modulus)
    h3_events = make_potential_history(n, [2, 1, 0, 5], edges, modulus)
    h3 = compile_history(n, h3_events, modulus)

    # H4: illegal local overlap. Start from explicit legal latches, then corrupt edge 0-2.
    explicit = list(explicit_latches_from(h1))
    out: List[HistoryEvent] = []
    corrupted = False
    for ev in explicit:
        if not corrupted and ev.kind == "L" and ev.edge == (0, 2):
            out.append(HistoryEvent("L", edge=(0, 2), value=((ev.value or 0) + 1) % modulus, label="l02.bad"))
            corrupted = True
        else:
            out.append(ev)
    h4 = compile_history(n, out, modulus)

    return [
        Scenario("H1_legal_baseline", h1, True, "legal complete 4-chart retained history"),
        Scenario("H2_legal_rewrite", h2, True, "adjacent independent swap of H1"),
        Scenario("H3_same_projection_different_retained", h3, True, "same parity projection as H1, different retained potentials"),
        Scenario("H4_illegal_cocycle", h4, False, "one overlap latch corrupted to violate cycle closure"),
    ]


def random_legal_scenario(idx: int, n: int, modulus: int, rng: random.Random) -> Scenario:
    if n <= 4:
        edges = complete_edges(n)
    else:
        edges = ring_plus_chord_edges(n)
    potentials = [rng.randrange(modulus) for _ in range(n)]
    events = make_potential_history(n, potentials, edges, modulus)
    # Apply a few legal adjacent swaps to avoid only canonical order.
    for _ in range(rng.randrange(1, 8)):
        events = legal_adjacent_swap(events)
    return Scenario(f"R{idx:03d}_legal_n{n}", compile_history(n, events, modulus), True, "random potential-derived admissible history")


def random_illegal_scenario(idx: int, n: int, modulus: int, rng: random.Random) -> Scenario:
    sc = random_legal_scenario(idx, n, modulus, rng)
    explicit = list(explicit_latches_from(sc.compiled))
    # Corrupt an edge that participates in at least one triangle so local cycle scouts can detect it.
    edges = set(sc.compiled.transfer.keys())
    triangle_edges = set()
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                tri = {(i, j), (j, k), (i, k)}
                if tri.issubset(edges):
                    triangle_edges.update(tri)
    latch_idxs = [i for i, ev in enumerate(explicit) if ev.kind == "L" and ev.edge in triangle_edges]
    if not latch_idxs:
        latch_idxs = [i for i, ev in enumerate(explicit) if ev.kind == "L"]
    pos = rng.choice(latch_idxs)
    ev = explicit[pos]
    explicit[pos] = HistoryEvent("L", edge=ev.edge, value=((ev.value or 0) + rng.randrange(1, modulus)) % modulus, label=ev.label + ".bad")
    return Scenario(f"R{idx:03d}_illegal_n{n}", compile_history(n, explicit, modulus), False, "random single-latch cocycle violation")
