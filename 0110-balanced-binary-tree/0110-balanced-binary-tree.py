# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        def maxDepth(root):
            if not root:
                return 0

            return 1 + max(maxDepth(root.left), maxDepth(root.right))
        l = maxDepth(root.left)
        r = maxDepth(root.right)

        return (abs(l - r) < 2) and self.isBalanced(root.left) and self.isBalanced(root.right)