class Solution:
    def minSteps(self, n: int) -> int:
        dp = {}

        def dfs(i=1, last=1):
            if i == n:
                return 0
            if i > n:
                return float('inf')

            # if dp.get(i, None):
            #     if dp[i] != float('inf'):
            #         return dp[i]
            
            dp[i] = min(
                2 + dfs(i + i, i),
                1 + dfs(i + last, last)
            )
            return dp[i]

        ans = dfs()
        return ans + 1 if ans else 0

# 1 2 4 8 16 32 64 86 118 150
# 1 3 5 7 9  11 12 13 14  15