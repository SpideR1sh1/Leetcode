# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def dfs(node):
            if not node:
                return False
            
            elif isSim(node, subRoot):
                return True
            
            return dfs(node.left) or dfs(node.right)
        
    
        def isSim(p, q):

            if not p or not q:
                return p is None and q is None

            
            return (p.val == q.val) and isSim(p.right, q.right) and isSim(p.left, q.left)
    
        return dfs(root)