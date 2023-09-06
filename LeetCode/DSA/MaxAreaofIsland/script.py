# Max Area of Island -> Python3

'''
Explanation: Traverse island and set it to 0 save max area in ans and return. Need to define trav 
function with i and j param. Above n and m set to row and column in impossible set of conditions 
return 0 then set grid i j to 0 and return 1 + 4 trav call as sum with +1 -1 combo. In main 
function i,j product for loop check if grid i,j and set ans to max ans and trav i j.
'''

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans, n, m = 0, len(grid), len(grid[0])
        def trav(i,j):
            if i< 0 or j < 0 or i >= n or j >= m or grid[i][j] == 0: return 0
            grid[i][j] = 0
            return 1 + trav(i-1, j) + trav(i, j-1) + trav(i+1,j) + trav(i,j+1)
        for i, j in product(range(n),range(m)):
            if grid[i][j]: ans = max(ans, trav(i, j))
        return ans