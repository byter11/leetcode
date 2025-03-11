class Solution:
    def minSteps(self, n: int) -> int:
        dp = {}

        def dfs(i=1, last=1):
            if i == n:
                return 0
            if i > n:
                return float('inf')

            dp[i] = dp.get(i, {})
            if dp[i].get(last, None):
                return dp[i][last]

            dp[i][last] = min(
                2 + dfs(i + i, i),
                1 + dfs(i + last, last)
            )
            return dp[i][last]

        ans = dfs()
        return ans + 1 if ans else 0

# 1 2 4 8 16 32 64 86 118 150
# 1 3 5 7 9  11 12 13 14  15