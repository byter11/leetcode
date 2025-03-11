# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    leaves = 0
    count = 0
    
    @property
    def cameras(self):
        return self.count
    
    def minCameraCover(self, root: Optional[TreeNode], p=None) -> int:
        if not root:
            return self.cameras
        self.minCameraCover(root.left, root)
        self.minCameraCover(root.right, root)
        
        wt = 0
        if root.left: wt += root.left.val
        else: wt += 1
        if root.right: wt += root.right.val
        else: wt += 1
        
        
        if wt < 2:
            root.val = 1
            if p:
                p.val = 1
            self.count += 1
            return self.cameras
        
        return self.cameras + int(not root.val)
            