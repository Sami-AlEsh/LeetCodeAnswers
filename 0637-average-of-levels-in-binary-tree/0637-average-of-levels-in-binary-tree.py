# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        result = []
        q = deque([root])
        while q:
            count = len(q)
            _sum = 0
            for _ in range(count):
                node = q.popleft()
                _sum += node.val
                
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            result.append(_sum/count)
        return result