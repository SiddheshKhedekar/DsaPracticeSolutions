# Unique Paths III -> Python3

'''
Explanation: First we figure out the start point, end point and number of empty cells. Explore cell 
and update it then dfs explore its 4 directions and if we reach end then update count.
'''

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.res, m, n, empty = 0, len(grid), len(grid[0]), 1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1: x, y = i, j
                elif grid[i][j] == 0: empty += 1
        def dfs(x, y, empty):
            if not (0 <= x < m and 0 <= y < n and grid[x][y] >= 0): return
            if grid[x][y] == 2:
                self.res += empty == 0
                return
            grid[x][y] = -2
            dfs(x + 1, y, empty - 1)
            dfs(x - 1, y, empty - 1)
            dfs(x, y + 1, empty - 1)
            dfs(x, y - 1, empty - 1)
            grid[x][y] = 0
        dfs(x, y, empty)
        return self.res