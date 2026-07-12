from __future__ import annotations

from dataclasses import asdict, dataclass, replace


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
        return self.u, self.v

    @property
    def pair_product(self) -> int:
        return self.u * self.v

    @property
    def phase_mod4(self) -> int:
        return self.phase_quarters % 4

    @property
    def phase_label(self) -> str:
        return ("1", "i", "-1", "-i")[self.phase_mod4]

    def evolve(self, **changes: object) -> "CustodyState":
        return replace(self, **changes)

    def to_dict(self) -> dict[str, object]:
        payload = asdict(self)
        payload["pair"] = [self.u, self.v]
        payload["pair_product"] = self.pair_product
        payload["phase_mod4"] = self.phase_mod4
        payload["phase_label"] = self.phase_label
        return payload
