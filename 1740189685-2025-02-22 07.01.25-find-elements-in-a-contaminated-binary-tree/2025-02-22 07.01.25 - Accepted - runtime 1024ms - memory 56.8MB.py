# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.tree = []
        q = deque([root])
        total = self.count(root)
        done = 0
        
        while q:
          n = q.popleft() or TreeNode(None)
          if n.val is not None:
            done += 1
          
          self.tree.append(n.val)
          if done < total:
            q.append(n.left)
            q.append(n.right)
    
    def count(self, root):
      if not root:
        return 0
      
      return 1 + self.count(root.left) + self.count(root.right)
    
    def find(self, target: int) -> bool:
      return len(self.tree) > target and self.tree[target] is not None
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)