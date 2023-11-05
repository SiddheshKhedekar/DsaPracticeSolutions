# Longest Valid Parentheses -> Python3

'''
Explanation: Set dp as array of 0 of len s + 1 and stk as empty array. Then run loop for range len 
s to check if s at x is ( and append x in stk else check if stk and pop it in b set the dp at x + 1 
as dp at b value after adding x - b + 1 and finally return the max of dp. We form the condition for 
dp based on the position of ( in stack that matches the current ).
'''

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        dp, stk = [0] * (len(s) + 1), []
        for x in range(len(s)):
            if s[x] == '(': stk.append(x)
            else:
                if stk:
                    b = stk.pop()
                    dp[x + 1] = dp[b] + x - b + 1
        return max(dp)