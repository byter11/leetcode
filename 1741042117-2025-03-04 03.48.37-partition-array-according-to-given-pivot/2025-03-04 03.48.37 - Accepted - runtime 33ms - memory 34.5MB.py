class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        i, n = 0, len(nums)
        ans = []
        for n in nums:
            if n < pivot: ans.append(n)

        for n in nums:
            if n == pivot: ans.append(n)
        
        for n in nums:
            if n > pivot: ans.append(n)
        
        return ans