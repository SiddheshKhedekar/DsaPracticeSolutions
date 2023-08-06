# Number of Increasing Paths in a Grid -> Python3

'''
Explanation: We iterate all index in grid in increasing order as we want strictly increasing paths 
there is no cycle of pathwhile iterating we call count function on index and sum all return values 
after modulo. Inside cached count we set temp rees iterate all directions check if valid and 
increment res by recursive call to count x, y after modulo.
'''

class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        a, b, modulo = len(grid), len(grid[0]), 10 ** 9 + 7
        @lru_cache(None)
        def count(i, j):
            res = 1
            for x, y in [[i, j + 1], [i, j - 1], [i + 1, j], [i - 1, j]]:
                if 0 <= x < a and 0 <= y < b and grid[x][y] < grid[i][j]:
                    res += count(x, y) % modulo
            return res
        return sum(count(i, j) for i in range(a) for j in range(b)) % modulo