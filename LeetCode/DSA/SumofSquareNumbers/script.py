# Sum of Square Numbers -> Python3

'''
Explanation: Use math properties and set a to 0 and while a multiplied by itself is less than of 
equal to c, set b to square root of c-a*a and if b is same as int(b) then return true else 
increment a by 1.
'''

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = 0
        while a*a <= c:
            b = sqrt(c-a*a)
            if b == int(b): return True
            a+=1
        return False