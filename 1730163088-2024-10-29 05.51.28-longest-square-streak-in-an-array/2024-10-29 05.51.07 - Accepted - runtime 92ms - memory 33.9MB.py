class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        s = set(nums)

        mx = -1
        for n in nums:
            cur = 1
            if sqrt(n) in s:
                continue
            
            while n*n in s:
                cur += 1
                mx = max(mx, cur)
                n = n*n
        
        return mx


# 2 3 4 16 256 999
# ans: 2 4 16

# 2 -> 4 -> 16 -> 256     cur=4, max=4