class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        cs = nums[0] 
        sumFreq = defaultdict(int)
        sumFreq[cs] += 1
        ans = int(cs == k)
        for i in range(1, n):
            cs += nums[i]
            if cs == k:
                ans += 1

            ans += sumFreq[cs - k]
            sumFreq[cs] += 1
        
        return ans

        