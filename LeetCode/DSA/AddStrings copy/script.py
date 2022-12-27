# Maximum Bags With Full Capacity of Rocks -> Python3

'''
Explanation: Get the difference between capacity and rocks in array and sort in reverse order. Loop 
the array and subtract additional rocks from it.
'''

class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        count = sorted(c - r for c, r in zip(capacity, rocks))[::-1]
        while count and additionalRocks and count[-1] <= additionalRocks:
            additionalRocks -= count.pop()
        return len(rocks) - len(count)