# N-th Tribonacci Number -> Python3

'''
Explanation: Initialize first 3 elements after checking length condition then iterate on range of 
length-2. Inside set fn as sum of first three numbers and than swap numbers in line including fn 
value as next in sequence. Return f2 at end.
'''

class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0: return n
        f0, f1, f2 = 0, 1, 1
        for _ in range(n-2):
            fn = f0 + f1 + f2
            f0 = f1
            f1 = f2
            f2 = fn
        return f2