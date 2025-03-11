class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        return 0 if not start and not goal else (start & 1 != goal & 1) + self.minBitFlips(start >> 1, goal >> 1)