# Triangle -> Python3

'''
Explanation: Set res as last row of input and then loop from second last row to first. Inside loop 
over the values in row and set res j to min (res j, res j+1) + triangel ij and finally return 
res[0] outside both loops.
'''

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle: return
        res = triangle[-1]
        for i in range(len(triangle)-2,-1,-1):
            for j in range(len(triangle[i])):
                res[j] =  min(res[j], res[j+1]) + triangle[i][j]
        return res[0]