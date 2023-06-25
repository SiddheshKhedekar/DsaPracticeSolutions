# Decode Ways -> Python3

'''
Explanation: Set dp, dp1, dp2, n to 0, 1, 0, len(s). Loop for i in range n in reverse order to 0. 
If s[i] != 0 then dp+=dp1. If i+1 < n and (s[i] == '1' or s[i] == '2' and s[i+1] <= '6') then 
dp+=dp2. Outside set dp, dp1,dp2 to 0, dp, dp1. Finally out return dp1.
'''

class Solution:
    def numDecodings(self, s: str) -> int:
        dp, dp1, dp2, n = 0, 1, 0, len(s)
        for i in range(n-1,-1,-1):
            if s[i] != '0': dp += dp1
            if i+1 < n and (s[i] == '1' or s[i] == '2' and s[i+1] <= '6'):
                dp+=dp2
            dp, dp1, dp2 = 0, dp, dp1
        return dp1