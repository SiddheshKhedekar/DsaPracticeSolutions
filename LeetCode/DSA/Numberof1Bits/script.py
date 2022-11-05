# Number of 1 Bits -> Python3

'''
Explanation: Use format with parameter ‘b’ to get the binary conversion of the number.
'''

class Solution:
    def hammingWeight(self, n: int) -> int:
        new = format(n, "b")
        count = 0
        for i in str(new):
            if i == '1':
                count+=1
        return count