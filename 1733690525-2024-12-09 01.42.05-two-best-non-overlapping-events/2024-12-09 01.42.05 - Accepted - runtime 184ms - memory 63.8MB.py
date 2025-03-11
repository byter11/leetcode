class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        points = []
        for s, e, v in events:
            points.append((s, 0, v))
            points.append((e, 1, v))
        
        points.sort()
        
        ans, mx = 0, 0
        for p, t, v in points:
            if t == 0:
                ans = max(ans, mx + v)
            if t == 1:
                mx = max(mx, v)

        return ans