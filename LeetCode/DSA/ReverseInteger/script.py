# Reverse Integer -> Python3

'''
Explanation: Get the sign of the original number and then reverse the string and add sign finally 
check the size limits.
'''

class Solution:
    def reverse(self, x: int) -> int:
        string = [1, -1][x < 0]
        rev = string * int(str(abs(x))[::-1])
        return rev if -(2**31)-1 < rev < (2**31) else 0