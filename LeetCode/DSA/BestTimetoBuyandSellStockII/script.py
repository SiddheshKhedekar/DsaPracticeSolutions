# Best Time to Buy and Sell Stock II -> Python3

'''
Explanation: Loop on first to second last index in prices as i then check if prices at i is less 
than the value at i + 1 and increment profit by prices at i + 1 after subtracting value at i.
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices) - 1):
            if prices[i] < prices[i + 1]: profit += (prices[i + 1] - prices[i])
        return profit