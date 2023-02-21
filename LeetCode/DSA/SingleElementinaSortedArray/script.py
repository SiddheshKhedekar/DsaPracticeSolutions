# Single Element in a Sorted Array -> Python3

'''
Explanation: Use one pointer from start and another from end. While l < r run loop and set m to 
mid if mid is odd then decrement by 1. If mid is even then its duplocate should be in the next 
index set l to m+2 and if not set r to m as we know that the odd element exists on that side.
'''

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if m % 2 == 1: m -= 1
            if nums[m] != nums[m + 1]: r = m
            else: l = m + 2
        return nums[l]