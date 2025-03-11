# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal_str: str) -> Optional[TreeNode]:
        traversal = []
        cur = [0, ""]
        part = 1
        for c in traversal_str:
            if c != "-":
                part = 2
                cur[1] += c
            else:
                if part == 2:
                    cur[1] = int(cur[1])
                    traversal.append(cur)
                    cur = [0, ""]
                part = 1
                cur[0] += 1

        cur[1] = int(cur[1])
        traversal.append(cur)       
        
        root = TreeNode()
        height_stack = defaultdict(deque)
        height_stack[-1].append(root)
        for d, n in traversal:
            node = TreeNode(n)
            for i in range(d, 1000):
                height_stack[i].clear()

            height_stack[d].append(node)

            # print(d, n, height_stack)
            parent = height_stack[d-1].popleft()
            if not parent.left:
                parent.left = node
                height_stack[d-1].appendleft(parent)
            elif not parent.right:
                parent.right = node
        
        return root.left