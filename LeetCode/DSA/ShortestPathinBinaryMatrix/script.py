# Shortest Path in Binary Matrix -> Python3

'''
Explanation: Need to keep tuple with elements distance, x coord and y coord in loop we extract left 
of queue check if accords meet the ending point and if they return distance. If not then we check 
for all eight neighbours. If still in grid and value 0 and not already visited then we add new node 
in visited to the end of queue.
'''

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)
        neibs = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
        queue = deque([(1,0,0)]) if grid[0][0] == 0 else deque()
        visited = set()
        while queue:
            dist, x, y = queue.popleft()
            if (x,y) == (N-1,N-1): return dist
            for dx, dy in neibs:
                if 0<=x+dx<N and 0<=y+dy<N and grid[x+dx][y+dy] == 0 and (x+dx, y+dy) not in visited:
                    visited.add((x+dx, y+dy))
                    queue.append((dist+1,x+dx, y+dy))
        return -1