class Solution:
    def getLucky(self, s: str, k: int) -> int:
        c = ''.join([str(ord(c) - ord('a') + 1) for c in s])
        for _ in range(k):
            c = str(sum([int(d) for d in c]))
        return int(c)