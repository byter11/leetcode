class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        n = len(matrix)
        m = len(matrix[0])
        self.summatrix = [[0]*(m+1) for i in range(n+1)]
        
        for k in matrix:
            print(k)
            
        for i in range(n):
            for j in range(m):
                self.summatrix[i+1][j+1] = (
                    self.summatrix[i][j+1] + self.summatrix[i+1][j] - self.summatrix[i][j] + matrix[i][j]
                )
        for m in self.summatrix:
            print(m)
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.summatrix[row2+1][col2+1] - self.summatrix[row1][col2+1] - self.summatrix[row2+1][col1] + self.summatrix[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)