# Best Time to Buy and Sell Stock with Cooldown -> Python3

'''
Explanation: For any given price set the previous values and then set cooldown to max of previous 
cooldown and sell. Set sell to previous hold + current price and set hold to max of previous hold 
and previous cooldown - current price. Finally return max of sell and cooldown.
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cooldown, sell, hold = 0, 0, -float('inf')
        for stock_price_i in prices:
            prev_cd, prev_sell, prev_hold = cooldown, sell, hold
            cooldown = max(prev_cd, prev_sell)
            sell = prev_hold + stock_price_i
            hold = max(prev_hold, prev_cd - stock_price_i)
        return max(sell, cooldown)