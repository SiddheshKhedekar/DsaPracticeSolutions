# Shortest Bridge -> Python3

'''
Explanation: We get root of first island from first function then we dfs root and add indexes to 
bfs. In first function we perform next loop and validity check and in dfs we append to bfs and loop 
for all 4 directions then check valid condition to call recursively again. Loop on bfs and expand 
the first island finally return earlier step when facing other island. Inside while loop we loop 
for items in bfs and again for all directions check necessary conditions and update values.
'''

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            grid[i][j] = -1
            bfs.append((i, j))
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= x < n and 0 <= y < n and grid[x][y] == 1: dfs(x, y)
        def first():
            for i in range(n):
                for j in range(n):
                    if grid[i][j]: return i, j
        n, step, bfs = len(grid), 0, []
        dfs(*first())
        while bfs:
            new = []
            for i, j in bfs:
                for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                    if 0 <= x < n and 0 <= y < n:
                        if grid[x][y] == 1: return step
                        elif not grid[x][y]:
                            grid[x][y] = -1
                            new.append((x, y))
            step += 1
            bfs = new