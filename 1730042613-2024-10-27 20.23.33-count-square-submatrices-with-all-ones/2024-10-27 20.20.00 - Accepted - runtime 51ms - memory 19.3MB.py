class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        ones = 0

        def is_all_ones(i, j, p, q):
            k, l = i, j
            while k >= p:
                if matrix[k][j] != 1: return False
                k -= 1

            while l >= q:
                if matrix[i][l] != 1: return False
                l -= 1
            
            return True

        for i in range(n):
            for j in range(m):
                e = matrix[i][j]
                if e == 1:
                    ones += 1
                    k, l = i + 1, j + 1
                    
                    while k < n and l < m and is_all_ones(k, l, i, j):
                        # print("is_all_ones", k, l, is_all_ones(k, l, i, j))
                        k, l = k + 1, l + 1
                        ones += 1

        return ones

# 2 = 1
# 3 = 5
# 4 = 16
                    # 1 1 1 1
                    # 1 1 1 1
                    # 1 1 1 1
                    # 1 1 1 1

                    # 5 + 1 + 

                    # [1,0,1],
                   #  [1,1,0],
                   #  [1,1,0]]