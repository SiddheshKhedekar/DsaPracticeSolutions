# K Closest Points to Origin -> Python3

'''
Explanation: Initialize array a run a loop of x,y on points then maintain a min heap of dist and 
points. If len of heap is greater than k then pop immediately after inserting else just push in 
heap. Finally return the array of points in heap.
'''

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        hp = []
        for (i, j) in points:
            dist = -(i * i + j * j)
            if len(hp) == k: heapq.heappushpop(hp, (dist, i, j))
            else: heapq.heappush(hp, (dist, i, j))
        return [(i, j) for (dist, i, j) in hp]