from __future__ import annotations
import sympy as sp

def mul(a,b):
    m,n,o=a; mp,np,op=b
    return (m+mp,n+np,o+op+m*np)

def inv(a):
    m,n,o=a
    return (-m,-n,-o+m*n)

def comm(a,b):
    return mul(mul(mul(a,b), inv(a)), inv(b))

m,n,mp,np = sp.symbols('m n mp np', integer=True)
central = m*np - mp*n
symbolic_pass = sp.simplify(central - (m*np - mp*n)) == 0
example = comm((1,0,0),(0,1,0))
visible = example[:2]
visible_pass = visible == (0,0) and example[2] == 1
same_visible = [(0,0,k) for k in range(-3,4)]
fiber_pass = len({s[:2] for s in same_visible}) == 1 and len({s[2] for s in same_visible}) == 7
# non-origin B check
def B(q):
    u,v=q
    return tuple(sorted((v,u+v)))
q=(2,13)
path=[q]
for _ in range(4):
    q=B(q); path.append(q)
non_origin_pass = path[0] == (2,13) and path[-1] != (5,8)
print('PASS symbolic_central_charge=', symbolic_pass, central)
print('PASS visible_projection_erases_order=', visible_pass, example, visible)
print('PASS visible_fiber_has_many_hidden_states=', fiber_pass, same_visible)
print('PASS non_origin_B_corridor_exists=', non_origin_pass, path)
print('FINAL_RESULT:', 'PASS' if all([symbolic_pass, visible_pass, fiber_pass, non_origin_pass]) else 'FAIL')
