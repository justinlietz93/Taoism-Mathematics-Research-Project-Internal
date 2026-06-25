-- ShadowResidualThetaGateV58.lean
-- Companion proof skeleton for the v58 shadow-residual gate.
-- This is intentionally elementary: it attacks the scalar derivative closure.

def chi12Residue (r : Nat) : Int :=
  match r % 12 with
  | 1 => 1
  | 11 => 1
  | 5 => -1
  | 7 => -1
  | _ => 0

-- Supported residues for χ12 are even under r ↦ -r mod 12:
-- χ12(1)=χ12(11)=1 and χ12(5)=χ12(7)=-1.
example : chi12Residue 1 = chi12Residue 11 := by decide
example : chi12Residue 5 = chi12Residue 7 := by decide

-- A scalar Jacobi derivative that avoids pairwise cancellation would need an odd
-- residue coefficient c(-r)=-c(r). Matching positive χ12 would require the opposite
-- equalities above, so the scalar odd-character closure is obstructed.
example : chi12Residue 11 ≠ - chi12Residue 1 := by decide
example : chi12Residue 7 ≠ - chi12Residue 5 := by decide
