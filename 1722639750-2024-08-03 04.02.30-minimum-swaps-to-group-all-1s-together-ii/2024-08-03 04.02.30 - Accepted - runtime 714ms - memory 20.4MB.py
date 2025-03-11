class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        ones = 0
        for n in nums:
            if n == 1:
                ones += 1
        
        c = 0
        for i in range(ones):
            c += nums[i]

        mx = c
        i = 0
        j = ones - 1        
        while i < len(nums):
            c -= nums[i]
            i += 1


            j = (j+1)%len(nums)
            c += nums[j]
        
            mx = max(mx, c)
        
        return ones - mx