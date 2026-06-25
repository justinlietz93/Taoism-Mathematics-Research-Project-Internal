from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Iterable, List, Sequence, Tuple

from .events import HistoryEvent


def _sorted_edge(edge: Tuple[int, int]) -> Tuple[int, int]:
    i, j = edge
    return (i, j) if i <= j else (j, i)


@dataclass
class CompiledHistory:
    n: int
    modulus: int
    potentials: Tuple[int, ...]
    projection: Tuple[int, ...]
    transfer: Dict[Tuple[int, int], int]
    events: Tuple[HistoryEvent, ...]
    normal_word: Tuple[Tuple, ...]
    normal_layers: Tuple[Tuple[Tuple, ...], ...]

    def matrix(self) -> Tuple[Tuple[int, ...], ...]:
        rows: List[List[int]] = [[0 for _ in range(self.n)] for _ in range(self.n)]
        for (i, j), v in self.transfer.items():
            rows[i][j] = v % self.modulus
            rows[j][i] = (-v) % self.modulus
        return tuple(tuple(r) for r in rows)

    def visible_id(self) -> Tuple[int, ...]:
        return self.projection

    def coupling_signature(self) -> Tuple[Tuple[int, int, int], ...]:
        return tuple(sorted((i, j, int(v) % self.modulus) for (i, j), v in self.transfer.items()))


def independent(a: HistoryEvent, b: HistoryEvent) -> bool:
    return set(a.support()).isdisjoint(set(b.support()))


def canonical_word(events: Sequence[HistoryEvent]) -> Tuple[HistoryEvent, ...]:
    # Adjacent independent swaps are legal. Repeatedly place independent events in key order.
    # Dependent events keep their causal order.
    out = list(events)
    changed = True
    while changed:
        changed = False
        for idx in range(len(out) - 1):
            left, right = out[idx], out[idx + 1]
            if independent(left, right) and right.key() < left.key():
                out[idx], out[idx + 1] = right, left
                changed = True
    return tuple(out)


def foata_layers(events: Sequence[HistoryEvent]) -> Tuple[Tuple[Tuple, ...], ...]:
    word = canonical_word(events)
    layers: List[List[HistoryEvent]] = []
    for ev in word:
        placed = False
        for layer in layers:
            if all(independent(ev, other) for other in layer):
                layer.append(ev)
                placed = True
                break
        if not placed:
            layers.append([ev])
    return tuple(tuple(ev.key() for ev in layer) for layer in layers)


def compile_history(n: int, events: Sequence[HistoryEvent], modulus: int = 7) -> CompiledHistory:
    potentials = [0 for _ in range(n)]
    transfer: Dict[Tuple[int, int], int] = {}
    for ev in events:
        if ev.kind == "Q" and ev.chart is not None:
            potentials[ev.chart] = (potentials[ev.chart] + 1) % modulus
        elif ev.kind == "L" and ev.edge is not None:
            i, j = _sorted_edge(ev.edge)
            if ev.value is None:
                val = (potentials[j] - potentials[i]) % modulus
            else:
                val = int(ev.value) % modulus
            transfer[(i, j)] = val
    projection = tuple(p % 2 for p in potentials)
    word = canonical_word(events)
    return CompiledHistory(
        n=int(n),
        modulus=int(modulus),
        potentials=tuple(int(x) for x in potentials),
        projection=projection,
        transfer=transfer,
        events=tuple(events),
        normal_word=tuple(ev.key() for ev in word),
        normal_layers=foata_layers(word),
    )


def make_potential_history(n: int, potentials: Sequence[int], edges: Sequence[Tuple[int, int]], modulus: int = 7) -> Tuple[HistoryEvent, ...]:
    events: List[HistoryEvent] = []
    for chart, count in enumerate(potentials):
        for k in range(int(count) % modulus):
            events.append(HistoryEvent("Q", chart=chart, label=f"q{chart}.{k}"))
    for e in sorted(_sorted_edge(x) for x in edges):
        events.append(HistoryEvent("B", edge=e, label=f"b{e[0]}{e[1]}"))
        events.append(HistoryEvent("L", edge=e, label=f"l{e[0]}{e[1]}"))
    return tuple(events)


def corrupt_one_latch(events: Sequence[HistoryEvent], edge: Tuple[int, int], delta: int = 1, modulus: int = 7) -> Tuple[HistoryEvent, ...]:
    e0 = _sorted_edge(edge)
    out: List[HistoryEvent] = []
    done = False
    for ev in events:
        if not done and ev.kind == "L" and ev.edge is not None and _sorted_edge(ev.edge) == e0:
            base = 0 if ev.value is None else int(ev.value)
            # If value is implicit, the caller should compile first and pass explicit illegal value.
            out.append(HistoryEvent("L", edge=e0, value=(base + delta) % modulus, label=ev.label + ".bad"))
            done = True
        else:
            out.append(ev)
    return tuple(out)


def explicit_latches_from(compiled: CompiledHistory) -> Tuple[HistoryEvent, ...]:
    out: List[HistoryEvent] = []
    for ev in compiled.events:
        if ev.kind == "L" and ev.edge is not None:
            e = _sorted_edge(ev.edge)
            out.append(HistoryEvent("L", edge=e, value=compiled.transfer[e], label=ev.label))
        else:
            out.append(ev)
    return tuple(out)


def legal_adjacent_swap(events: Sequence[HistoryEvent]) -> Tuple[HistoryEvent, ...]:
    out = list(events)
    for idx in range(len(out) - 1):
        if independent(out[idx], out[idx + 1]):
            out[idx], out[idx + 1] = out[idx + 1], out[idx]
            return tuple(out)
    return tuple(out)
