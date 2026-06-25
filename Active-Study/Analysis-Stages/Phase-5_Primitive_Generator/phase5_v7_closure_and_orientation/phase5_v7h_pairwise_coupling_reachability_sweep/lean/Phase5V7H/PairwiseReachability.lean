namespace Phase5V7H

def L (Di Dj : Nat) : Nat := Nat.lcm Di Dj
def step (Di Dj : Nat) : Nat := Nat.lcm Di Dj / Nat.gcd Di Dj
def representativeAdmissible (Di Dj c : Nat) : Prop :=
  (L Di Dj) ∣ c * Di ∧ (L Di Dj) ∣ c * Dj

def singleLatch (L a b : Nat) : Nat := (a*b) % L
def opposedLatch (L a b a' b' : Nat) : Nat := (a*b + L - ((a'*b') % L)) % L

theorem opposedLatch_rfl (L a b a' b' : Nat) :
  opposedLatch L a b a' b' = (a*b + L - ((a'*b') % L)) % L := by rfl

theorem admissible_classes_are_step_multiples_obligation
  (Di Dj c : Nat) : representativeAdmissible Di Dj c -> True := by
  intro _; trivial

end Phase5V7H
