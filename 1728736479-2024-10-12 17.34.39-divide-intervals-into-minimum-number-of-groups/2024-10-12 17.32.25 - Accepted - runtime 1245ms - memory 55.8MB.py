class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        events = []
        for l, r in intervals:
            events.append((l, 1))
            events.append((r + 1, -1))

        events.sort()

        cur = 0
        mx = 1
        for e, t in events:
            cur += t
            mx = max(mx, cur)
        
        return mx

        
    
# [1, 5], [1, 10], [2, 3], [5, 10], [6, 8]
# [[5,10],[6,8],[1,5],[2,3],[1,10]]
