# Arranging Coins -> Python3

'''
Explanation: We can solve it as a math problem using the completing of square technique. We can 
solve for result by inverting formula and getting the square root of 2*N - 1/4 and subtracting 1/2.
'''

class Solution:
    def arrangeCoins(self, n: int) -> int:
        return (int)((2*n + 0.25)**0.5- 0.5)