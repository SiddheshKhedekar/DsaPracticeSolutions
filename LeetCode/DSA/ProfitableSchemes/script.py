# Profitable Schemes -> Python3

'''
Explanation: Initialize dp as a 2d array of 0 of n+1 cols and minprofit-1 rows then set dp at 0,0 
to 1. Run for loop on zip profit and group. Inside run loop for range minprofit in reverse and 
inside that loop run another loop for range n-g in reverse then increment dp at min x+p, minprofit 
and y+g by dp at x,y and finally return the sum of dp at minprofit after modulo.
'''

class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        dp = [[0] * (n + 1) for x in range(minProfit + 1)]
        dp[0][0] = 1
        for p, g in zip(profit, group):
            for x in range(minProfit, -1, -1):
                for y in range(n - g, -1, -1): dp[min(x + p, minProfit)][y + g] += dp[x][y]
        return sum(dp[minProfit]) % (10**9 + 7)