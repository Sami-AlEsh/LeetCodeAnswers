# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def traverse(node, ls):
            if node:
                traverse(node.left, ls)
                traverse(node.right, ls)
                ls.append(node.val)
        
        ls = []
        traverse(root, ls)
        return ls