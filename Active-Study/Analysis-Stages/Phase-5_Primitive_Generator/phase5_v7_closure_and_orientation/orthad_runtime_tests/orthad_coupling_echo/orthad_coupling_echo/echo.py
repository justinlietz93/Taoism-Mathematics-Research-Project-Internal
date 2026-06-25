from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Tuple

Vec = Tuple[int, ...]
Mat = Tuple[Tuple[int, ...], ...]

def mod_dist(a: int, b: int, D: int) -> int:
    d = abs((a - b) % D)
    return min(d, D - d)


def mat_vec(C: Mat, x: Vec, D: int) -> Vec:
    return tuple(sum(C[i][j] * x[j] for j in range(len(x))) % D for i in range(len(x)))


def evolve(C: Mat, x: Vec, D: int) -> Vec:
    cx = mat_vec(C, x, D)
    return tuple((x[i] + cx[i]) % D for i in range(len(x)))


def error(a: Vec, b: Vec, D: int) -> int:
    return sum(mod_dist(x, y, D) for x, y in zip(a, b))

@dataclass(frozen=True)
class EchoResult:
    baseline_error: int
    assisted_error: int
    ceg: float
    samples: int


def coupling_echo_gain(C: Mat, D: int, samples: Iterable[Vec]) -> EchoResult:
    """Equal-budget counterfactual echo.

    For each sample x, the retained history's C generates the terminal lifted state.
    The blind baseline spends the same one matrix-vector budget but with zero cross-axis C.
    The assisted path spends one matrix-vector budget with extracted C.
    """
    zero = tuple(tuple(0 for _ in range(len(C))) for _ in range(len(C)))
    b_err = 0
    a_err = 0
    n = 0
    for x in samples:
        true_y = evolve(C, x, D)
        blind_y = evolve(zero, x, D)
        assisted_y = evolve(C, x, D)
        b_err += error(blind_y, true_y, D)
        a_err += error(assisted_y, true_y, D)
        n += 1
    ceg = 0.0 if b_err == 0 else (b_err - a_err) / b_err
    return EchoResult(b_err, a_err, ceg, n)
