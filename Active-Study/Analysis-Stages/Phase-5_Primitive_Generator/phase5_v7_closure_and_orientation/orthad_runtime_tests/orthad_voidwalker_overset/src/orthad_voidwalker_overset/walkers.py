from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Tuple
import random

from .events import WalkerEvent
from .overset import OversetGraph, edge_key
from .maps import TelemetryMaps


@dataclass
class VoidWalker:
    wid: int
    node: int
    mode: str
    path: List[int] = field(default_factory=list)

    def __post_init__(self) -> None:
        if not self.path:
            self.path = [self.node]


def _edge_value(graph: OversetGraph, a: int, b: int) -> Tuple[Tuple[int, int], int]:
    e = edge_key(a, b)
    return e, graph.transfer[e]


def _choose_frontier(graph: OversetGraph, maps: TelemetryMaps, node: int, tick: int) -> int:
    ns = graph.neighbors(node)
    if not ns:
        return node
    return max(ns, key=lambda j: maps.cold.score(edge_key(node, j), tick))


def _choose_heat(graph: OversetGraph, maps: TelemetryMaps, node: int, tick: int, rng: random.Random) -> int:
    ns = graph.neighbors(node)
    if not ns:
        return node
    # Prefer heat but allow exploration.
    if rng.random() < 0.15:
        return rng.choice(ns)
    return max(ns, key=lambda j: maps.heat.get(edge_key(node, j), tick) + 0.1 * maps.excitation.get(edge_key(node, j), tick))


def _choose_cycle(graph: OversetGraph, maps: TelemetryMaps, walker: VoidWalker, tick: int, rng: random.Random) -> int:
    ns = graph.neighbors(walker.node)
    if not ns:
        return walker.node
    # Close a 3- or 4-cycle if possible, otherwise pick cold frontier.
    recent = walker.path[-4:]
    for cand in ns:
        if cand in recent[:-1] and len(set(recent[recent.index(cand):] + [cand])) >= 3:
            return cand
    return _choose_frontier(graph, maps, walker.node, tick)


def _cycle_path_if_closed(path: List[int]) -> Tuple[int, ...] | None:
    if len(path) < 4:
        return None
    last = path[-1]
    for idx in range(max(0, len(path) - 6), len(path) - 2):
        if path[idx] == last:
            cycle = tuple(path[idx:-1])
            if len(set(cycle)) >= 3:
                return cycle
    return None


def step_walker(graph: OversetGraph, maps: TelemetryMaps, walker: VoidWalker, tick: int, rng: random.Random) -> List[WalkerEvent]:
    events: List[WalkerEvent] = [WalkerEvent("vt_touch", tick=tick, walker=walker.wid, node=walker.node)]
    if walker.mode == "frontier":
        nxt = _choose_frontier(graph, maps, walker.node, tick)
    elif walker.mode == "heat":
        nxt = _choose_heat(graph, maps, walker.node, tick, rng)
    elif walker.mode == "cycle":
        nxt = _choose_cycle(graph, maps, walker, tick, rng)
    else:
        ns = graph.neighbors(walker.node)
        nxt = rng.choice(ns) if ns else walker.node

    if nxt != walker.node:
        e, val = _edge_value(graph, walker.node, nxt)
        events.append(WalkerEvent("edge_transfer", tick=tick, walker=walker.wid, edge=e, value=float(val)))
        walker.node = nxt
        walker.path.append(nxt)
        if len(walker.path) > 12:
            walker.path = walker.path[-12:]
        cycle = _cycle_path_if_closed(walker.path)
        if cycle is not None:
            residual = graph.cycle_residual(cycle)
            events.append(WalkerEvent("cycle_hit", tick=tick, walker=walker.wid, residual=float(residual), path=cycle))
    return events


def run_voidwalkers(graph: OversetGraph, ticks: int = 128, walkers: int = 12, seed: int = 0) -> TelemetryMaps:
    rng = random.Random(int(seed))
    maps = TelemetryMaps(range(graph.n), graph.edges())
    modes = ["frontier", "cycle", "heat", "random"]
    ws: List[VoidWalker] = []
    for wid in range(int(walkers)):
        node = wid % graph.n
        ws.append(VoidWalker(wid=wid, node=node, mode=modes[wid % len(modes)]))
    for tick in range(int(ticks)):
        batch: List[WalkerEvent] = []
        for w in ws:
            if tick > 0 and tick % 37 == 0 and w.mode == "frontier":
                # Blue-noise reseed: push a frontier scout to a cold chart without scanning edge weights.
                cold_node = maps.cold.coldest(range(graph.n), tick)
                if cold_node is not None:
                    w.node = int(cold_node)
                    w.path = [w.node]
            batch.extend(step_walker(graph, maps, w, tick, rng))
        maps.fold(batch, graph.modulus)
    return maps
