class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        n = len(grid)
        m = len(grid[0])
        
        def rec(grid, i, j, cur=0):
            if i >= n or j >= m or j < 0 or i < 0 or grid[i][j] == 0:
                return 0
            
            grid[i][j] = 0
            
            return 1 + rec(grid, i+1, j) + rec(grid, i, j+1) + rec(grid, i, j-1) + rec(grid, i-1, j)
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    ans = max(ans, rec(grid, i, j))
                    
        return ans
            
            