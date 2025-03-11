class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-g for g in gifts]
        heapq.heapify(gifts)

        for i in range(k):
            g = -heapq.heappop(gifts)
            g = int(sqrt(g))
            heapq.heappush(gifts, -g)
    
        return -sum(gifts)