# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
            
        def traverse(node, pre_sum):
            if not node: return 0
            _sum = pre_sum * 10 + node.val
            if not node.left and not node.right: return _sum
            return traverse(node.left, _sum) + traverse(node.right, _sum)
            
        return traverse(root, 0)