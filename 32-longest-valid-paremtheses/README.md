# Longest Valid Parentheses

**Difficulty:** Hard

## Problem

Given a string containing just the characters `'('` and `')'`, return the length of the longest valid (well-formed) parentheses substring.

## Examples

**Example 1:**
```
Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".
```

**Example 2:**
```
Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".
```

**Example 3:**
```
Input: s = ""
Output: 0
```

## Constraints

- `0 <= s.length <= 3 * 10^4`
- `s[i]` is `'('` or `')'`.

## Approach Ideas

- **Stack-based:** Push indices of unmatched `'('` (and a base `-1` sentinel). On `')'`, pop the stack; if it empties, push the current index as the new base, otherwise update the max length using `i - stack.top()`.
- **Dynamic Programming:** `dp[i]` = length of the longest valid substring ending at index `i`. Only need to handle `s[i] == ')'` cases.
- **Two-pass counters (O(1) space):** Scan left-to-right tracking counts of `'('` and `')'`; when equal, update max, when `')'` count exceeds, reset. Repeat right-to-left to catch cases like `"((()"`.

## Complexity

| Approach          | Time  | Space |
|-------------------|-------|-------|
| Stack             | O(n)  | O(n)  |
| DP                | O(n)  | O(n)  |
| Two-pass counters | O(n)  | O(1)  |
