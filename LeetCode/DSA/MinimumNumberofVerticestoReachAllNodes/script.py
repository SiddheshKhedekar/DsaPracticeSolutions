# Minimum Number of Vertices to Reach All Nodes -> Python3

'''
Explanation: We take set of all vertices and remove all the reachable vertices from it to return 
the remaining in list format.
'''

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        return list(set(range(n)) - set(y for x, y in edges))