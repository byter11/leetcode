class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        queries = sorted([(q, i) for i, q in enumerate(queries)])
        ni, nq = len(intervals), len(queries)

        ans = [-1]*nq

        j = 0
        pq = []
        for q, i in queries:
            while j < ni and intervals[j][0] <= q:
                heapq.heappush(pq, (intervals[j][1] - intervals[j][0] + 1, intervals[j]))
                j += 1
                
            while pq and pq[0][1][1] < q:
                heapq.heappop(pq)

            ans[i] = pq[0][0] if pq else -1 

        return ans