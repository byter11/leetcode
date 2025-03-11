class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        # nums[j] - nums[i] == j - i
        # nums[j] - j == nums[i] - i
        if len(nums) == 1:
            return 0
        
        if len(nums) == 2:
            return int(nums[1] - nums[0] != 1)

        good = defaultdict(int)
        good_count = 0
        for i, x in enumerate(nums):
            good_count += good[nums[i] - i]
            good[nums[i] - i] += 1
        
        return int(self.nPr(len(nums), 2)) - good_count

    def nPr(self, n, r):
        return factorial(n)/(factorial(r) * factorial(n-r))