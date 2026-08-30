# Combinations

**Difficulty:** Medium

## Problem

Given two integers `n` and `k`, return all possible combinations of `k` numbers chosen from the range `[1, n]`.

You may return the answer in any order.

## Examples

**Example 1:**
```
Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.
```

**Example 2:**
```
Input: n = 1, k = 1
Output: [[1]]
Explanation: There is 1 choose 1 = 1 total combination.
```

## Constraints

- `1 <= n <= 20`
- `1 <= k <= n`

## Approach Ideas

- **Backtracking:** Build combinations incrementally. Maintain a running list and a `start` index; at each step, try adding every number from `start` to `n`, recurse with `start + 1`, then backtrack (remove the last added number). When the running list reaches size `k`, record it as a valid combination.
- **Pruning:** Stop early if there aren't enough remaining numbers to complete a combination of size `k` (i.e., skip candidates where `n - current + 1 < k - chosen.size()`), which significantly reduces the search space.
- **Iterative (Bitmask):** Since `n <= 20`, iterate over all `2^n` bitmasks, keep those with exactly `k` bits set, and translate each mask into the corresponding number set. Simple but less efficient than backtracking with pruning.
- **Lexicographic/Iterative Combination Generation:** Start with the first combination `[1, 2, ..., k]` and repeatedly compute the next combination in lexicographic order until none remain.

## Complexity

| Approach                    | Time                      | Space         |
|------------------------------|---------------------------|---------------|
| Backtracking (with pruning)   | O(C(n, k) * k)            | O(k)          |
| Bitmask                       | O(2^n * n)                | O(1) extra    |

Where `C(n, k)` is the binomial coefficient "n choose k", representing the total number of valid combinations.
