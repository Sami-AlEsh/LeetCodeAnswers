"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        def traverse(node, ls):
            if not node: return
            ls.append(node.val)
            [traverse(n, ls) for n in node.children]
        
        ls = list()
        traverse(root, ls)
        return ls
        