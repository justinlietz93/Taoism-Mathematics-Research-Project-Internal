from __future__ import annotations

from dataclasses import dataclass
from math import gcd


@dataclass(frozen=True)
class AxisValue:
    real_num: int
    imag_num: int
    den: int

    def reduced(self) -> "AxisValue":
        common = gcd(gcd(abs(self.real_num), abs(self.imag_num)), self.den)
        if common == 0:
            return self
        return AxisValue(self.real_num // common, self.imag_num // common, self.den // common)

    def with_den(self, den: int) -> "AxisValue":
        real_sign = 0 if self.real_num == 0 else (1 if self.real_num > 0 else -1)
        imag_sign = 0 if self.imag_num == 0 else (1 if self.imag_num > 0 else -1)
        return AxisValue(real_sign, imag_sign, den)

    def as_record(self) -> dict[str, int | str]:
        return {
            "real_num": self.real_num,
            "imag_num": self.imag_num,
            "den": self.den,
            "exact": f"({self.real_num}+{self.imag_num}i)/{self.den}",
        }
