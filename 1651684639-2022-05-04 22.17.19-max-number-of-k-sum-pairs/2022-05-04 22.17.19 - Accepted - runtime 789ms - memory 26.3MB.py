class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        res = 0
        lo = 0; hi = n-1
        
        while hi >= 0 and nums[hi] >= k:
            hi -= 1
            
        while lo < hi:
            s = nums[lo] + nums[hi]
            if s == k:
                lo += 1
                hi -= 1
                res += 1
            elif s < k:
                lo += 1
            else:
                hi -= 1
        return res