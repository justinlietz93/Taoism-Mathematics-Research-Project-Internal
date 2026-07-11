import csv,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; STAMP='20260711T141656'

def test_minimal_interface_and_open_type():
 c=json.load(open(ROOT/'outputs'/f'{STAMP}_claim_model.json'))
 assert c['MINIMAL_PAIRING_INTERFACE']=='DERIVED'
 assert c['EXACT_PRIMARY_PAIRING_TYPE']=='NOT_YET_DERIVED'

def test_candidate_elimination():
 rows={r['candidate']:r['verdict'] for r in csv.DictReader(open(ROOT/'outputs'/f'{STAMP}_pairing_type_elimination_table.csv'))}
 assert rows['general morphism H_t -> D(H_t)']=='DERIVED'
 assert rows['quadratic refinement']=='RULED_OUT'
 assert rows['Hermitian form']=='ADMISSIBLE_BUT_NOT_FORCED'

def test_axis_boundary():
 a=json.load(open(ROOT/'outputs'/f'{STAMP}_initial_axis_object.json'))
 assert a['one_architectural_axis_before_first_L']
 assert not a['one_dimensional_module_forced']

def test_lifted_state_schema_only():
 c=json.load(open(ROOT/'outputs'/f'{STAMP}_claim_model.json'))
 s=c['lifted_state_schema']
 assert s['name']=='lifted_state_schema' and not s['instantiated']
 assert all(s[k] is None for k in ['pairing','Omega_plus','Omega_minus','T_plus_to_minus','T_minus_to_plus'])
