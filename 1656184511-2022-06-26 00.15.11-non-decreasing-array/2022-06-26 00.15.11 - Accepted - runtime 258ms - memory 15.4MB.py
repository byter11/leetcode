class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        cnt = 0
        n = len(nums)
        for i in range(1, n):
            if nums[i] < nums[i-1]:
                l = (i+1 < n and nums[i-1] <= nums[i+1]) or i+1>=n
                r = ((i-2) >= 0 and nums[i] >= nums[i-2]) or i-2<0
                if (l or r):
                    cnt += 1
                else:
                    cnt += 2
                print()
            if cnt >= 2:
                return False
        return True 