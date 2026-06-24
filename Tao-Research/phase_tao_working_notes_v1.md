# Phase Calculus ↔ Taoism/Yijing Math Working Notes v1

## Locked correction

The previous phrasing “B external match beyond Fibonacci/Farey adjacency still unresolved” was wrong for the internal Phase side.

**B is already exact internally:**

```text
B(u,v) = sort(v, u+v)
```

Starting from `(1,1)`, the B corridor reaches the first balanced floor anchor at depth 9:

```text
d0  (1,1)
d1  (1,2)
d2  (2,3)
d3  (3,5)
d4  (5,8)
d5  (8,13)
d6  (13,21)
d7  (21,34)
d8  (34,55)
d9  (55,89)

uv = 4895
r  = 1/4895
```

So the unresolved question is **not whether B is real**. The unresolved question is whether the Tao/Yijing material contains an external structural correlate to B-depth / branch-refinement / floor-anchor behavior.

## What “4+6” actually came from

“4+6” was sloppy shorthand and should be replaced.

The Vincent John article gives two adjacent structures:

1. **Si-Xiang / Four Appearances**
   - Take one Yin/Yang pair.
   - Add a Yin/Yang pair to each branch.
   - Follow bottom-to-top paths.
   - This yields four two-line appearances:
     - Tai-Yang
     - Shao-Yin
     - Shao-Yang
     - Tai-Yin

2. **Chinese Medicine / Six Levels**
   - The six-level view keeps the four appearances **plus the generating Yin/Yang pair that built them**.
   - The builder Yang is Yang-Ming.
   - The builder Yin is Jue-Yin.

Correct shorthand:

```text
4 appearances + 2 builder/generator states = 6-level reading
```

Not:

```text
4 + 6
```

## Why this matters for Q

The candidate structural bridge is:

```text
Yijing/article side:
  four visible appearances
  + two generator/builder states
  = six-level carrier reading

Phase/Q side:
  four equatorial quarter-turn phase seats
  + two axial/radix-pole seats
  = six-seat carrier
```

This is a **structural candidate**, not yet a proven identity. But it is the correct thing to test.

## Q locked model

```text
seat set = {+x, +y, -x, -y, +z, -z}

Q_z:
  +x -> +y -> -x -> -y -> +x

fixed axial pair:
  +z, -z
```

Q is therefore:

```text
4 visible quarter phases around a retained radix/axis
2 axial seats retained as fixed poles / generator axis
```

## B locked model

Matrix form:

```text
F = [[0,1],
     [1,1]]
```

Path:

```text
F^9(1,1) = (55,89)
```

The determinant is `-1`, so each B step is orientation-reversing in the two-coordinate carrier while preserving the integer recurrence structure.

## Shape article: important extracted mechanics

The article’s root math sequence is:

```text
Wuji
-> Taiji
-> Yin/Yang
-> infinite binary tree
-> Si-Xiang / 4 appearances
-> Chinese Medicine 6 levels
-> Bagua / 8 trigrams
-> I-Ching / 64 hexagrams
-> 10,000 things / indefinite manifestation
```

Article-side structural statements extracted from the pass:

```text
Wuji = preliminary absence / void / potential state
Taiji = separating line / present boundary / interface
Yin-Yang = binary actualization / split
Tao pattern = infinite binary tree rising from Wuji
Si-Xiang = four two-line path groupings
Six Levels = four appearances plus builder Yin/Yang pair
Bagua = add another Yin/Yang line to get 8 trigrams
I-Ching = 8 x 8 trigram product, producing 64 six-line states
Pre-Heaven arrangement = standing in center looking outward
Post-Heaven arrangement = middle-line inversion + center split
```

## B correlation target from article

The article’s B-like behavior is not “B by name.” It is this sequence:

```text
root pair
-> add Yin/Yang pair to each branch
-> paths through branches define appearances
-> add another line to refine into trigrams
-> product two trigrams into six-line hexagrams
```

This is branch-refinement with retained path structure. It is not yet the exact Fibonacci/Farey B unless the refinement path can be encoded by the same `(v,u+v)` or equivalent denominator-pair law.

## What to test next

### Test A: Yijing six-level/Q seat candidate

Build an encoding where:

```text
four appearances = equatorial phase states
builder Yin/Yang pair = axial generator states
```

Pass condition:

```text
The four appearances cycle under a quarter-turn operator while the two builder states stay fixed or mediate the orbit.
```

Fail condition:

```text
The six-level system cannot support a four-around-two decomposition without arbitrary relabeling.
```

### Test B: B-depth / Yijing branch-depth candidate

Encode the article’s branching construction as binary paths. Try to derive a denominator-pair or continued-fraction measure from each path.

Pass condition:

```text
A non-arbitrary measure of branch refinement follows Fibonacci/Farey growth, or the depth-9 anchor appears as a natural floor under frozen rules.
```

Fail condition:

```text
The Yijing branch tree is merely binary count growth 2^n and has no B-like denominator/refinement law.
```

### Test C: Pre-Heaven -> Post-Heaven as L

Article-side move:

```text
Heaven middle line flips to Yin -> Fire
Earth middle line flips to Yang -> Water
center Earth splits into Earth/Mountain
```

Phase-side L candidate:

```text
same carrier pieces
internal line/axis changes
visible identity changes
arrangement re-articulates into a new domain
```

Pass condition:

```text
The transformation preserves a carried invariant while changing visible trigram identity and global arrangement.
```

Fail condition:

```text
The transformation is just a named rearrangement with no invariant-preserving lift.
```

## Current status after correction

```text
Q: strong structural lead.
B: exact internally; external branch-refinement lead exists, exact match not yet tested.
L: strong structural lead through line inversion, center split, projection/lift, and modular SL2/PSL2 loss.
Shadow: strong eta/theta/chi12 lead, not closed.
```

## Do not forget

- Do not look for literal `QBL` in historical sources.
- Q is not “5 elements.” Q is four phases around a radix/axis with six carrier seats.
- The article’s six-level structure is `4 appearances + 2 builder states`, not `4+6`.
- B is the depth-9 Fibonacci/Farey floor-anchor operator path.
- The external B question is whether ancient/Yijing branch-refinement has the same path law, not whether B exists in Phase Calculus.
