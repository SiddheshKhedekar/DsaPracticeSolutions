# Course Schedule -> Python3

'''
Explanation: Generate graph of arrays where size is numcourses and deg is array of 0 similar in 
size to graph. Then loop on prerequisite and append y in graph at x and at same stime increment deg 
at y by 1. Set bfs as the x in numcourses where deg at x is 0 then run loop on this bfs with nested 
loop on graph at x. Inside decrement deg at y by 1 and  if deg at y is 0 append y in bfs. Finally 
return if len bfs is numcourses.
'''

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph, deg = [[] for x in range(numCourses)], [0] * numCourses
        for y, x in prerequisites:
            graph[x].append(y)
            deg[y] += 1
        bfs = [x for x in range(numCourses) if deg[x] == 0]
        for x in bfs:
            for y in graph[x]:
                deg[y] -= 1
                if deg[y] == 0: bfs.append(y)
        return len(bfs) == numCourses