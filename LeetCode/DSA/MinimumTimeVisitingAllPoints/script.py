# Minimum Time Visiting All Points -> Python3

'''
Explanation: The time cost to travel between 2 neighboring points equals the larger value between 
the absolute values of the difference of respective x and y coordinates of the 2 points. First loop 
on points, next points as crnt, pre then loop on them as cr, pr and get the max of the abs diff 
between cr - pr in this loop and return the sum of the one before it. 
'''

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        return sum(max(abs(cr - pr) for cr, pr in zip(crnt, pre)) for crnt, pre in \
        zip(points, points[1:]))