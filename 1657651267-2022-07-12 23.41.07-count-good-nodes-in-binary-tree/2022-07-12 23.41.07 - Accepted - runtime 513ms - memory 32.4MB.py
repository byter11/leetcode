# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode, mx = -1e5) -> int:
        if not root:
            return 0
        
        return (
            int(mx <= root.val) + 
            self.goodNodes(root.left, max(mx, root.val)) + 
            self.goodNodes(root.right, max(mx, root.val))
        )
        