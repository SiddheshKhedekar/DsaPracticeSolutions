# Longest Palindrome -> Python3

'''
Explanation: Get frequency using Counter and loop on the values increment the even frequencies 
possible and check for middle element.
'''

class Solution:
    def longestPalindrome(self, s: str) -> int:
        res = 0
        for i in collections.Counter(s).values():
            res += i // 2 * 2
            if res % 2 == 0 and i % 2 == 1:
                res += 1
        return res