# Local Descendant Scope

On Domain 0 before the first `L`,

\[
a_t=i^{\#Q(W_t)}/(u_tv_t).
\]

This gives exact updates

\[
B:a\mapsto a\,u/(u+v),\qquad Q:a\mapsto ia.
\]

| step | selected | prefix | A | q | Q-count | k | j | local descendant |
|---:|:---:|---|---:|---|---:|---:|---:|---|
| 0 | `start` | `∅` | 0 | (1,1) | 0 | 0 | 1 | `1` |
| 1 | `B` | `B` | 0 | (1,2) | 0 | 0 | 1 | `1/2` |
| 2 | `Q` | `BQ` | 0 | (1,2) | 1 | 1 | 2 | `i/2` |
| 3 | `Q` | `BQQ` | 0 | (1,2) | 2 | 2 | 3 | `-1/2` |
| 4 | `B` | `BQQB` | 0 | (2,3) | 2 | 2 | 3 | `-1/6` |
| 5 | `B` | `BQQBB` | 0 | (3,5) | 2 | 2 | 3 | `-1/15` |
| 6 | `B` | `BQQBBB` | 0 | (5,8) | 2 | 2 | 3 | `-1/40` |
| 7 | `Q` | `BQQBBBQ` | 0 | (5,8) | 3 | 3 | 4 | `-i/40` |
| 8 | `B` | `BQQBBBQB` | 0 | (8,13) | 3 | 3 | 4 | `-i/104` |
| 9 | `Q` | `BQQBBBQBQ` | 0 | (8,13) | 4 | 4 | 5 | `1/104` |
| 10 | `B` | `BQQBBBQBQB` | 0 | (13,21) | 4 | 4 | 5 | `1/273` |
| 11 | `B` | `BQQBBBQBQBB` | 0 | (21,34) | 4 | 4 | 5 | `1/714` |
| 12 | `Q` | `BQQBBBQBQBBQ` | 0 | (21,34) | 5 | 5 | 6 | `i/714` |
| 13 | `B` | `BQQBBBQBQBBQB` | 0 | (34,55) | 5 | 5 | 6 | `i/1870` |
| 14 | `B` | `BQQBBBQBQBBQBB` | 0 | (55,89) | 5 | 5 | 6 | `i/4895` |
| 15 | `L` | `BQQBBBQBQBBQBBL` | 1 | (55,89) | 5 | 0 | 7 | `new active axis opened; old=i/4895` |

At `L`, `i/4895` is latched as the completed old-axis descendant. The newborn active axis is distinct and unmutated. The source does not identify `a_t` with a diagonal or any specific one of the four descendant blocks.
