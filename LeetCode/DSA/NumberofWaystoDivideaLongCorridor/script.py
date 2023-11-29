# Number of Ways to Divide a Long Corridor -> Python3

'''
Explanation: Set x as off index in corridor where value at cor is S and set r to 1. Loop from 1 to 
len of x - 1 in steps of 2 to set ans as the product of itself with x at y+1 - x at y. Finally 
return ans mod by given val multiplied by len of x % 2 == 0 and len of x greater than or same as 2.
'''

class Solution:
    def numberOfWays(self, corridor: str) -> int:
        x, ans = [y for y, cor in enumerate(corridor) if cor == 'S'], 1
        for y in range(1, len(x) - 1, 2): ans *= x[y + 1] - x[y]
        return ans % (10 ** 9 + 7) * (len(x) % 2 == 0 and len(x) >= 2)