class Solution:
    def minimumSteps(self, s: str) -> int:
        n = len(s)
        swaps = 0
        j = n - 1
        for i in range(n - 1, -1, -1):
            if s[i] == '1':
                swaps += j - i
                j -= 1
        return swaps

# 001001110
# 001001101
# 001001011
# 001000111
# 000100111
# 000010111
# 000001111
