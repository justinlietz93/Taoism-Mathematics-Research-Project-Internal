from __future__ import annotations


def _positions(A: int) -> int:
    return 6 * (2**A)


def _start(A: int) -> int:
    return 1 + 6 * ((2**A) - 1)


def _capacity(j: int) -> int:
    return 2 if j == 1 else 4 if j == 2 else 2 ** (2 * j)


def independent_oracle() -> list[dict[str, object]]:
    A, u, v, phase, k, j, word = 0, 1, 1, 0, 0, 1, ""
    rows: list[dict[str, object]] = []
    saw_l = False
    for tick in range(1, 101):
        positions = _positions(A)
        cap = _capacity(j)
        nu, nv = v, u + v
        can_q = k < positions - 1
        can_b = (nu * nv <= cap) if can_q else (u * v < cap)
        primitive = "B" if can_b else "Q" if can_q else "L"
        before = (A, u, v, phase, k, j, word)
        if primitive == "B":
            u, v = nu, nv
        elif primitive == "Q":
            phase += 1
            k += 1
            j += 1
        else:
            A += 1
            k = 0
            j = _start(A)
        word += primitive
        rows.append({
            "step_index": tick,
            "primitive": primitive,
            "before_tuple": list(before[:6]),
            "after_tuple": [A, u, v, phase, k, j],
            "word_prefix": word,
            "capacity_before": cap,
            "available_positions_before": positions,
        })
        if primitive == "L":
            saw_l = True
        elif saw_l:
            return rows
    raise RuntimeError("oracle did not terminate")
