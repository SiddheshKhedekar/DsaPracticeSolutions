# Single Number II -> Python3

'''
Explanation: Use bit manipulation to efficiently keep track of the counts of each bit position. By 
utilizing XOR and AND operations, we can identify the bits of the single number that appears only 
once in the array while ignoring the bits that appear multiple times.
'''

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        singles, doubles = 0, 0
        for n in nums:
            singles ^= (n & ~doubles)
            doubles ^= (n & ~singles)
        return singles