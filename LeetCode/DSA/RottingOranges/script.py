# Rotting Oranges -> Python3

'''
Explanation: Iterate over grid using product and append (i,j) in queueif rotten and if fresh 
increment by 1. Set dirs to 0 1 inc dec combo and levels to 0. While queue increment levels and run 
for loop on queue len inside set x,y to queue popleft. Another for loop on dirs check if 0<=x+dx<m 
and 0<=y+dy<n and grid[x+dx][y+dy] == 1 and decrement fresh by 1 set grid[x+dx][y+dy] to 2 and 
append in queue the indexes just set. Finally return -1 if fresh != 0 else max(levels-1, 0).
'''

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n, queue, fresh = len(grid), len(grid[0]), deque(), 0
        for i, j in product(range(m), range(n)):
            if grid[i][j] == 2: queue.append((i,j))
            if grid[i][j] == 1: fresh += 1
        dirs, levels = [[1,0],[-1,0],[0,1],[0,-1]], 0
        while queue:
            levels += 1
            for _ in range(len(queue)):
                x,y = queue.popleft()
                for dx, dy in dirs:
                    if 0<=x+dx<m and 0<=y+dy<n and grid[x+dx][y+dy] == 1:
                        fresh -= 1
                        grid[x+dx][y+dy] = 2
                        queue.append((x+dx, y+dy))
        return -1 if fresh != 0 else max(levels-1,0)