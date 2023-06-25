# Count Negative Numbers in a Sorted Matrix -> Python3

'''
Explanation: In m and n get the len of column and row also take r and m-1 and c and cnt as 0. Run 
while loop for r>=0 and c<n.insode loop check if grid r c value is less than 0 and increment cnt by 
n-c and decrement r by 1. Else increment c.
'''

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        r, c, cnt = m-1, 0, 0
        while r >= 0 and c < n:
            if grid[r][c] < 0:
                cnt += n-c
                r-=1
            else: c+=1
        return cnt