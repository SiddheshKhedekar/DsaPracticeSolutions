# Spiral Matrix -> Python3

'''
Explanation: Run loop while matrix is not empty and add to result by popping matrix 0 position. 
Then ste matrix by getting the column values as row from last to first. 
'''

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        while matrix:
            res += matrix.pop(0)
            matrix = (list(zip(*matrix)))[::-1]
        return res