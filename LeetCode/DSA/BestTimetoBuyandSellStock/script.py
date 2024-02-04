# Best Time to Buy and Sell Stock -> Python3

'''
Explanation: Consider buy 0 and sell 1 pointer along with a variable for max gain. Run a while loop 
for condition sell < len of prices. Inside initialize temp gain for sell - buy. If the item at sell 
is greater than buy check for max in max gain and temp gain and set it to max gain. Else set  buy 
to sell out of condition update sell by 1.
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP, buy, sell = 0, 0, 1
        while sell < len(prices):
            tempP = prices[sell]-prices[buy]
            if prices[sell] > prices[buy]: maxP = max(maxP,tempP)
            else: buy = sell
            sell+=1
        return maxP