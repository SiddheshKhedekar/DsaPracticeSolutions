# Bitwise AND of Numbers Range -> Python3

'''
Explanation: Set x as 0 then run loop while left is not same as right and inside set left as 
left >> 1 and same for right then increment x finally out of loop return right << x. 
'''

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        x = 0
        while left != right:
            left >>= 1
            right >>= 1
            x += 1
        return right << x