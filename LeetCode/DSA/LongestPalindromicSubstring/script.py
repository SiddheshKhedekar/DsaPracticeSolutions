# Longest Palindromic Substring -> Python3

'''
Explanation: Define string ans and run a for loop on range len s. Set temp to helper passing i as 
l, r to helper and check if len of temp greater than len of ans to set temp to ans, do the same 
again with i, i+1. Inside the helper run a loop while l and r are within string constraints and s 
at l, r are same then return the string between l and r.
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def helper(s, l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]: l -= 1; r += 1
            return s[l+1:r]
        ans = ""
        for i in range(len(s)):
            temp = helper(s, i, i)
            if len(temp) > len(ans): ans = temp
            temp = helper(s, i, i+1)
            if len(temp) > len(ans): ans = temp
        return ans