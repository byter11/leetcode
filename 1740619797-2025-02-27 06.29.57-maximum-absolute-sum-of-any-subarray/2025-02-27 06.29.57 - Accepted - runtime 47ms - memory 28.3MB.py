class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        min_sum = 0
        max_sum = 0
        cum_sum = 0

        for n in nums:
            cum_sum += n
            min_sum = min(min_sum, cum_sum)
            max_sum = max(max_sum, cum_sum)
        
        return max_sum - min_sum