# Stone Game II -> Python3

'''
Explanation: Set l as len of piles then run for loop on range l-2 to -1 in reverse and inside 
increment the value at piles x by value at x + 1. Define a cached dp function with x and m as 
input and call it in return call to it in main with 0, 1. Inside dp check if x + 2 * m is greater 
than or same as l and return piles at x and return piles at x - min of dp call to x + y, max of 
m, y where y in range 1 to 2 * m + 1.
'''

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        l = len(piles)
        for x in range(l - 2, -1, -1): piles[x] += piles[x + 1]
        @lru_cache(None)
        def dp(x, m):
            if x + 2 * m >= l: return piles[x]
            return piles[x] - min(dp(x + y, max(m, y)) for y in range(1, 2 * m + 1))
        return dp(0, 1)