# Shortest Path in a Grid with Obstacles Elimination -> Python3

'''
Explanation: Define set len and width along with deque(0,0,0,k). Check if breakable is min path and 
return min path. While queue do popleft on queue if final loc then return steps. Run for loop on 
all traversal directions check if within bounds and breakable - current val = 0. Check if new tuple 
not in set and add to set append to queue, return -1 at end of while.
'''

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n, r, q = len(grid), len(grid[0]), set(), deque([(0,0,0,k)])
        if k >= m+n-2: return m+n-2
        while q:
            s, x, y, k = q.popleft()
            if (x,y) == (n-1,m-1): return s
            for dx, dy in (x,y-1),(x,y+1),(x-1,y),(x+1,y):
                if 0<=dx<n and 0<=dy<m and k - grid[dy][dx] >= 0:
                    v = (dx, dy, k-grid[dy][dx])
                    if v not in r:
                        r.add(v)
                        q.append((s+1,)+v)
        return -1