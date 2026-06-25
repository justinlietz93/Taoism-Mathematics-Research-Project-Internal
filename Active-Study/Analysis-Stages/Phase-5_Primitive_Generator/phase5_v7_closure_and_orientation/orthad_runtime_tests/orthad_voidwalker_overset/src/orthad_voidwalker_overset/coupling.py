from __future__ import annotations

from typing import Dict, Tuple, List
import math

from .maps import TelemetryMaps
from .overset import OversetGraph


def extract_transfer_from_memory(graph: OversetGraph, maps: TelemetryMaps) -> Dict[Tuple[int, int], int]:
    out: Dict[Tuple[int, int], int] = {}
    for e in graph.edges():
        val = maps.memory.mean_edge(e)
        if val is not None:
            out[e] = int(round(val)) % graph.modulus
    return out


def matrix_from_transfer(n: int, modulus: int, transfer: Dict[Tuple[int, int], int]) -> Tuple[Tuple[int, ...], ...]:
    rows = [[0 for _ in range(n)] for _ in range(n)]
    for (i, j), v in transfer.items():
        rows[i][j] = int(v) % modulus
        rows[j][i] = (-int(v)) % modulus
    return tuple(tuple(r) for r in rows)


def max_triangle_residual_from_transfer(n: int, modulus: int, transfer: Dict[Tuple[int, int], int]) -> int:
    def val(a: int, b: int) -> int:
        e = (a, b) if a <= b else (b, a)
        x = int(transfer.get(e, 0)) % modulus
        return x if e == (a, b) else (-x) % modulus
    mx = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if all(((a, b) if a <= b else (b, a)) in transfer for a, b in [(i, j), (j, k), (i, k)]):
                    r = (val(i, j) + val(j, k) + val(k, i)) % modulus
                    mx = max(mx, r)
    return mx


def echo_gain(true_matrix: Tuple[Tuple[int, ...], ...], discovered_matrix: Tuple[Tuple[int, ...], ...], modulus: int, seed: int = 0) -> dict:
    # Deterministic hidden-process echo target. The target is generated from true_matrix.
    # Discovery must come from walker memory. Blind baseline uses no coupling.
    n = len(true_matrix)
    x = [((seed + 3) * (i + 2) + 1) % modulus for i in range(n)]
    def apply(mat):
        y = []
        for i in range(n):
            acc = x[i]
            for j in range(n):
                acc += mat[i][j] * x[j]
            y.append(acc % modulus)
        return y
    y_true = apply(true_matrix)
    y_assist = apply(discovered_matrix)
    zero = tuple(tuple(0 for _ in range(n)) for _ in range(n))
    y_blind = apply(zero)
    def err(a, b):
        return math.sqrt(sum((float(aa) - float(bb)) ** 2 for aa, bb in zip(a, b)))
    e_blind = err(y_true, y_blind)
    e_assist = err(y_true, y_assist)
    gain = 0.0 if e_blind == 0 else (e_blind - e_assist) / e_blind
    return {
        "blind_error": float(e_blind),
        "assisted_error": float(e_assist),
        "coupling_echo_gain": float(gain),
        "x": x,
        "y_true": y_true,
        "y_assisted": y_assist,
        "y_blind": y_blind,
    }


def signature(matrix: Tuple[Tuple[int, ...], ...]) -> Tuple[Tuple[int, ...], ...]:
    return matrix
