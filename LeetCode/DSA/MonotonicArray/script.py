# Monotonic Array -> Python3

'''
Explanation: Use two flags and run loop for length-1. Inside unset one flag if next num is lesser 
than current num and unset the other if next num is greater than current num. 
'''

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        i = j = True
        for k in range(len(nums)-1):
            if nums[k] > nums[k+1]: i = False
            if nums[k] < nums[k+1]: j = False
        return i or j