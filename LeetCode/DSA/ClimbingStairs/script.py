# Climbing Stairs -> Python3

'''
Explanation: Starting from initial floor a is the number of ways to reach current floor and b will 
give the number of steps to the next floor. Run loop on number of stairs and set the values of a 
and b. We get value of a by setting it to b and b new value is calculated as a+b.
'''

class Solution:
    def climbStairs(self, n: int) -> int:
        a = b = 1
        for _ in range(n):
            a, b = b, a+b
        return a