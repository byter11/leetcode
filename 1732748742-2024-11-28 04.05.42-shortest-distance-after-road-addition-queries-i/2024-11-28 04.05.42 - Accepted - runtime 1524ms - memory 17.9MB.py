class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        g = defaultdict(list)
        for i in range(n-1):
            g[i] = [i+1]
        
        def bfs():
            q = [(0, 0)]
            dist = [float('inf')] * n
            dist[0] = 0

            while q:
                _, u = heapq.heappop(q)
                for v in g[u]:
                    if dist[v] > dist[u] + 1:
                        dist[v] = dist[u] + 1
                        heapq.heappush(q, (dist[v], v))

            return dist[n-1]
        
        res = []
        for u, v in queries:
            g[u].append(v)
            res.append(bfs())

        return res