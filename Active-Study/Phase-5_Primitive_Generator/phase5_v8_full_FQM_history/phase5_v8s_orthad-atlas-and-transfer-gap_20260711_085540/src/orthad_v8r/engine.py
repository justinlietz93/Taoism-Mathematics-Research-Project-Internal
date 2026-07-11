from __future__ import annotations

from dataclasses import asdict, dataclass

from .law import can_b, can_q, capacity, floor_reached, next_pair, positions, selected_primitive, validate_state
from .state import CustodyState


@dataclass(frozen=True, slots=True)
class StepRecord:
    step_index: int
    primitive: str
    before: dict[str, object]
    after: dict[str, object]
    can_b_before: bool
    can_q_before: bool
    floor_reached_before: bool
    capacity_before: int
    available_positions_before: int
    next_pair_before: list[int]
    next_pair_product_before: int
    word_prefix: str

    def to_dict(self) -> dict[str, object]:
        return asdict(self)


def apply_primitive(state: CustodyState, primitive: str) -> CustodyState:
    validate_state(state)
    if primitive != selected_primitive(state):
        raise ValueError("primitive violates B > Q > L")
    if primitive == "B":
        u1, v1 = next_pair(state)
        out = state.evolve(u=u1, v=v1, word=state.word + "B")
    elif primitive == "Q":
        out = state.evolve(
            phase_quarters=state.phase_quarters + 1,
            k=state.k + 1,
            j=state.j + 1,
            word=state.word + "Q",
        )
    elif primitive == "L":
        if not floor_reached(state):
            raise ValueError("L requires floor predicate")
        A1 = state.A + 1
        out = state.evolve(A=A1, k=0, j=1 + 6 * ((2**A1) - 1), word=state.word + "L")
    else:
        raise ValueError(primitive)
    validate_state(out)
    return out


def step(state: CustodyState, step_index: int) -> tuple[CustodyState, StepRecord]:
    primitive = selected_primitive(state)
    proposed = next_pair(state)
    after = apply_primitive(state, primitive)
    record = StepRecord(
        step_index=step_index,
        primitive=primitive,
        before=state.to_dict(),
        after=after.to_dict(),
        can_b_before=can_b(state),
        can_q_before=can_q(state),
        floor_reached_before=floor_reached(state),
        capacity_before=capacity(state.j),
        available_positions_before=positions(state.A),
        next_pair_before=[proposed[0], proposed[1]],
        next_pair_product_before=proposed[0] * proposed[1],
        word_prefix=after.word,
    )
    return after, record


def run_first_crossing_and_next_b() -> tuple[CustodyState, list[StepRecord]]:
    state = CustodyState()
    validate_state(state)
    records: list[StepRecord] = []
    saw_l = False
    while len(records) < 100:
        state, record = step(state, len(records) + 1)
        records.append(record)
        if record.primitive == "L":
            saw_l = True
        elif saw_l:
            if record.primitive != "B":
                raise AssertionError("first next-domain primitive must be B")
            return state, records
    raise RuntimeError("first crossing did not terminate")
