# Transpose Matrix -> Python3

'''
Explanation: Return the zip of * matrix as it is the expected result.
'''

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]: return zip(*matrix)