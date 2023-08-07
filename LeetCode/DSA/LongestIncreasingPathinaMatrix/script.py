# Longest Increasing Path in a Matrix -> Python3

'''
Explanation: Check if not edge then initialise directions and cache. In dfs check if visited and 
work with neighbours inside its for loop we need new count for each direction finally saving it in 
cache before returning res. Then again in main function call dfs for row and call and save the max 
of res and dfs call in res.
'''

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix: return 0
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        m, n, res = len(matrix), len(matrix[0]), 0
        cache = [[-1 for _ in range(n)] for _ in range(m)]
        def dfs(i, j):
            if cache[i][j] != -1: return cache[i][j]
            res = 1
            for direction in directions:
                x, y = i + direction[0], j + direction[1]
                if x < 0 or x >= m or y < 0 or y >= n or matrix[x][y] <= matrix[i][j]: continue
                length = 1 + dfs(x, y)
                res = max(length, res)
            cache[i][j] = res
            return res
        for i in range(m):
            for j in range(n):
                cur_len = dfs(i, j)
                res = max(res, cur_len)
        return res