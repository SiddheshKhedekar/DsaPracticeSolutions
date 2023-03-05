# Find the Winner of the Circular Game -> Python3

'''
Explanation: Loop on range 2 to n+1 and set ans to ans + k and mod by index then return ans + 1 on 
loop end.
'''

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        res = 0
        for i in range(2, n + 1): res = (res + k) % i
        return res + 1