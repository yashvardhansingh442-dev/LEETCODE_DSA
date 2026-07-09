# 108. Convert Sorted Array to Binary Search Tree

**Difficulty:** Easy
**Topics:** Array, Divide and Conquer, Tree, Binary Search Tree, Binary Tree

## Problem

Given an integer array `nums` where the elements are sorted in **ascending order**, convert it to a **height-balanced** binary search tree.

## Examples

**Example 1:**
```
Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:
```

**Example 2:**
```
Input: nums = [1,3]
Output: [3,1]
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.
```

## Constraints

- `1 <= nums.length <= 10^4`
- `-10^4 <= nums[i] <= 10^4`
- `nums` is sorted in a **strictly increasing** order.

## Definition for a binary tree node

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

## Starter Code

```python
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
```

---
*What does "height-balanced" mean here, and which element of a sorted array would you naturally pick as a root to guarantee that? Think recursively — once you pick a root, what are your left and right subarrays?*
