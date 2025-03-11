class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        arr = []
        for i in range(len(nums)):
            s = 0
            for j in range(i, len(nums)):
                s += nums[j]
                arr.append(s)
        
        arr.sort()
        return sum(arr[left-1:right]) % int(1e9+7)