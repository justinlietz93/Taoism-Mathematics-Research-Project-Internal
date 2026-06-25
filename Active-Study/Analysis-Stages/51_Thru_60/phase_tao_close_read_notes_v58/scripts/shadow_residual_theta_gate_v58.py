from math import gcd

def chi12(n: int) -> int:
    r = n % 12
    if r in (1, 11):
        return 1
    if r in (5, 7):
        return -1
    return 0

# 1. evenness of chi12
for n in range(1, 200):
    assert chi12(-n) == chi12(n)

# 2. bilateral derivative cancels pairwise
for n in range(1, 200):
    assert chi12(n) * n + chi12(-n) * (-n) == 0

# 3. no scalar odd periodic coefficient c mod 12 can match positive chi12 on all supported residues
for r in (1, 5, 7, 11):
    assert chi12((-r) % 12) != -chi12(r)

# 4. eta pentagonal reconciliation: chi12(6k-1)=(-1)^k and chi12(6k+1)=(-1)^k
for k in range(-50, 51):
    assert chi12(6*k - 1) == (-1)**k
    assert chi12(6*k + 1) == (-1)**k

print('PASS shadow_residual_theta_gate_v58')
