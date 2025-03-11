class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        nums = [(x, i) for i, x in enumerate(nums)]
        heapq.heapify(nums)

        while k:
            x, i = heapq.heappop(nums)
            x *= multiplier
            heapq.heappush(nums, (x, i))
            k -= 1
        
        ans = [0]*len(nums)
        for x, i in nums:
            ans[i] = x

        return ans