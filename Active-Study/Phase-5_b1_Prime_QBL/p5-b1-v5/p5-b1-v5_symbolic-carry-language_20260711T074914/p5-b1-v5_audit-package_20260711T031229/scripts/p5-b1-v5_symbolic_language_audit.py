#!/usr/bin/env python3
from __future__ import annotations
import argparse,csv,json,tempfile,zipfile
from decimal import Decimal,getcontext
from pathlib import Path

STATES='789'

def extract(zip_path:Path, td:str)->Path:
    with zipfile.ZipFile(zip_path) as z:z.extractall(td)
    roots=[p for p in Path(td).iterdir() if p.is_dir()]
    if len(roots)!=1: raise RuntimeError('expected one package root')
    return roots[0]

def main()->None:
    ap=argparse.ArgumentParser();ap.add_argument('zip_path',type=Path);ap.add_argument('--json-out',type=Path);args=ap.parse_args()
    with tempfile.TemporaryDirectory() as td:
        root=extract(args.zip_path,td)
        num=json.loads(next((root/'outputs').glob('*_numerical_results.json')).read_text())
        gamma=Decimal(num['constants']['gamma']); getcontext().prec=180; a=(gamma-Decimal(8))/2
        parts={'7':(Decimal(-1),-Decimal('0.5')-a),'8':(-Decimal('0.5')-a,-a),'9':(-a,Decimal(0))}
        def inter(x,y):
            lo=max(x[0],y[0]);hi=min(x[1],y[1]);return (lo,hi) if hi>lo else None
        def image(iv,c):
            off=gamma-Decimal(int(c));return (2*iv[0]+off,2*iv[1]+off)
        levels=[{s:parts[s] for s in STATES}]
        for n in range(2,14):
            cur={}
            for w,iv in levels[-1].items():
                im=image(iv,w[-1])
                for s in STATES:
                    x=inter(im,parts[s])
                    if x is not None:cur[w+s]=x
            levels.append(cur)
        counts=[len(x) for x in levels]
        expected=[2**(n+1)-1 for n in range(1,14)]
        l3=set(levels[2]); envelope=set()
        M={'7':'89','8':'789','9':'78'}
        for a0 in STATES:
            for b in M[a0]:
                for c in M[b]: envelope.add(a0+b+c)
        witnesses=[]
        wp=next((root/'outputs').glob('*_markov_order_counterexamples.csv'))
        for r in csv.DictReader(wp.open()):
            n=int(r['witness_length']); w1=r['word_1'];w2=r['word_2']
            e1=''.join(s for s in STATES if w1+s in levels[n]);e2=''.join(s for s in STATES if w2+s in levels[n])
            witnesses.append({'order':int(r['tested_markov_order']),'word_1':w1,'word_2':w2,'computed_extensions_1':e1,'computed_extensions_2':e2,'reported_extensions_1':r['extensions_1'],'reported_extensions_2':r['extensions_2'],'pass':e1==r['extensions_1'] and e2==r['extensions_2']})
        result={'direct_counts_1_13':counts,'expected_counts_1_13':expected,'complexity_counts_pass':counts==expected,'length3_actual_count':len(l3),'length3_envelope_count':len(envelope),'length3_envelope_excess':sorted(envelope-l3),'length3_pass':len(l3)==15 and sorted(envelope-l3)==['787','989'],'markov_witnesses':witnesses,'markov_witnesses_reproduce':all(x['pass'] for x in witnesses),'arithmetic_status':'high-precision Decimal using the package decimal gamma; not an exact or outward-rounded certificate'}
        result['overall_pass']=result['complexity_counts_pass'] and result['length3_pass'] and result['markov_witnesses_reproduce']
        text=json.dumps(result,indent=2)+"\n";print(text,end='')
        if args.json_out:args.json_out.write_text(text)
        if not result['overall_pass']:raise SystemExit(1)
if __name__=='__main__':main()
