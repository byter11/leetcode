class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        g = defaultdict(list)
        for u, v in prerequisites:
            g[u].append(v)

        dp = defaultdict(dict)

        def dfs(u, v):
            if u == v:
                return True

            if u in dp and v in dp[u]: return dp[u][v]

            dp[u][v] = any((dfs(a, v) for a in g[u]))
            return dp[u][v]

        ans = []
        for u, v in queries:
            ans.append(dfs(u,v))

        return ans
