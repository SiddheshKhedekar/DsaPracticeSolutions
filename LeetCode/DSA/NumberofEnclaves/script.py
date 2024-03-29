# Number of Enclaves -> Python3

'''
Explanation: Loop over grid and check if it is an edge along with it being an island and call dfs 
and inside dfs set island to 0 and clean out all of its 4 edges and call dfs again. Return sum of 
entire grid.
'''

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            grid[i][j] = 0
            for x, y in (i-1, j),(i+1, j),(i, j-1),(i, j+1):
                if 0<=x<m and 0<=y<n and grid[x][y]: dfs(x, y)
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i==0 or j==0 or i==m-1 or j ==n-1): dfs(i, j)
        return sum(sum(row) for row in grid)