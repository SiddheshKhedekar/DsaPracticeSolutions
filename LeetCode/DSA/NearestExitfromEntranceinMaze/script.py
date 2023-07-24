# Nearest Exit from Entrance in Maze -> Python3

'''
Explanation: Get maze size to check if neighbor is valid and set directions as array then 
initialise q as deque of array entrance and visited as dict of tuple entrance. Use steps to keep 
track of bfs and loop while q then loop in range of len q. Set xo, yo inside loop by popleft on q 
and check base validity to return steps then loop xn,yn in directions and update x, y to check if 
new position has been visited or not and only continue if not visited and add x,y in visited and q. 
In main while increment steps by 1 and at end return -1.
'''

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n, steps = len(maze), len(maze[0]), 0
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        q, visited = deque([entrance]), {tuple(entrance)}
        while q:
            for _ in range(len(q)):
                xo, yo = q.popleft()
                if (0 in [xo, yo] or xo == m-1 or yo == n-1) and [xo, yo] != entrance:
                    return steps
                for xn, yn in directions:
                    x, y = xo+xn, yo+yn
                    if 0<=x<m and 0<=y<n and maze[x][y]=='.' and (x,y) not in visited:
                        visited.add((x,y))
                        q.append([x,y])
            steps+=1
        return -1