# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        sums = []
        def level_sum(r, lvl):
          if not r: return

          level_sum(r.left, lvl + 1)
          while len(sums) < lvl + 1:
            sums.append(0)
          sums[lvl] += r.val
          level_sum(r.right, lvl + 1)

        def replace_values(r, lvl, sibling=0):
          if not r: return
          left = r.left.val if r.left else 0
          right = r.right.val if r.right else 0
          
          replace_values(r.left, lvl + 1, right)
          replace_values(r.right, lvl + 1, left)

          r.val = sums[lvl] - r.val
          if sibling: 
            r.val -= sibling


        level_sum(root, 0)
        replace_values(root, 0)
        return root