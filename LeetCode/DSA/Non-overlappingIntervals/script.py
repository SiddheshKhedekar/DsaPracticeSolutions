# Non-overlapping Intervals -> Python3

'''
Explanation: Set max as inf neg and loop on the sorted intervals where key is second element. If 
start is greater than or equal to max then set max to end else increase count.
'''

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        maxim, count = float('-inf'), 0
        for start, end in sorted(intervals, key=lambda i: i[1]):
            if start >= maxim: maxim = end
            else: count += 1
        return count