# Pacific Atlantic Water Flow -> Python3

'''
Explanation: Starting from each point, we dfs its neighbor if the neighbor is equal or less than 
itself. And maintain two boolean matrix for two oceans, indicating an ocean can reach to that point 
or not. Finally go through all nodes again and see if it can be both reached by two oceans. If a 
node is already visited, no need to visit again.
'''

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights: return []
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        m, n, result = len(heights), len(heights[0]), []
        p_seen = [[False for _ in range(n)] for _ in range(m)]
        a_seen = [[False for _ in range(n)] for _ in range(m)]
        def dfs(i, j, seen):
            seen[i][j] = True
            for direction in directions:
                x, y = i + direction[0], j + direction[1]
                if x < 0 or x >= m or y < 0 or y >= n or seen[x][y] or heights[x][y] < heights[i][j]: continue
                dfs(x, y, seen)
        for i in range(m):
            dfs(i, 0, p_seen)
            dfs(i, n - 1, a_seen)
        for j in range(n):
            dfs(0, j, p_seen)
            dfs(m - 1, j, a_seen)
        for i in range(m):
            for j in range(n):
                if p_seen[i][j] and a_seen[i][j]: result.append([i, j])
        return result