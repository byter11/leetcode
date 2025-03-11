class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        n = len(nums)
        cur = 0
        for x in nums:
            cur ^= x
    
        # print(cur)
        ans = []
        for i in range(n):
            k = cur ^ ((1 << maximumBit) - 1)
            ans.append(k)
            cur ^= nums[n-i-1]
            # print(cur, i, k)
        
        return ans