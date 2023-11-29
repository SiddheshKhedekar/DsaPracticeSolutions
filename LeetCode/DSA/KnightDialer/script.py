# Knight Dialer -> Python3

'''
Explanation: Check if n is 1 to return 10 then set modulo, res, n as given value, 1, n-1. Set m as 
np matrix of each number possible initial values and loop while n to check if n % 2 to set res * m 
after mod set m as itself multiplied by it after mod and floor divide n by 2. Finally return int of 
the sum of res after mod.
'''

import numpy as np
class Solution:
    def knightDialer(self, n: int) -> int:
        if n == 1: return 10
        modulo, res, n = 10 ** 9 + 7, 1, n - 1
        m = np.matrix([[0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
                       [0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
                       [0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
                       [1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [1, 1, 0, 0, 0, 0, 0, 1, 0, 0],
                       [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
                       [0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
                       [0, 0, 1, 0, 1, 0, 0, 0, 0, 0]])
        while n:
            if n % 2: res = res * m % modulo
            m = m * m % modulo
            n //= 2
        return int(np.sum(res)) % modulo