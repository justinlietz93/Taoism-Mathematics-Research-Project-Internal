from __future__ import annotations

from dataclasses import asdict, dataclass, replace
from fractions import Fraction
from typing import Iterable


@dataclass(frozen=True, slots=True)
class CustodyState:
    A: int = 0
    u: int = 1
    v: int = 1
    phase_quarters: int = 0
    k: int = 0
    j: int = 1
    word: str = ""

    @property
    def pair(self) -> tuple[int, int]:
        return (self.u, self.v)

    @property
    def product(self) -> int:
        return self.u * self.v

    @property
    def phase_mod4(self) -> int:
        return self.phase_quarters % 4

    @property
    def phase_label(self) -> str:
        return ("1", "i", "-1", "-i")[self.phase_mod4]

    def evolve(self, **updates: object) -> "CustodyState":
        return replace(self, **updates)

    def to_dict(self) -> dict[str, object]:
        data = asdict(self)
        data.update(
            pair=[self.u, self.v],
            pair_product=self.product,
            phase_mod4=self.phase_mod4,
            phase_label=self.phase_label,
            theta_exact=f"{self.phase_quarters}*pi/2",
        )
        return data


@dataclass(frozen=True, slots=True)
class ActiveAxisTrace:
    phase_quarters: int = 0
    denominator: int = 1

    @property
    def phase_label(self) -> str:
        return ("1", "i", "-1", "-i")[self.phase_quarters % 4]

    @property
    def exact_label(self) -> str:
        if self.denominator == 1:
            return self.phase_label
        return f"{self.phase_label}/{self.denominator}"

    def after_b(self, state_after: CustodyState) -> "ActiveAxisTrace":
        return ActiveAxisTrace(self.phase_quarters, state_after.product)

    def after_q(self) -> "ActiveAxisTrace":
        return ActiveAxisTrace(self.phase_quarters + 1, self.denominator)


def positions(A: int) -> int:
    return 6 * (2**A)


def j_start(A: int) -> int:
    return 1 + 6 * ((2**A) - 1)


def capacity(j: int) -> int:
    if j == 1:
        return 2
    if j == 2:
        return 4
    return 2 ** (2 * j)


def next_pair(state: CustodyState) -> tuple[int, int]:
    return (state.v, state.u + state.v)


def can_q(state: CustodyState) -> bool:
    return state.k < positions(state.A) - 1


def can_b(state: CustodyState) -> bool:
    u_next, v_next = next_pair(state)
    if can_q(state):
        return u_next * v_next <= capacity(state.j)
    return state.product < capacity(state.j)


def floor_reached(state: CustodyState) -> bool:
    return not can_b(state) and not can_q(state)


def select_primitive(state: CustodyState) -> str:
    if can_b(state):
        return "B"
    if can_q(state):
        return "Q"
    return "L"


def apply_primitive(state: CustodyState, primitive: str) -> CustodyState:
    selected = select_primitive(state)
    if primitive != selected:
        raise ValueError(f"priority violation: selected={selected}, requested={primitive}")
    if primitive == "B":
        u_next, v_next = next_pair(state)
        return state.evolve(u=u_next, v=v_next, word=state.word + "B")
    if primitive == "Q":
        return state.evolve(
            phase_quarters=state.phase_quarters + 1,
            k=state.k + 1,
            j=state.j + 1,
            word=state.word + "Q",
        )
    A_next = state.A + 1
    return state.evolve(A=A_next, k=0, j=j_start(A_next), word=state.word + "L")


def trace_first_crossing_and_next_b() -> list[dict[str, object]]:
    state = CustodyState()
    active = ActiveAxisTrace()
    rows: list[dict[str, object]] = []
    saw_l = False
    for step_index in range(1, 101):
        primitive = select_primitive(state)
        before = state
        active_before = active
        after = apply_primitive(before, primitive)
        if primitive == "B":
            active = active.after_b(after)
        elif primitive == "Q":
            active = active.after_q()
        row = {
            "step_index": step_index,
            "prefix_before": before.word,
            "prefix_after": after.word,
            "selected_primitive": primitive,
            "before": before.to_dict(),
            "after": after.to_dict(),
            "capacity_before": capacity(before.j),
            "positions_before": positions(before.A),
            "can_b_before": can_b(before),
            "can_q_before": can_q(before),
            "floor_reached_before": floor_reached(before),
            "active_axis_before": {
                "phase_quarters": active_before.phase_quarters,
                "phase_label": active_before.phase_label,
                "denominator": active_before.denominator,
                "local_shorthand": active_before.exact_label,
            },
            "active_axis_after": {
                "phase_quarters": active.phase_quarters,
                "phase_label": active.phase_label,
                "denominator": active.denominator,
                "local_shorthand": active.exact_label,
            },
        }
        if primitive == "L":
            row["active_axis_latched"] = active.exact_label
            row["new_active_axis_local_shorthand"] = "1"
        rows.append(row)
        state = after
        if primitive == "L":
            saw_l = True
        elif saw_l:
            return rows
    raise RuntimeError("first crossing and next-domain B not reached")


def independent_oracle() -> list[tuple[str, str, int, int, int, int, int, int]]:
    A, u, v, phase, k, j, word = 0, 1, 1, 0, 0, 1, ""
    rows: list[tuple[str, str, int, int, int, int, int, int]] = []
    saw_l = False
    for _ in range(100):
        N = 6 * (2**A)
        cap = 2 if j == 1 else 4 if j == 2 else 2 ** (2 * j)
        u_next, v_next = v, u + v
        cq = k < N - 1
        cb = u_next * v_next <= cap if cq else u * v < cap
        primitive = "B" if cb else "Q" if cq else "L"
        if primitive == "B":
            u, v = u_next, v_next
        elif primitive == "Q":
            phase += 1
            k += 1
            j += 1
        else:
            A += 1
            k = 0
            j = 1 + 6 * ((2**A) - 1)
        word += primitive
        rows.append((primitive, word, A, u, v, phase, k, j))
        if primitive == "L":
            saw_l = True
        elif saw_l:
            return rows
    raise RuntimeError("oracle did not reach next-domain B")


def exact_word(rows: Iterable[dict[str, object]], include_next_b: bool = False) -> str:
    letters = [str(row["selected_primitive"]) for row in rows]
    if include_next_b:
        return "".join(letters)
    if "L" not in letters:
        raise ValueError("trace has no L")
    return "".join(letters[: letters.index("L") + 1])


def local_axis_fraction(state: CustodyState) -> tuple[str, Fraction]:
    label = state.phase_label
    return label, Fraction(1, state.product)
