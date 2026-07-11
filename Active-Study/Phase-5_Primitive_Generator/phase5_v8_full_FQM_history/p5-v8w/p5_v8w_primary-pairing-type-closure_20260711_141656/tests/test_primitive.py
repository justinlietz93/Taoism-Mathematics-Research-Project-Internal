from orthad_v8w.primitive import trace_first_crossing_and_next_b, exact_word

def test_exact_word_and_boundary():
 rows=trace_first_crossing_and_next_b(); li=next(i for i,r in enumerate(rows) if r['selected_primitive']=='L')
 assert exact_word(rows)=='BQQBBBQBQBBQBBL'
 assert rows[li]['before']['pair']==[55,89]
 assert rows[li]['after']['pair']==[55,89]
 assert rows[li+1]['after']['pair']==[89,144]

def test_floor_is_not_symbol():
 assert 'FLOOR' not in exact_word(trace_first_crossing_and_next_b())
