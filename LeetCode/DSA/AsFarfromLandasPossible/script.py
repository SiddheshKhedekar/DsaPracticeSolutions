# As Far from Land as Possible -> Python3

'''
Explanation: Similar to Rotting Oranges problem get all land values in queue get the level from one 
end traverse all directions to get another level needed and then add the new level found to the 
queue from other end and set level traversed. 
'''

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        m, n, lvl = len(grid), len(grid[0]), 0
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        queue = deque([(i,j) for i in range(m) for j in range(n) if grid[i][j] == 1])
        if len(queue) == m*n or len(queue) == 0: return -1
        while queue:
            for _ in range(len(queue)):
                x,y = queue.popleft()
                for dx, dy in dirs:
                    xdx, ydy = x+dx, y+dy
                    if 0<=xdx<m and 0<=ydy<n and grid[xdx][ydy] == 0:
                        grid[xdx][ydy] = 1
                        queue.append((xdx, ydy))
            lvl += 1
        return lvl-1