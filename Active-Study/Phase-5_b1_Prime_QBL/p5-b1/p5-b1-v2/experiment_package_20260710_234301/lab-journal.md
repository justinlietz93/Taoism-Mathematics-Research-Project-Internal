# Lab Journal

## 20260710T234301

### Question

Why does the B-count near-doubling correction appear confined to `-2,-1,0,1,2`, and does that create a meaningful prime gate?

### Entry 1: exact threshold coordinate

Rewrote the Fibonacci product threshold using the Binet leading term. The resulting real threshold coordinate is affine in `2^A`, with recurrence `y_A = 2 y_(A-1) + gamma`.

### Entry 2: carry extraction

Defined `c_A = ceil(y_A) - 2 ceil(y_(A-1))`. Because `gamma` lies between 8 and 9 and the ceiling remainder lies in `(0,1)`, the carry can only be 7, 8, or 9.

### Entry 3: defect identity

Expanded `B_A=T_A-T_(A-1)` and obtained `d_A=c_A-c_(A-1)`. The observed five-value alphabet is forced.

### Entry 4: exact-threshold certification

Compared the exact Fibonacci-product log against the affine candidate using the Binet correction. The scan `A=0..10000` has positive terminal and preterminal margins after the correction bounds.

### Entry 5: symbolic dynamics

Derived the three carry intervals and their translated doubling map. The outer symbols cannot self-repeat: `7->7` and `9->9` are forbidden.

### Entry 6: prime gate

Since `B_A=2B_(A-1)+d_A`, odd B counts occur exactly on `d_A=+/-1`. All B-primes through `A=1000` satisfy this gate.

### Entry 7: negative control

Replaced dimensional doubling with tripling while retaining the same `d2=B_A-2B_(A-1)` diagnostic. The correction grows beyond 2, confirming that the bounded alphabet is tied to dyadic growth.

### Disposition

The bounded correction is explained. The interesting surviving thread is the ternary carry word, its dyadic symbolic dynamics, and whether prime/gauge events align with its nearest-neighbor transitions.
