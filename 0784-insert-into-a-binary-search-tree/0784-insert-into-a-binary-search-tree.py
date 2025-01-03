# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        node = root

        if val > node.val:
            if node.right:
                self.insertIntoBST(node.right, val)
            else:
                node.right = TreeNode(val)
        else:
            if node.left:
                self.insertIntoBST(node.left, val)
            else:
                node.left = TreeNode(val)

        return root          
