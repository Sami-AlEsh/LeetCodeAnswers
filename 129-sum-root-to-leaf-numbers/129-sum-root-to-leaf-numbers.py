# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leaf_sum(self, node, prev_s):
        if not node: return 0
        
        s = prev_s * 10 + node.val

        if not node.left and not node.right: return s

        return self.leaf_sum(node.left, s) + self.leaf_sum(node.right, s)

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.leaf_sum(root, 0)