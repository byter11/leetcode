class Solution:
    def findComplement(self, num: int) -> int:
        ans = 0

        n = 1
        while n < num:
            if not num & n:
                ans += n
            n *= 2

        return ans
