# Determine if a Cell Is Reachable at a Given Time -> Python3

'''
Explanation: We first calculate the min steps we need to reach from start to end then if need is 
greater than 0 we check if t is greater than or same as need if it is 0 then target is start and if 
t is 1 than when we go out of the current cell we can not reach.
'''

class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        z = max(abs(sx - fx), abs(sy - fy))
        return t >= z if z else t != 1