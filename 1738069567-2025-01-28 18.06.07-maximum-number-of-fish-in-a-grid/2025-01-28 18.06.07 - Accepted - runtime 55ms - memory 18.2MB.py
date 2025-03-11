class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        vis = [[False]*m for _ in range(n)]
        def dfs(i, j):
            if i< 0 or j < 0 or i >= n or j >= m: return 0
            if grid[i][j] == 0: return 0
            if vis[i][j]:
                return 0

            vis[i][j] = True

            return grid[i][j] + sum(
                    (dfs(k,l) for k,l in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)])
                    )
        
        ans = 0
        for i in range(n):
            for j in range(m):
                ans = max(ans, dfs(i,j))
                
        return ans
