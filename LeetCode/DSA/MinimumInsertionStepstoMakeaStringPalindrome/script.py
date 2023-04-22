# Minimum Insertion Steps to Make a String Palindrome -> Python3

'''
Explanation: We try to find the common subsequence and then get the number of chars to add. Set l 
as the len of s and sp as 2d array of 0 of dimension l+1 then run nexted for loop on range l with x 
and y as iterators. Set dp at next x and y diagonally as dp at current x and y plus 1 if the 
current s char at x and ~y which is -y-1 is the same else set it as the max of item in dp 1 step 
above or one step back.
'''

class Solution:
    def minInsertions(self, s: str) -> int:
        l = len(s)
        dp = [[0] * (l + 1) for _ in range(l + 1)]
        for x in range(l):
            for y in range(l):
                dp[x + 1][y + 1] = dp[x][y]+1 if s[x] == s[~y] else max(dp[x][y + 1], dp[x + 1][y])
        return l - dp[l][l]