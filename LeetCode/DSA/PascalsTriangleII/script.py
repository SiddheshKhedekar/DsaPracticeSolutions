# Pascal's Triangle II -> Python3

'''
Explanation: Initialize starting point of pascals triangle and then in loop get the current row by 
appending 0 to the previous row where needed and getting the sum.
'''

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1]
        for _ in range(rowIndex):
            res = [i + j for i, j in zip([0]+res, res+[0])]
        return res