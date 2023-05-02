# Restore The Array -> Python3

'''
Explanation: Define dp as an array of len s with -1 as items and return the dfs call with s, k, 0 
as x and dp. Inside the function definition check if x is len s and return 1 then check if s at x 
is char 0 and return 0 also check if dp at x is not -1 to return dp at x. Initialize res and num as 
0 then run loop for y in range x to len s. Inside set num as num * 10 + int of s at y and check if 
num is greater than k to break flow then set res as res + dfs call with y + 1 as x and after 
modulo. Outside loop set dp at x as res and return res.
'''

class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        def dfs(s, k, x, dp):
            if x == len(s): return 1
            if s[x] == '0': return 0
            if dp[x] != -1: return dp[x]
            res, num = 0, 0
            for y in range(x, len(s)):
                num = num * 10 + int(s[y])
                if num > k: break
                res = (res + dfs(s, k, y + 1, dp)) % (10**9 + 7)
            dp[x] = res
            return res
        dp = [-1] * len(s)
        return dfs(s, k, 0, dp)