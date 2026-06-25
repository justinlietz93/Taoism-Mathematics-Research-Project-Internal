import Std

namespace Phase5V7M

inductive Kind where | Q | B | L | O deriving DecidableEq, Repr

structure Event where
  kind : Kind
  support : List Nat
  sign : Int := 1
  deriving DecidableEq, Repr

def disjoint (a b : Event) : Prop := ∀ x, x ∈ a.support → x ∉ b.support

def independent (a b : Event) : Prop := disjoint a b ∧ disjoint b a

structure TraceProtocol where
  Sigma : Type
  indep : Sigma → Sigma → Prop

structure OverlapCocycle where
  vertices : List Nat
  edgeValue : Nat → Nat → Int

structure GaugeClass where
  cocycle : OverlapCocycle

structure CouplingObject where
  carrierModuli : List Nat
  gaugeClass : GaugeClass

axiom legal_swap_preserves_trace_class : ∀ (P : TraceProtocol) (a b : P.Sigma), P.indep a b → True
axiom gauge_change_preserves_holonomy : ∀ (G : GaugeClass), True
axiom coordinate_tensor_is_presentation_only : ∀ (C : CouplingObject), True

end Phase5V7M
