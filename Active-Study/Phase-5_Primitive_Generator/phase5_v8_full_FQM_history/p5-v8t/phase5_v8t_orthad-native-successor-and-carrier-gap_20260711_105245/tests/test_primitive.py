from orthad_v8t.primitive import run_first_crossing_and_next_b,independent_oracle

def test_word():
 _,r=run_first_crossing_and_next_b(); assert next(x for x in r if x['primitive']=='L')['after']['word']=='BQQBBBQBQBBQBBL'
def test_floor():
 _,r=run_first_crossing_and_next_b(); L=next(x for x in r if x['primitive']=='L'); assert L['before']['pair']==[55,89] and L['before']['phase_quarters']==5
def test_carry():
 _,r=run_first_crossing_and_next_b(); L=next(x for x in r if x['primitive']=='L'); assert L['after']['pair']==[55,89] and L['after']['phase_quarters']==5 and L['after']['k']==0
def test_next_b():
 _,r=run_first_crossing_and_next_b(); assert r[-1]['primitive']=='B' and r[-1]['after']['pair']==[89,144]
def test_oracle():
 _,r=run_first_crossing_and_next_b(); o=independent_oracle(); assert [(x['primitive'],x['word_prefix']) for x in r]==[(x[0],x[1]) for x in o]
