class Solution:
    def makeFancyString(self, s: str) -> str:
        i = 0
        while i < len(s) - 2:
            if s[i] == s[i+1] == s[i+2]:
                s = s[:i] + s[i+1:]
            else:
                i += 1
        
        return s