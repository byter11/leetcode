class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        cur_len = 0
        heap = []
        res = [-1]*(n-k+1)

        for i in range(n):
            if len(heap) and heap[0][1] < i - k:
                heapq.heappop(heap)
            
            if cur_len == k:
                mx, j = heap[0]
                res[i - cur_len] = -mx
                cur_len -= 1

            if i > 0 and nums[i] != nums[i-1] + 1:
                heap = []
                cur_len = 0
            
            heapq.heappush(heap, (-nums[i], i) )
            cur_len += 1

        if cur_len == k:
            mx, j = heap[0]
            res[-1] = -mx

        return res

            