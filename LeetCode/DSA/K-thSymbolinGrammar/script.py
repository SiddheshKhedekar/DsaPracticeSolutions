# K-th Symbol in Grammar -> Python3

'''
Explanation: Return the count of 1 in bin value of k - 1 after and with 1. The answer to this 
problem depends on whether the number of 1 bits in binary K - 1 is odd or even
'''

class Solution:
    def kthGrammar(self, n: int, k: int) -> int: return bin(k - 1).count('1') & 1