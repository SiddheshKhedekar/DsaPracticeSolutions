# Non-decreasing Subsequences -> Python3

'''
Explanation: Build all sub sequences and then filter by length condition. Possible to use tuple to 
tuple, union operation and loops to build the sub sequences.
'''

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        subseqs = {()}
        for n in nums:
            subseqs |= {ss + (n,)
            for ss in subseqs
            if not ss or ss[-1] <= n}
        return [s for s in subseqs if len(s) >= 2]