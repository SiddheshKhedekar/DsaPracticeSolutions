# Power of Two -> Python3

'''
Explanation: While number greater than 2 we keep dividing and updating the original number. If the 
final value of number is not equal to 1 then it is not a power of 2
'''

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        while n >= 2:
            n /= 2
        if n == 1:
            return True
        return False