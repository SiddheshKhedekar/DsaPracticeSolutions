# Insert Interval -> Python3

'''
Explanation: Iterate on the intervals then check for start and end on interval to be added and add 
to left and right side arrays else update the start and end.
'''

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start, end = newInterval[0], newInterval[1]
        l, r = [], []
        for x in intervals:
            if x[1] < start: l += x,
            elif x[0] > end: r += x,
            else:
                start, end = min(start, x[0]), max(end, x[1])
        return l + [[start,end]] + r