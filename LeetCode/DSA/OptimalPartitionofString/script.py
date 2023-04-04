# Optimal Partition of String -> Python3

'''
Explanation: Set x, flg as 0 and res as 1. Run loop while x is less than len of string and set val 
as ord s at x - ord a. Check if flg and 1 << val to reset flag to 0 and increment res by 1. After 
if set flg |= 1 << val and increment x by 1.
'''

class Solution:
    def partitionString(self, s: str) -> int:
        x, res, flg = 0, 1, 0
        while x < len(s):
            val = ord(s[x]) - ord('a')
            if flg & (1 << val):
                flg = 0
                res += 1
            flg |= 1 << val
            x += 1
        return res