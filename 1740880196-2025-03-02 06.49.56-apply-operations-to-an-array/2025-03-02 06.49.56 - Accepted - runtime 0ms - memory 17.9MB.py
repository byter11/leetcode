class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
         
        ans = []
        z = []
        for n in nums:
            if n != 0:
                ans.append(n)
            else: z.append(n)
        return ans + z
            