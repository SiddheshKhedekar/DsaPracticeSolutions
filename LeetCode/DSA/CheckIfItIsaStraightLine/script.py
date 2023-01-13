# Check If It Is a Straight Line -> Python3

'''
Explanation: Get the first two values from the input. Loop the input and check for the condition 
where we need to convert division to multiplication to prevent divide by 0 case.
'''

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        (x0,y0),(x1,y1) = coordinates[:2]
        for x,y in coordinates:
            if (x1-x0)*(y-y1) != (x-x1)*(y1-y0):
                return False
        return True