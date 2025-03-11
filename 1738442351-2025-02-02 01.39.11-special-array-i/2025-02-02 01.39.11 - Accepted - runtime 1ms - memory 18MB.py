class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        for i in range(1, len(nums)):
            a, b = nums[i-1], nums[i]
            if a % 2 == b % 2:
                return False
        return True
        