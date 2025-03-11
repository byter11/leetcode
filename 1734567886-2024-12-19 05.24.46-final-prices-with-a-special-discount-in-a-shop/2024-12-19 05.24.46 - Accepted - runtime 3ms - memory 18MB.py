class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        pq = []
        ans = [p for p in prices]

        for i, p in enumerate(prices):
            while pq and (-pq[0][0]) >= p:
                ans[pq[0][1]] -= p
                heapq.heappop(pq)

            heapq.heappush(pq, (-p, i))

        return ans