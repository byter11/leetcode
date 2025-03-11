# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def dfs(cursor, level=0):
            if not cursor: return

            if len(ans) <= level:
                ans.append(-float('inf'))
            
            ans[level] = max(ans[level], cursor.val)

            dfs(cursor.left, level + 1)
            dfs(cursor.right, level + 1)
        
        dfs(root)
        return ans