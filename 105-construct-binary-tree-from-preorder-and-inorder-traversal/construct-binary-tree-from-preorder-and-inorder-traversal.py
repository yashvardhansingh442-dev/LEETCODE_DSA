# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        index_map = {val: i for i, val in enumerate(inorder)}
        self.pre_idx = 0

        def build(left: int, right: int) -> TreeNode | None:
            if left > right:
                return None

            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            node = TreeNode(root_val)

            mid = index_map[root_val]
            node.left = build(left, mid - 1)
            node.right = build(mid + 1, right)

            return node

        return build(0, len(inorder) - 1)