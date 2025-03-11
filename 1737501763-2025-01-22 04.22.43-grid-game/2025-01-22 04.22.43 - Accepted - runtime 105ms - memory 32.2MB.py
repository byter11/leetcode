class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        prefix = [grid[1][0]]*n
        suffix = [grid[0][n-1]]*n
        split = [0]*n
    
        for i in range(1, n):
            prefix[i] = prefix[i-1] + grid[1][i]

        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i+1] + grid[0][i]
        
        for i in range(n):
            split[i] = max(prefix[i] - grid[1][i], suffix[i] - grid[0][i])
        
        return min(split)

# 1  3  9  1
# 1  8  1  15
# 26 28 28 29

# 2  5  4
# 1  5  1
# 9  13 12