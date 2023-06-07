# New 21 Game -> Python3

'''
Explanation: Check if k is 0 or n is greater than or same as k + maxpts to return 1. Set dp as 
array of 1.0 + 0.0 * n and pts sum as 1.0 then run loop for x in range 1 to n + 1. Inside set dp at 
x as ptssum divide by maxpts then check if x < k to increment ptssum by dp at x and check if 
x - maxpts greater than or same as 0 to decrement ptssum by dp at x - maxpts. Finally return sum of 
dp k to end.
'''

class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0 or n >= k + maxPts: return 1
        dp, ptsSum = [1.0] + [0.0] * n, 1.0
        for x in range(1, n + 1):
            dp[x] = ptsSum / maxPts
            if x < k: ptsSum += dp[x]
            if x - maxPts >= 0: ptsSum -= dp[x - maxPts]
        return sum(dp[k:])