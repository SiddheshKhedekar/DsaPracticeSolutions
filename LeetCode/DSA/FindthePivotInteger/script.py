# Find the Pivot Integer -> Python3

'''
Explanation: Use math based formula to set tmp as the square of n + n and floor div by 2 then set 
sqr as the int of sqrt temp. Check if square of sqr is tmp and return sqr otherwise return -1.
'''

class Solution:
    def pivotInteger(self, n: int) -> int:
        tmp = (n * n + n) // 2
        sqr = int(sqrt(tmp))
        if sqr * sqr == tmp: return sqr
        return -1