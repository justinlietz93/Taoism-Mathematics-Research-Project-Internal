from __future__ import annotations

from dataclasses import dataclass, field
from typing import Iterable

from .events import CHARTS, Event
from .coupling import canon_pair

@dataclass
class Telemetry:
    heat: dict[str, int] = field(default_factory=dict)
    excitation: dict[str, int] = field(default_factory=dict)
    inhibition: dict[str, int] = field(default_factory=dict)
    memory: dict[str, int] = field(default_factory=dict)
    trail: list[str] = field(default_factory=list)
    cycle_hits: int = 0
    boundary_spikes: int = 0
    topology_spikes: int = 0

    def as_dict(self) -> dict[str, object]:
        return {
            "heat": self.heat,
            "excitation": self.excitation,
            "inhibition": self.inhibition,
            "memory": self.memory,
            "trail": self.trail,
            "cycle_hits": self.cycle_hits,
            "boundary_spikes": self.boundary_spikes,
            "topology_spikes": self.topology_spikes,
        }


def fold_telemetry(events: Iterable[Event], cocycle_residual: int) -> Telemetry:
    t = Telemetry()
    seen_pairs: set[str] = set()
    for ev in events:
        tok = ev.token()
        t.trail.append(tok)
        if ev.kind == "L":
            edge = "".join(canon_pair(ev.support))
            t.heat[edge] = t.heat.get(edge, 0) + 1
            t.excitation[edge] = t.excitation.get(edge, 0) + (1 if ev.sign > 0 else 0)
            t.inhibition[edge] = t.inhibition.get(edge, 0) + (1 if ev.sign < 0 else 0)
            t.memory[edge] = t.memory.get(edge, 0) + ev.sign
            t.boundary_spikes += 1
            seen_pairs.add(edge)
            if set(seen_pairs) == {"AB", "AC", "BC"}:
                t.cycle_hits += 1
                seen_pairs.clear()
        elif ev.kind in {"Q", "B"}:
            chart = next(iter(ev.support))
            t.heat[chart] = t.heat.get(chart, 0) + 1
    if cocycle_residual != 0:
        t.topology_spikes += 1
        t.inhibition["cycle"] = t.inhibition.get("cycle", 0) + abs(cocycle_residual)
    return t
