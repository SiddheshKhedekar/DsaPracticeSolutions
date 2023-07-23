# Best Sightseeing Pair -> Python3

'''
Explanation: Set the crnt best score in all previous spots and as we iterate to next spot the value 
of crnt best score decrements by 1.
'''

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        crnt, res = 0, 0
        for v in values:
            res = max(res, crnt + v)
            crnt = max(crnt, v) - 1
        return res