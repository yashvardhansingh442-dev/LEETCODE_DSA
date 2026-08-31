# Balanced Binary Tree

**Difficulty:** Easy

## Problem

Given a binary tree, determine if it is height-balanced.

A height-balanced binary tree is defined as a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

## Examples

**Example 1:**
```
Input: root = [3,9,20,null,null,15,7]
Output: true
```

**Example 2:**
```
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
```

**Example 3:**
```
Input: root = []
Output: true
```

## Constraints

- The number of nodes in the tree is in the range `[0, 5000]`.
- `-10^4 <= Node.val <= 10^4`

## Approach Ideas

- **Brute Force (Top-Down):** For each node, compute the height of its left and right subtrees independently, check if they differ by more than 1, and recurse on both children to check their balance as well. Recomputing heights repeatedly leads to O(n^2) time in the worst case.
- **Bottom-Up (Optimal):** Use a post-order DFS that returns the height of a subtree, or a sentinel value (e.g., `-1`) if the subtree is already known to be unbalanced. This way, height and balance are computed in a single pass — as soon as an imbalance is detected, it propagates up immediately without extra recomputation. O(n) time.

## Complexity

| Approach              | Time     | Space |
|------------------------|----------|-------|
| Brute Force (Top-Down) | O(n^2)   | O(h)  |
| Bottom-Up (Optimal)    | O(n)     | O(h)  |

Where `n` is the number of nodes and `h` is the height of the tree (recursion stack depth).
