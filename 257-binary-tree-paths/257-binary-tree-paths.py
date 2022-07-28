# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        def is_leaf(node):
            return node.left is None and node.right is None 
        
        def traverse(node, prevs, paths):    
            if node is None: return
            
            prevs.append(str(node.val))
            
            if is_leaf(node):
                paths.append(prevs)
            else:
                traverse(node.left, list(prevs), paths)
                traverse(node.right, list(prevs), paths)
        
        paths = []
        traverse(root, [], paths)
        return ["->".join(p) for p in paths]
        

            
            
            
            
            
            
            