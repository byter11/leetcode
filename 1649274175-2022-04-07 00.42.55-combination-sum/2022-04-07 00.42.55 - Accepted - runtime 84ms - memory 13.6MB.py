class Solution(object):
    def combinationSum_r(self, c, t, r, cb = [], i=0):
        s = sum(r)
        if s > t:
            return
        if s == t:
           cb.append(r)
           return 

        for j in range(i, len(c)):
            self.combinationSum_r(c, t, r+[c[j]], cb, j)

        return cb
    

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        return self.combinationSum_r(candidates, target, [], [])
        
        