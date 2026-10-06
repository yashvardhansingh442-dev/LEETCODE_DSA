# 89. Gray Code

**Difficulty:** Medium
**Topics:** Math, Backtracking, Bit Manipulation

## Question

An **n-bit Gray code sequence** is a sequence of `2^n` integers where:

- Every integer is in the inclusive range `[0, 2^n - 1]`.
- The first integer is `0`.
- An integer appears **no more than once** in the sequence.
- The binary representation of every pair of **adjacent** integers differs by **exactly one bit**.
- The binary representation of the **first and last** integers differs by **exactly one bit**.

Given an integer `n`, return any valid n-bit Gray code sequence.

### Example 1

```
Input: n = 2
Output: [0, 1, 3, 2]
```

Binary: `00 → 01 → 11 → 10`. Each adjacent pair (and the last-first pair) differs by one bit.

### Example 2

```
Input: n = 1
Output: [0, 1]
```

### Constraints

- `1 <= n <= 16`

## Approach

### 1. Formula (Binary to Gray) — used in the solution

The i-th Gray code is:

```
gray(i) = i ^ (i >> 1)
```

Generate this for every `i` from `0` to `2^n - 1`.

**Why it works:** going from `i` to `i + 1` flips a trailing run of bits. XORing with the right-shifted value cancels all of those flips except one, so adjacent codes differ by exactly one bit. The sequence starts at `0`, and the last value is `1 << (n-1)`, which differs from `0` by one bit, so the wrap-around condition holds.

- **Time:** O(2^n)
- **Space:** O(1) extra (output excluded)

### 2. Reflection method (alternative)

Build the sequence for `n` bits from the sequence for `n-1` bits:

1. Start with `[0]`.
2. For each bit position `i` from `0` to `n-1`, take the current list in **reverse order**, set bit `i` on each value, and append it to the list.

Example for n = 2: `[0]` → `[0, 1]` → `[0, 1, 3, 2]`.

**Why it works:** the mirrored half is the same as the original half read backwards, so the junction between the two halves differs only in the newly added high bit. Within each half, adjacent values keep their one-bit difference.

- **Time:** O(2^n)
- **Space:** O(1) extra (output excluded)

## Solution (Python)

```python
class Solution:
    def grayCode(self, n: int) -> list[int]:
        return [i ^ (i >> 1) for i in range(1 << n)]
```
