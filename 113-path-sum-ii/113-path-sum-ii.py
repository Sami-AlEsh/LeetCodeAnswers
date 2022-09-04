# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, node, prevs, all_paths, target):
        if not node: return
        
        prevs.append(node.val)
        
        if not node.left and not node.right:
            if sum(prevs) == target: all_paths.append(prevs)
        else:
            self.traverse(node.left, list(prevs), all_paths, target)
            self.traverse(node.right, list(prevs), all_paths, target)
        
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        all_paths = []
        self.traverse(root, [], all_paths, targetSum)
        return all_paths