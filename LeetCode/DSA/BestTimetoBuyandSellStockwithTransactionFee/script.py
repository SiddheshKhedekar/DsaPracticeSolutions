# Best Time to Buy and Sell Stock with Transaction Fee -> Python3

'''
Explanation: Use greedy solution by setting minimum as first index value from prices then loop on 
range of len to check if prices at x is less than min to set min as the prices at x. Else if prices 
at x is greater than min + fee then increment res by prices at x - fee - min and set min as prices 
at x - fee.
'''

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        l, res, minm = len(prices), 0, prices[0]
        if l < 2: return 0
        for x in range(1, l):
            if prices[x] < minm: minm = prices[x]
            elif prices[x] > minm + fee:
                res += prices[x] - fee - minm
                minm = prices[x] - fee
        return res