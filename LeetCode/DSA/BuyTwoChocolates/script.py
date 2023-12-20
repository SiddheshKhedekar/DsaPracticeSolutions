# Buy Two Chocolates -> Python3

'''
Explanation: Set mn1 and mn2 as max possible then loop on price in prices and check if price is 
less than mn1 to set mn2 as mn1 and mn1 as price and also check if price is less than mn2 to set 
mn2 as price. Outside loop set mn as sum of mn1 and mn2 then return money - mn if it is less than 
money else return money.
'''

class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        mn1 = mn2 = float('inf')
        for price in prices:
            if price < mn1: mn2, mn1 = mn1, price
            elif price < mn2: mn2 = price
        mn = mn1 + mn2
        return money - mn if mn <= money else money