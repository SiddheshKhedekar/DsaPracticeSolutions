# Last Day Where You Can Still Cross -> Python3

'''
Explanation: Every next day new cell becomes flooded so if on i day we cant cross from top to 
bottom then all days after i we similarly cant cross. So we can implement binary search to find the 
last day we can walk in range of len cells. For each mid we need to check if we can still cross. To 
do so we build grid for dayat and then use bfs to check if we can reach the cells in bottom roww by 
starting from any cells in top row.
'''

class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        dir, lft, rgt, res = [0, 1, 0, -1, 0], 1, len(cells), 0
        def canWalk(dayAt):
            grd = [[0] * col for _ in range(row)]
            for x in range(dayAt):
                r, c = cells[x]
                grd[r - 1][c - 1] = 1
            bfs = deque([])
            for c in range(col):
                if grd[0][c] == 0:
                    bfs.append((0, c))
                    grd[0][c] = 1
            while bfs:
                r, c, = bfs.popleft()
                if r == row - 1: return True
                for x in range(4):
                    nr, nc = r + dir[x], c + dir[x + 1]
                    if nr < 0 or nr == row or nc < 0 or nc == col or \
                        grd[nr][nc] == 1: continue
                    grd[nr][nc] = 1
                    bfs.append((nr, nc))
            return False
        while lft <= rgt:
            mid = (lft + rgt) // 2
            if canWalk(mid): res, lft = mid, mid + 1
            else: rgt = mid - 1
        return res