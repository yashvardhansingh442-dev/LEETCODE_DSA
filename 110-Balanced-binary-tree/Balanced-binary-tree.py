# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def check(node):
            if not node:
                return 0  # height of empty tree
            
            left_height = check(node.left)
            if left_height == -1:
                return -1  # left subtree already unbalanced
            
            right_height = check(node.right)
            if right_height == -1:
                return -1  # right subtree already unbalanced
            
            if abs(left_height - right_height) > 1:
                return -1  # current node unbalanced
            
            return max(left_height, right_height) + 1
        
        return check(root) != -1
