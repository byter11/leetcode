class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n, k = len(nums), max(nums)
        l, r, ans = 0, 0, 1

        while l < n:
            if nums[l] == k:
                r = l
                while r < n and nums[r] == k: 
                    r += 1
                ans = max(ans, r - l)
                l = r
            else:
                l += 1

        return ans


    