# Equal Row and Column Pairs -> Python3

'''
Explanation: Set mem as defaultdict int and count as 0 then run loop for r in grid to increment the 
mem at str r by 1. Run another loop for x in range len of grid 0 and initialize c as empty array. 
Run nested loop for y in range of len grid and append grid at y,x in c then outside inner loop 
increment count by mem at str c.
'''

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        mem, count = defaultdict(int), 0
        for r in grid: mem[str(r)] += 1
        for x in range(len(grid[0])):
            c = []
            for y in range(len(grid)): c.append(grid[y][x])
            count += mem[str(c)]
        return count