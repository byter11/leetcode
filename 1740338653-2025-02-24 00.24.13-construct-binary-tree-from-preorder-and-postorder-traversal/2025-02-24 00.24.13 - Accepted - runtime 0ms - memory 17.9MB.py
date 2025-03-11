# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        g = {}
        for n in preorder:
            g[n] = TreeNode(n)
        
        def recur(parent, pre, post):
            # print(parent, pre, post)
            if len(pre) == 0 or len(post) < 2:
                return

            left = pre[1]
            right = post[-2]

            if left == right:
                parent.left = g[left]
                return recur(g[left], pre[1:], post[:-1])

            parent.left = g[left]
            parent.right = g[right]


            pre_left = pre[pre.index(left) : pre.index(right)] # [2, 4, 5]
            post_right = post[post.index(left) + 1 : post.index(right) + 1] # [6, 7, 3]

            post_left = post[(post.index(left) + 1) - len(pre_left) : post.index(left) + 1]
            pre_right = pre[pre.index(right) : pre.index(right) + len(post_right)] # [3, 6, 7]

            recur(g[left], pre_left, post_left)
            recur(g[right], pre_right, post_right)

        recur(g[preorder[0]], preorder, postorder)
        return g[preorder[0]]

# 2^5 = 32