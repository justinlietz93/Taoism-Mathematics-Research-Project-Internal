from orthad_v8u.research import baseline
def test_baseline(): assert baseline()['pass']
def test_word(): assert baseline()['word']=='BQQBBBQBQBBQBBL'
def test_carry():
 b=baseline(); assert b['after_L']['pair']==[55,89] and b['after_L']['phase_quarters']==5
def test_next_b(): assert baseline()['after_next_B']['pair']==[89,144]
