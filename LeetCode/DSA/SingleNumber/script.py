# Single Number -> Python3

'''
Explanation: Iterate on list and xor the list values with result that we declare as 0. Using bit 
manipulation all duplicate values will cancel each other out leaving the single number.
'''

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            res ^= i
        return res