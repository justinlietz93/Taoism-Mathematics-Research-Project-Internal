#!/usr/bin/env python3
"""v8k audit: SNF radical-size verification for the five residual cores
(validated against enumeration on rank5/rank6 during the session).
Run: python3 v8k_checks.py <v8k-package-root>"""
import csv, json, sys
from math import gcd
def lcm(a,b): return a*b//gcd(a,b)

def snf_invariants(mat, need):
    A=[row[:] for row in mat]; R,C=len(A),len(A[0]); out=[]; r=0
    while r<need:
        piv=None
        for i in range(r,R):
            for j in range(r,C):
                if A[i][j]!=0 and (piv is None or abs(A[i][j])<abs(A[piv[0]][piv[1]])): piv=(i,j)
        if piv is None: out.append(0); r+=1; continue
        pi,pj=piv; A[r],A[pi]=A[pi],A[r]
        for i in range(R): A[i][r],A[i][pj]=A[i][pj],A[i][r]
        while True:
            moved=False
            for i in range(r+1,R):
                if A[i][r]%A[r][r]!=0:
                    qd=A[i][r]//A[r][r]
                    for j in range(r,C): A[i][j]-=qd*A[r][j]
                    A[r],A[i]=A[i],A[r]; moved=True; break
            if moved: continue
            for i in range(r+1,R):
                if A[i][r]:
                    qd=A[i][r]//A[r][r]
                    for j in range(r,C): A[i][j]-=qd*A[r][j]
            moved=False
            for j in range(r+1,C):
                if A[r][j]%A[r][r]!=0:
                    qd=A[r][j]//A[r][r]
                    for i in range(r,R): A[i][j]-=qd*A[i][r]
                    for i in range(r,R): A[i][r],A[i][j]=A[i][j],A[i][r]
                    moved=True; break
            if moved: continue
            for j in range(r+1,C):
                if A[r][j]:
                    qd=A[r][j]//A[r][r]
                    for i in range(r,R): A[i][j]-=qd*A[i][r]
            if all(A[i][r]==0 for i in range(r+1,R)) and all(A[r][j]==0 for j in range(r+1,C)): break
        out.append(abs(A[r][r])); r+=1
    return out

def radical_size_snf(D,du,edges):
    n=len(D); M=1
    for d in D: M=lcm(M,2*d)
    for i in range(n):
        for j in range(i+1,n): M=lcm(M,lcm(D[i],D[j]))
    G=[[0]*n for _ in range(n)]
    for i in range(n): G[i][i]=du[i]*(M//D[i])
    for i,j,c in edges:
        u=c*(M//lcm(D[i],D[j])); G[i][j]+=u; G[j][i]+=u
    mat=[[G[j][i] for j in range(n)]+[M if k==i else 0 for k in range(n)] for i in range(n)]
    d=snf_invariants(mat,n)
    num=1
    for x in D: num*=x
    for x in d: num*=x
    return num//(M**n)

def main():
    root=sys.argv[1]
    rows=list(csv.DictReader(open(root+'/outputs/phase5_v8k_rankge5_complete_form_spec_and_radical_measurement.csv')))
    allok=True
    for r in rows:
        D=json.loads(r['D2_core']); du=json.loads(r['diag_units'])
        ed=[tuple(e) for e in json.loads(r['edges_2core'])]
        mine=radical_size_snf(D,du,ed); theirs=int(r['radical_size_ambient'])
        print(r['case'],'mine=',mine,'theirs=',theirs,'match=',mine==theirs)
        allok &= (mine==theirs)
    print('ALL MATCH:',allok)
    sys.exit(0 if allok else 1)

if __name__=='__main__': main()
