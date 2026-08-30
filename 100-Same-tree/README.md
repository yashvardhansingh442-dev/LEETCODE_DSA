# Same Tree

**Difficulty:** Easy

## Problem

Given the roots of two binary trees `p` and `q`, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

## Examples

**Example 1:**
```
Input: p = [1,2,3], q = [1,2,3]
Output: true
```

**Example 2:**
```
Input: p = [1,2], q = [1,null,2]
Output: false
```

**Example 3:**
```
Input: p = [1,2,1], q = [1,1,2]
Output: false
```

## Constraints

- The number of nodes in both trees is in the range `[0, 100]`.
- `-10^4 <= Node.val <= 10^4`

## Approach Ideas

- **Recursive (DFS):** Base cases — if both nodes are `null`, they're the same (return `true`); if exactly one is `null`, they differ (return `false`); if their values differ, return `false`. Otherwise, recursively check that the left subtrees are the same AND the right subtrees are the same.
- **Iterative (BFS/Stack):** Use a queue or stack to traverse both trees in lockstep, pushing pairs of nodes `(p_node, q_node)`. At each step, apply the same null/value checks as above before continuing to compare children.

## Complexity

| Approach          | Time  | Space |
|-------------------|-------|-------|
| Recursive (DFS)   | O(n)  | O(h)  |
| Iterative (BFS)   | O(n)  | O(n)  |

Where `n` is the total number of nodes across both trees, and `h` is the height of the tree (recursion stack depth).
