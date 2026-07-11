import csv
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; S='20260711T105245'
def test_lineage():
 rows=list(csv.DictReader(open(ROOT/'outputs'/f'{S}_native_successor_source_inventory.csv'))); d={r['source_key']:r['availability'] for r in rows}; assert all(d[k]=='AVAILABLE' for k in ['v7p_event_alphabet','v7c_successor_rerun','v7q_scalar_ratios','v7e_shared_L','v7m_external_manifest','v7u_full_lens_compiler','v8a_confluence_cocycle']) and d['orthad_overset_grids.zip']=='UNAVAILABLE_EXACT_ARCHIVE'
def test_no_promoted_pairing():
 import json; d=json.loads((ROOT/'outputs'/f'{S}_successor_to_pairing_bridge.json').read_text()); assert d['status']=='NOT_YET_DERIVED'

def test_baseline_reuse_provenance():
 import json,csv
 p=json.loads((ROOT/'outputs'/f'{S}_baseline_provenance.json').read_text())
 rows=list(csv.DictReader(open(ROOT/'outputs'/f'{S}_baseline_reuse_inventory.csv')))
 assert p['baseline_zip_sha256']=='947211aa29891e0f454aac78478fb4e0567301f46e3b2909edfa8ba3e206c502' and len(rows)==5
