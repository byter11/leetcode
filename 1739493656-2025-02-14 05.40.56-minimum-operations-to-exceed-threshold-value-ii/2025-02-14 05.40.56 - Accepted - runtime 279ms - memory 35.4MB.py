class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
      ops = 0
      heapq.heapify(nums)
      while len(nums) >=2 and nums[0] < k:
        a = heapq.heappop(nums)
        b = heapq.heappop(nums)
        heapq.heappush(nums, min(a,b)*2 + max(a,b))
        ops += 1
       
      return ops
        