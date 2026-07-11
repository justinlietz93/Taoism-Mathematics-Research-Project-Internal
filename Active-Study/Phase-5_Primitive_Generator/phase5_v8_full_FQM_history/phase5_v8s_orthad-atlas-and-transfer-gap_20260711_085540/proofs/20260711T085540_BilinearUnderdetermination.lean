import Mathlib

namespace Phase5V8S

abbrev H := ℚ × ℚ

def iotaPlus (x : ℚ) : H := (x, 0)
def iotaMinus (x : ℚ) : H := (0, x)

def P (m : ℚ) (x y : H) : ℚ :=
  x.1 * y.1 + x.2 * y.2 + m * (x.1 * y.2 + x.2 * y.1)

theorem plusRestrictionIndependent (m n x y : ℚ) :
    P m (iotaPlus x) (iotaPlus y) = P n (iotaPlus x) (iotaPlus y) := by
  simp [P, iotaPlus]

theorem minusRestrictionIndependent (m n x y : ℚ) :
    P m (iotaMinus x) (iotaMinus y) = P n (iotaMinus x) (iotaMinus y) := by
  simp [P, iotaMinus]

theorem mixedTransferDiffers :
    P 0 (iotaMinus 1) (iotaPlus 1) ≠ P 1 (iotaMinus 1) (iotaPlus 1) := by
  norm_num [P, iotaPlus, iotaMinus]

end Phase5V8S
