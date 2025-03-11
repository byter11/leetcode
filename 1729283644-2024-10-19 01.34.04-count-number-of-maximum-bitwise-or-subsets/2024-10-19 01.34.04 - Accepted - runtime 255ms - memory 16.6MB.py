class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        n = len(nums)
        max_or = 0
        for x in nums: max_or |= x

        def check(cur, i, ans = 0):
            if i >= n: return 0
            if cur == max_or: ans += 1

            for j in range(i+1, n):
                ans += check(cur | nums[j], j, 0)

            return ans

        ans = 0
        for i in range(n):
            ans += check(nums[i], i, 0)
        return ans
    
    # 0 1 1
    # 0 1 0
    # 0 0 1
    # 1 0 1
# 2 - 1
# 2 2 - 2
# 2 2 2 - 3
# 2 - 4
# 2 2 - 5
# 