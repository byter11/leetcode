class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        leaders = set([i for i in range(n)])

        for i, o in edges:
            if o in leaders:
                leaders.remove(o)
        
        if len(leaders) == 1:
            return list(leaders)[0]
        return -1