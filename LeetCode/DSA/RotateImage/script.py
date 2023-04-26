# Rotate Image -> Python3

'''
Explanation: Reverse the matrix and run loop with i on matrix len and another loop with j on i. 
Inside nested loop swap the matrix value at i, j and j, i.
'''

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix.reverse()
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]