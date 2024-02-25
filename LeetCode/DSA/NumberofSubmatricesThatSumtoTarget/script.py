# Number of Submatrices That Sum to Target -> Python3

'''
Explanation: First calculate the prefix sum for each row then for each pair of columns calculate 
the accumulated sum of rows. Then loop on len of matrix first row b as x and inside loop on range x 
to b as y. Set temp as depaultdict of int and crnt, temp at 0 as 0 and 1. Then loop on len of 
matrix a and increment crnt by matrix at x, y - the matrix at z, x-1 if x is greater than 0 else by 
0. Increment ans by temp at crnt - target and temp at crnt by 1 then after loop end return ans.
'''

class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        a, b, ans = len(matrix), len(matrix[0]), 0
        for row in matrix:
            for col in range(b - 1): row[col + 1] += row[col]
        for x in range(b):
            for y in range(x, b):
                temp = defaultdict(int)
                crnt, temp[0] = 0, 1
                for z in range(a):
                    crnt += matrix[z][y] - (matrix[z][x - 1] if x > 0 else 0)
                    ans += temp[crnt - target]
                    temp[crnt] += 1
        return ans