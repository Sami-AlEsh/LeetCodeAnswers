# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math

class Solution:
    def __init__(self):
        self.max_path = -math.inf
    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.traverse(root)
        return self.max_path
    
    def traverse(self, node):
        if not node:
            return 0
        
        left = self.traverse(node.left)
        right = self.traverse(node.right)

        self.max_path = max(self.max_path, node.val + left + right)

        return max(0, node.val + max(left, right))
        