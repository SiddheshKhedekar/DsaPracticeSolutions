# Special Positions in a Binary Matrix -> Python3

'''
Explanation: First loop on matrix and set rcnt and ccnt as sum of 1 in mat row and col. Then loop 
on it again and check for the conditions rcnt, ccnt and mat value at r, c being met to update res.
'''

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        res, x, y = 0, len(mat), len(mat[0])
        rCnt, cCnt = [0] * x, [0] * y
        for r in range(x):
            for c in range(y):
                if mat[r][c] == 1:
                    rCnt[r] += 1
                    cCnt[c] += 1
        for r in range(x):
            for c in range(y):
                if mat[r][c] == 1 and rCnt[r] == 1 and cCnt[c] == 1: res += 1
        return res