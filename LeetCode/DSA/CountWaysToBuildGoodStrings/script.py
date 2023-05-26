# Count Ways To Build Good Strings -> Python3

'''
Explanation: Initialize dp, modulo as counter dict 0:1, given and run a loop on range 1 to high+1. 
Inside set dp at x as dp at x - zero plus dp at x - one after modulo. Then return sum of dp at x 
where x in range low and high + 1 after modulo.
'''

class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp, modulo = Counter({0: 1}), 10 ** 9 + 7
        for x in range(1, high + 1):
            dp[x] = (dp[x - zero] + dp[x - one]) % modulo
        return sum(dp[x] for x in range(low, high + 1)) % modulo