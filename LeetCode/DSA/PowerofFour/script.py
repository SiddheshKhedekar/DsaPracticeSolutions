# Power of Four -> Python3

'''
Explanation: While number greater than 4 we keep dividing and updating the original number. If the 
final value of number is not equal to 1 then it is not a power of 4
'''

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        while n >= 4:
            n = n/4
        if n == 1:
            return True
        return False