from __future__ import annotations

from dataclasses import asdict, dataclass

from .engine import StepRecord


@dataclass(frozen=True, slots=True)
class AxisRow:
    step_index: int
    primitive: str
    word_prefix: str
    A: int
    pair: list[int]
    global_phase_quarters: int
    active_phase_quarters: int
    active_phase_mod4: int
    phase_factor: str
    denominator: int
    active_axis: str
    latched_axis: str | None
    active_axis_after_l: str | None

    def to_dict(self) -> dict[str, object]:
        return asdict(self)


def _label(mod4: int) -> str:
    return ("1", "i", "-1", "-i")[mod4]


def _axis_string(phase_mod4: int, denominator: int) -> str:
    phase = _label(phase_mod4)
    if denominator == 1:
        return phase
    return f"{phase}/{denominator}"


def compile_active_axis(records: list[StepRecord]) -> list[AxisRow]:
    rows: list[AxisRow] = []
    local_phase = 0
    denominator = 1
    for record in records:
        latched = None
        new_active = None
        after = record.after
        if record.primitive == "B":
            denominator = int(after["pair_product"])
        elif record.primitive == "Q":
            local_phase += 1
        elif record.primitive == "L":
            latched = _axis_string(local_phase % 4, denominator)
            local_phase = 0
            denominator = 1
            new_active = "1"
        rows.append(AxisRow(
            step_index=record.step_index,
            primitive=record.primitive,
            word_prefix=record.word_prefix,
            A=int(after["A"]),
            pair=list(after["pair"]),
            global_phase_quarters=int(after["phase_quarters"]),
            active_phase_quarters=local_phase,
            active_phase_mod4=local_phase % 4,
            phase_factor=_label(local_phase % 4),
            denominator=denominator,
            active_axis=_axis_string(local_phase % 4, denominator),
            latched_axis=latched,
            active_axis_after_l=new_active,
        ))
    return rows


RECURRENCE = {
    "seed": "a=1, local_phase=0, denominator=1",
    "B": "after (u,v)->(v,u+v), denominator:=u*v and phase is retained",
    "Q": "local_phase:=local_phase+1; a:=i*a; denominator retained",
    "L": "latch a; append a new active axis 1; global pair and phase carry",
}
