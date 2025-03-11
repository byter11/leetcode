class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2: return True
        unequal_idx = [i for i in range(len(s1)) if s1[i] != s2[i]]
        
        if len(unequal_idx) != 2:
            return False
        
        i, j = unequal_idx

        # c(a) a a(b)
        # a(c) a z(d)
        a, b, c, d = s1[i], s1[j], s2[i], s2[j]
        return a == d and b == c

        