class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        rows = [0]*n
        cols = [0]*m

        for i, r in enumerate(grid):
            for j, c in enumerate(r):
                if c == 1:
                    rows[i] += 1
                    cols[j] += 1

        ans = 0
        for i, r in enumerate(grid):
            for j, c in enumerate(r):
                if c == 1 and (rows[i] > 1 or cols[j] > 1):
                    ans += 1

        return ans