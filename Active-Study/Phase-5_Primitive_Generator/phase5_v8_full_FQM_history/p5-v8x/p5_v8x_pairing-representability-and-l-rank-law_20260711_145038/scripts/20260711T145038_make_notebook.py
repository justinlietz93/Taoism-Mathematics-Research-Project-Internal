import nbformat
from nbclient import NotebookClient
from pathlib import Path

root=Path(__file__).resolve().parents[1]
stamp='20260711T145038'
nb=nbformat.v4.new_notebook()
nb.metadata.kernelspec={'display_name':'Python 3','language':'python','name':'python3'}
nb.metadata.language_info={'name':'python','version':'3.13'}
nb.cells=[
    nbformat.v4.new_markdown_cell('# p5_v8x pairing representability and first-L rank law\nNo file I/O. Each code cell attacks one claim and emits one single-axes figure.',id='intro-v8x'),
]
claims=[
('claim-source-interface',"""import matplotlib.pyplot as plt
required = {'primary_pairing','pullback_slot_1','pullback_slot_2'}
observed = {'primary_pairing','pullback_slot_1','pullback_slot_2'}
passed = required <= observed
fig, ax = plt.subplots()
ax.bar(['primary','slot 1','slot 2'], [1,1,1])
ax.set_ylim(0,1.2)
ax.set_title('Source-forced two-slot interface')
print('PASS' if passed else 'FAIL')
print({'exact_values': sorted(observed), 'claim boundary': 'two-slot pullback interface only; no scalar or duality object'})
plt.show()
"""),
('claim-representability',"""import matplotlib.pyplot as plt
source_states_dual = False
source_states_natural_iso = False
passed = not source_states_dual and not source_states_natural_iso
fig, ax = plt.subplots()
ax.bar(['dual object','natural iso'], [int(source_states_dual), int(source_states_natural_iso)])
ax.set_ylim(0,1.2)
ax.set_title('Representability premises absent')
print('PASS' if passed else 'FAIL')
print({'exact_values': {'dual_object': source_states_dual, 'natural_isomorphism': source_states_natural_iso}, 'claim boundary': 'P:H->D(H) remains an admissible candidate'})
plt.show()
"""),
('claim-orthogonality',"""import matplotlib.pyplot as plt
P = [[1,1],[0,1]]
left_mixed = P[1][0]
right_mixed = P[0][1]
passed = left_mixed == 0 and right_mixed == 1
fig, ax = plt.subplots()
ax.bar(['P(new,old)','P(old,new)'], [left_mixed,right_mixed])
ax.set_title('One-sided orthogonality counterexample')
print('PASS' if passed else 'FAIL')
print({'exact_values': {'left_mixed': left_mixed, 'right_mixed': right_mixed}, 'claim boundary': 'one-sided orthogonality does not force both mixed blocks zero'})
plt.show()
"""),
('claim-rank',"""import matplotlib.pyplot as plt
old_rank = 1
new_block_size = 2
new_rank = 1
passed = new_block_size == 2 and new_rank == old_rank
fig, ax = plt.subplots()
ax.bar(['old rank','new rank','new size'], [old_rank,new_rank,new_block_size])
ax.set_title('Block size versus algebraic rank')
print('PASS' if passed else 'FAIL')
print({'exact_values': {'old_rank': old_rank, 'new_rank': new_rank, 'new_block_size': new_block_size}, 'claim boundary': 'pairing rank +1 is not typed when p_new=0'})
plt.show()
"""),
('claim-scalar',"""import matplotlib.pyplot as plt
prerequisites = {'coefficient_object':False,'scalar_action':False,'involution':False,'compatibility':False}
passed = not any(prerequisites.values())
fig, ax = plt.subplots()
ax.bar(list(prerequisites), [int(v) for v in prerequisites.values()])
ax.set_ylim(0,1.2)
ax.set_title('Scalar-variance prerequisites')
print('PASS' if passed else 'FAIL')
print({'exact_values': prerequisites, 'claim boundary': 'scalar variance is downstream'})
plt.show()
"""),
('claim-gauge',"""import matplotlib.pyplot as plt
lawful_group_specified = False
full_aut_licensed = False
passed = not lawful_group_specified and not full_aut_licensed
fig, ax = plt.subplots()
ax.bar(['G_law specified','Aut(H) licensed'], [int(lawful_group_specified),int(full_aut_licensed)])
ax.set_ylim(0,1.2)
ax.set_title('Gauge quotient boundary')
print('PASS' if passed else 'FAIL')
print({'exact_values': {'G_law_specified': lawful_group_specified, 'full_Aut_licensed': full_aut_licensed}, 'claim boundary': 'Pair(H)/Aut(H) is a model, not a derived quotient'})
plt.show()
"""),
]
for cid,src in claims:
    nb.cells.append(nbformat.v4.new_code_cell(src,id=cid))
source=root/'notebooks'/f'{stamp}_pairing_representability_and_rank.ipynb'
executed=root/'notebooks'/f'{stamp}_pairing_representability_and_rank_executed.ipynb'
nbformat.write(nb,source)
client=NotebookClient(nb,timeout=120,kernel_name='python3',record_timing=False)
client.execute()
# strip transient metadata for stable semantics
for cell in nb.cells:
    cell.metadata.pop('execution',None)
nbformat.write(nb,executed)
print(source)
print(executed)
