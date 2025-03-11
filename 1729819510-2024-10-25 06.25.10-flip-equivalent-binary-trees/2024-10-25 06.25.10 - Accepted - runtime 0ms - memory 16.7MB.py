# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def nodeEquiv(self, node1, node2) -> bool:
        return (not node1 and not node2) or (node1 and node2 and node1.val == node2.val)

    def childsEquiv(self, root1, root2) -> bool:
        return (
            (
                self.nodeEquiv(root1.left, root2.left) and 
                self.nodeEquiv(root1.right, root2.right)
            ) or (
                self.nodeEquiv(root1.left, root2.right) and 
                self.nodeEquiv(root1.right, root2.left)
            )
        )
        

    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if root1 and root2 and root1.val != root2.val: return False
        if not root1 and root2: return False
        if not root2 and root1: return False
        if not root1 and not root2: return True
        if not self.childsEquiv(root1, root2):
            return False
        
        return (
                self.flipEquiv(root1.left, root2.left) and
                self.flipEquiv(root1.right, root2.right)
            ) or (
                self.flipEquiv(root1.left, root2.right) and
                self.flipEquiv(root1.right, root2.left)
            )