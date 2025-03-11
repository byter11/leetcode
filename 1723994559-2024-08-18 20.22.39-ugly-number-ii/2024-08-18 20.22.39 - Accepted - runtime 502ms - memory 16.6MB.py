class Solution:
    def nthUglyNumber(self, n: int) -> int:
        factors = set()
        factors.add(1)
        cur = 1
        for _ in range(n):
            cur = min(list(factors))
            factors.remove(cur)
            for p in [2,3,5]:
                factors.add(cur * p)
            
        return cur
     