# Largest Submatrix With Rearrangements -> Python3

'''
Explanation: Iterate through the matrix starting from the second row and for each matrix[a][b] = 1 
update it as the sum of itself and previous row's corresponding cell. Then for each row sorted in 
reverse update res as the max of itself and the area of submatrix ending at current cell. Then at 
the end of loop return res.
'''

class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        x, y, res = len(matrix), len(matrix[0]), 0
        for a in range(1, x):
            for b in range(y):
                if matrix[a][b] == 1: matrix[a][b] += matrix[a - 1][b]
        for a in matrix:
            a.sort(reverse = True)
            for b in range(y): res = max(res, a[b] * (b + 1))
        return res