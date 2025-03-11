class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        p = set()
        
        def dfs(cur, left):
          if cur: p.add(cur)
          for i in range(len(left)):
            dfs(cur + left[i], left[:i] + left[i+1:])
                
        dfs("", tiles)
     #   print(p)
        return len(p)