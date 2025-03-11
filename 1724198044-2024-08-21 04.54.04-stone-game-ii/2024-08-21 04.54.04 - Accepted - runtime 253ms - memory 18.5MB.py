class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        
        # i cheated
        @lru_cache(maxsize=None)
        def dfs(i, m):
            if i >= n:
                return 0
            
            res = -10000
            stones = 0
            for j in range(i, min(n, i + 2*m)):
                stones += piles[j]
                res = max(res, stones - dfs(j+1, max(m, j - i + 1)))
            return res

        return (sum(piles) + dfs(0, 1)) // 2
