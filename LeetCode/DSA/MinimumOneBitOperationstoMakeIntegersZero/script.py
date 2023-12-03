# Minimum One Bit Operations to Make Integers Zero -> Python3

'''
Explanation: Set res as 0 and loop while n. In loop set res as the negative of it - the xor of n 
with n - 1 then set n as n & with n - 1. outside loop return abs of res.
'''

class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        res = 0
        while n:
            res = -res - (n ^ (n - 1))
            n &= n - 1
        return abs(res)