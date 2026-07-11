import json,csv
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; S='20260711T105245'
def J(n): return json.loads((ROOT/'outputs'/f'{S}_{n}.json').read_text())
def test_carrier_case2():
 rows=list(csv.DictReader(open(ROOT/'outputs'/f'{S}_retained_carrier_prefix_table.csv'))); assert rows[0]['axis_moduli']=='[12]' and rows[-1]['axis_moduli']=='[12,24]'
def test_successor_open(): assert J('native_successor_recurrence_assessment')['status']=='NOT_YET_DERIVED'
def test_ambient_optional(): assert J('ambient_module_role')['status']=='OPTIONAL_FORMAL_PRESENTATION'
def test_bilinear_nondegenerate():
 w=J('bilinear_underdetermination_witness'); assert w['determinants']==[1,-3] and w['mixed_terms']==[0,2] and all(w['nondegenerate'])
def test_v7e_not_first_birth(): assert J('v7e_shared_L_coupling_assessment')['disposition']=='RECONSTRUCTION_CLUE_NOT_APPLICABLE_TO_FIRST_AXIS_BIRTH'
def test_downstream_closed():
 s=J('statuses'); assert s['ORTHAD_CAUSAL_PROJECTION']=='NOT_RUN' and s['GAUGE_FQM_WEIL_DESCENT']=='NOT_RUN'
