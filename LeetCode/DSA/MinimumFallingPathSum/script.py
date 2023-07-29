# Minimum Falling Path Sum -> Python3

'''
Explanation: Save the minimum value at each step of itself and the min value of the ones above it 
and at end return the min value in the last row.
'''

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        for i in range(1, len(matrix)):
            for j in range(len(matrix[0])):
                if j == 0: matrix[i][j] = min(matrix[i][j] + matrix[i - 1][j], matrix[i][j] + \
                matrix[i - 1][j + 1])
                elif j == len(matrix[0]) - 1: matrix[i][j] =  min(matrix[i][j] + matrix[i - 1][j], \
                matrix[i][j] + matrix[i - 1][j - 1])
                else: matrix[i][j] =  min(matrix[i][j] + matrix[i - 1][j], matrix[i][j] + \
                matrix[i - 1][j + 1], matrix[i][j] + matrix[i - 1][j - 1])
        return min(matrix[len(matrix) - 1])