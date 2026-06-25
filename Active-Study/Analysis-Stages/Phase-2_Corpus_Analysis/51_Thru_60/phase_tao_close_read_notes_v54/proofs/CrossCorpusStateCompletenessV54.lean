/-
CrossCorpusStateCompletenessV54
Static companion proof sketch for the finite projection-loss gate.
The local environment used for this package did not provide lake/lean execution;
this file is intentionally elementary and mirrors the SymPy/Python witness logic.
-/

inductive HiddenState where
  | mk : Nat -> Nat -> HiddenState
  deriving DecidableEq, Repr

def visible : HiddenState -> Nat
  | HiddenState.mk x _z => x

def step : HiddenState -> HiddenState
  | HiddenState.mk x z => HiddenState.mk x (z+1)

theorem visible_collision_hidden_split :
  visible (HiddenState.mk 0 0) = visible (HiddenState.mk 0 1) ∧
  step (HiddenState.mk 0 0) ≠ step (HiddenState.mk 0 1) := by
  constructor
  · rfl
  · intro h
    cases h

inductive Chart where
  | yin | yang
  deriving DecidableEq, Repr

structure ChartVector where
  c : Chart
  x : Int
  y : Int
  z : Int
  deriving DecidableEq, Repr

def componentProjection (v : ChartVector) : Int × Int × Int := (v.x,v.y,v.z)

def chartAwareStep (v : ChartVector) : Chart × Int × Int × Int :=
  match v.c with
  | Chart.yin => (Chart.yin, v.x, v.y, v.z)
  | Chart.yang => (Chart.yang, -v.x, -v.y, -v.z)

theorem same_components_not_chart_complete :
  componentProjection ⟨Chart.yin,1,2,3⟩ = componentProjection ⟨Chart.yang,1,2,3⟩ ∧
  chartAwareStep ⟨Chart.yin,1,2,3⟩ ≠ chartAwareStep ⟨Chart.yang,1,2,3⟩ := by
  constructor
  · rfl
  · intro h
    cases h
