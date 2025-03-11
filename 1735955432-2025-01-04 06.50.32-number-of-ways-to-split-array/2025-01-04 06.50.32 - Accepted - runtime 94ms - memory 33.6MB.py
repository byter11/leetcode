class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)

        suffix_sum = [nums[n-1]]*n
        for i in range(n-2, -1, -1): suffix_sum[i] = nums[i] + suffix_sum[i+1]

        res = 0
        running_sum = 0
        for i in range(n):
            running_sum += nums[i]
            if i < n - 1 and running_sum >= suffix_sum[i+1]:
                res += 1
            
        return res