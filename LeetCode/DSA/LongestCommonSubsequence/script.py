# Longest Common Subsequence -> Python3

'''
Explanation: Set a, b as len text1, text2 and set dp as 0 array of length is b + 1. Then run loop 
of c in text 1 and set preR, preRc as 0, 0. Run another loop for r, d in enumerate text2 and inside 
set preR. preRc as dp at r + 1, preR and set dp at r + 1 as preRc + 1 if c is same as d else max of 
dp at r, preR and out of both loops return dp at -1.
'''

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        a, b = len(text1), len(text2)
        dp = [0] * (b + 1)
        for c in text1:
            preR, preRc = 0, 0
            for r, d in enumerate(text2):
                preR, preRc = dp[r + 1], preR
                dp[r + 1] = preRc + 1 if c == d else max(dp[r], preR)
        return dp[-1]