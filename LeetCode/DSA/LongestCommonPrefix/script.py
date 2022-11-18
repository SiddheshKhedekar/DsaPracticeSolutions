# Longest Common Prefix -> Python3

'''
Explanation: Set s1 and s2 to min and max of input array. Enumerate over s1 and check if string 
characters match and return the string to the point they do.
'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ''
        s1 = min(strs)
        s2 = max(strs)
        for i, c in enumerate(s1):
            if c != s2[i]: return s1[:i]
        return s1