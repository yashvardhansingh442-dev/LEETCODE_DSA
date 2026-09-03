# Maximum Depth of Binary Tree

**Difficulty:** Easy

## Problem

Given the `root` of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

## Examples

**Example 1:**
```
Input: root = [3,9,20,null,null,15,7]
Output: 3
```

**Example 2:**
```
Input: root = [1,null,2]
Output: 2
```

## Constraints

- The number of nodes in the tree is in the range `[0, 10^4]`.
- `-100 <= Node.val <= 100`

## Approach

**Recursive (DFS):** The maximum depth of a tree rooted at `node` is `1 + max(depth(node.left), depth(node.right))`. Base case: an empty tree (`null` node) has depth `0`.

**Iterative (BFS):** Traverse the tree level by level using a queue. Each time you finish processing a full level, increment the depth counter. The final counter value is the max depth.



## Complexity

| Approach          | Time  | Space |
|-------------------|-------|-------|
| Recursive (DFS)   | O(n)  | O(h)  |
| Iterative (BFS)   | O(n)  | O(w)  |

Where `n` is the number of nodes, `h` is the height of the tree (recursion stack), and `w` is the maximum width of the tree (queue size).
