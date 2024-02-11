# Palindromic Substrings -> Python3

'''
Explanation: Initialize l as len of s and ans as 0 then set dp as 2d array of dimension l with 0 as 
default value. Traverse first loop x from end to beginning and second loop y from x to end. Inside 
check if s at x is same as s at y and y - x + 1 is less than 3 or the dp value at x + 1 and y - 1 
is true and set it to dp value at dp at x, y then increment ans by the same and return ans at end.
'''

class Solution:
    def countSubstrings(self, s: str) -> int:
        l, ans = len(s), 0
        dp = [[0] * l for _ in range(l)]
        for x in range(l - 1, -1, -1):
            for y in range(x, l):
                dp[x][y] = s[x] == s[y] and ((y - x + 1) < 3 or dp[x + 1][y - 1])
                ans += dp[x][y]
        return ans