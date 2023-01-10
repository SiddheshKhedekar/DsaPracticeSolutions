# Repeated Substring Pattern -> Python3

'''
Explanation: Check if string is in the concatenation of string with itself and after removing the 
first and last character.
'''

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s+s)[1:-1]