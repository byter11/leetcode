# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        sums = []
        def inorder(r, lvl):
          if not r: return
          
          inorder(r.left, lvl + 1)
          
          while len(sums) < lvl + 1:
            sums.append(0)
          sums[lvl] += r.val
          
          inorder(r.right, lvl + 1)
         
        inorder(root, 0)
        sums.sort(reverse=True)
        #print(sums)
        return sums[k-1] if len(sums) >= k else -1