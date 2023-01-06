# Maximum Ice Cream Bars -> Python3

'''
Explanation: Sort the costs and loop on them. Subtract the cost from coins and return index when 
coins becomes negative else return the length after loop end.
'''

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        for i, a in enumerate(costs):
            coins -= a
            if coins < 0: return i
        return len(costs)