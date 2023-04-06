# Number of Closed Islands -> Python3

'''
Explanation: Need to traverse the entire grid and perform dfs on it and return the sum. Within the 
dfs call need to check if current element is boundary and return 0, if current cell value is 
positive then return 1 and set grid value to 2 finally return dfs calls to all 4 neighbours after 
performing multiplication.
'''

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]): return 0
            if grid[i][j]: return 1
            grid[i][j] = 2
            return dfs(i, j+1) * dfs(i, j-1) * dfs(i+1, j) * dfs(i-1, j)
        return sum(dfs(i, j) for i, row in enumerate(grid) \
                for j, cell in enumerate(row) if not cell)