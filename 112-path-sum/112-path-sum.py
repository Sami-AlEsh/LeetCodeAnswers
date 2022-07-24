# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def traverse(node, s, target):
            if node is None: return False
            
            if node.val + s == target and node.left is None and node.right is None: return True
            
            return traverse(node.left, s + node.val, target) or  traverse(node.right, s + node.val, target)
        
        return traverse(root, 0, targetSum)