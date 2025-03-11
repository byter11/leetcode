class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s = "0"
        k -= 1
        while k:
            s += "1"
            k -= 1
            i = len(s) - 2
            while k and i >= 0:
                s += "1" if s[i] == "0" else "0"
                i -= 1
                k -= 1
        
        return s[-1]
