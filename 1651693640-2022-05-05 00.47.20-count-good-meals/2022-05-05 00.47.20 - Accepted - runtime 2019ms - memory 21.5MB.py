import math
class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        n = len(deliciousness)
        ans = 0
        d = {}
        
        for x in deliciousness:
            for k in [1 << i for i in range(22)]:
                ans += d.get(k-x, 0)
            if not d.get(x): d[x] = 0
            d[x] += 1

                    
        return ans % ((10 ** 9) + 7)
                 