# Destination City -> Python3

'''
Explanation: Map x, y as set of zip *paths then subtract x from y and return the pop from it.
'''

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        x, y = map(set, zip(*paths))
        return (y - x).pop()