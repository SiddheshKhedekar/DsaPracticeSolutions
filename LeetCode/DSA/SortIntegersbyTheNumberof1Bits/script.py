# Sort Integers by The Number of 1 Bits -> Python3

'''
Explanation: Use sorted function for the array where the key is a lambda function for the binary 
value of respective array element.
'''

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key = lambda a: [bin(a).count('1'),a])