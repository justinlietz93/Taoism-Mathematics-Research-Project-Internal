from __future__ import annotations

from dataclasses import asdict, dataclass, replace

from primitive_custody.domain.state import CustodyState


ORTHAD_CHART_RECURRENCE_NOT_YET_DERIVED = "ORTHAD_CHART_RECURRENCE_NOT_YET_DERIVED"


@dataclass(frozen=True, slots=True)
class OrthadDerivationBoundary:
    status: str = ORTHAD_CHART_RECURRENCE_NOT_YET_DERIVED
    observed_word_prefix: str = ""
    observed_ticks: int = 0
    retained_axes: int = 1
    primary_pairing: None = None
    omega_plus: None = None
    omega_minus: None = None
    transfer_plus_to_minus: None = None
    transfer_minus_to_plus: None = None
    derivation_gap: str = (
        "The primary source fixes pairing-first direction and per-primitive duties, "
        "but explicitly leaves exact chart-map recurrence as a formalization obligation."
    )

    def observe(self, state: CustodyState, primitive: str) -> "OrthadDerivationBoundary":
        new_axes = self.retained_axes + (1 if primitive == "L" else 0)
        return replace(
            self,
            observed_word_prefix=state.word,
            observed_ticks=self.observed_ticks + 1,
            retained_axes=new_axes,
        )

    def to_dict(self) -> dict[str, object]:
        return asdict(self)


class OrthadNotDerivedError(RuntimeError):
    pass


def terminal_projection(boundary: OrthadDerivationBoundary) -> None:
    raise OrthadNotDerivedError(
        f"terminal projection unavailable: {boundary.status}"
    )
