# Majority Element -> Python3

'''
Explanation: The element at n/2 position is the most frequently occurring in a list after sorting. Floor division helps in handeling even number of values in the list.
'''

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]