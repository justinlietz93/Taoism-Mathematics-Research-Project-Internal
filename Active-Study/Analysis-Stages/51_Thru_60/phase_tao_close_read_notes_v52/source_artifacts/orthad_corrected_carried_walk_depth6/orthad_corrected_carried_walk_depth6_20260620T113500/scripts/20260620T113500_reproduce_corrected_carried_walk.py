
from fractions import Fraction
import math

def phase_sign(q): return 1 if q % 4 in (0,1) else -1
u,v=1,1; qturn=0; signs=[]; anchors=[]
for lap in range(6):
    lap_sign=[]
    for pos in range(6):
        u,v=sorted((v,u+v))
        anchors.append(Fraction(1,u*v))
        qturn += 1
        lap_sign.append(phase_sign(qturn))
    signs.append(lap_sign)
print("q", (u,v), "theta_quarters", qturn)
print("sign laps", signs)
assert signs[1] == [-x for x in signs[0]]
assert signs[2] == signs[0]
print("PASS corrected carried walk")
