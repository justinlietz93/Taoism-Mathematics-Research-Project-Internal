import csv, json, sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from orthad_v8s.analysis import baseline_sanity, bilinear_witness, typed_gap, statuses, active_scalar_role, overlap_assessment, coupling_audit, first_L_obligations


def test_baseline_sanity():
    assert baseline_sanity(ROOT)['pass']

def test_bilinear_underdetermination():
    w=bilinear_witness()
    assert w['pass'] and w['diagonal_restriction_residual']==0 and w['mixed_transfer_difference']==1

def test_earliest_gap_is_typed_before_pairing():
    g=typed_gap()
    assert g['earliest_missing_object']=='ambient_retained_module_functor'
    assert 'H_t' in g['typed_declaration']

def test_downstream_stays_closed():
    s=statuses()
    assert s['ORTHAD_CAUSAL_PROJECTION']=='NOT_RUN'
    assert s['GAUGE_FQM_WEIL_DESCENT']=='NOT_RUN'

def test_local_scalar_not_promoted():
    assert active_scalar_role()['classification']=='LOCAL_DESCENDANT_ONLY'

def test_O_semantics_not_name_rejection():
    o=overlap_assessment()
    assert o['semantic_role']=='DERIVED_OVERLAP_UPDATE'
    assert o['modern_per_tick_schedule']=='NOT_YET_DERIVED'

def test_coupling_verdicts():
    c={r['formula']:r['verdict'] for r in coupling_audit()}
    assert c['T_ab=lens(b)/lens(a)']=='CONDITIONALLY_LICENSED'
    assert c['pair_c(ai,aj)']=='REJECTED_WITH_EXACT_DEFECT'

def test_first_L_obligation():
    x=first_L_obligations()
    assert x['before_rank']==1 and x['after_rank']==2 and x['status']=='NOT_YET_DERIVED'

def test_lineage_inventory_exists():
    rows=list(csv.DictReader(open(ROOT/'outputs'/'20260711T085540_source_lineage_inventory.csv')))
    arts={r['artifact']:r['availability'] for r in rows}
    assert all(arts[x]=='AVAILABLE' for x in ['v7p','v7q','v7m','v7u','v8a'])
    assert arts['orthad_overset_grids.zip']=='UNAVAILABLE_EXACT_ARCHIVE'
