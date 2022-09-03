# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def is_leaf(node):
            return (not node.left and not node.right)
        
        if not root: 
            return 0
        
        q = [(root, 1)]
        
        while len(q) > 0:
            node, depth = q.pop(0)
            if is_leaf(node): return depth
            if node.left: q.append((node.left, depth + 1))
            if node.right: q.append((node.right, depth + 1))
        
        return 1