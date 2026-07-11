from orthad_v8u.research import statuses
def test_downstream_closed():
 s=statuses(); assert s['PRIMARY_PAIRING_RECURRENCE']=='NOT_YET_DERIVED' and s['ORTHAD_CAUSAL_PROJECTION']=='NOT_RUN'
