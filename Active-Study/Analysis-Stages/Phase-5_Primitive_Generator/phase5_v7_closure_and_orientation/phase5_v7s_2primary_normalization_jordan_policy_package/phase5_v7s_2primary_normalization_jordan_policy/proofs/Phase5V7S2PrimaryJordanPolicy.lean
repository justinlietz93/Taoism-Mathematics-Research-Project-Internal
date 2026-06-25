import Std

namespace Phase5V7S

inductive BlockKind where
  | A | U | V
  deriving Repr, DecidableEq

structure TwoPrimaryBlock where
  kind : BlockKind
  k : Nat
  oddity : Nat
  brown : Nat
  deriving Repr, DecidableEq

def normalizeOddity (t : Nat) : Nat := t % 8

def normalizedKey (b : TwoPrimaryBlock) : Nat × Nat × Nat :=
  match b.kind with
  | BlockKind.A => (b.k, normalizeOddity b.oddity, b.brown % 8)
  | BlockKind.U => (b.k, 100, b.brown % 8)
  | BlockKind.V => (b.k, 200, b.brown % 8)

theorem raw_shift_policy_stable (k t br : Nat) :
  normalizedKey ⟨BlockKind.A, k, t + 8, br⟩ = normalizedKey ⟨BlockKind.A, k, t, br⟩ := by
  simp [normalizedKey, normalizeOddity, Nat.add_mod]

theorem U_V_separated_by_tag (k br : Nat) :
  normalizedKey ⟨BlockKind.U, k, 0, br⟩ ≠ normalizedKey ⟨BlockKind.V, k, 0, br⟩ := by
  simp [normalizedKey]

end Phase5V7S
