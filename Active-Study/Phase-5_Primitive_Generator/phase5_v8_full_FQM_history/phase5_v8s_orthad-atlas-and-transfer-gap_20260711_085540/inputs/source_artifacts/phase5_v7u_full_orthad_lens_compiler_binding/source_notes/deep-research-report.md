# Canonical Coupling from Retained QBL History

## Core finding

The literature does not appear to contain a single off-the-shelf theorem of the exact form

```text
arbitrary retained QBL history
  -> canonical normal form
  -> unique coupling tensor up to gauge
```

but it does contain most of the needed pieces in adjacent fields. The strongest composite bridge is: **trace theory** for canonical history reduction under legal commutations, **Čech-cocycle / sheaf / monodromy formalisms** for turning overlap-local transition data into a global invariant modulo gauge, and **finite quadratic modules with Weil representations** for classifying the resulting bilinear or quadratic coupling object up to basis change. The most important corrective is that the canonical object in these literatures is usually **not** a raw matrix \(C=(c_{ij})\), but a **gauge class** of transition data, holonomy data, or an isometry class of bilinear/quadratic form; a matrix appears only after choosing coordinates. citeturn33view0turn17view0turn32view0turn25view2turn8view2

So the best-supported answer to your blocker is not “yes, every arbitrary retained history canonically yields a unique tensor” in the raw sense. It is closer to: **yes, provided the history is admissible and the legal rewrites are confluent, one can plausibly extract a canonical coupling object from history alone, but the invariant object should be treated as a gauge class of cocycle/holonomy/quadratic data, not as a basis-fixed tensor.** The strongest obstruction in the surveyed literature is also clear: without overlap-compatibility and rewrite confluence, arbitrary local histories need not glue to a unique global object at all. citeturn14view0turn17view0turn33view0turn32view0

## Histories modulo legal rewrites

The best direct match for your “history word \(\to\) canonical normal form” problem is **Mazurkiewicz trace theory**. In this setting one starts with an alphabet of events and an independence relation saying which letters may commute. A trace is then an equivalence class of words under adjacent swaps of independent letters. Classical trace theory gives a **unique Cartier–Foata normal form**: every nonempty trace has a unique decomposition into a sequence of nonempty cliques or steps, and these steps encode maximal parallel layers. More recent concurrency papers restate the same fact algorithmically: the Foata normal form is a **unique decomposition of the trace into maximal steps**. citeturn12search16turn33view0

That matters for QBL because it precisely matches the distinction you drew between commuting and noncommuting retained events. If different axes are genuinely independent, their letters should commute; if a latch, overlap, or boundary event couples them, those letters should remain dependent. In that model, “legal rewrites preserve the same history object” becomes the standard statement that different linearisations represent the same trace, and the normal form gives a canonical representative of the retained history class. This is the strongest external hit I found for the missing **normal-form** half of your bridge. citeturn12search16turn33view0

The concurrency literature goes further than just existence of a normal form. In the asynchronous-automata formulation, the **diamond property** guarantees that all linearisations of the same trace reach the same automaton state, so invariance under legal swaps is proved by construction. The same paper also shows that Foata normal forms of local process views can be merged by **stepwise unions** to recover larger views and ultimately the global trace. That is unusually close to your desired pattern:

```text
local retained views
  -> canonical local normal forms
  -> explicit merge law
  -> global history invariant
```

In other words, the literature already knows how to canonicalize partially commutative histories and how to fuse local retained views without dropping the invisible carried structure. citeturn33view0

For Orthad, this suggests a concrete modeling move: treat a retained QBL history as a word in an event alphabet \(\Sigma\) equipped with an independence relation \(I\). Then the canonical history object is not the raw word \(h\), but the trace class \([h] \in M(\Sigma,I)\), with a unique Foata decomposition \(F(h)\). What still has to be added, and what trace theory alone does not provide, is how those normalized history layers induce your coupling data \(C\). That bridge has to come from overlap-cocycle or holonomy machinery. citeturn12search16turn33view0

## From overlaps to global invariants

