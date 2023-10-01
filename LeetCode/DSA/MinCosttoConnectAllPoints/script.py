# Min Cost to Connect All Points -> Python3

'''
Explanation: Define a manhattan function to return the distance between two points. Set res as 0 l 
as len of points, visited as empty set and vertices as array of tuple 0 with tuple 0, 0. Then run 
loop while len of visited is less than l and inside set c, tuple a, b as heappop on vertices. Check 
if b is in visited and continue otherwise increment res by c and add b to visited. Run loop for f 
in range l and check if f not visited and f is not same as b to heappush the tuple of manhattan 
call on points f, b and tuple b, f into vertices. Finally return res.
'''

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def manhattan(d, e): return abs(d[0] - e[0]) + abs(d[1] - e[1])
        res, l, visited, vertices = 0, len(points), set(), [(0, (0, 0))]
        while len(visited) < l:
            c, (a, b) = heapq.heappop(vertices)
            if b in visited: continue
            res += c
            visited.add(b)
            for f in range(l):
                if f not in visited and f != b:
                    heapq.heappush(vertices, (manhattan(points[f], points[b]), (b, f)))
        return res