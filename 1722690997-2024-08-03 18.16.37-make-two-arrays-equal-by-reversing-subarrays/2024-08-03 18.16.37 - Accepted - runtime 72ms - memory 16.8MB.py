class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        nums = {}
        for a in arr:
            nums[a] = nums.get(a, 0) + 1

        for t in target:
            if t not in nums:
                return False
            nums[t] -= 1
        
        for n in nums:
            if nums[n] > 0:
                return False
                
        return True