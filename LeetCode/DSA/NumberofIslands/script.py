# Number of Islands -> Python3

'''
Explanation: If not grid return 0, set count to 0 and define function dfs(i,j). For i in range len 
grid run another loop for j in range len grid[0], inside check if grid ij = ‘1’ and call dfs(ij) 
and increment count by 1 finally out of loops return count. Inside the dfs function check if i<0 or 
j<0 or i >= len grid or j >= len grid[0] or grid ij != ‘1’ and return. Set grid ij to ‘0’ and call 
dfs 4 times i+1, i-1,j+1,j-1 where the other var is i first or j second.
'''

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        count = 0
        def dfs(i,j):
            if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != '1': return
            grid[i][j] = '0'
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i,j)
                    count+=1
        return count