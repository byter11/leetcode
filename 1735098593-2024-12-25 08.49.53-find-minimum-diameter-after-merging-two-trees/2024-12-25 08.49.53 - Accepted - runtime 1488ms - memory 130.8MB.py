class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        d1 = self.diameter(self.graph(edges1))
        d2 = self.diameter(self.graph(edges2))

        # print(d1, d2)
        return max(d1, d2, ceil(d1/2) + ceil(d2/2) + 1)

    def graph(self, edges):
        g = defaultdict(list)
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        return g

    def diameter(self, g):
        if len(g) == 0:
            return 0

        dp = defaultdict(dict)

        def dfs(a, last=None):
            mx = 0
            for b in g[a]:
                if b == last: continue

                if b in dp[a]:
                    # print('hit', a, b, dp[a][b])
                    mx = max(mx, 1 + dp[a][b])
                else:
                    # print('miss', a, b, dfs(b, a))
                    mx = max(mx, 1 + dfs(b, a))

            dp[last][a] = mx
            return mx
                
        return max(dfs(node) for node in g)