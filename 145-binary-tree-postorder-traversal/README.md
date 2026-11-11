# [145. Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/)

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen)
![Status](https://img.shields.io/badge/Status-Solved-blue)

**Topics:** Stack · Tree · Depth-First Search · Binary Tree

## Problem

Given the `root` of a binary tree, return the **postorder traversal** of its nodes' values.

### Examples

**Example 1**
```
Input:  root = [1,null,2,3]
Output: [3,2,1]
```

**Example 2**
```
Input:  root = [1,2,3,4,5,null,8,null,null,6,7,9]
Output: [4,6,7,5,2,9,8,3,1]
```

**Example 3**
```
Input:  root = []
Output: []
```

**Example 4**
```
Input:  root = [1]
Output: [1]
```

### Constraints

- The number of nodes in the tree is in the range `[0, 100]`.
- `-100 <= Node.val <= 100`

**Follow up:** Recursive solution is trivial, could you do it iteratively?

## Approach

Postorder visits nodes in the order **Left → Right → Root**.

### 1. Recursive DFS

Visit the left subtree, then the right subtree, then record the current node's value.

### 2. Iterative (Stack + Reverse)

Do a modified preorder traversal (**Root → Right → Left**) using a stack, then reverse the result. Reversing gives **Left → Right → Root**, which is exactly postorder.

1. Push `root` onto the stack.
2. Pop a node and append its value to `res`.
3. Push its left child, then its right child (so right is popped first).
4. Repeat until the stack is empty.
5. Return `res` reversed.

## Solution

### Recursive

```python
class Solution:
    def postorderTraversal(self, root):
        res = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            dfs(node.right)
            res.append(node.val)

        dfs(root)
        return res
```

### Iterative

```python
class Solution:
    def postorderTraversal(self, root):
        if not root:
            return []
        res, stack = [], [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return res[::-1]
```

## Complexity

| Approach  | Time | Space |
|-----------|------|-------|
| Recursive | O(n) | O(h) recursion stack (O(n) worst case for a skewed tree) |
| Iterative | O(n) | O(n) result list + stack |

where `n` is the number of nodes and `h` is the height of the tree.
