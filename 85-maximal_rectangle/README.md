# Maximal Rectangle

**Difficulty:** Hard
**Topics:** Array, Dynamic Programming, Stack, Matrix, Monotonic Stack
**Companies:** (varies by source — commonly asked at FAANG-tier companies)

## Problem

Given a `rows x cols` binary `matrix` filled with `0`'s and `1`'s, find the largest rectangle containing only `1`'s and return its area.

## Examples

### Example 1

```
Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 6
Explanation: The maximal rectangle is shown in the above picture.
```

### Example 2

```
Input: matrix = [["0"]]
Output: 0
```

### Example 3

```
Input: matrix = [["1"]]
Output: 1
```

## Constraints

- `rows == matrix.length`
- `cols == matrix[i].length`
- `1 <= rows, cols <= 200`
- `matrix[i][j]` is `'0'` or `'1'`.

## Approach

This problem can be reduced to repeated applications of the **Largest Rectangle in Histogram** problem:

1. For each row in the matrix, build a "height" array where `height[j]` represents the number of consecutive `1`'s ending at the current row in column `j` (i.e., it accumulates from previous rows, resetting to `0` whenever a `0` is encountered).
2. For each row's height array, compute the largest rectangle area using a **monotonic stack** approach (as in the Largest Rectangle in Histogram problem).
3. Track the maximum area found across all rows.

### Steps in detail

- Initialize a `heights` array of size `cols`, all zeros.
- For each row `i` from `0` to `rows - 1`:
  - For each column `j`, update `heights[j] = heights[j] + 1` if `matrix[i][j] == '1'`, else `heights[j] = 0`.
  - Compute the max rectangle area in the histogram represented by `heights` using a stack-based approach.
  - Update the global maximum area.
- Return the global maximum area.

### Histogram Max Area (helper)

Using a monotonic increasing stack of indices:

- Iterate through the histogram bars (with a sentinel `0` appended at the end to flush the stack).
- While the current bar is shorter than the bar at the top of the stack, pop the stack, compute the area with the popped bar as the smallest bar, using the current index and the new stack top to determine the width.
- Push the current index onto the stack.

