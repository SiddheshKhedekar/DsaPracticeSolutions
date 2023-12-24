# Path Crossing -> Python3

'''
Explanation: Set crnt as tuple of 0, 0 and drtn as dict of each of the four directions and its 
corresponding step in each of the two axis as tuple then set visited as dict of crnt and loop for 
each character in path. Inside add the drtn step to crnt and then check if it is in visited to 
return true. Add crnt in visited and finally outside of loop return false.
'''

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        crnt, drtn = (0, 0), {'N' : (0, 1), 'S' : (0, -1), 'E' : (1, 0), 'W' : (-1, 0)}
        visited = {crnt}
        for c in path:
            crnt = tuple(map(operator.add, crnt, drtn[c]))
            if crnt in visited: return True
            visited.add(crnt)
        return False