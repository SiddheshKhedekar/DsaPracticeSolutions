# Concatenation of Consecutive Binary Numbers -> Python3

'''
Explanation: Run a loop on range n and set out to the binary representation. On each step we need 
to multiply the number by length of the new number and add the new number along with using mod.
'''

class Solution:
    def concatenatedBinary(self, n: int) -> int:
        out, mod = 0, 10**9+7
        for i in range(n):
            out = (out * (1 << (len(bin(i+1)) - 2)) + i+1) % mod
        return out