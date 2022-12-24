# Domino and Tromino Tiling -> Python3

'''
Explanation: For each n tile combo value can be from previous n tile combo values.
'''

class Solution:
    def numTilings(self, n: int) -> int:
        dp = [1, 2, 5] + [0] * n
        for i in range(3, n):
            dp[i] = (dp[i-1] * 2+dp[i-3]) % 1000000007
        return dp[n-1]