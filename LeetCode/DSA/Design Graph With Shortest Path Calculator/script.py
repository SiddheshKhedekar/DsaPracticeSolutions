# Design Graph With Shortest Path Calculator -> Python3

'''
Explanation: Store edges as adjacency matrix in init, then in addedge append the data and in 
shortestpath implement dijkstras algorithm on the matrix. Set parq as array of 0, node1 as set and 
set dst at node1 as 0 then loop while parq to set t, nd as parq heappop. Check if nd is node2 to 
return t then check if t is greater than dst at np to continue otherwise run loop for nbr, val in 
adjlst at nd. Set ndst as t + val and check if ndst is less than dst at nbr. Inside set dst at nbr 
as ndst and heappush in parq ndst, nbr. At end return -1 as node not reachable.
'''

class Graph:
    def __init__(self, n: int, edges: List[List[int]]):
        self.adjLst = [[] for _ in range(n)]
        for x, y, val in edges: self.adjLst[x].append((y, val))
    def addEdge(self, edge: List[int]) -> None:
        x, y, val = edge
        self.adjLst[x].append((y, val))
    def shortestPath(self, node1: int, node2: int) -> int:
        n, parQ = len(self.adjLst), [(0, node1)]
        dst = [inf] * (n)
        dst[node1] = 0
        while parQ:
            t, nd = heappop(parQ)
            if nd == node2: return t
            if t > dst[nd]: continue
            for neighbor, val in self.adjLst[nd]:
                nDst = t + val
                if nDst < dst[neighbor]:
                    dst[neighbor] = nDst
                    heappush(parQ, (nDst, neighbor))
        return -1