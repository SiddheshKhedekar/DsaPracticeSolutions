# Difference Between Ones and Zeros in Row and Column -> Python3

'''
Explanation: Set x, y as len of matrix and matrix at 0 then define getcount to return the twice of 
sum nums - len of nums. Set r and c value list of map getcount grid and zip * grid respectively. 
Run loop on product of range x, y and set grid a, b as r at a + c at b and return grid on loop end. 
'''

class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        x, y = len(grid), len(grid[0])
        def getCount(nums): return 2 * sum(nums) - len(nums)
        r = list(map(getCount, grid))
        c = list(map(getCount, zip(*grid)))
        for a, b in product(range(x), range(y)): grid[a][b] = r[a] + c[b]
        return grid