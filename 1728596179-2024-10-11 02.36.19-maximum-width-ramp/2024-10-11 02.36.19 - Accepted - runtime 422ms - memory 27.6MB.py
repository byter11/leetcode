class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n, mx = len(nums), 0
        nums = sorted([(k, i) for i, k in enumerate(nums)])

        mn = n
        for x, i in nums:
            mx = max(mx, i - mn)
            mn = min(mn, i) 

        return mx



# [0, 1, 2, 5, 6, 8]