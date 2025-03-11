class Solution:
    def check(self, nums: List[int]) -> bool:
        start = -1
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                start = i
                break
        
        if start == -1:
            return True
        
        i = (start + 1) % len(nums)
        while i != start:
            if nums[i] < nums[i-1]:
                return False
                
            i = (i + 1) % len(nums)

        return True
