# Longest Palindromic Subsequence -> Python3

'''
Explanation: Set len as l along with dp and dpp as arrays of size l. Run a for loop in reverse from 
second last element set dp at current x to 1 then run another loop from x + 1 to l. Inside check if 
s at x value is same as s at current y value and set dp at y to dpp at y - 1 after adding 2 else 
set dp at y to max of dp at y and dpp at y - 1. After inner loop end swap dp and dpp and finally 
return the last element in dpp.
'''

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        l = len(s)
        dp, dpp = [0] * l, [0] * l
        for x in range(l - 1, -1, -1):
            dp[x] = 1
            for y in range(x + 1, l):
                if s[x] == s[y]: dp[y] = dpp[y - 1] + 2
                else: dp[y] = max(dpp[y], dp[y - 1])
            dp, dpp = dpp, dp
        return dpp[l - 1]