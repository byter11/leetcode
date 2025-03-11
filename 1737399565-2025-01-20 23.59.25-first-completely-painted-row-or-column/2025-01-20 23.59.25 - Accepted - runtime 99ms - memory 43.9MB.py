class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        n, m = len(mat), len(mat[0])
        indexes = [None]*(n*m + 1)
        painted_rows = [0]*n
        painted_cols = [0]*m

        # Populate indexes map
        for i in range(n):
            for j in range(m):
                indexes[mat[i][j]] = (i, j)

        for k, x in enumerate(arr):
            i, j = indexes[x]
            painted_rows[i] += 1
            painted_cols[j] += 1

            # print(k, x, i, j, painted_rows[i], painted_cols[j])
        
            if painted_rows[i] == m or painted_cols[j] == n:
                return k
            
        return -1

