# Zigzag Conversion -> Python3

'''
Explanation: Check for base conditions then define res as array of empty string times the numrows 
index as 0 and stp as 1. Loop for i in s to increment res by i and check if index is 0 to set stp 
as 1 else if index is numrows -1 set spt-1 and increment index by stp. Finally join and return res.
'''

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s): return s
        res, indx, stp = [''] * numRows, 0, 1
        for i in s:
            res[indx] += i
            if indx == 0: stp = 1
            elif indx == numRows -1: stp = -1
            indx += stp
        return ''.join(res)