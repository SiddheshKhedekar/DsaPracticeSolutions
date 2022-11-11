# Toeplitz Matrix -> Python3

'''
Explanation: We loop on the matrix to the second last column and row to check if the current and 
its next diagonal element are equal and return total iteration values using all function.
'''

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        return all(matrix[i][j] == matrix[i+1][j+1] for i in range(len(matrix)-1) for j in range(len(matrix[0])-1))