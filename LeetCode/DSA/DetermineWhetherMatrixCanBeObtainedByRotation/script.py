# Determine Whether Matrix Can Be Obtained By Rotation -> Python3

'''
Explanation: Run a loop 4 times as matrix can be rotated 90 degrees. If matrix matches target then 
true else set new matrix after rotation. For rotation traverse the matrix in reverse order column 
wise using zip and list comprehension.
'''

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        for _ in range(4):
            if mat == target: return True
            mat = [list(x) for x in zip(*mat[::-1])]
        return False