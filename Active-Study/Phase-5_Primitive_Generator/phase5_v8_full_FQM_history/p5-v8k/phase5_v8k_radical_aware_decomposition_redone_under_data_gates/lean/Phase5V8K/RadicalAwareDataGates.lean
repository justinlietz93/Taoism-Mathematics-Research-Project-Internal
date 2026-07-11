namespace Phase5V8K

-- Integer-level audit target for the worked certificate.
def b (x0 x1 y0 y1 : Int) : Int := (2*x0*y0 + 2*x1*y1 + 2*(x0*y1 + x1*y0)) % 4
def q (x0 x1 : Int) : Int := (x0*x0 + x1*x1 + 2*x0*x1) % 4

theorem worked_R_bii_zero : b 1 1 1 1 = 0 := by native_decide
theorem worked_R_q_zero : q 1 1 = 0 := by native_decide
theorem worked_A_q_one : q 1 0 = 1 := by native_decide

end Phase5V8K
