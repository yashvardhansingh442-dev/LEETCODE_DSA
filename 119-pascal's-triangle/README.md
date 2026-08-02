\# Pascal's Triangle II

**LC 119** | Easy | Array, Math, DP

## Problem
Given `rowIndex`, return the `rowIndex`th row (0-indexed) of Pascal's triangle.

## Constraints
- `0 <= rowIndex <= 33`
- Follow-up: O(rowIndex) extra space

## Examples
```
rowIndex = 3 → [1,3,3,1]
rowIndex = 0 → [1]
rowIndex = 1 → [1,1]
```

## Intuition
Pascal's triangle row `n` has `n+1` elements, each = sum of two elements above it in the previous row. Row `rowIndex` in terms of binomial coefficients:

$$C(n, k) = C(n, k-1) \times \frac{n-k+1}{k}$$

So instead of building the whole triangle (O(n²) space), you can generate a single row using this multiplicative relationship — each element derived from the previous one in the *same* row.

## Approaches

### 1. Build full triangle (brute force)
- Build row by row from row 0 to rowIndex, each row derived from previous.
- Space: O(rowIndex²) — wasteful, we only need the last row.

### 2. In-place single row update (O(rowIndex) space) ✅
- Start with `row = [1]`.
- For each new row, iterate **backwards** and update in place: `row[j] += row[j-1]`.
- Append a `1` at the end each time.
- Backwards iteration avoids overwriting values you still need (classic 1D DP trick, same pattern as 0/1 knapsack space optimization).

### 3. Direct binomial coefficient formula
- `row[k] = row[k-1] * (rowIndex - k + 1) / k`
- Single pass, O(rowIndex) space, no repeated row-building — most elegant.
- Watch for integer overflow / division order in other languages (Python fine).

## Complexity
| Approach | Time | Space |
|---|---|---|
| Full triangle | O(n²) | O(n²) |
| In-place update | O(n²) | O(n) |
| Binomial formula | O(n) | O(n) |


