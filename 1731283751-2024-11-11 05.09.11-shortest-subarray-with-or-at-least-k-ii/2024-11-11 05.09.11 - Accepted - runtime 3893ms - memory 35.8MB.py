class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        cur = nums[0]
        i, j = 0, 0

        bits = [0] * 64
        def add_bits(x, d = 1):
            i = 0
            while x:
                bits[i] += d * (x & 1)
                x >>= 1
                i += 1
        add_bits(nums[0])

        def from_bits():
            x = 0
            for i in range(len(bits)):
                x += int(bits[i] > 0) << i
            return x

        ans = float('inf')
        while i < n and j < n:
            cur = from_bits()
            # print(i, j, cur)
            if cur >= k:
                ans = min(ans, j - i + 1)

            if j <= i or cur < k:
                j += 1
                if j < n:
                    add_bits(nums[j], 1)
            else:
                add_bits(nums[i], -1)
                i += 1

            

        return -1 if ans == float('inf') else ans
