# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        node = root
        if p.val > q.val:
            p, q = q, p
        
        while True:
            if p.val <= node.val <= q.val:
                return node
            if node.val < p.val:
                node = node.right
            else:
                node = node.left