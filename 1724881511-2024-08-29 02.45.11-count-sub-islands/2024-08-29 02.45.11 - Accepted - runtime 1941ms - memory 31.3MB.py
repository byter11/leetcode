class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        n, m = len(grid2), len(grid2[0])

        def eraseIsland(i, j, is_sub):
            if (not 0 <= i < n) or (not 0 <= j < m) or grid2[i][j] == 0:
                return is_sub

            grid2[i][j] = 0
            is_sub = grid1[i][j] == 1
            return eraseIsland(i+1, j, is_sub) & eraseIsland(i-1, j, is_sub) & eraseIsland(i, j+1, is_sub) & eraseIsland(i, j-1, is_sub)
        
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid2[i][j] == 1:
                    ans += eraseIsland(i, j, grid1[i][j] == 1)

        return ans
