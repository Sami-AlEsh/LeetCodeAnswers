# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.diameter = 0
        
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.traverse_hight(root)
        return self.diameter - 1 if self.diameter > 0 else 0
    
    def traverse_hight(self, node):
        if node is None:
            return 0

        left = self.traverse_hight(node.left)
        right = self.traverse_hight(node.right)

        # Check if it is not a leaf
        if left != 0 or right != 0:
            self.diameter = max(left + right + 1, self.diameter)
            
        return 1 + max(left, right)
