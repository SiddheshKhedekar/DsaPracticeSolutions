# Unique Paths -> Python3

'''
Explanation: In a m X n matrix we can try to solve it as a math combinatorics problem. We understand we need to make m-1 right moves and n-1 down mover to reach finish from the start out of total m+n-2 moves. Considering all different combinations we use the factorial of m+n-2 and floor divide by factorial of m-1 and n-1.
'''

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return factorial(m+n-2)//factorial(m-1)//factorial(n-1)