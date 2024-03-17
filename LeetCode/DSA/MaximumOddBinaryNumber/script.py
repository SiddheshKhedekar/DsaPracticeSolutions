# Maximum Odd Binary Number -> Python3

'''
Explanation: Get ones count and return the created string formed out of 1 * ones count - 1 and 
adding 0 * zeros count and again adding the last 1 to make it odd.
'''

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones = s.count('1')
        return '1' * (ones - 1) + '0' * (len(s) - ones) + '1'