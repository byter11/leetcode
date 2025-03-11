class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        l = [0]*64

        for c in candidates:
            i = 0
            while c:
                l[i] += c & 1
                c >>= 1
                i += 1
        
        return max(l)