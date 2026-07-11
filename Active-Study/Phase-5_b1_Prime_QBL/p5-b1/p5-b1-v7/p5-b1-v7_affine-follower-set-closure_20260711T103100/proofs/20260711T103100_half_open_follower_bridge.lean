import Mathlib.Data.Set.Lattice
import Mathlib.Order.Interval.Set.Basic

open Set

namespace QBLCarryFollowerBridge

/-- The actual interval convention used by the carry coding. -/
def halfOpen (a b : ℝ) : Set ℝ := Set.Ioc a b

/-- The left endpoint is excluded. -/
theorem left_not_mem_halfOpen {a b : ℝ} : a ∉ halfOpen a b := by
  intro h
  exact (lt_irrefl a) h.1

/-- The right endpoint is included whenever the interval is nonempty. -/
theorem right_mem_halfOpen {a b : ℝ} (h : a < b) : b ∈ halfOpen a b := by
  exact ⟨h, le_rfl⟩

/-- Image of the actual word cylinder after the word length. -/
def followerRegion {α β : Type*} (f : α → β) (Cw : Set α) : Set β :=
  f '' Cw

/-- Exact set-theoretic concatenation cylinder. -/
def concatCylinder {α β : Type*} (f : α → β) (Cw : Set α) (Cv : Set β) : Set α :=
  Cw ∩ f ⁻¹' Cv

/--
The endpoint-preserving bridge used in the standard follower-set proof.
No interior or closure replacement occurs: included endpoints remain included,
and excluded endpoints remain absent because the statement is exact set membership.
-/
theorem concat_nonempty_iff_follower_intersection_nonempty
    {α β : Type*} (f : α → β) (Cw : Set α) (Cv : Set β) :
    (concatCylinder f Cw Cv).Nonempty ↔
      ((followerRegion f Cw) ∩ Cv).Nonempty := by
  constructor
  · rintro ⟨x, hxw, hxf⟩
    exact ⟨f x, ⟨x, hxw, rfl⟩, hxf⟩
  · rintro ⟨y, ⟨x, hxw, rfl⟩, hy⟩
    exact ⟨x, hxw, hy⟩

/-- The exact half-open form of the ordered follower-region pair. -/
def minusRegion (α q : ℝ) : Set ℝ := halfOpen α q

def plusRegion (q β : ℝ) : Set ℝ := halfOpen q β

/-- The oriented handoff belongs to the minus region. -/
theorem handoff_mem_minus {α q : ℝ} (h : α < q) :
    q ∈ minusRegion α q := by
  exact right_mem_halfOpen h

/-- The same handoff is excluded from the plus region. -/
theorem handoff_not_mem_plus {q β : ℝ} :
    q ∉ plusRegion q β := by
  exact left_not_mem_halfOpen

end QBLCarryFollowerBridge
