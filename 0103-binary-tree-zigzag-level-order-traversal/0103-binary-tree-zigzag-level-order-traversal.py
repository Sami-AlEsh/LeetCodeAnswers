# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []

        rtl = False
        q = deque([root])
        result = []
        
        while q:
            cur = []
            n = len(q)
            for _ in range(n):
                node = q.popleft()
                if rtl: cur.insert(0, node.val)
                else: cur.append(node.val)
                    
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            result.append(cur)
            rtl = not rtl
        return result
                
