# Data Stream as Disjoint Intervals -> Python3

'''
Explanation: Define set and add number values to it. For getting intervals define array and set 
start and end to none for each value in numbers set start and end as per conditions con continuous 
numbers and finally check once again if start is none and append the last interval.
'''

class SummaryRanges:
    def __init__(self):
        self.numbers = set()
    def addNum(self, value: int) -> None:
        self.numbers.add(value)
    def getIntervals(self) -> List[List[int]]:
        intervals, start, end = [], None, None
        for val in sorted(self.numbers):
            if start is None: start = end = val
            elif val - end == 1: end = val
            else:
                intervals.append([start, end])
                start = end = val
        if start is not None: intervals.append([start, end])
        return intervals