class Fenwick():
    def __init__(self, matrix):
        self.N, self.M = len(matrix), len(matrix[0])
        self.tree = [[0 for j in range(self.M)] for i in range(self.N)]
    
    def update(self, row, col, val): # (row, col) 1-indexed
        while row <= self.M:
            while col <= self.N:
                self.tree[row][col] += val
                col += (col & -col)
            row += (row & -row)
        
    def sum_range(self, row1, col1, row2, col2):
        return self.read(row2, col2) - self.read(row2, col1-1) - self.read(row1 - 1, col2) + self.read(row1-1, col1-1)

    def read(self, row, col):
        total = 0
        while row > 0:
            while col > 0:
                total += self.tree[row][col]
                col -= (col & -col)
            row -= (row & -row)
        return total

        