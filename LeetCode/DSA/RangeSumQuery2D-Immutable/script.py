# Range Sum Query 2D - Immutable -> Python3

'''
Explanation: In init populate grid using prefix sum then in sum region use the prefix sum to 
subtract the needed values and return value. When creating prefix sum add one to the range of len 
and similarly in sumregion start by adding 1 to the region indices.
'''

class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        x, y = len(matrix), len(matrix[0])
        self.s = [[0] * (y + 1) for _ in range(x + 1)]
        for r in range(1, x + 1):
            for c in range(1, y + 1):
                self.s[r][c] = self.s[r - 1][c] + self.s[r][c - 1] - \
                                    self.s[r - 1][c - 1] + matrix[r - 1][c - 1]
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1, c1, r2, c2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        return self.s[r2][c2] - self.s[r2][c1 - 1] - \
                self.s[r1 - 1][c2] + self.s[r1 - 1][c1 - 1]