from orthad_v8u.research import *
def test_translation_nonuniqueness(): assert sum(r['single_cycle'] for r in translation_generators(12))==4
def test_shift_narrow(): assert fixed_shift_identity(12)['clean_QBL_seed_status']=='HISTORICAL_DESCENDANT_ONLY'
def test_seed_open(): assert successor_seed_assessment()['status']=='NOT_YET_DERIVED'
def test_pre_l_open(): assert len(pre_l_trace(baseline()['trace']))==14 and all(r['status']=='NOT_YET_DERIVED' for r in pre_l_trace(baseline()['trace']))
def test_product_candidate():
 r=next(x for x in carrier_claims() if x['claim']=='first-L retained carrier Z/12Z x Z/24Z'); assert r['evidence_class']=='CANDIDATE_FORMALIZATION'
def test_v7e_zero_lawful(): assert v7e_assessment()['Q_DEPTH_ZERO']=='LAWFUL_VALUE_IN_V7E'
def test_spectral_required(): assert 'REQUIRED' in spectral_assessment()['status_line']
