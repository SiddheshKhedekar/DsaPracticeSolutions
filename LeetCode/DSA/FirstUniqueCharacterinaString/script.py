# First Unique Character in a String -> Python3

'''
Explanation: Define letters of alphabet then set index as array of s index of l where l in letters 
and where s count of l is 1. Return min index if not empty else return -1.
'''

class Solution:
    def firstUniqChar(self, s: str) -> int:
        letters = 'abcdefghijklmnopqrstuvwxyz'
        index = [s.index(l) for l in letters if s.count(l) == 1]
        return min(index) if len(index) else -1