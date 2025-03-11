class Solution:
    def minChanges(self, s: str) -> int:
        n = len(s)

        ans = 0
        for i in range(0, n-1, 2):
            cur, nxt = s[i], s[i+1]

            if cur != nxt:
                ans += 1
        
        return ans


# 111111001