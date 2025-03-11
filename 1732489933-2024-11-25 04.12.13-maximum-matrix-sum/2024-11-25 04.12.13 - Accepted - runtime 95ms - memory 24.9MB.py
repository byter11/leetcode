class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        abs_sum = 0
        negs = 0
        mn = float('inf')
        for r in matrix:
            for c in r:
                negs += c < 0
                abs_sum += abs(c)
                mn = min(mn, abs(c))
        
        if negs % 2 == 0:
            return abs_sum
        
        return abs_sum - 2*mn