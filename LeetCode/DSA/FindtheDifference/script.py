# Find the Difference -> Python3

'''
Explanation: Initialize cnt as 0 and run loop on s and t to xor ord value of iterator into cnt and 
return char of cnt at end.
'''

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        cnt = 0
        for cntS in s: cnt ^= ord(cntS)
        for cntT in t: cnt ^= ord(cntT)
        return chr(cnt)