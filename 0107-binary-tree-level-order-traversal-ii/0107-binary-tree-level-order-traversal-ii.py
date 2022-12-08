# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        
        def traverse(level, node, d):
            if not node: return
            d[level].append(node.val)
            traverse(level + 1, node.left, d)
            traverse(level + 1, node.right, d)
        
        d = defaultdict(lambda: list())
        traverse(0, root, d)
        
        ans = [0] * len(d.keys())

        for k, v in d.items():
            print(k)
            ans[k] = v
        return reversed(ans)