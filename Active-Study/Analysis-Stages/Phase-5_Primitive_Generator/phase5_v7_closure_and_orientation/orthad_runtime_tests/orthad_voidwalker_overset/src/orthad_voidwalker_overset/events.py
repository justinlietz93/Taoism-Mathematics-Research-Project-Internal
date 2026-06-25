from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple


@dataclass(frozen=True)
class HistoryEvent:
    kind: str
    chart: int | None = None
    edge: Tuple[int, int] | None = None
    value: int | None = None
    label: str = ""

    def support(self) -> Tuple[str, ...]:
        if self.kind == "Q" and self.chart is not None:
            return (f"c:{self.chart}",)
        if self.kind in {"B", "L"} and self.edge is not None:
            i, j = sorted(self.edge)
            return (f"c:{i}", f"c:{j}", f"e:{i}-{j}")
        return ("global",)

    def key(self) -> Tuple:
        e = tuple(sorted(self.edge)) if self.edge is not None else None
        return (self.kind, -1 if self.chart is None else self.chart, e, -999 if self.value is None else self.value, self.label)


@dataclass(frozen=True)
class WalkerEvent:
    kind: str
    tick: int
    walker: int
    node: int | None = None
    edge: Tuple[int, int] | None = None
    value: float = 0.0
    residual: float = 0.0
    path: Tuple[int, ...] = ()
