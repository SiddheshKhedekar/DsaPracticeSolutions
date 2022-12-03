# Ugly Number -> Python3

'''
Explanation: Run loop on the factors and while n % factor is 0 and 0 is less than the new number 
set number to number floor divide factor. Number is ugly if it is 1 at end.
'''

class Solution:
    def isUgly(self, n: int) -> bool:
        for i in 2, 3, 5:
            while  n % i == 0 < n: n //= i
        return n == 1