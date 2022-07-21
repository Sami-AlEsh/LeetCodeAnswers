# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def get_depth(root) -> int:
            if not root:
                return 0
            left = get_depth(root.left)
            right = get_depth(root.right)
            if left == -1 or right == -1:
                return -1
            if abs(left-right) > 1:
                return -1
            return max(left, right) + 1

        mode = get_depth(root)
        return ~mode