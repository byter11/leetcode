class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        freq = defaultdict(int)
        dups = set()
        
        i = 0
        cur = 0
        while i < n:
            cur += nums[i]
            freq[nums[i]] += 1
            if freq[nums[i]] > 1:
                dups.add(nums[i])

            if i >= k:
                freq[nums[i-k]] -= 1
                if freq[nums[i-k]] <= 1 and nums[i-k] in dups:
                    dups.remove(nums[i-k])
                cur -= nums[i-k]

            # print(i-k, i, cur, nums[i], len(dups))
            if i >= k - 1 and len(dups) == 0:
                # print("adding", cur)
                ans = max(ans, cur)

            i += 1
        
        return ans

# [5,5,4,2,9,9,9,4,2]