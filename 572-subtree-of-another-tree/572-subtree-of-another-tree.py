# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def bfs_match(node):
            q = [(node, subRoot)]
            while q:
                n1, n2 = q.pop(0)
                if n1 and n2:
                    if n1.val != n2.val: return False
                    q.append((n1.left, n2.left))
                    q.append((n1.right, n2.right))
                
                elif n1 or n2: return False
            return True

        
        if root is None or subRoot is None:
            return False

        q = [root]
        while q:
            node = q.pop(0)
            if node.val == subRoot.val and bfs_match(node): return True
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        return False