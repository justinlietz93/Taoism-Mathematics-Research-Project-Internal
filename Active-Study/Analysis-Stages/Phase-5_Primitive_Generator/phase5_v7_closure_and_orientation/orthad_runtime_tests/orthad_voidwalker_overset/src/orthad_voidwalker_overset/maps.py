from __future__ import annotations

from collections import defaultdict, deque
from dataclasses import dataclass, field
from typing import Deque, Dict, Iterable, List, Tuple
import math

from .events import WalkerEvent


def _decay(value: float, dt: int, half_life: int) -> float:
    if dt <= 0:
        return value
    return value * (2.0 ** (-(dt / max(1.0, float(half_life)))))


class DecayMap:
    def __init__(self, half_life: int = 50, keep_max: int = 2048):
        self.half_life = int(max(1, half_life))
        self.keep_max = int(max(16, keep_max))
        self.value: Dict[object, float] = {}
        self.last: Dict[object, int] = {}

    def add(self, key: object, tick: int, amount: float) -> None:
        old = self.value.get(key, 0.0)
        old = _decay(old, int(tick) - self.last.get(key, int(tick)), self.half_life)
        self.value[key] = max(0.0, old + float(amount))
        self.last[key] = int(tick)
        if len(self.value) > self.keep_max:
            self._prune()

    def get(self, key: object, tick: int) -> float:
        if key not in self.value:
            return 0.0
        return _decay(self.value[key], int(tick) - self.last.get(key, int(tick)), self.half_life)

    def _prune(self) -> None:
        keep = sorted(self.value.items(), key=lambda kv: kv[1], reverse=True)[: self.keep_max]
        keep_keys = {k for k, _ in keep}
        self.value = {k: self.value[k] for k in keep_keys}
        self.last = {k: self.last[k] for k in keep_keys if k in self.last}

    def head(self, tick: int, n: int = 8) -> List[Tuple[object, float]]:
        pairs = [(k, self.get(k, tick)) for k in self.value]
        pairs.sort(key=lambda kv: kv[1], reverse=True)
        return pairs[:n]

    def max_value(self, tick: int) -> float:
        vals = [self.get(k, tick) for k in self.value]
        return max(vals) if vals else 0.0


class ColdMap:
    def __init__(self, universe: Iterable[object], half_life: int = 50):
        self.half_life = int(max(1, half_life))
        self.last_seen = {k: -self.half_life * 8 for k in universe}

    def touch(self, key: object, tick: int) -> None:
        self.last_seen[key] = int(tick)

    def score(self, key: object, tick: int) -> float:
        age = int(tick) - self.last_seen.get(key, -self.half_life * 8)
        return 1.0 - (2.0 ** (-(max(0, age) / float(self.half_life))))

    def coldest(self, keys: Iterable[object], tick: int) -> object | None:
        keys = list(keys)
        if not keys:
            return None
        return max(keys, key=lambda k: self.score(k, tick))

    def max_value(self, tick: int) -> float:
        return max((self.score(k, tick) for k in self.last_seen), default=0.0)


@dataclass
class MemoryMap:
    edge_sum: Dict[Tuple[int, int], float] = field(default_factory=lambda: defaultdict(float))
    edge_count: Dict[Tuple[int, int], int] = field(default_factory=lambda: defaultdict(int))
    cycle_residuals: List[Tuple[int, Tuple[int, ...], int]] = field(default_factory=list)
    conflicts: int = 0

    def observe_edge(self, edge: Tuple[int, int], value: float) -> None:
        old_count = self.edge_count[edge]
        if old_count > 0:
            old_mean = self.edge_sum[edge] / old_count
            if abs(old_mean - value) > 1e-9:
                self.conflicts += 1
        self.edge_sum[edge] += float(value)
        self.edge_count[edge] += 1

    def mean_edge(self, edge: Tuple[int, int]) -> float | None:
        count = self.edge_count.get(edge, 0)
        if count <= 0:
            return None
        return self.edge_sum[edge] / count

    def record_cycle(self, tick: int, path: Tuple[int, ...], residual: int) -> None:
        self.cycle_residuals.append((int(tick), path, int(residual)))

    def max_residual(self) -> int:
        return max((abs(r) for _, _, r in self.cycle_residuals), default=0)


class TelemetryMaps:
    def __init__(self, node_universe: Iterable[int], edge_universe: Iterable[Tuple[int, int]]):
        keys = list(node_universe) + list(edge_universe)
        self.heat = DecayMap(half_life=20)
        self.trail = DecayMap(half_life=80)
        self.excitation = DecayMap(half_life=35)
        self.inhibition = DecayMap(half_life=35)
        self.cold = ColdMap(keys, half_life=30)
        self.memory = MemoryMap()
        self.topology_spikes: List[WalkerEvent] = []
        self.events_seen = 0

    def fold(self, events: Iterable[WalkerEvent], modulus: int) -> None:
        for ev in events:
            self.events_seen += 1
            if ev.node is not None:
                self.heat.add(ev.node, ev.tick, 0.25)
                self.trail.add(ev.node, ev.tick, 0.05)
                self.cold.touch(ev.node, ev.tick)
            if ev.edge is not None:
                self.heat.add(ev.edge, ev.tick, 0.5)
                self.trail.add(ev.edge, ev.tick, 0.1)
                self.cold.touch(ev.edge, ev.tick)
                if ev.kind == "edge_transfer":
                    self.memory.observe_edge(ev.edge, ev.value)
                    mag = min(1.0, abs(float(ev.value)) / max(1.0, float(modulus)))
                    self.excitation.add(ev.edge, ev.tick, mag)
            if ev.kind == "cycle_hit":
                self.memory.record_cycle(ev.tick, ev.path, int(ev.residual))
                if int(ev.residual) % int(modulus) != 0:
                    self.inhibition.add(ev.path, ev.tick, 1.0 + abs(float(ev.residual)))
                    self.topology_spikes.append(ev)

    def snapshot(self, tick: int) -> dict:
        return {
            "events_seen": int(self.events_seen),
            "heat_max": float(self.heat.max_value(tick)),
            "cold_max": float(self.cold.max_value(tick)),
            "trail_max": float(self.trail.max_value(tick)),
            "excitation_max": float(self.excitation.max_value(tick)),
            "inhibition_max": float(self.inhibition.max_value(tick)),
            "topology_spikes": int(len(self.topology_spikes)),
            "memory_edges": int(len(self.memory.edge_count)),
            "cycle_hits": int(len(self.memory.cycle_residuals)),
            "max_cycle_residual_seen": int(self.memory.max_residual()),
        }
