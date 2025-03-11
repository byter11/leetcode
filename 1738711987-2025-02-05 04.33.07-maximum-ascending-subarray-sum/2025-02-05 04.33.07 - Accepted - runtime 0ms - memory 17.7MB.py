class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        mx = nums[0]
        cur = mx

        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                cur = 0

            cur += nums[i]
            mx = max(mx, cur)
        
        return mx