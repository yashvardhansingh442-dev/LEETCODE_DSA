# Sqrt(x)

**Difficulty:** Easy

## Problem

Given a non-negative integer `x`, return the square root of `x` rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

- For example, do not use `pow(x, 0.5)` in C++ or `x ** 0.5` in Python.

## Examples

**Example 1:**
```
Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.
```

**Example 2:**
```
Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
```

## Constraints

- `0 <= x <= 2^31 - 1`

## Approach Ideas

- **Binary Search:** Search for the largest integer `mid` such that `mid * mid <= x`, over the range `[0, x]`. Standard binary search narrowing `low`/`high` each step. O(log x) time, O(1) space. Watch for overflow when computing `mid * mid` for large `x` — use a 64-bit type.
- **Newton's Method:** Start with a guess (e.g., `x`) and iteratively refine using `next = (guess + x / guess) / 2` until it converges (`next >= guess`). Converges quickly, typically O(log x) iterations, O(1) space.
- **Linear Scan (Brute Force):** Increment a counter from `0` upward until `counter * counter > x`, then return `counter - 1`. O(sqrt(x)) time — too slow for large inputs but simple to reason about.

## Complexity

| Approach        | Time      | Space |
|------------------|-----------|-------|
| Binary Search    | O(log x)  | O(1)  |
| Newton's Method  | O(log x)  | O(1)  |
| Linear Scan      | O(sqrt(x))| O(1)  |
