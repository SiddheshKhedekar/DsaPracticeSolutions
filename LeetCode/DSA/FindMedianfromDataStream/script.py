# Find Median from Data Stream -> Python3

'''
Explanation: Use heaps and push in the smaller heap the negative of popping larger where number is 
default. Consider length and push in large the negative of popping smaller heap. When finding 
median check length and either return the first value in larger heap else diff between heap first 
indexed divided by 2.
'''

class MedianFinder:

    def __init__(self):
        self.heaps = [], []

    def addNum(self, num: int) -> None:
        small, large = self.heaps
        heappush(small, -heappushpop(large, num))
        if len(large) < len(small):
            heappush(large, -heappop(small))

    def findMedian(self) -> float:
        small, large = self.heaps
        if len(large) > len(small):
            return float(large[0])
        return (large[0] - small[0]) / 2.0