# Minimize Maximum of Array -> Python3

'''
Explanation: We need to calculate the prefix sum and average using enumerate on accumulate for 
input. Then we get the ceiling value using floor division and return the max of all values.
'''

class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        return max((y + x) // (x + 1) for x, y in enumerate(accumulate(nums)))