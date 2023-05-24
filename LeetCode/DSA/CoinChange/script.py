# Coin Change -> Python3

'''
Explanation: Set maxamt as float inf and dp as array of 0 + maxamt * amount. Then run for loop on 
range 1 to amount + 1 and inside ste dp at x as min from array of dp at x - c if x - c is greater 
than or same as 0 else maxamt for c in coins after + 1. Finally return the dp at amount if dp 
amount is max amount else -1.
'''

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        maxAmt = float('inf')
        dp = [0] + [maxAmt] * amount
        for x in range(1, amount + 1):
            dp[x] = min([dp[x - c] if x - c >= 0 else maxAmt for c in coins]) + 1
        return [dp[amount], -1][dp[amount] == maxAmt]