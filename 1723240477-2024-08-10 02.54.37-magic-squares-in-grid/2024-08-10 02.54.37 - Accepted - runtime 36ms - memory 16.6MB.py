class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        ans = 0
        for j in range(1, len(grid) - 1):
            for k in range(1, len(grid[j]) - 1):
                a, b, c = grid[j-1][k-1], grid[j-1][k], grid[j-1][k+1]
                d, e, f = grid[j][k-1], grid[j][k], grid[j][k+1]
                g, h, i = grid[j+1][k-1], grid[j+1][k], grid[j+1][k+1]

                if not self.valid([a,b,c,d,e,f,g,h,i]):
                    continue
                
                if a + b + c == d + e + f == g + h + i == a + d + g == b + e + h == c + f + i == a + e + i == c + e + g:
                    ans += 1

        return ans

    def valid(self, items):
        if len(set(items)) != 9:
            return False

        for it in items:
            if it > 9 or it < 1:
                return False

        return True