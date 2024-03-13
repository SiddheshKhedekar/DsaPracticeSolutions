# Squares of a Sorted Array -> Python3

'''
Explanation: Loop on list and assign each item as its square then sort the items and return.
'''

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(0,len(nums)): nums[i] = nums[i]*nums[i]
        nums.sort()
        return nums