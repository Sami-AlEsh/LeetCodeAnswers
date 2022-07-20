# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        def traverse(node, needed, target):
            if node is None: return False
            
            if node.val in needed: return True
            
            needed.add(target - node.val)
            
            return traverse(node.left, needed, target) or traverse(node.right, needed, target)
        
        return traverse(root, set(), k)