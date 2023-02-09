# Where Will the Ball Fall -> Python3

'''
Explanation: Iterate on grid from top to bottom column wise and check if the temp value is not 
within bound or temp not equal to original grid value then return -1 else set i to temp and return 
from test function. In return call map function with range n as param.
'''

class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        def test(i):
            for j in range(m):
                i2 = i + grid[j][i]
                if i2 < 0 or i2 >= n or grid[j][i2] != grid[j][i]: return -1
                i = i2
            return i
        return map(test, range(n))