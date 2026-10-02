# 150. Evaluate Reverse Polish Notation

**Difficulty:** Medium
**Topics:** Array, Math, Stack
**Link:** [LeetCode Problem](https://leetcode.com/problems/evaluate-reverse-polish-notation/)

---

## Problem Statement

You are given an array of strings `tokens` that represents an arithmetic expression in a [Reverse Polish Notation](http://en.wikipedia.org/wiki/Reverse_Polish_notation).

Evaluate the expression. Return an integer that represents the value of the expression.

**Note that:**

- The valid operators are `'+'`, `'-'`, `'*'`, and `'/'`.
- Each operand may be an integer or another expression.
- The division between two integers always truncates toward zero.
- There will not be any division by zero.
- The input represents a valid arithmetic expression in a reverse polish notation.
- The answer and all the intermediate calculations can be represented in a **32-bit integer**.

---

## Examples

### Example 1

```
Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
```

### Example 2

```
Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
```

### Example 3

```
Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
```

---

## Constraints

- `1 <= tokens.length <= 10^4`
- `tokens[i]` is either an operator: `"+"`, `"-"`, `"*"`, or `"/"`, or an integer in the range `[-200, 200]`.

---

## Approach (Stack)

In RPN, an operator always acts on the two most recent operands, which is exactly what a stack gives us.

1. Create an empty stack.
2. For each token:
   - If it is a number, push it onto the stack.
   - If it is an operator, pop `b` (top) then `a`, compute `a op b`, and push the result.
3. The single value left on the stack is the answer.

**Watch out:** pop order matters for `-` and `/`. The first pop is the right operand `b`. For division use `int(a / b)` so the result truncates toward zero (Python's `//` floors, which is wrong for negatives).

---
