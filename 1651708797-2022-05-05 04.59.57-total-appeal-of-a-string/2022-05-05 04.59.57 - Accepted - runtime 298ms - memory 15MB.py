class Solution:
    def _appeal(self, s):
        return len(set(s))
        
    def appealSum(self, s: str) -> int:
        n = len(s)
        ans = 1
        mem = {s[0]: 0}
        
        c = 1
        for i in range(1, n):
            if s[i] in mem:
                c += (i - mem[s[i]])
            else:
                c += (i + 1)
                
            ans += c
            mem[s[i]] = i

        return ans
        