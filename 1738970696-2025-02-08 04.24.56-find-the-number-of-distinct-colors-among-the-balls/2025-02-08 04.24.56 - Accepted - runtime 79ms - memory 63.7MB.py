class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        balls = {}
        colors = defaultdict(int)
        ans = [0]*len(queries)

        for i, (x, y) in enumerate(queries):
            if i > 0:
                ans[i] = ans[i-1]
                
            if x in balls:
                colors[balls[x]] -= 1
                if colors[balls[x]] == 0:
                    ans[i] -= 1
            
            balls[x] = y
            colors[y] += 1
            if colors[y] == 1:
                ans[i] += 1
        
        return ans
