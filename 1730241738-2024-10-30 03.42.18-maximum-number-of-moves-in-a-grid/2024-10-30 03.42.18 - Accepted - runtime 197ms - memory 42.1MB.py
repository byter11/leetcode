class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        dp = {}
        def dfs(r, c, last=-1):
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return 0
            
            if grid[r][c] <= last:
                return 0

            if dp.get((r,c), None):
                return dp[(r,c)]
            # print(r, c, grid[r][c])

            mx = 0
            for i in range(-1,2):
                mx = max(mx, 1 + dfs(r + i, c + 1, grid[r][c]))

            dp[(r, c)] = mx
            return mx

        ans = 1
        for i in range(rows):
            ans = max(ans, dfs(i, 0))

        return ans - 1

#
# [270,192,213,26,270],
# [288,99,1,136,98],
# [143,168,117,127,38],
# [193,218,16,61,216],
# [59,224,106,9,144],
# [253,166,202,132,281],
# [233,197,253,98,36],
# [105,289,255,277,98],
# [247,125,15,275,35],
# [208,76,147,22,124],
# [198,245,6,167,105],
# [28,100,15,84,300],
# [197,263,2,251,155],
# [87,41,216,91,112],
# [263,32,225,102,298]]        