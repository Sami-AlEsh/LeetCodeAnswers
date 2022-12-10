"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return root
        
        q = deque([root])
        while q:
            for _ in range(len(q)):
                if _ == 0:
                    node = q.popleft()
                    prev = node
                else:
                    node = q.popleft()
                    prev.next = node
                    prev = node

                if node.left: q.append(node.left)
                if node.right: q.append(node.right)

        return root