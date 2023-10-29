# Binary Trees With Factors -> Python3

'''
Explanation: Set dp as dict and then run loop for x in sorted arr. Inside loop set dp at x as the 1 
plus sum of dp at y multiplied by the dp value through get at x divided by y, 0 for y in dp if x 
mod y is 0. Finally return the sum of dp values mod by given modulo constant.
'''

class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        dp = {}
        for x in sorted(arr): dp[x] = sum(dp[y] * dp.get(x / y, 0) for y in dp if x % y == 0) + 1
        return sum(dp.values()) % (10**9 + 7)