# Stone Game III -> Python3

'''
Explanation: Set dp as array with three 0 then run for loop on range len of stonevalue in reverse 
order. Set dp at x % 3 as the max of the sum of stonevalue between x and x + y - dp at x + y % 3 
where y loops on 1, 2, 3. Finally return between tie, alice, bob based on compare between dp at 0 
and 0.
'''

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        dp = [0] * 3
        for x in range(len(stoneValue) - 1, -1, -1):
            dp[x % 3] = max(sum(stoneValue[x:x + y]) - dp[(x + y) % 3] for y in (1, 2, 3))
        return ['Tie', 'Alice', 'Bob'][(dp[0] > 0) - (dp[0] < 0)]