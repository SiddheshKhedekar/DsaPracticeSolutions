# Find Peak Element -> Python3

'''
Explanation: Use binary search and return mid when it is greater than its neighbours. Otherwise 
return left or right depending on whichever is greater.
'''

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while left < right-1:
            mid = (left+right)//2
            if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]: return mid
            if nums[mid] < nums[mid+1]: left = mid+1
            else: right = mid-1
        return left if nums[left] >= nums[right] else right