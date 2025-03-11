class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        g = defaultdict(list)
        for i in range(n-1):
            g[i] = [i+1]
        
        def bfs():
            q = deque()
            q.append((0, 0))
            vis = set()
            mn = float('inf')

            while len(q):
                u, steps = q.popleft()
                if u == n-1:
                    mn = min(mn, steps)

                if u in vis:
                    continue

                vis.add(u)
                for v in g[u]:
                    q.append((v, steps + 1))

            return mn
        
        res = []
        for u, v in queries:
            g[u].append(v)
            res.append(bfs())
            
        return res