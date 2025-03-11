class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid) * 3
        matrix = [[0]*n for _ in range(n)]

        for i, row in enumerate(grid):
            for j, s in enumerate(row):
                a, b = i*3, j*3
                if s == '/':
                    matrix[a][b + 2] = 1
                    matrix[a + 1][b + 1] = 1
                    matrix[a + 2][b] = 1
                elif s == '\\':
                    matrix[a][b] = 1
                    matrix[a + 1][b + 1] = 1
                    matrix[a + 2][b + 2] = 1
        
        # for m in matrix: print(m)
        ans = 0
        for i in range(n):
            for j in range(n):
                if matrix[i][j] == 0:
                    self.markRegion(matrix, i, j)
                    ans += 1
                    # for m in matrix: print(m)
            # print("")
        
        return ans
    
    def markRegion(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]) or grid[i][j] == 1:
            return
        
        # print(i , j)
        grid[i][j] = 1
        for a in [1, -1]:
            self.markRegion(grid, i, j+a)
            self.markRegion(grid, i+a, j)
