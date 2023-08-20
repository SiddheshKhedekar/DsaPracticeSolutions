# Integer Break -> Python3

'''
Explanation: Set dp as array of None, 1 and run loop for a in range 2 to n + 1. Set y, x, mx as 
a - 1, 1, 0 and run loop while x is less than or same as y. Inside set mx as max of mx or the 
product of max in x, dp at y and max of y, dp at y then decrement y by 1 and increment x by 1. 
After while loop end append mx in dp and finally return dp at n.
'''

class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [None, 1]
        for a in range(2, n + 1):
            y, x, mx = a - 1, 1, 0
            while x <= y:
                mx = max(mx, max(x, dp[x]) * max(y, dp[y]))
                y, x = y - 1, x + 1
            dp.append(mx)
        return dp[n]