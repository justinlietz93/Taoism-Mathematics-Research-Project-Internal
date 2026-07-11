from __future__ import annotations
from dataclasses import dataclass, asdict, replace

@dataclass(frozen=True, slots=True)
class State:
    A:int=0; u:int=1; v:int=1; phase_quarters:int=0; k:int=0; j:int=1; word:str=""
    @property
    def pair(self): return (self.u,self.v)
    @property
    def product(self): return self.u*self.v
    @property
    def phase_label(self): return ("1","i","-1","-i")[self.phase_quarters%4]
    def evolve(self,**kw): return replace(self,**kw)
    def to_dict(self):
        d=asdict(self); d.update(pair=[self.u,self.v],pair_product=self.product,phase_mod4=self.phase_quarters%4,phase_label=self.phase_label); return d

def positions(A): return 6*(2**A)
def start_j(A): return 1+6*((2**A)-1)
def capacity(j): return 2 if j==1 else 4 if j==2 else 2**(2*j)
def next_pair(s): return (s.v,s.u+s.v)
def can_q(s): return s.k<positions(s.A)-1
def can_b(s):
    n=next_pair(s)
    return n[0]*n[1]<=capacity(s.j) if can_q(s) else s.product<capacity(s.j)
def floor_reached(s): return not can_b(s) and not can_q(s)
def select(s): return "B" if can_b(s) else "Q" if can_q(s) else "L"

def apply(s,p):
    if p!=select(s): raise ValueError('priority violation')
    if p=='B':
        u,v=next_pair(s); return s.evolve(u=u,v=v,word=s.word+'B')
    if p=='Q': return s.evolve(phase_quarters=s.phase_quarters+1,k=s.k+1,j=s.j+1,word=s.word+'Q')
    A=s.A+1; return s.evolve(A=A,k=0,j=start_j(A),word=s.word+'L')

def run_first_crossing_and_next_b():
    s=State(); rows=[]; saw_l=False
    for idx in range(1,101):
        p=select(s); before=s; s=apply(s,p)
        rows.append({'step_index':idx,'primitive':p,'before':before.to_dict(),'after':s.to_dict(),'can_b_before':can_b(before),'can_q_before':can_q(before),'floor_reached_before':floor_reached(before),'capacity_before':capacity(before.j),'available_positions_before':positions(before.A),'word_prefix':s.word})
        if p=='L': saw_l=True
        elif saw_l: return s,rows
    raise RuntimeError('no first crossing')

def independent_oracle():
    A,u,v,ph,k,j,w=0,1,1,0,0,1,''; out=[]; saw=False
    for idx in range(1,101):
        N=6*(2**A); cap=2 if j==1 else 4 if j==2 else 2**(2*j); nu,nv=v,u+v
        cq=k<N-1; cb=(nu*nv<=cap) if cq else (u*v<cap); p='B' if cb else 'Q' if cq else 'L'
        if p=='B': u,v=nu,nv
        elif p=='Q': ph+=1; k+=1; j+=1
        else: A+=1; k=0; j=1+6*((2**A)-1)
        w+=p; out.append((p,w,A,u,v,ph,k,j))
        if p=='L': saw=True
        elif saw: return out
    raise RuntimeError
