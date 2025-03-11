class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        n = len(items)
        items.sort(key = lambda x: x[1], reverse=True)
        queries = sorted([(q, i) for i, q in enumerate(queries)], reverse=True)

        i = 0
        j = 0
        ans = [0]*len(queries)
        for q, j in queries:
            while i < n and items[i][0] > q:
                i += 1

            if i >= n:
                return ans
            
            ans[j] = items[i][1]
        
        return ans
                        
