<h2><a href="https://leetcode.com/problems/min-stack/">155. Min Stack</a></h2>

<h3>Medium</h3>

<hr>

Design a stack that supports `push`, `pop`, `top`, and retrieving the minimum element in constant time.

Implement the `MinStack` class:

* `MinStack()` initializes the stack object.
* `void push(int val)` pushes the element `val` onto the stack.
* `void pop()` removes the element on the top of the stack.
* `int top()` gets the top element of the stack.
* `int getMin()` retrieves the minimum element in the stack.

You must implement a solution with `O(1)` time complexity for each function.

### Example 1

```
Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]
```

**Explanation**

```
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
```

### Constraints

* `-2^31 <= val <= 2^31 - 1`
* `pop`, `top` and `getMin` operations will always be called on non-empty stacks.
* At most `3 * 10^4` calls will be made to `push`, `pop`, `top`, and `getMin`.

---

## Approach

**Pattern: Stack + auxiliary information.**

The challenge is that the minimum can change after a `pop`, so a single `min` variable is not enough.

The trick is to store, alongside each element, **the minimum of the stack up to that point**. Keep `(value, current_min)` pairs in the stack. Whenever a new element is pushed:

`new_min = min(value, previous_min)`

When an element is popped, its pair is removed, and the pair beneath it still carries the previous minimum, so nothing needs to be recomputed. Both `top()` and `getMin()` are read directly from the top pair in O(1).
