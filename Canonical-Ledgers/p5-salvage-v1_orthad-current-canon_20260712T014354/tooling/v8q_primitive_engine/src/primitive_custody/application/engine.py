from __future__ import annotations

from dataclasses import asdict, dataclass

from primitive_custody.domain.law import (
    can_b,
    can_q,
    capacity,
    floor_reached,
    next_pair,
    positions,
    selected_primitive,
    validate_state,
)
from primitive_custody.domain.state import CustodyState
from primitive_custody.orthad.boundary import OrthadDerivationBoundary


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
    orthad_boundary: dict[str, object]

    def to_dict(self) -> dict[str, object]:
        return asdict(self)


@dataclass(frozen=True, slots=True)
class LiftedCustody:
    custody: CustodyState
    orthad_boundary: OrthadDerivationBoundary


def initial_lifted_state() -> LiftedCustody:
    state = CustodyState()
    validate_state(state)
    return LiftedCustody(state, OrthadDerivationBoundary())


def apply_primitive(state: CustodyState, primitive: str) -> CustodyState:
    validate_state(state)
    if primitive != selected_primitive(state):
        raise ValueError("primitive does not satisfy B > Q > L")
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
            raise ValueError("L requires the floor predicate")
        out = state.evolve(
            A=state.A + 1,
            k=0,
            j=1 + 6 * ((2 ** (state.A + 1)) - 1),
            word=state.word + "L",
        )
    else:
        raise ValueError(primitive)
    validate_state(out)
    return out


def step(lifted: LiftedCustody, step_index: int) -> tuple[LiftedCustody, StepRecord]:
    before = lifted.custody
    primitive = selected_primitive(before)
    proposed = next_pair(before)
    after = apply_primitive(before, primitive)
    boundary = lifted.orthad_boundary.observe(after, primitive)
    record = StepRecord(
        step_index=step_index,
        primitive=primitive,
        before=before.to_dict(),
        after=after.to_dict(),
        can_b_before=can_b(before),
        can_q_before=can_q(before),
        floor_reached_before=floor_reached(before),
        capacity_before=capacity(before.j),
        available_positions_before=positions(before.A),
        next_pair_before=[proposed[0], proposed[1]],
        next_pair_product_before=proposed[0] * proposed[1],
        word_prefix=after.word,
        orthad_boundary=boundary.to_dict(),
    )
    return LiftedCustody(after, boundary), record


def run_to_first_l_and_next_b() -> tuple[LiftedCustody, list[StepRecord]]:
    lifted = initial_lifted_state()
    records: list[StepRecord] = []
    saw_l = False
    while True:
        lifted, record = step(lifted, len(records) + 1)
        records.append(record)
        if record.primitive == "L":
            saw_l = True
            continue
        if saw_l:
            if record.primitive != "B":
                raise AssertionError("first next-domain primitive must be B")
            return lifted, records
        if len(records) > 100:
            raise RuntimeError("first crossing did not terminate")
