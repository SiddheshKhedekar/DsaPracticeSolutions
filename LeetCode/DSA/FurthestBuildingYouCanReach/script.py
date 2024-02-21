# Furthest Building You Can Reach -> Python3

'''
Explanation: Set hp as array and then loop for range of len heights - 1. Set dist as heights at 
x + 1 minus the heights at x then check if dist is greater than 0 to push dist in hp then check if 
len hp is greater than ladders to decrement bricks by pop on hp also check if bricks is less than 0 
to return x. Finally at end return len heights - 1. 
'''

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        hp = []
        for x in range(len(heights) - 1):
            dist = heights[x + 1] - heights[x]
            if dist > 0: heapq.heappush(hp, dist)
            if len(hp) > ladders: bricks -= heapq.heappop(hp)
            if bricks < 0: return x
        return len(heights) - 1