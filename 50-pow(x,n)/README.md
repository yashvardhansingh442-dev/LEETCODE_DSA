# Pow(x, n)

**Difficulty:** Medium

## Problem

Implement [pow(x, n)](http://www.cplusplus.com/reference/valarray/pow/), which calculates `x` raised to the power `n` (i.e., `x^n`).

## Examples

**Example 1:**
```
Input: x = 2.00000, n = 10
Output: 1024.00000
```

**Example 2:**
```
Input: x = 2.10000, n = 3
Output: 9.26100
```

**Example 3:**
```
Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2^-2 = 1/2^2 = 1/4 = 0.25
```

## Constraints

- `-100.0 < x < 100.0`
- `-2^31 <= n <= 2^31 - 1`
- `n` is an integer.
- Either `x` is not zero or `n > 0`.
- `-10^4 <= x^n <= 10^4`

## Approach Ideas

- **Naive Loop:** Multiply `x` by itself `n` times. O(n) time — too slow for large `n` given the constraints.
- **Fast (Binary) Exponentiation — Recursive:** Use the recurrence `x^n = (x^(n/2))^2` when `n` is even, and `x^n = x * (x^(n/2))^2` when `n` is odd. Halves the problem size each call. O(log n) time, O(log n) space (call stack).
- **Fast Exponentiation — Iterative:** Same idea without recursion. Walk through the bits of `n`, squaring `x` each iteration and multiplying the result by the current `x` whenever the corresponding bit is set. O(log n) time, O(1) space.
- **Handling Negative `n`:** Convert to the positive case by computing `1 / x^(-n)`. Careful with the edge case `n = -2^31`, since its positive counterpart `2^31` overflows a 32-bit signed integer — cast `n` to a 64-bit type before negating.

## Complexity

| Approach                     | Time     | Space    |
|-------------------------------|----------|----------|
| Naive Loop                    | O(n)     | O(1)     |
| Fast Exponentiation (Recursive)| O(log n)| O(log n) |
| Fast Exponentiation (Iterative)| O(log n)| O(1)     |
