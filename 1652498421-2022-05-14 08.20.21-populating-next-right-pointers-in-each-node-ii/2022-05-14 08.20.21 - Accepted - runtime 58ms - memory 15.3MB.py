"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        node = root
        q = [(node, 0)]
        last = q[0]
        
        while q:
            n, level = q.pop(0)
            if n:
                if last[1] == level and last[0] != n:
                    last[0].next = n
                q.append((n.left, level+1))
                q.append((n.right, level+1))
                last = (n, level)
        return root