# Minimum Flips to Make a OR b Equal to c -> Python3

'''
Explanation: Return the value of after adding bit_count of c := (a or b) xor c and bit_count of 
a & b & c.
'''

class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        return (c := (a | b) ^ c).bit_count() + (a & b & c).bit_count()