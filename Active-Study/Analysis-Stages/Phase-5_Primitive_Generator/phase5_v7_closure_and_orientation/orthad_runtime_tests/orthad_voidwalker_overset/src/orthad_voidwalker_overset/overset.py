from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Iterable, List, Sequence, Set, Tuple

from .history import CompiledHistory


def edge_key(i: int, j: int) -> Tuple[int, int]:
    return (i, j) if i <= j else (j, i)


@dataclass
class OversetGraph:
    n: int
    modulus: int
    transfer: Dict[Tuple[int, int], int]

    def neighbors(self, node: int) -> List[int]:
        out: List[int] = []
        for i, j in self.transfer:
            if i == node:
                out.append(j)
            elif j == node:
                out.append(i)
        return sorted(out)

    def edges(self) -> Tuple[Tuple[int, int], ...]:
        return tuple(sorted(self.transfer.keys()))

    def value(self, i: int, j: int) -> int:
        e = edge_key(i, j)
        val = int(self.transfer.get(e, 0)) % self.modulus
        if (i, j) == e:
            return val
        return (-val) % self.modulus

    def cycle_residual(self, cycle: Sequence[int]) -> int:
        if len(cycle) < 3:
            return 0
        total = 0
        nodes = list(cycle)
        if nodes[0] != nodes[-1]:
            nodes.append(nodes[0])
        for a, b in zip(nodes, nodes[1:]):
            total = (total + self.value(a, b)) % self.modulus
        return total % self.modulus

    def all_triangles(self) -> Tuple[Tuple[int, int, int], ...]:
        triangles: List[Tuple[int, int, int]] = []
        e = set(self.edges())
        for i in range(self.n):
            for j in range(i + 1, self.n):
                for k in range(j + 1, self.n):
                    if edge_key(i, j) in e and edge_key(j, k) in e and edge_key(i, k) in e:
                        triangles.append((i, j, k))
        return tuple(triangles)

    def max_cycle_residual(self) -> int:
        vals = [self.cycle_residual(t) for t in self.all_triangles()]
        return max(vals) if vals else 0

    def adjacency_density(self) -> float:
        denom = self.n * (self.n - 1) / 2
        return len(self.transfer) / denom if denom else 0.0

    def out_degree_gini(self) -> float:
        deg = [0 for _ in range(self.n)]
        for i, j in self.transfer:
            deg[i] += 1
            deg[j] += 1
        xs = sorted(deg)
        total = sum(xs)
        if total == 0:
            return 0.0
        n = len(xs)
        return sum((2 * (idx + 1) - n - 1) * x for idx, x in enumerate(xs)) / (n * total)


def graph_from_history(compiled: CompiledHistory) -> OversetGraph:
    return OversetGraph(n=compiled.n, modulus=compiled.modulus, transfer=dict(compiled.transfer))
