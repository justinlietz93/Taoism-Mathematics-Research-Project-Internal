universe u v

theorem no_full_transition_map
  {S : Type u} {P : Type v}
  (proj : S -> P) (step : S -> S) (x y : S)
  (hproj : proj x = proj y)
  (hstep : step x != step y) :
  Not (Exists (fun G : P -> S => forall z : S, G (proj z) = step z)) := by
  intro h
  rcases h with ⟨G, hG⟩
  have hx : G (proj x) = step x := hG x
  have hy : G (proj y) = step y := hG y
  have hyx : G (proj x) = step y := by
    simpa [hproj] using hy
  have hxy : step x = step y := Eq.trans hx.symm hyx
  exact hstep hxy

theorem no_projected_transition_map
  {S : Type u} {P : Type v}
  (proj : S -> P) (step : S -> S) (x y : S)
  (hproj : proj x = proj y)
  (hnext : proj (step x) != proj (step y)) :
  Not (Exists (fun H : P -> P => forall z : S, H (proj z) = proj (step z))) := by
  intro h
  rcases h with ⟨H, hH⟩
  have hx : H (proj x) = proj (step x) := hH x
  have hy : H (proj y) = proj (step y) := hH y
  have hyx : H (proj x) = proj (step y) := by
    simpa [hproj] using hy
  have hxy : proj (step x) = proj (step y) := Eq.trans hx.symm hyx
  exact hnext hxy