The cleanest mathematical language for “overlap / boundary / transition data \(\to\) global object” is **Čech cocycles**. Standard bundle reconstruction works exactly by assigning transition functions \(g_{\alpha\beta}\) on pairwise overlaps, requiring inverse-compatibility and a cocycle law on triple overlaps. Cavalcanti’s notes make the point explicitly: the family \(\{g_{\alpha\beta}\}\) contains enough information to reconstruct the bundle with local trivialisations, and isomorphism classes of bundles over a good cover correspond to equivalence classes of such transition families. They also spell out the gauge relation induced by a change of trivialisation,
\[
\tilde g_{\alpha\beta}=f_\beta^{-1}\,g_{\alpha\beta}\,f_\alpha,
\]
which is exactly the “same coupling object up to gauge” pattern you want. citeturn16view1turn16view2turn17view0

This source is especially relevant because it also identifies the nonabelian hazard. For \(k>1\), the transition values lie in \(\mathrm{GL}(k)\), which is noncommutative, so the abelian version of Čech cohomology is no longer enough “as is.” That is important for QBL/Orthad: once your overlap operators live in a noncommutative operator algebra, the right invariant is not a scalar cocycle class but a **nonabelian gauge class of transition data**. That is already closer to a coupling tensor up to gauge than to a unique basis-fixed matrix. citeturn16view1turn17view0

If you want a discrete, computable overlap formalism rather than atlas language, **cellular sheaves on graphs** are a very good fit. A sheaf on a graph assigns stalks to vertices and edges plus restriction maps to incidences; a section is a choice of local values that agree after restriction to each overlap. Hansen’s notes make this concrete: local consistency across an edge is exactly equality of the two restricted values, the space of global sections is the kernel of a coboundary map \(\delta\), and the associated sheaf Laplacian is \(L_F=\delta^\*\delta\). In other words, there is already a standard linear-algebraic way to encode “retained local data over overlapping regions” and ask whether it glues to a global object. citeturn14view0turn14view2

One sharp warning from the sheaf literature is highly relevant to your “arbitrary history” wording. Hansen notes that on a connected graph with a cycle and equal-dimensional stalks, **almost any** choice of restriction maps yields no nontrivial global sections. That means arbitrary local overlap histories are generically **not** globally compatible. For Orthad, this strongly suggests that the problem is not merely to reduce arbitrary history to a tensor; it is first to define an **admissibility criterion** saying which histories satisfy enough overlap compatibility to determine any global coupling object at all. Without that, uniqueness can fail before gauge even enters the picture. citeturn13view3turn14view1

The monodromy layer then gives the retained-loop invariant. Mathlib’s formalized covering-space library states several directly relevant facts: any path in the base of a covering map lifts uniquely once the starting point in the fiber is fixed; lifts of homotopic relative-endpoint paths end at the same point; the resulting monodromy depends only on the homotopy class of the path; and monodromy is organized as a functor from the **fundamental groupoid**. This is almost exactly the abstract structure you described: retained history lives in the lifted state, visible projection is not enough, loop history matters, and the history-induced action is invariant under allowed deformations of the path. citeturn32view0

Taken together, these sources suggest the following bridge template:

```text
normalized history class
  -> overlap transition cocycle / sheaf restrictions
  -> loop holonomy or monodromy
  -> gauge class of retained global object
```

That is the mathematically standard answer to “retained history exists; what coupling data does it determine?” The missing Orthad-specific work is to define the overlap graph, the event-to-transition assignment, and the target coefficient group or module in which the holonomy lives. citeturn17view0turn14view2turn32view0

## The most natural target is a quadratic module, not a raw tensor

