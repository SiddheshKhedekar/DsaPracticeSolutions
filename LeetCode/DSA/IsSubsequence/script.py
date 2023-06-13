# Is Subsequence -> Python3

'''
Explanation: Loop over both strings in single loop using two pointers while len of lists dont fall 
less than pointers. Check if the index elements are same and increment i. Outside condition 
increment j. At end return i == len first string.
'''

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]: i+=1
            j+=1
        return i == len(s)