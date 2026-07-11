# CF03 Active-Depth Extract

**Source:** `CF03_Hierarchical_Tachyonic_Interfaces.pdf`, DOI `10.5281/zenodo.19380133`, April 28, 2026.

## Load-bearing distinction used in p5-b3-v1

CF03 distinguishes:

- raw multiplicity: the number of cells, fragments, or boundary components visible at a scale;
- active hierarchy depth: the number of scales at which genuinely new boundaries remain after boundaries already visible at coarser scales are removed or masked.

Its extraction protocol is:

1. coarse-grain at each dyadic scale;
2. extract the boundary set at that scale;
3. subtract or mask boundaries already visible at coarser scales;
4. record the new multiplicity `m_k`;
5. add one unit of depth only when `m_k>0`.

Thus

`N(L) = #{k : m_k > 0}`.

This pass uses only the methodological consequence: equality or inequality between two raw counts does not prove equality of active hierarchy depth. A canonical refinement-preserving map is required.
