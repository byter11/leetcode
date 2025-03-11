class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        n = len(nums)
        cur = 0
        for x in nums:
            cur ^= x
    
        # print(cur)
        ans = []
        for i in range(n):
            k = 0
            for j in range(maximumBit):
                curbit = (cur >> j) & 1
                k += (not curbit) << j
            ans.append(k)
            cur ^= nums[n-i-1]
            # print(cur, i, k)
        
        return ans