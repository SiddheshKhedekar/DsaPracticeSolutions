# Maximum Value of K Coins From Piles -> Python3

'''
Explanation: Return the call to dp func with 0 and k as params. Define a dp func with x and a as 
params and check if a is 0 or x is len of piles then return 0. Set ans as dp with x+1 and crnt as 0 
then run a for loop on min of len piles x and a. Increment crnt by piles at x y then set ans as max 
of ans and crnt + dp at x+1, a-y-1 and return ans after loop end. 
'''

class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        @lru_cache(None)
        def dp(x, a):
            if a == 0 or x == len(piles): return 0
            ans, crnt = dp(x + 1, a), 0
            for y in range(min(len(piles[x]), a)):
                crnt += piles[x][y]
                ans = max(ans, crnt + dp(x + 1, a - y - 1))
            return ans
        return dp(0, k)