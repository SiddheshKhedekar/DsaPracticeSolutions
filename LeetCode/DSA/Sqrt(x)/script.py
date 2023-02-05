# Sqrt(x) -> Python3

'''
Explanation: Use binary search. If x is 0 return 0. In a while true loop initialize m to mid of i 
and j. If m is greater than x floor divide by m then j is m-1 else if m+1 is greater than x floor 
divide by (m+1) then return m. Outside if but in upper else set i to m+1.
'''

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        i, j = 1, x
        while True:
            m = i + (j - i)//2
            if m > x//m:
                j = m - 1
            else:
                if m + 1 > x // (m +1):
                    return m 
                i = m + 1