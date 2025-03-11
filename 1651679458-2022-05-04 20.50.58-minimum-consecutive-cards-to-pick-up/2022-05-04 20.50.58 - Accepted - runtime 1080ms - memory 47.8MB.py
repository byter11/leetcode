class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        d = {}
        res = float('inf')
        
        for i, c in enumerate(cards):
            sc = str(c)
            if d.get(sc):
                res = min(res, i - d[sc][-1] + 1)
                d[sc].append(i)
            else:
                d[sc] = [i]
            
        return res if res != float('inf') else -1
        