# Count Sub Islands -> Python3

'''
Explanation: Return sum of all dfs call on grid2 and inside dfs call check if grid2 index values are 
correct and value is 1 to return 1 set grid2 current value at indices to 0 and res to grid1 value. 
In for loop for all 4 edges call dfs and bitwise & it to res.
'''

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        n, m = len(grid2), len(grid2[0])
        def dfs(i, j):
            if not (0<=i<n and 0<=j<m and grid2[i][j]==1): return 1
            grid2[i][j], res = 0, grid1[i][j]
            for di, dj in [[0,1],[1,0],[-1,0],[0,-1]]:
                res &= dfs(i+di, j+dj)
            return res
        return sum(dfs(i, j) for i in range(n) for j in range(m) if grid2[i][j])