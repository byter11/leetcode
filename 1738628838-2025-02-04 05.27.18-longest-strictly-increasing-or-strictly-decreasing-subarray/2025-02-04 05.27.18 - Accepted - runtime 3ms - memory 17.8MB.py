class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        direction = -1
        length = 1
        ans = length

        for i in range(1, n):
            if nums[i] == nums[i-1]:
                length = 1
                continue
            
            if direction == -1:
                direction = 1 if nums[i] > nums[i-1] else 0

            same_dir = (nums[i] > nums[i-1] and direction == 1) or (nums[i] < nums[i-1] and direction == 0)
            if not same_dir:
                length = 1
                direction = int(not direction)

            length += 1
            ans = max(ans, length)
        return ans        