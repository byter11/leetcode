class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        op = 0
        ans = 0
        for c in s:
            if c == '(': op += 1
            if c == ')': op -= 1

            if op < 0:
                ans += 1
                op += 1

        return ans + op

# ()(()))(((