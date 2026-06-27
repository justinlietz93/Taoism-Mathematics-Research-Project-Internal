/-
Phase 5 v7f proof surface.
Local execution pending. This file states the arithmetic gates attacked by the Python/SymPy sweep.
-/
namespace Phase5V7F

def lcm (a b : Nat) : Nat := a * b / Nat.gcd a b

def admissibleStep (Di Dj : Nat) : Nat := lcm Di Dj / Nat.gcd Di Dj

def repInvariant (Di Dj c : Nat) : Prop :=
  let L := lcm Di Dj
  (c * Di) % L = 0 ∧ (c * Dj) % L = 0

/-- Coupling extracted from shared boundary latch terms. -/
def nativeCoupling (L : Nat) (terms : List (Int × Nat × Nat)) : Int :=
  terms.foldl (fun acc t => acc + t.1 * Int.ofNat ((t.2.1 + 1) * (t.2.2 + 1))) 0

/-- Audit theorem target: representative invariance is equivalent to divisibility by admissible step. -/
axiom repInvariant_step_target :
  ∀ (Di Dj c : Nat), Di > 0 → Dj > 0 →
  repInvariant Di Dj c ↔ c % admissibleStep Di Dj = 0

/-- Audit theorem target: nondegenerate coupling has singleton kernel. -/
axiom nondegenerate_kernel_target :
  ∀ (Di Dj c : Nat), repInvariant Di Dj c → Prop

end Phase5V7F
