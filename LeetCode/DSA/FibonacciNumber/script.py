# Fibonacci Number -> Python3

'''
Explanation: Start with base two fibonacci numbers and run for loop on n. Get the next fibonacci 
number and keep swapping the older two to next ones.
'''

class Solution:
    def fib(self, n: int) -> int:
        if n == 0: return n
        f0, f1 = 0, 1
        for _ in range(n-1):
            fn = f0 + f1
            f0 = f1
            f1 = fn
        return f1