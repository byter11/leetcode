class Solution:
    def __init__(self):
        self.ans = []
        self.g = defaultdict(list)

    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        for i, (a, b) in enumerate(edges):
            self.g[a].append((b, succProb[i]))
            self.g[b].append((a, succProb[i]))

        self.ans = [0.0] * n
        self.ans[start_node] = 1.0
        q = deque([start_node])
        while q:
            a = q.popleft()
            for b, prob in self.g[a]:
                if self.ans[a] * prob > self.ans[b]:
                    self.ans[b] = self.ans[a] * prob
                    q.append(b)
        
        return self.ans[end_node]