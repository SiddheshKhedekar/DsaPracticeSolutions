# Shortest Path to Get All Keys -> Python3

'''
Explanation: We may visit a point more than one times hence we maintain a set of x, y, keys in 
seen. We then visit each level using queue and by implementing bfs. Each vertex has at most 4 * 6 
edge then in the BFS algorithm, each vertice and edge is visited at most once and queue is used to 
visite vertices in the BFS order and a dictionary is used to store the visited status.
'''

class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        if not grid or not grid[0]: return -1
        m, n, allKs = len(grid), len(grid[0]), [0, 0, 0, 0, 0, 0]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '@': iS, jS = i, j
                elif grid[i][j].islower(): allKs[ord(grid[i][j]) - ord('a')] = 1
        allKs, cnt = tuple(allKs), 0
        curlvl = [(iS, jS, tuple(6 * [0]))]
        seen = {(iS, jS, tuple(6 * [0]))}
        while curlvl:
            nxtlvl = []
            for x, y, ks in curlvl:
                for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    r, c = x + dx, y + dy
                    if 0 <= r < m and 0 <= c < n and grid[r][c] != '#':
                        if grid[r][c] in '.@':
                            if (r, c, ks) not in seen:
                                seen.add((r, c, ks))
                                nxtlvl.append((r, c, ks))
                        elif grid[r][c].islower():
                            newKs = list(ks)
                            newKs[ord(grid[r][c]) - ord('a')] = 1
                            newKs = tuple(newKs)
                            if newKs == allKs: return cnt + 1
                            if (r, c, newKs) not in seen:
                                seen.add((r, c, newKs))
                                nxtlvl.append((r, c, newKs))
                        else:
                            if ks[ord(grid[r][c].lower()) - ord('a')] == 1 and (r, c, ks) not in seen:
                                seen.add((r, c, ks))
                                nxtlvl.append((r, c, ks))
            curlvl = nxtlvl
            cnt += 1
        return -1