# Reverse Bits -> Python3

'''
Explanation: Get the output by performing bit manipulation on original 32 times in loop.
'''

class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(32):
            ans = (ans << 1) + (n & 1)
            n >>= 1
        return ans