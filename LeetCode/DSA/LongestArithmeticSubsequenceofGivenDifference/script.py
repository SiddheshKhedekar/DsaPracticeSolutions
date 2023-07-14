# Longest Arithmetic Subsequence of Given Difference -> Python3

'''
Explanation: Set ans as a dict and run loop for n in arr. Inside set ans at n as the value in ans 
for n - diff or 0 + 1. Finally return the max of ans values.
'''

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        ans = {}
        for n in arr: ans[n] = ans.get(n - difference, 0) + 1
        return max(ans.values())