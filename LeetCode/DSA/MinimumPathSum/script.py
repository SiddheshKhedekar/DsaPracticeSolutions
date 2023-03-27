# Minimum Path Sum -> Python3

'''
Explanation: Get the grid lengths and set the cost to traverse the first row and column to the end. 
Then run nested loop for length and set the current grid value as increment to min of left and top 
value. Finally return the last grid value.
'''

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        a, b = len(grid), len(grid[0])
        for x in range(1, b): grid[0][x] += grid[0][x-1]
        for x in range(1, a): grid[x][0] += grid[x-1][0]
        for x in range(1, a):
            for y in range(1, b):
                grid[x][y] += min(grid[x-1][y], grid[x][y-1])
        return grid[-1][-1]