# Find The Original Array of Prefix Xor -> Python3

'''
Explanation: Return the xor map of pref and 0 + pref up to last index. Problem very similar to 
prefix sum but here be have xor instead.
'''

class Solution:
    def findArray(self, pref: List[int]) -> List[int]: return map(xor, pref, [0] + pref[:-1])