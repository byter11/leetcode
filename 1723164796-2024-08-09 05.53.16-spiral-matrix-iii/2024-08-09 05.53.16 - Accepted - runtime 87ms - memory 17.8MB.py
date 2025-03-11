class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        radius = 1
        dir = 1
        v = -1
        ans = []

        while len(ans) < rows*cols:
            for i in range(radius):
                if self.in_bounds(rows, cols, rStart, cStart):
                    ans.append([rStart, cStart])
                if v == 1:
                    rStart += dir
                else:
                    cStart += dir
            
            if v == 1:
                radius += 1
                dir *= -1

            v *= -1
            
        return ans
    
    def in_bounds(self, rows: int, cols: int, rStart: int, cStart: int):
        return rStart >= 0 and cStart >= 0 and rStart < rows and cStart < cols

