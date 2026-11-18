class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.ROW, self.COL = len(matrix) + 1, len(matrix[0]) + 1
        # ROW x COL
        self.prefix = [[0] * self.COL for _ in range(self.ROW)]

        for r, row in enumerate(matrix):
            total = 0
            for c, num in enumerate(row):
                total += num
                self.prefix[r+1][c+1] = total + self.prefix[r][c+1]
        print(self.prefix)
    
    def sumRegion(self, row1, col1, row2, col2):
        return self.prefix[row2+1][col2+1] - self.prefix[row1][col2+1] - self.prefix[row2+1][col1] + self.prefix[row1][col1]



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)


