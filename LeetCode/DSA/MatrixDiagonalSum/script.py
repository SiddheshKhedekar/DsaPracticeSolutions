# Matrix Diagonal Sum -> Python3

'''
Explanation: Set l, m, summ as the length the mid and 0. Run for loop and increment summ by the 
first diagonal as well as the second. Then check if diagonal overlap and subtract.
'''

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        l, m, summ = len(mat), len(mat) // 2, 0
        for x in range(l): summ = summ + mat[x][x] + mat[l-1-x][x]
        if l % 2 != 0: summ -= mat[m][m]
        return summ