Your Phase-5 target really does land in **finite quadratic module / discriminant form** territory. Strömberg defines a finite quadratic module \(Q=(D,Q)\) as a finite abelian group \(D\) with a nondegenerate quadratic form \(Q:D\to \mathbf{Q}/\mathbf{Z}\), together with the associated bilinear form \(B(x,y)=Q(x+y)-Q(x)-Q(y)\). He also emphasizes that the canonical example is the **discriminant form** \(D=L'/L\) attached to an even lattice. This is exactly the kind of object one expects when a coupling matrix should be meaningful only modulo basis change and should support Weil-type operators. citeturn8view2

The decisive classification fact is the **Jordan decomposition**. Strömberg states that the underlying finite abelian group decomposes into \(q\)-power components orthogonal with respect to the bilinear form, and that this decomposition is called the Jordan decomposition of the finite quadratic module. He also adds a crucial caveat: it is unique **except for \(p=2\)**. That caveat is not a side issue; it is probably the most important external warning for your project. It says that even when a canonical quadratic object exists, a completely rigid basis-level normal form can fail at the 2-primary part unless extra conventions are imposed. If Orthad is aiming for “unique coupling tensor up to gauge,” this is exactly the sort of obstruction one should expect. citeturn25view2

The same paper gives the computational side you want. It proves an explicit formula for the matrix coefficients of the Weil representation associated to an arbitrary finite quadratic module, and the abstract emphasizes that the formula is arranged to be easy to implement on a computer. Within the paper, Gauss sums over an orthogonal Jordan decomposition split into local factors, which is the standard reason these objects are tractable blockwise. So the literature already supplies both the **classification language** and an **algorithmic operator layer** once the quadratic module has been identified. citeturn0search2turn25view2

A further useful constructive result is that any finite quadratic module can be decomposed into indecomposables, and indecomposable finite quadratic modules can be realized explicitly as discriminant modules of even lattices with concrete Gram matrices. That matters because it says the target object is not merely abstractly classifiable; it can be realized in a concrete basis when needed. For Orthad, that supports the idea that once a canonical gauge class is extracted from history, one can still choose a concrete presentation \(C=(c_{ij})\) for computation, while remembering that the invariant content lies in the isometry/gauge class, not in the entries themselves. citeturn26search7turn8view2

The practical conclusion is that the mathematically clean target of your bridge is probably not “history \(\to\) tensor” in the first instance, but rather

```text
history
  -> finite abelian module D_h
  -> quadratic form q_h or bilinear form B_h
  -> tensor C_h after choosing a basis of D_h
```

with uniqueness expected only **up to change of basis / gauge**, and with special care required for the 2-primary sector. That formulation lines up with the external literature much better than trying to make the matrix itself the primitive invariant. citeturn8view2turn25view2

## Computational analogs that look like Orthad

The overset-grid literature is not just a loose metaphor; it solves a very close engineering problem. Chesshire and Henshaw describe conservative interpolation on overlapping grids by treating interpolation coefficients as free parameters and then deriving **constraints** that force conservation. A system of equations is solved to determine the coefficients. In essence, overlap-local transfer rules are not accepted merely because they interpolate; they are accepted only if they satisfy a globally meaningful invariant. That is the right computational analogy for “compile coupling from overlap history, but only through legal rewrites that preserve the same global tensor.” citeturn23view2

The Yin–Yang overset literature sharpens that analogy. Hall and Nair describe the Yin–Yang mesh as two rectangular grids placed at right angles with a small amount of overlap, explicitly note that overset methods are **not inherently conservative**, and cite work showing that exact conservation can be restored by a local cell-wise constraint. This is extremely close to your Orthad blocker: overlap by itself does not give a canonical global coupling; one needs an additional compatibility law that turns local transfer data into a globally conserved object. citeturn24view2

A second useful analog comes from overlapping domain decomposition with explicit interface variables. Discacciati, Gervasio, and Quarteroni formulate Stokes–Darcy coupling on overlapping regions using control variables that are the **traces of velocity and pressure on internal boundaries**, and they determine these controls by minimizing a cost functional that measures jumps across the interfaces. They say explicitly that the choice of cost functional is crucial to ensure **uniqueness** on the overlapping area. That is a very strong parallel with the Orthad situation: retained local histories on overlaps do not determine a unique coupling object until one specifies the invariant that legalizes or penalizes interface mismatch. citeturn36view0

The magnetic-topology literature gives the cleanest example of topology changing before visible projection changes. Longcope’s review distinguishes pointwise footpoint mappings from reduced connectivity models. Barnes, Longcope, and Leka then describe Magnetic Charge Topology models in which field lines are classified by source footpoints, the corona is divided into flux domains, and reconnection **exchanges footpoints** and transports flux from one domain to another. Titov, Hornig, and Démoulin formalize quasi-separatrix layers using the Jacobian of the footpoint mapping and show that the relevant connectivity change is encoded in the local mapping geometry, not in a visible emissive proxy. This is directly relevant to your point that retained topological custody changes precede terminal projection. citeturn13view8turn28view0turn8view6

These analogs all point the same way. The sought-for Orthad bridge should likely be phrased as: **compile a global coupling invariant by solving an overlap-consistency problem over a retained history graph, with conservation / holonomy / cocycle compatibility as the admissibility law.** That is the common structure shared by overset conservation, interface control, and magnetic connectivity tracking. citeturn23view2turn36view0turn28view0turn8view6

## What the literature implies for the Orthad theorem

The most defensible theorem schema suggested by the sources is something like this:

```text
Given:
  a QBL event alphabet Σ
  an independence relation I on Σ
  an overlap graph or cover U
  history-to-transition assignment T on overlaps
  admissibility laws:
    - trace-confluence under I
    - cocycle compatibility on overlaps
    - gauge relation by local frame change

Define:
  [h]          := trace class of retained history h
  F(h)         := Foata normal form of [h]
  g_h          := overlap cocycle induced by F(h) through T
  Hol(h)       := monodromy/holonomy class of g_h on cycles
  (D_h, q_h)   := finite quadratic module extracted from Hol(h)
  C_h          := matrix of the associated bilinear form in a chosen basis

Then:
  C_h is not canonical as a matrix,
  but (D_h, q_h), or its isometry class, is canonical up to gauge.
```

Every arrow in that schema has a close analogue in the literature. Trace theory supplies the canonical history normal form and rewrite invariance; cocycle and bundle theory supply the overlap compatibility and gauge quotient; covering-space monodromy supplies loop-sensitive retained action; finite quadratic modules supply the canonical bilinear/quadratic target together with Weil-compatible operator theory. citeturn33view0turn17view0turn32view0turn8view2turn25view2

The same sources also make the failure modes unusually clear. If legal rewrites do not satisfy a diamond/confluence property, different history words can survive normalization as genuinely different retained actions. If overlap transitions fail cocycle compatibility, local retained data need not glue to any global object. If one insists on a basis-fixed tensor rather than an isometry class, gauge changes and basis changes will falsely look like different couplings. And if the 2-primary sector is not normalized carefully, even Jordan data can fail to look unique at the presentation level. Those are not speculative worries; they are exactly the places where the surveyed theories say uniqueness can break. citeturn33view0turn14view0turn17view0turn25view2

There is also a pleasant formalization angle. Mathlib already has formalized objects for unique path lifting, homotopy lifting, monodromy as an action of the fundamental group, and monodromy as a functor from the fundamental groupoid. That means one of the most delicate retained-history pieces is already on a firm Lean-ready footing. By contrast, the main pieces that would still need bespoke formal development for your stack are the QBL-specific trace normalization layer and the extraction/classification of finite quadratic modules from the resulting overlap holonomy data. citeturn32view0turn33view0turn25view2

The net result is fairly sharp. External research does support the existence of a serious bridge from retained history to canonical coupling data, but it supports it in a **qualified** form: the invariant should be a **gauge class of overlap-holonomy / quadratic-module data**, and a unique coupling tensor should be expected only **after** choosing coordinates and only for histories satisfying explicit admissibility, cocycle, and confluence laws. In that sense, the literature points to a path for Orthad, but it also strongly suggests that “arbitrary history \(\to\) unique raw tensor” is too strong unless “arbitrary” is narrowed to “arbitrary admissible retained history.” citeturn33view0turn17view0turn32view0turn8view2turn25view2turn14view0