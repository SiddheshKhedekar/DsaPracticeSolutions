# Max Points on a Line -> Python3

'''
Explanation: Run a loop on points and run another loop inside on points starting from the next 
point given the upper loop. Get the slope of the current and upper loop point and increment the 
slope values in slopes array. In result get the max of slope count and result.
'''

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 2: return len(points)
        def get_slope(a1, a2):
            x1, y1 = a1
            x2, y2 = a2
            if x1-x2 == 0: return inf
            return (y1-y2)/(x1-x2)
        res = 1
        for i, a1 in enumerate(points):
            slopes = defaultdict(int)
            for j, a2 in enumerate(points[i+1:]):
                slope = get_slope(a1, a2)
                slopes[slope] += 1
                res = max(slopes[slope], res)
        return res+1