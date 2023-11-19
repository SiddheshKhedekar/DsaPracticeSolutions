# Unique Length-3 Palindromic Subsequences -> Python3

'''
Explanation: Initialize ans as 0 and run loop on all chars. Find chr in s from left and right to 
set x, y then check if x is not last index and append the len of set of s x+1 to y then after loop 
end return ans.
'''

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        ans = 0
        for chr in 'abcdefghijklmnopqrstuvwxyz':
            x, y = s.find(chr), s.rfind(chr)
            if x > -1: ans += len(set(s[x + 1: y]))
        return ans