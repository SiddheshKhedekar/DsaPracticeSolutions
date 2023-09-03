# 01 Matrix -> Python3

'''
Explanation: Iterate top left first then bottom right. Check only if mat ij value is > 0. Set top 
and left to  prev value of r and c if r and c > 0 else inf and in mat rc set min of (top bottom)+1. 
For bottom right it is opposite r and c +1 and r and c < m or n -1. Also while setting min mat rc 
bottom+1 and right+1 to be considered.
'''

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        for r in range(m):
            for c in range(n):
                if mat[r][c] > 0:
                    top = mat[r-1][c] if r > 0 else math.inf
                    left = mat[r][c-1] if c > 0 else math.inf
                    mat[r][c] = min(top, left) + 1
        for r in range(m-1,-1,-1):
            for c in range(n-1,-1,-1):
                if mat[r][c] > 0:
                    bottom = mat[r+1][c] if r < m-1 else math.inf
                    right = mat[r][c+1] if c < n-1 else math.inf
                    mat[r][c] = min(mat[r][c], bottom+1, right+1)
        return mat