# Path With Minimum Effort -> Python3

'''
Explanation: Set x, y as the len of heights and its first row, set path as the array of array 
populated by inf of size x and y as per heights. Set path at 0,0 as - and minHp as array of tuple 
0, 0, 0 and direction as array of 0, 1, 0, -1, 0. Run loop while minhp to set dist, row and col by 
heappop on minHp and check if dist is greater than path at row, col to continue, then check if row 
is same as x - 1 and col is same as y - 1 to return dist. Run loop for range 4 and set xr, yc as 
row + direction at index and col + direction at index + 1. Check if xr and yc is valid and set 
new_dist as max of dist and abs heights at xr, yc - heights at row, col then check if path at 
xr, yc is greater than new_dist to set it as new_dist and heappush it along with xr, yc in minHp.
'''

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        x, y = len(heights), len(heights[0])
        path = [[math.inf] * y for _ in range(x)]
        path[0][0], minHp, direction = 0, [(0, 0, 0)], [0, 1, 0, -1, 0]
        while minHp:
            dist, row, col = heappop(minHp)
            if dist > path[row][col]: continue
            if row == x - 1 and col == y - 1: return dist
            for indx in range(4):
                xr, yc = row + direction[indx], col + direction[indx + 1]
                if 0 <= xr < x and 0 <= yc < y:
                    new_dist = max(dist, abs(heights[xr][yc] - heights[row][col]))
                    if path[xr][yc] > new_dist:
                        path[xr][yc] = new_dist
                        heappush(minHp, (path[xr][yc], xr, yc))