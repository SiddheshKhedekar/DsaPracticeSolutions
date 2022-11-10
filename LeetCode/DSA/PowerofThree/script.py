# Power of Three -> Python3

'''
Explanation: While number greater than 3 we keep dividing and updating the original number. If the 
final value of number is not equal to 1 then it is not a power of 3
'''

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while n >= 3:
            n /= 3
        if n == 1:
            return True
        return False